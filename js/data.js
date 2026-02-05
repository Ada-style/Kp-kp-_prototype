/**
 * Kpékpé Data Source - 100% Togo Context
 * Mises à jour avec les données réelles fournies (Janvier 2026)
 */

// 1. Profils de Personnalité (Inchangé pour l'instant, logique interne)
const PERSONALITY_PROFILES = {
    ANALYTIQUE: {
        label: "Analytique & Logique",
        desc: "Tu aimes comprendre le 'pourquoi' et le 'comment'. Tu es structuré(e) et tu prends des décisions basées sur des faits.",
        bonus_tags: ["C", "D", "E", "Santé", "Ingénierie", "Informatique", "Finance", "Sciences"]
    },
    CREATIF: {
        label: "Créatif & Intuitif",
        desc: "Tu as beaucoup d'imagination et tu aimes innover. Les règles strictes t'ennuient, tu préfères créer tes propres solutions.",
        bonus_tags: ["A4", "Arts", "Architecture", "Design", "Communication", "Marketing", "Artisanat"]
    },
    METHODIQUE: {
        label: "Méthodique & Organisé",
        desc: "Tu es fiable, ordonné(e) et efficace. On peut compter sur toi pour gérer des projets et suivre des plans précis.",
        bonus_tags: ["G1", "G2", "Gestion", "Administration", "Comptabilité", "Logistique", "Droit"]
    },
    SOCIAL: {
        label: "Social & Empathique",
        desc: "Ton truc, c'est les gens. Tu aimes aider, enseigner, soigner ou collaborer. Tu réussis là où le contact humain est clé.",
        bonus_tags: ["Santé", "Enseignement", "Ressources Humaines", "Commerce", "Tourisme"]
    }
};

// 2. Séries du BAC Togolais (Enrichies)
const SERIES_DATA = {
    "C": {
        name: "Série C (Mathématiques & Physique)",
        desc: "La voie royale pour les sciences dures et l'ingénierie.",
        keywords: ["maths", "logique", "ingénieur", "informatique", "physique", "architecture"]
    },
    "D": {
        name: "Série D (Sciences de la Vie)",
        desc: "Idéal pour la santé, l'agriculture et la biologie.",
        keywords: ["biologie", "santé", "médecine", "pharmacie", "svt", "nature", "agriculture"]
    },
    "A4": {
        name: "Série A4 (Littéraire)",
        desc: "Pour les passionnés de lettres, langues, droit et communication.",
        keywords: ["littérature", "langues", "philosophie", "droit", "communication", "journalisme", "enseignement"]
    },
    "E": {
        name: "Série E (Maths & Techno)",
        desc: "L'excellence technique et mathématique.",
        keywords: ["technologie", "mécanique", "conception", "ingénierie", "informatique"]
    },
    "F1": { name: "F1 (Mécanique Générale)", keywords: ["mécanique", "industrie", "usine", "construction"] },
    "F2": { name: "F2 (Électronique)", keywords: ["électronique", "circuits", "réparation", "informatique"] },
    "F3": { name: "F3 (Électrotechnique)", keywords: ["électricité", "énergie", "installation", "bâtiment"] },
    "F4": { name: "F4 (Génie Civil)", keywords: ["bâtiment", "construction", "architecture", "dessin", "chantier"] },
    "G1": { name: "G1 (Administration)", keywords: ["administration", "bureau", "secrétariat"] },
    "G2": { name: "G2 (Gestion/Compta)", keywords: ["comptabilité", "gestion", "chiffres", "banque", "finance"] },
    "G3": { name: "G3 (Commerce)", keywords: ["commerce", "vente", "marketing", "logistique"] },
    "TI": { name: "TI (Info)", keywords: ["informatique", "ordinateur", "réseaux", "programmation"] }
};

// 3. Établissements (Liste étendue et consolidée)
// Note: Coûts retirés sur demande utilisateur pour prototype
const SCHOOLS_DB = [
    // PUBLICS
    { name: "Université de Lomé (UL)", type: "Public", ville: "Lomé", domaines: ["Santé", "Sciences", "Droit", "Économie", "Ingénierie", "Agronomie", "Lettres"] },
    { name: "Université de Kara (UK)", type: "Public", ville: "Kara", domaines: ["Santé", "Droit", "Gestion", "Lettres"] },
    { name: "ENS Atakpamé", type: "Public", ville: "Atakpamé", domaines: ["Enseignement", "Éducation"] },
    { name: "INFA de Tové", type: "Public", ville: "Kpalimé", domaines: ["Agriculture", "Élevage"] },
    { name: "ENSI (UL)", type: "Public", ville: "Lomé", domaines: ["Ingénierie", "Informatique", "Génie Civil"] },
    { name: "FSS (UL)", type: "Public", ville: "Lomé", domaines: ["Santé", "Médecine", "Pharmacie"] },
    { name: "EAMAU", type: "Inter-États", ville: "Lomé", domaines: ["Architecture", "Urbanisme"] },

    // PRIVÉS (Sélection représentative)
    { name: "UCAO-UUT", type: "Privé", ville: "Lomé", domaines: ["Droit", "Communication", "Gestion", "Informatique"] },
    { name: "Lomé Business School (LBS)", type: "Privé", ville: "Lomé", domaines: ["Management", "Audit", "Marketing"] },
    { name: "ESGIS", type: "Privé", ville: "Lomé", domaines: ["Informatique", "Gestion", "Sciences"] },
    { name: "IAEC", type: "Privé", ville: "Lomé", domaines: ["Administration", "Commerce"] },
    { name: "ESA", type: "Privé", ville: "Lomé", domaines: ["Affaires", "Comptabilité"] },
    { name: "IPNET", type: "Privé", ville: "Lomé", domaines: ["Informatique", "Technologie"] },
    { name: "FORMATEC", type: "Privé", ville: "Lomé", domaines: ["Santé", "BTP", "Technique"] },
    { name: "CFMI", type: "Partenariat", ville: "Lomé", domaines: ["Industrie", "Mécanique"] },
    { name: "IFAD", type: "Public/Privé", ville: "Divers", domaines: ["Bâtiment", "Aquaculture", "Élevage"] }
];

// Helper pour trouver des écoles par domaine
function getSchoolsForJob(jobTags) {
    // Simple matching heuristic
    const matches = new Set();
    const tags = jobTags.map(t => t.toLowerCase());

    SCHOOLS_DB.forEach(school => {
        const schoolDomains = school.domaines.map(d => d.toLowerCase());
        // Check intersection
        const hasMatch = tags.some(tag =>
            schoolDomains.some(domain => domain.includes(tag) || tag.includes(domain))
        );

        if (hasMatch) matches.add(school.name);
    });

    // Fallback defaults if empty based on generic types
    if (matches.size === 0) {
        if (tags.includes("santé")) matches.add("Université de Lomé (FSS)");
        if (tags.includes("informatique")) matches.add("IPNET / ESGIS");
        if (tags.includes("commerce")) matches.add("Lomé Business School");
    }

    return Array.from(matches).slice(0, 3); // Return top 3 unique
}


// 4. Base de Données Métiers Enrichie (50 Métiers)
// Structure adaptée pour l'app
const JOBS_DATA = [
    // --- SANTÉ (8) ---
    { id: "medecin", title: "Médecin Généraliste", category: "Santé", tags: ["santé", "soin", "biologie", "sciences", "aider", "médecine"], profiles: ["ANALYTIQUE", "SOCIAL"], series: ["D", "C"], studies: "7-8 ans", recruiters: ["CHU", "Cliniques"], desc: "Diagnostic et soin des patients.", salary_indice: "Élevé" },
    { id: "pharmacien", title: "Pharmacien", category: "Santé", tags: ["santé", "médicament", "chimie", "commerce"], profiles: ["ANALYTIQUE", "METHODIQUE"], series: ["D", "C"], studies: "6 ans", recruiters: ["Pharmacies", "Laboratoires"], desc: "Spécialiste du médicament.", salary_indice: "Élevé" },
    { id: "infirmier", title: "Infirmier d'État", category: "Santé", tags: ["santé", "soin", "contact", "aider"], profiles: ["SOCIAL", "METHODIQUE"], series: ["D", "A4"], studies: "3 ans", recruiters: ["Hôpitaux", "ONG"], desc: "Suivi et soins des patients.", salary_indice: "Moyen" },
    { id: "sage_femme", title: "Sage-femme", category: "Santé", tags: ["santé", "femme", "bébé", "social"], profiles: ["SOCIAL"], series: ["D"], studies: "3 ans", recruiters: ["Maternités"], desc: "Accompagnement des naissances.", salary_indice: "Moyen" },
    { id: "dentiste", title: "Chirurgien-Dentiste", category: "Santé", tags: ["santé", "dent", "soin", "bouche"], profiles: ["ANALYTIQUE", "METHODIQUE"], series: ["D", "C"], studies: "6 ans", recruiters: ["Cabinets", "CHU"], desc: "Soin des dents et de la bouche.", salary_indice: "Élevé" },
    { id: "optique", title: "Opticien", category: "Santé", tags: ["santé", "vue", "lunettes", "précision"], profiles: ["METHODIQUE", "ANALYTIQUE"], series: ["D", "C", "F"], studies: "3 ans", recruiters: ["Centres optiques"], desc: "Correction de la vision.", salary_indice: "Moyen" },
    { id: "laborantin", title: "Technicien de Labo", category: "Santé", tags: ["santé", "analyse", "sciences", "biologie"], profiles: ["ANALYTIQUE", "METHODIQUE"], series: ["D", "C"], studies: "3 ans", recruiters: ["Laboratoires", "CHU"], desc: "Analyses médicales.", salary_indice: "Moyen" },
    { id: "veto", title: "Vétérinaire", category: "Santé", tags: ["animaux", "santé", "bio", "soin"], profiles: ["ANALYTIQUE", "SOCIAL"], series: ["D", "C"], studies: "6 ans", recruiters: ["Indépendant", "État"], desc: "Santé animale.", salary_indice: "Moyen" },

    // --- AGRICULTURE & ENVIRONNEMENT (7) ---
    { id: "agronome", title: "Ingénieur Agronome", category: "Agriculture", tags: ["agriculture", "nature", "terre", "sciences", "terrain", "géographie"], profiles: ["ANALYTIQUE", "METHODIQUE"], series: ["D", "C"], studies: "5 ans", recruiters: ["Ministère", "ONG"], desc: "Modernisation de l'agriculture.", salary_indice: "Élevé" },
    { id: "elevage", title: "Éleveur Moderne", category: "Agriculture", tags: ["animaux", "ferme", "business", "terrain"], profiles: ["METHODIQUE", "CREATIF"], series: ["Toutes"], studies: "Formation pro", recruiters: ["Auto-entrepreneur"], desc: "Production animale rentable.", salary_indice: "Variable" },
    { id: "environnement", title: "Expert Environnement", category: "Environnement", tags: ["nature", "écologie", "géographie", "climat", "météo"], profiles: ["ANALYTIQUE", "SOCIAL"], series: ["D", "C", "A4"], studies: "3-5 ans", recruiters: ["ONG", "État"], desc: "Protection des ressources naturelles.", salary_indice: "Moyen" },
    { id: "peche", title: "Technicien Halieutique", category: "Agriculture", tags: ["poisson", "mer", "eau", "alimentation"], profiles: ["METHODIQUE"], series: ["D", "C"], studies: "3 ans", recruiters: ["IFAD", "Privé"], desc: "Gestion de la pêche et aquaculture.", salary_indice: "Moyen" },
    { id: "foret", title: "Garde Forestier", category: "Environnement", tags: ["nature", "arbres", "protection", "terrain"], profiles: ["METHODIQUE", "SOCIAL"], series: ["Toutes"], studies: "Formation pro", recruiters: ["État"], desc: "Surveillance des forêts.", salary_indice: "Moyen" },
    { id: "agro_alim", title: "Ingénieur Agroalimentaire", category: "Agriculture", tags: ["nourriture", "usine", "transformation", "chimie"], profiles: ["ANALYTIQUE", "METHODIQUE"], series: ["C", "D", "E"], studies: "5 ans", recruiters: ["Industries"], desc: "Transformation des produits agricoles.", salary_indice: "Élevé" },
    { id: "meteologue", title: "Météorologue / Chercheur", category: "Environnement", tags: ["géographie", "climat", "météo", "sciences", "physique"], profiles: ["ANALYTIQUE"], series: ["C", "D", "E"], studies: "5 ans", recruiters: ["ASECNA", "État"], desc: "Étude et prévision du temps.", salary_indice: "Moyen" },

    // --- ARTS & MÉDIAS (8) ---
    { id: "journaliste", title: "Journaliste / Reporter", category: "Média", tags: ["parler", "écriture", "reportage", "voyage", "géographie", "histoire"], profiles: ["CREATIF", "SOCIAL"], series: ["A4", "G"], studies: "3 ans", recruiters: ["TV", "Radio", "Web"], desc: "Informer le public.", salary_indice: "Moyen" },
    { id: "acteur", title: "Acteur / Comédien", category: "Arts", tags: ["spectacle", "théâtre", "cinéma", "expression", "art"], profiles: ["CREATIF", "SOCIAL"], series: ["Toutes"], studies: "École d'art", recruiters: ["Compagnies", "Freelance"], desc: "Interprétation de rôles.", salary_indice: "Variable" },
    { id: "realisateur", title: "Réalisateur / Monteur", category: "Arts", tags: ["cinéma", "vidéo", "image", "reportage", "technique"], profiles: ["CREATIF", "ANALYTIQUE"], series: ["A4", "F", "TI"], studies: "2-3 ans", recruiters: ["Studios", "Freelance"], desc: "Création de contenus audiovisuels.", salary_indice: "Moyen" },
    { id: "styliste", title: "Styliste / Designer Mode", category: "Arts", tags: ["mode", "vêtement", "dessin", "création", "art"], profiles: ["CREATIF", "METHODIQUE"], series: ["Toutes"], studies: "École de mode", recruiters: ["Ateliers", "Marques"], desc: "Création de collections de mode.", salary_indice: "Variable" },
    { id: "graphiste", title: "Graphiste / UX Designer", category: "Numérique", tags: ["dessin", "ordinateur", "image", "création", "art"], profiles: ["CREATIF", "METHODIQUE"], series: ["Toutes"], studies: "2 ans", recruiters: ["Agences", "Startups"], desc: "Communication visuelle numérique.", salary_indice: "Moyen" },
    { id: "photographe", title: "Photographe Pro", category: "Arts", tags: ["image", "photo", "art", "voyage", "technique"], profiles: ["CREATIF", "SOCIAL"], series: ["Toutes"], studies: "Expérience/Formation", recruiters: ["Studios", "Events"], desc: "Capture d'images.", salary_indice: "Variable" },
    { id: "musicien", title: "Musicien / Producteur", category: "Arts", tags: ["musique", "son", "art", "spectacle", "création"], profiles: ["CREATIF", "SOCIAL"], series: ["Toutes"], studies: "Conservatoire/Pro", recruiters: ["Freelance"], desc: "Création et production musicale.", salary_indice: "Variable" },
    { id: "danseur", title: "Danseur Chorégraphe", category: "Arts", tags: ["danse", "corps", "spectacle", "expression", "art"], profiles: ["CREATIF", "SOCIAL"], series: ["Toutes"], studies: "Expérience/Formation", recruiters: ["Troupes", "Indépendant"], desc: "Art du mouvement.", salary_indice: "Variable" },

    // --- ARTISANAT & TECHNIQUE (8) ---
    { id: "menuisier", title: "Menuisier", category: "Artisanat", tags: ["bois", "manuel", "meuble", "artisanat", "construction"], profiles: ["METHODIQUE", "CREATIF"], series: ["F4", "Sans Bac"], studies: "Apprentissage/CAP", recruiters: ["Ateliers"], desc: "Travail du bois.", salary_indice: "Variable" },
    { id: "macon", title: "Chef de Chantier / Maçon", category: "BTP", tags: ["construction", "bâtiment", "manuel", "terrain", "pratique"], profiles: ["METHODIQUE", "SOCIAL"], series: ["F4", "Sans Bac"], studies: "CAP/BT", recruiters: ["Entreprises BTP"], desc: "Réalisation de bâtiments.", salary_indice: "Moyen" },
    { id: "electricien", title: "Électricien", category: "Technique", tags: ["électricité", "courant", "manuel", "réparation", "sécurité"], profiles: ["METHODIQUE", "ANALYTIQUE"], series: ["F3", "Sans Bac"], studies: "BT/BTS", recruiters: ["État", "Ateliers"], desc: "Installations électriques.", salary_indice: "Moyen" },
    { id: "mecanicien", title: "Mécanicien Auto", category: "Technique", tags: ["voiture", "moteur", "réparation", "manuel", "technique"], profiles: ["METHODIQUE", "ANALYTIQUE"], series: ["F1", "Sans Bac"], studies: "Apprentissage", recruiters: ["Garages"], desc: "Entretien de véhicules.", salary_indice: "Moyen" },
    { id: "cuisinier", title: "Cuisinier / Chef", category: "Artisanat", tags: ["cuisine", "nourriture", "restaurant", "manuel", "art"], profiles: ["CREATIF", "METHODIQUE"], series: ["Toutes"], studies: "CAP/Hôtellerie", recruiters: ["Hôtels", "Restos"], desc: "Gastronomie et service.", salary_indice: "Moyen" },
    { id: "soudure", title: "Soudeur / Ferronnier", category: "Artisanat", tags: ["fer", "métal", "manuel", "construction", "artisanat"], profiles: ["METHODIQUE", "CREATIF"], series: ["F1", "Sans Bac"], studies: "Apprentissage", recruiters: ["PME", "Indépendant"], desc: "Travail du métal.", salary_indice: "Moyen" },
    { id: "couturier", title: "Couturier / Tailleur", category: "Artisanat", tags: ["mode", "tissu", "couture", "manuel", "vêtement"], profiles: ["METHODIQUE", "CREATIF"], series: ["Toutes", "Sans Bac"], studies: "Apprentissage", recruiters: ["Ateliers"], desc: "Confection de vêtements.", salary_indice: "Variable" },
    { id: "plombier", title: "Plombier", category: "Artisanat", tags: ["eau", "tuyau", "manuel", "réparation", "maison"], profiles: ["METHODIQUE"], series: ["Sans Bac"], studies: "Apprentissage", recruiters: ["Indépendant", "BTP"], desc: "Installations sanitaires.", salary_indice: "Moyen" },

    // --- NUMÉRIQUE & INGÉNIERIE (7) ---
    { id: "dev_web", title: "Développeur Web/Mobile", category: "Numérique", tags: ["informatique", "code", "internet", "création", "logique"], profiles: ["ANALYTIQUE", "CREATIF"], series: ["C", "E", "TI", "F2"], studies: "2-5 ans", recruiters: ["Startups", "Gozem"], desc: "Créer des sites et applis.", salary_indice: "Élevé" },
    { id: "data_analyst", title: "Data Analyst", category: "Numérique", tags: ["données", "chiffres", "maths", "analyse", "informatique"], profiles: ["ANALYTIQUE", "METHODIQUE"], series: ["C", "E"], studies: "3-5 ans", recruiters: ["Télécoms", "Banques"], desc: "Analyse des données.", salary_indice: "Élevé" },
    { id: "cybersecurite", title: "Expert Cyber-sécurité", category: "Numérique", tags: ["sécurité", "informatique", "code", "réseaux", "protection"], profiles: ["ANALYTIQUE", "METHODIQUE"], series: ["C", "E", "TI"], studies: "5 ans", recruiters: ["Banques", "État"], desc: "Protection des systèmes.", salary_indice: "Élevé" },
    { id: "ing_civil", title: "Ingénieur Génie Civil", category: "BTP", tags: ["construction", "chantier", "calcul", "technique", "physique"], profiles: ["ANALYTIQUE", "METHODIQUE"], series: ["C", "E", "F4"], studies: "5 ans", recruiters: ["Ebomaf", "CECO"], desc: "Grands projets BTP.", salary_indice: "Élevé" },
    { id: "architecte", title: "Architecte", category: "BTP", tags: ["maison", "dessin", "art", "plans", "géographie"], profiles: ["CREATIF", "ANALYTIQUE"], series: ["C", "D", "F4"], studies: "5 ans", recruiters: ["EAMAU"], desc: "Conception de bâtiments.", salary_indice: "Élevé" },
    { id: "electromec", title: "Ingénieur Électroméca", category: "Technique", tags: ["usine", "machine", "énergie", "technique", "physique"], profiles: ["ANALYTIQUE", "METHODIQUE"], series: ["E", "C", "F1", "F3"], studies: "5 ans", recruiters: ["WACEM", "T-Energy"], desc: "Maintenance industrielle.", salary_indice: "Élevé" },
    { id: "res_reseaux", title: "Admin Réseaux", category: "Numérique", tags: ["ordinateur", "internet", "connexion", "technique"], profiles: ["METHODIQUE", "ANALYTIQUE"], series: ["TI (Informatique)", "F2 (Électronique)", "C (Maths)", "E (Maths-Techno)"], studies: "3 ans", recruiters: ["PME", "Fournisseurs"], desc: "Gestion des parcs informatiques.", salary_indice: "Moyen" },

    // --- DROIT, GESTION & SOCIAL (12) ---
    { id: "avocat", title: "Avocat / Juriste", category: "Droit", tags: ["loi", "défendre", "parler", "justice", "histoire", "politique"], profiles: ["ANALYTIQUE", "SOCIAL"], series: ["A4"], studies: "5 ans", recruiters: ["Barreau", "Entreprises"], desc: "Défense et conseil juridique.", salary_indice: "Élevé" },
    { id: "comptable", title: "Comptable", category: "Gestion", tags: ["chiffres", "argent", "gestion", "rigueur", "maths"], profiles: ["METHODIQUE", "ANALYTIQUE"], series: ["G2", "C"], studies: "2-5 ans", recruiters: ["Toutes entreprises"], desc: "Gestion des finances.", salary_indice: "Moyen" },
    { id: "commercial", title: "Responsable Commercial", category: "Commerce", tags: ["vente", "négociation", "client", "parler", "argent", "business"], profiles: ["SOCIAL", "ANALYTIQUE"], series: ["G3", "A4"], studies: "3 ans", recruiters: ["Distribution", "Banques"], desc: "Développement des ventes.", salary_indice: "Moyen à Élevé" },
    { id: "logisticien", title: "Logisticien", category: "Transport", tags: ["port", "marchandise", "organisation", "voyage", "géographie"], profiles: ["METHODIQUE", "ANALYTIQUE"], series: ["G3", "C"], studies: "3 ans", recruiters: ["PAL", "AGL"], desc: "Gestion des flux.", salary_indice: "Moyen à Élevé" },
    { id: "enseignant", title: "Enseignant", category: "Éducation", tags: ["école", "transmettre", "aider", "savoir", "social", "histoire", "géographie"], profiles: ["SOCIAL", "METHODIQUE"], series: ["Toutes"], studies: "3-5 ans", recruiters: ["ENS", "Écoles"], desc: "Formation des jeunes.", salary_indice: "Moyen" },
    { id: "rh", title: "Responsable RH", category: "Gestion", tags: ["social", "recrutement", "humain", "entreprise", "aider"], profiles: ["SOCIAL", "METHODIQUE"], series: ["A4", "G1"], studies: "3-5 ans", recruiters: ["Entreprises"], desc: "Gestion du personnel.", salary_indice: "Moyen" },
    { id: "banquier", title: "Gestionnaire de Compte", category: "Banque", tags: ["argent", "client", "banque", "finance", "confiance"], profiles: ["SOCIAL", "METHODIQUE"], series: ["G2", "C", "A4"], studies: "3 ans", recruiters: ["Banques (Orabank)"], desc: "Conseils financiers clients.", salary_indice: "Moyen" },
    { id: "cm", title: "Community Manager", category: "Média", tags: ["internet", "communication", "réseaux sociaux", "web", "image"], profiles: ["CREATIF", "SOCIAL"], series: ["A4", "G3"], studies: "2 ans", recruiters: ["Agences", "PME"], desc: "Gestion de l'image web.", salary_indice: "Moyen" },
    { id: "assurance", title: "Assureur", category: "Finance", tags: ["protection", "sécurité", "client", "négociation", "argent"], profiles: ["METHODIQUE", "SOCIAL"], series: ["G3", "A4"], studies: "3 ans", recruiters: ["Assurances"], desc: "Gestion des risques.", salary_indice: "Moyen" },
    { id: "douane", title: "Agent de Douane", category: "Administration", tags: ["port", "loi", "argent", "frontière", "sécurité"], profiles: ["METHODIQUE", "ANALYTIQUE"], series: ["A4", "D", "G2"], studies: "Concours", recruiters: ["État"], desc: "Contrôle des marchandises.", salary_indice: "Moyen" },
    { id: "policier", title: "Policier / Gendarme", category: "Sécurité", tags: ["loi", "protection", "sécurité", "ordre", "aider"], profiles: ["METHODIQUE", "SOCIAL"], series: ["Toutes"], studies: "Concours", recruiters: ["État"], desc: "Maintien de la paix.", salary_indice: "Moyen" },
    { id: "transitaire", title: "Transitaire", category: "Transport", tags: ["port", "documents", "logistique", "commerce", "marchandise"], profiles: ["METHODIQUE", "ANALYTIQUE"], series: ["G3", "G2", "A4"], studies: "2-3 ans", recruiters: ["Sociétés Transit"], desc: "Formalités douanières.", salary_indice: "Moyen" }
];


// --- LOGIQUE DE MATCHING ---
// (Récupérée et adaptée pour utiliser les nouvelles données)

function getRecommendedJobs(personalityType, userKeywords) {
    // 1. Filter by Personality
    // Boost jobs that match the Personality Type Profile

    // 2. Score by Keywords
    // Simple occurrence counting

    // NOTE: This logic is executed in chat.js
    // ensuring data.js stays pure data container if possible
    // or providing helper functions here.

    return JOBS_DATA.filter(j => true); // Placeholder, logic in chat.js
}
