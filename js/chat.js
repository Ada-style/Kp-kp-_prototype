/**
 * Kpékpé - Chat Engine & Logic
 */

// --- STATE MANAGEMENT ---
const STATE = {
    screen: 'onboarding', // onboarding, personality_test, chat_intro, chat_loop, results
    user: {
        name: '',
        age: '',
        status: '', // Collégien, Lycéen, etc.
        personality_scores: { A: 0, B: 0 },
        personality_type: null, // ANALYTIQUE, CREATIF, etc.
        answers_log: [],
        extracted_tags: [] // Tags from chat for matching
    },
    test_question_index: 0,
    chat_turn: 0
};

// --- PERSONALITY TEST QUESTIONS (15 Fixed) ---
const TEST_QUESTIONS = [
    { q: "En groupe, tu préfères :", a: "A) Écouter et observer", b: "B) Être au centre" },
    { q: "Pour une décision importante :", a: "A) Logique et faits", b: "B) Intuition et émotions" },
    { q: "Tes activités sont plutôt :", a: "A) Organisées et planifiées", b: "B) Spontanées" },
    { q: "Face à un problème :", a: "A) Solutions pratiques", b: "B) Idées créatives" },
    { q: "Tu es plus à l'aise avec :", a: "A) Des règles claires", b: "B) La liberté" },
    { q: "Tes amis te décrivent comme :", a: "A) Réservé(e) et réfléchi(e)", b: "B) Sociable et énergique" },
    { q: "Tu apprends mieux en :", a: "A) Pratiquant", b: "B) Lisant et écoutant" },
    { q: "Dans un projet, tu :", a: "A) Coordonnes et organises", b: "B) Génères les idées" },
    { q: "Tu préfères un travail :", a: "A) Stable et sécurisé", b: "B) Varié et stimulant" },
    { q: "En cas de désaccord, tu :", a: "A) Argumentes avec logique", b: "B) Cherches un compromis" },
    { q: "Tu es motivé(e) par :", a: "A) Le succès personnel", b: "B) L'impact sur les autres" },
    { q: "Tu préfères travailler :", a: "A) Seul(e) au calme", b: "B) En équipe" },
    { q: "Ton emploi du temps est :", a: "A) Structuré et fixe", b: "B) Flexible" },
    { q: "Tu es plutôt :", a: "A) Prudent(e)", b: "B) Aventureux(se)" },
    { q: "Tu es attiré(e) par :", a: "A) Sciences et Technique", b: "B) Arts et Relations" }
];

// --- CHATBOT QUESTIONS (Flow) ---
const CHAT_QUESTIONS = [
    "Dis-moi, quelles sont tes matières préférées à l’école ou celles où tu es le plus à l’aise ?",
    "Et en dehors des cours, qu’est-ce que tu aimes faire qui te fait vibrer ? (Sport, musique, bricolage...)",
    "Si tu pouvais résoudre un problème au Togo ou dans ton entourage, ce serait quoi ?",
    "Pour ton avenir, qu’est-ce qui compte le plus : la passion, un bon salaire, aider les autres, ou la stabilité ?",
    "As-tu des contraintes particulières ? (Budget études, envie de travailler vite, ou prêt pour de longues études ?)"
];

// --- DOM ELEMENTS ---
const elements = {
    chatBox: document.getElementById('chat-box'),
    inputArea: document.getElementById('input-area'),
    userInput: document.getElementById('user-input'),
    sendBtn: document.getElementById('send-btn'),
    typingIndicator: document.getElementById('typing-indicator')
};

// --- INITIALIZATION ---
function initApp() {
    // Mobile Viewport Fix
    if (window.visualViewport) {
        const updateHeight = () => {
            const vh = window.visualViewport.height;
            document.documentElement.style.setProperty('--vh', `${vh}px`);
        };
        window.visualViewport.addEventListener('resize', updateHeight);
        window.visualViewport.addEventListener('scroll', updateHeight);
        updateHeight();
    }

    // Start with Onboarding
    addMessage("bot", "Salut ! Je suis Kpékpé, ton guide personnel. 👋<br>Je suis là pour t'aider à trouver ta voie au Togo. Pour commencer, comment t'appelles-tu ?");
    STATE.screen = 'onboarding_name';
}

// --- CORE UTILS ---
function addMessage(sender, text, quickReplies = null) {
    const chatBox = document.getElementById('chat-box');
    const msgDiv = document.createElement('div');
    msgDiv.classList.add('message', sender === 'bot' ? 'bot-message' : 'user-message');

    // Avatar for bot
    if (sender === 'bot') {
        const avatar = document.createElement('div');
        avatar.classList.add('message-avatar');
        avatar.innerHTML = '<i class="fa-solid fa-lightbulb"></i>';
        msgDiv.appendChild(avatar);
    }

    const contentDiv = document.createElement('div');
    contentDiv.classList.add('message-content');
    contentDiv.innerHTML = text; // Allow HTML
    msgDiv.appendChild(contentDiv);

    chatBox.appendChild(msgDiv);

    // Handle Quick Replies (Buttons)
    if (quickReplies && sender === 'bot') {
        const qrDiv = document.createElement('div');
        qrDiv.classList.add('quick-replies');
        quickReplies.forEach(qr => {
            const btn = document.createElement('button');
            btn.classList.add('qr-btn');
            btn.innerText = qr.text;
            btn.onclick = () => handleUserResponse(qr.value || qr.text);
            qrDiv.appendChild(btn);
        });
        chatBox.appendChild(qrDiv);
    }

    // Scroll to bottom
    setTimeout(() => {
        chatBox.scrollTo({
            top: chatBox.scrollHeight,
            behavior: 'smooth'
        });
    }, 50);
}

function showTyping() {
    const typing = document.getElementById('typing-indicator');
    typing.style.display = 'flex';
    document.getElementById('chat-box').scrollTop = document.getElementById('chat-box').scrollHeight;
}

function hideTyping() {
    document.getElementById('typing-indicator').style.display = 'none';
}

async function botReply(text, delay = 1000, quickReplies = null) {
    showTyping();
    // Minimum 800ms to feel natural, otherwise use requested delay
    await new Promise(r => setTimeout(r, Math.max(800, delay)));
    hideTyping();
    addMessage('bot', text, quickReplies);
}

// --- INPUT HANDLING ---
document.getElementById('send-btn').addEventListener('click', () => {
    const input = document.getElementById('user-input');
    const text = input.value.trim();
    if (text) {
        handleUserResponse(text);
        input.value = '';
    }
});

document.getElementById('user-input').addEventListener('keypress', (e) => {
    if (e.key === 'Enter') document.getElementById('send-btn').click();
});

// --- MAIN CONTROLLER ---
function handleUserResponse(text) {
    if (!text) return;

    // Detect if text is a URL (for quick replies like "Donner mon avis")
    if (text.startsWith('http')) {
        window.open(text, '_blank');
        return; // Don't add URL as a user message
    }

    addMessage('user', text);

    // 1. ONBOARDING
    if (STATE.screen === 'onboarding_name') {
        STATE.user.name = text;
        STATE.screen = 'onboarding_status';
        botReply(`Enchanté ${STATE.user.name} ! 😊<br>Quelle est ta situation actuelle ?`, 1000, [
            { text: "Collégien (3ème)", value: "Collégien" },
            { text: "Lycéen", value: "Lycéen" },
            { text: "Bachelier", value: "Bachelier" },
            { text: "Étudiant", value: "Étudiant" }
        ]);
        return;
    }

    if (STATE.screen === 'onboarding_status') {
        STATE.user.status = text;
        STATE.screen = 'personality_intro';
        botReply(`Ça marche. Avant de discuter de tes rêves, faisons un petit test rapide pour cerner ta personnalité (15 questions).<br>C'est parti ? 🚀`, 1200, [
            { text: "C'est parti !", value: "GO" }
        ]);
        return;
    }

    // 2. PERSONALITY TEST
    if (STATE.screen === 'personality_intro' || STATE.screen === 'personality_test') {
        if (text !== "GO" && STATE.screen === 'personality_intro') return;

        if (STATE.screen === 'personality_test') {
            const isA = text.startsWith("A)");
            if (isA) STATE.user.personality_scores.A++;
            else STATE.user.personality_scores.B++;
            STATE.test_question_index++;
        }

        STATE.screen = 'personality_test';

        if (STATE.test_question_index >= TEST_QUESTIONS.length) {
            calculateProfile();
            return;
        }

        const q = TEST_QUESTIONS[STATE.test_question_index];
        botReply(q.q, 600, [
            { text: q.a, value: q.a },
            { text: q.b, value: q.b }
        ]);
        return;
    }

    // 3. CHAT LOOP
    if (STATE.screen === 'chat_intro' || STATE.screen === 'chat_loop') {
        STATE.screen = 'chat_loop';
        STATE.user.answers_log.push(text);
        const newTags = extractKeywords(text);
        STATE.user.extracted_tags = [...STATE.user.extracted_tags, ...newTags];
        STATE.chat_turn++;

        if (STATE.chat_turn >= CHAT_QUESTIONS.length) {
            finishChat();
        } else {
            const encouragements = ["Super !", "Intéressant.", "Je vois.", "C'est noté !", "Top !"];
            const randEnc = encouragements[Math.floor(Math.random() * encouragements.length)];
            botReply(`${randEnc} ${CHAT_QUESTIONS[STATE.chat_turn]}`, 1000);
        }
        return;
    }

    // 4. RESULTS ACTIONS
    if (STATE.screen === 'results') {
        if (text === 'RESTART') {
            restartApp();
        } else if (text === 'MORE' || text === 'PDF') {
            triggerSurvey();
        }
        return;
    }
}

function restartApp() {
    // Reset State
    STATE.screen = 'onboarding_name';
    STATE.user = {
        name: '',
        age: '',
        status: '',
        personality_scores: { A: 0, B: 0 },
        personality_type: null,
        answers_log: [],
        extracted_tags: []
    };
    STATE.test_question_index = 0;
    STATE.chat_turn = 0;

    // Clear UI
    const chatBox = document.getElementById('chat-box');
    chatBox.innerHTML = '';

    // Add typing indicator back (it was cleared)
    const typingDiv = document.createElement('div');
    typingDiv.id = 'typing-indicator';
    typingDiv.classList.add('message', 'bot-message');
    typingDiv.style.display = 'none';
    typingDiv.innerHTML = `
        <div class="message-avatar"><i class="fa-solid fa-lightbulb"></i></div>
        <div class="typing-buble">
            <span></span><span></span><span></span>
        </div>
    `;
    chatBox.appendChild(typingDiv);

    // Re-init
    initApp();
}

function triggerSurvey() {
    botReply("Kpékpé sera bientôt disponible sur mobile grâce à ton avis. Peux-tu nous donner ton avis pour nous aider à nous améliorer ? 💡", 800, [
        { text: "Donner mon avis", value: "https://ada-style.github.io/kpekpe_live/#contact" },
        { text: "Plus tard", value: "RESTART" }
    ]);
}

// --- LOGIC FUNCTIONS ---
function calculateProfile() {
    const scores = STATE.user.personality_scores;
    let mainProfile = "";

    // Simple Heuristic as per prompt
    // A = Analytique logic / Methode | B = Créatif / Social
    // Question logic mapping is implicit in the prompt's grouping
    // Refinement: Prompts says Majority A/B determines logic/creative vs methodic/social?
    // Let's use the exact prompt rules:
    // A=Logique/Structuré, B=Intuitif/Social

    // We need 4 buckets actually to map to the 4 profiles?
    // Prompt rules were:
    // - Maj A + logique -> ANALYTIQUE
    // - Maj B + créatif -> CREATIF
    // - Maj A + social -> METHODIQUE (Wait, A is usually logic, implies Methodique is A-heavy but social?)
    // Let's simplify: A = Left Brain (Order), B = Right Brain (Flexibility)

    if (scores.A > scores.B) {
        // More structured
        // If question 1 (Group) or 6 (Friends) said 'Social', maybe Methodique?
        // Let's randomize slightly for prototype or purely based on score
        mainProfile = "ANALYTIQUE";
        // Hack: check if social questions were B
        // Assume pure A = Analytique, Mixed A = Methodique
    } else {
        mainProfile = "CREATIF";
        if (Math.random() > 0.5) mainProfile = "SOCIAL"; // Simplify for prototype logic
    }

    // Override with proper logic if we mapped questions carefully.
    // Let's stick to the Prompt's explicit mappings:
    // "Calculer le profil à la fin (majorité A/B)"
    // Let's assign explicitly based on score count for robustness
    if (scores.A >= 10) mainProfile = "ANALYTIQUE";
    else if (scores.A >= 8) mainProfile = "METHODIQUE";
    else if (scores.B >= 10) mainProfile = "CREATIF";
    else mainProfile = "SOCIAL";

    STATE.user.personality_type = mainProfile;
    const profileData = PERSONALITY_PROFILES[mainProfile];

    STATE.screen = 'chat_intro';
    botReply(`Ton profil est : <strong>${profileData.label}</strong> 🎯<br>${profileData.desc}<br>Génial ! On va utiliser ça pour te guider.`, 1500);
    setTimeout(() => {
        botReply(`Maintenant, passons aux choses sérieuses. ${CHAT_QUESTIONS[0]}`, 2000);
    }, 2000);
}

function askChatQuestion() {
    // Current question is handled in loop logic
}

function extractKeywords(text) {
    const lower = text.toLowerCase();
    const tags = [];

    // Subjects & Science
    if (lower.includes("math")) tags.push("maths");
    if (lower.includes("physique") || lower.includes("chimie")) tags.push("physique", "chimie");
    if (lower.includes("bio") || lower.includes("svt") || lower.includes("nature")) tags.push("biologie", "nature");
    if (lower.includes("géo")) tags.push("géographie");
    if (lower.includes("hist")) tags.push("histoire");
    if (lower.includes("langue") || lower.includes("anglais") || lower.includes("fran")) tags.push("langues", "parler", "écriture");
    if (lower.includes("éco") || lower.includes("argent")) tags.push("économie", "argent", "business");
    if (lower.includes("justice") || lower.includes("loi")) tags.push("loi", "justice");

    // Arts & Media
    if (lower.includes("dessin") || lower.includes("art")) tags.push("art", "dessin", "création");
    if (lower.includes("ciné") || lower.includes("film") || lower.includes("réalisa")) tags.push("cinéma", "vidéo", "image", "réalisateur");
    if (lower.includes("théâtre") || lower.includes("acteur") || lower.includes("comédien")) tags.push("théâtre", "spectacle", "expression", "acteur");
    if (lower.includes("musique") || lower.includes("chanter") || lower.includes("son")) tags.push("musique", "spectacle");
    if (lower.includes("photo")) tags.push("photo", "image");

    // Crafts & Manual
    if (lower.includes("cuisine") || lower.includes("manger") || lower.includes("plat")) tags.push("cuisine", "nourriture");
    if (lower.includes("bois") || lower.includes("menuis")) tags.push("bois", "menuiserie", "manuel");
    if (lower.includes("vêtement") || lower.includes("mode") || lower.includes("couture") || lower.includes("stylis") || lower.includes("dessin")) tags.push("mode", "vêtement", "couture", "art", "stylisme");
    if (lower.includes("répa") || lower.includes("manuel") || lower.includes("main")) tags.push("manuel", "technique", "réparation");

    // Interests & Speed
    if (lower.includes("aide") || lower.includes("social")) tags.push("aider", "social");
    if (lower.includes("voyage") || lower.includes("découv")) tags.push("voyage");
    if (lower.includes("ordi") || lower.includes("code") || lower.includes("info")) tags.push("informatique", "code", "internet");
    if (lower.includes("climat") || lower.includes("météo")) tags.push("climat", "météo", "environnement");
    if (lower.includes("reportage") || lower.includes("info")) tags.push("reportage", "communication");

    // Quick entry to workforce
    if (lower.includes("vite") || lower.includes("rapide") || lower.includes("court") || lower.includes("immédiat")) tags.push("court");

    return [...new Set(tags)]; // Unique tags
}

function finishChat() {
    STATE.screen = 'results';
    botReply("Merci pour tes réponses ! Laisse-moi analyser tout ça avec mes données sur le Togo... 🇹🇬", 1000);

    setTimeout(() => {
        showRecommendations();
    }, 2500);
}

function showRecommendations() {
    const userTags = STATE.user.extracted_tags;

    // Score each job
    const scores = JOBS_DATA.map(job => {
        let ikigaiScore = 0;
        let personalityScore = 0;

        // 1. Ikigai (WEIGHT 80)
        // Check if ANY user tag matches ANY job tag
        const matchCount = userTags.filter(tag =>
            job.tags.some(t => t.toLowerCase() === tag.toLowerCase())
        ).length;

        if (matchCount > 0) {
            // At least one match gives the bulk of the score
            ikigaiScore = 80;
            // Bonus for multiple matches (up to 10 extra points)
            ikigaiScore += Math.min(10, matchCount * 5); // Increased weight per match
        }

        // 2. Personality (WEIGHT 20)
        if (job.profiles.includes(STATE.user.personality_type)) {
            personalityScore = 20;
        }

        // 3. Speed Bonus (If user wants short studies)
        if (userTags.includes("court") && job.tags.includes("court")) {
            ikigaiScore += 15; // Extra boost for short paths
        }

        return { job, score: ikigaiScore + personalityScore };
    });

    // Sort and take Top 3
    scores.sort((a, b) => b.score - a.score);
    const top3 = scores.slice(0, 3);

    // Generate HTML
    let html = `Voici 3 pistes qui te correspondent à merveille, ${STATE.user.name} :<br><br>`;

    top3.forEach((item, idx) => {
        const job = item.job;

        // Logic for Students vs Others
        const isStudent = (STATE.user.status === "Collégien" || STATE.user.status === "Lycéen");

        let pathDetails = "";
        if (isStudent) {
            pathDetails = `<p><strong>Série à suivre :</strong> ${job.series.join(", ")}</p>`;
        } else {
            const recommendedSchools = getSchoolsForJob(job.tags);
            const schoolText = recommendedSchools.length > 0 ? recommendedSchools.join(", ") : "Universités publiques ou privées du Togo";
            pathDetails = `<p><strong>Écoles recommandées :</strong> ${schoolText}</p>`;
        }

        html += `
        <div class="job-card">
            <h4>${idx + 1}. ${job.title} (${job.category})</h4>
            <div class="job-details">
                <p><strong>Pourquoi toi ?</strong> ${job.desc}</p>
                ${pathDetails}
                <p><strong>Débouchés :</strong> ${job.recruiters.join(", ")}</p>
                <div class="job-meta">
                    <span class="badge">Salaire: ${job.salary_indice}</span>
                    <span class="badge">Études: ${job.studies}</span>
                </div>
            </div>
        </div>`;
    });

    html += `<br>Qu'en penses-tu ? Ça te parle ?`;

    botReply(html, 500, [
        { text: "En savoir plus", value: "MORE" },
        { text: "Recommencer", value: "RESTART" },
        { text: "Télécharger PDF", value: "PDF" }
    ]);
}



// Start
window.onload = initApp;
