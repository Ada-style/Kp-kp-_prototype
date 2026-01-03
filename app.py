import streamlit as st
import sys
from pathlib import Path

# Ajouter le dossier parent au path pour les imports
sys.path.append(str(Path(__file__).parent))

from data.series import SERIES_DATA
from data.metiers import METIERS_DATA
from data.chatbot_responses import CHATBOT_RESPONSES
from data.universites import UNIVERSITES_PUBLIQUES, UNIVERSITES_PRIVEES_PRINCIPALES, trouver_ecoles_par_domaine
from data.debouches_secteurs import DEBOUCHES_PAR_SECTEUR, obtenir_metiers_forte_demande
from utils.scoring import calculer_recommandations_texte_libre
from utils.Ikigai import calculer_score_ikigai

# Configuration de la page
st.set_page_config(
    page_title="Kpékpé - Ton guide d'orientation",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS personnalisé - Design épuré avec couleurs nudes
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    .main-header {
        background: linear-gradient(135deg, #E8DDD3 0%, #D4C4B0 100%);
        padding: 3rem 2rem;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
    
    .main-header h1 {
        color: #5C4D42;
        font-weight: 600;
        margin-bottom: 0.5rem;
        font-size: 2.5rem;
    }
    
    .main-header p {
        color: #7A6C5D;
        font-weight: 300;
        font-size: 1.1rem;
    }
    
    .stButton>button {
        background-color: #9C8B7A;
        color: white;
        border-radius: 8px;
        padding: 0.75rem 2rem;
        font-weight: 500;
        border: none;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        background-color: #8A7869;
        box-shadow: 0 4px 12px rgba(156, 139, 122, 0.3);
    }
    
    .section-header {
        color: #5C4D42;
        font-weight: 600;
        font-size: 1.5rem;
        margin-top: 2rem;
        margin-bottom: 1rem;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #E8DDD3;
    }
    
    .question-context {
        background-color: #FAF8F6;
        padding: 1rem;
        border-radius: 8px;
        border-left: 3px solid #C9B8A5;
        margin-bottom: 1rem;
        color: #6B5D52;
        font-size: 0.95rem;
        line-style: italic;
    }
    
    .result-card {
        background-color: #FAF8F6;
        padding: 2rem;
        border-radius: 12px;
        border-left: 4px solid #9C8B7A;
        margin-bottom: 1.5rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
    
    .result-card h3 {
        color: #5C4D42;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    
    .result-score {
        color: #9C8B7A;
        font-weight: 600;
        font-size: 1.2rem;
    }
    
    .chatbot-container {
        background-color: #F5F3F0;
        padding: 1.5rem;
        border-radius: 12px;
        margin-top: 3rem;
        border: 1px solid #E8DDD3;
    }
    
    .stTextArea textarea {
        border-radius: 8px;
        border: 1px solid #D4C4B0;
        font-family: 'Inter', sans-serif;
    }
    
    .stTextInput input {
        border-radius: 8px;
        border: 1px solid #D4C4B0;
    }
    
    .helper-text {
        color: #9C8B7A;
        font-size: 0.85rem;
        font-style: italic;
        margin-top: 0.3rem;
    }
    
    .info-box {
        background-color: #F5F3F0;
        padding: 1rem;
        border-radius: 8px;
        color: #6B5D52;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Initialisation de la session
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'quiz_started' not in st.session_state:
    st.session_state.quiz_started = False
if 'quiz_completed' not in st.session_state:
    st.session_state.quiz_completed = False
if 'responses' not in st.session_state:
    st.session_state.responses = {}

# Fonction d'authentification
def check_password():
    """Vérifie le mot de passe"""
    st.markdown('<div class="main-header"><h1>Kpékpé</h1><p>Découvre ton orientation scolaire et professionnelle</p></div>', unsafe_allow_html=True)
    
    st.markdown('<div class="info-box">Cette application est en phase de test. Merci d\'entrer le code d\'accès pour continuer.</div>', unsafe_allow_html=True)
    
    password = st.text_input("Code d'accès", type="password")
    
    if st.button("Accéder à l'application"):
        if password == "kpekpe2025":
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("Code d'accès incorrect. Contacte l'équipe Kpékpé pour obtenir l'accès.")

# Page d'accueil
def page_accueil():
    st.markdown('<div class="main-header"><h1>Kpékpé</h1><p>Trouve ta voie, construis ton avenir</p></div>', unsafe_allow_html=True)
    
    st.markdown("""
    ### Bienvenue
    
    Kpékpé t'accompagne dans ta réflexion sur ton orientation scolaire ou professionnelle. 
    Ce n'est pas un simple questionnaire, mais un moment pour mieux te comprendre.
    
    **Ce que nous allons explorer ensemble :**
    
    - Ce qui te passionne vraiment dans la vie
    - Les talents et forces que tu possèdes déjà
    - L'impact que tu souhaites avoir dans le monde
    - Tes priorités pour ton avenir professionnel
    
    À la fin, tu recevras des pistes d'orientation personnalisées, adaptées au contexte togolais.
    """)
    
    st.markdown('<p class="section-header">Commençons par te connaître</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Je suis en classe de 3ème", use_container_width=True):
            st.session_state.profil = "collegien"
            st.session_state.quiz_started = True
            st.rerun()
    
    with col2:
        if st.button("Je suis lycéen ou bachelier", use_container_width=True):
            st.session_state.profil = "lyceen"
            st.session_state.quiz_started = True
            st.rerun()

# Quiz avec questions ouvertes
def page_quiz():
    st.markdown('<div class="main-header"><h1>Questionnaire d\'orientation</h1></div>', unsafe_allow_html=True)
    
    profil = st.session_state.profil
    profil_text = "Collégien (3ème)" if profil == "collegien" else "Lycéen/Bachelier"
    
    st.markdown(f'<div class="info-box">Profil sélectionné : {profil_text}</div>', unsafe_allow_html=True)
    
    st.markdown("""
    Prends ton temps pour répondre. Il n'y a pas de bonne ou mauvaise réponse. 
    L'important est d'être sincère avec toi-même.
    """)
    
    # Section A : Ce qui te passionne
    st.markdown('<p class="section-header">Ce qui te passionne</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="question-context">
    Pense à ces moments où tu es vraiment absorbé par ce que tu fais, où le temps passe sans que tu t'en rendes compte. 
    Qu'est-ce qui te donne cette sensation ?
    </div>
    """, unsafe_allow_html=True)
    
    passion_principale = st.text_area(
        "Décris en quelques phrases ce que tu aimes vraiment faire",
        height=120,
        placeholder="Par exemple : J'adore comprendre comment les choses fonctionnent, démonter des objets pour voir ce qu'il y a à l'intérieur...",
        key="passion_principale"
    )
    st.markdown('<p class="helper-text">Sois aussi précis que possible. Pense aux activités, aux matières, aux moments où tu te sens vraiment toi-même.</p>', unsafe_allow_html=True)
    
    st.markdown("**Pour t'aider à réfléchir, coche ce qui résonne avec toi :**")
    
    col1, col2 = st.columns(2)
    with col1:
        matieres_preferees = st.multiselect(
            "Matières qui t'intéressent vraiment",
            ["Mathématiques", "Physique-Chimie", "SVT", "Français", "Anglais", 
             "Histoire-Géographie", "Philosophie", "Économie", "Arts", "Sport", 
             "Technologie", "Informatique"],
            key="matieres_preferees"
        )
    
    with col2:
        activites_favorites = st.multiselect(
            "Types d'activités que tu apprécies",
            ["Lire et écrire", "Créer et dessiner", "Calculer et analyser", "Parler et convaincre",
             "Construire et réparer", "Aider les autres", "Organiser et gérer", 
             "Utiliser l'ordinateur", "Expérimenter et tester"],
            key="activites_favorites"
        )
    
    # Section B : Tes forces naturelles
    st.markdown('<p class="section-header">Tes forces naturelles</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="question-context">
    On a tous des choses qu'on fait plus facilement que d'autres. Parfois, on ne s'en rend même pas compte parce que ça nous semble naturel.
    Qu'est-ce que les gens autour de toi remarquent chez toi ? Qu'est-ce qu'on te demande souvent de faire ?
    </div>
    """, unsafe_allow_html=True)
    
    forces_naturelles = st.text_area(
        "Décris les choses pour lesquelles tu es doué, même si ça te paraît simple",
        height=120,
        placeholder="Par exemple : Mes amis viennent toujours me voir quand ils ont un problème à résoudre. Je suis patient et j'arrive à expliquer les choses clairement...",
        key="forces_naturelles"
    )
    st.markdown('<p class="helper-text">N\'hésite pas à être honnête. Ce ne sont pas des vantardises, juste des observations sur toi-même.</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        matieres_fortes = st.multiselect(
            "Matières où tu réussis bien",
            ["Mathématiques", "Physique-Chimie", "SVT", "Français", "Anglais", 
             "Histoire-Géographie", "Philosophie", "Économie", "Arts", "Sport", 
             "Technologie", "Informatique"],
            key="matieres_fortes"
        )
    
    with col2:
        talents = st.multiselect(
            "Talents que tu reconnais en toi",
            ["Logique et raisonnement", "Créativité", "Communication", "Habileté manuelle",
             "Leadership", "Empathie", "Organisation", "Sens technique"],
            key="talents"
        )
    
    # Section C : Ton impact souhaité
    st.markdown('<p class="section-header">L\'impact que tu veux avoir</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="question-context">
    Si tu pouvais améliorer quelque chose dans le monde, dans ton pays, dans ta communauté, ce serait quoi ?
    Quel problème te touche particulièrement ?
    </div>
    """, unsafe_allow_html=True)
    
    impact_souhaite = st.text_area(
        "Décris le changement que tu aimerais voir ou contribuer à créer",
        height=120,
        placeholder="Par exemple : Je vois que beaucoup de gens tombent malades à cause du manque d'accès aux soins. J'aimerais que chacun puisse se faire soigner facilement...",
        key="impact_souhaite"
    )
    st.markdown('<p class="helper-text">Il n\'y a pas de petit ou grand impact. Ce qui compte, c\'est ce qui te parle vraiment.</p>', unsafe_allow_html=True)
    
    probleme = st.selectbox(
        "Si tu devais choisir un domaine prioritaire",
        ["Santé et bien-être", "Éducation et formation", "Environnement et climat", 
         "Technologie et innovation", "Réduction de la pauvreté", "Construction et infrastructure", 
         "Commerce et économie", "Justice et droits", "Agriculture et alimentation"],
        key="probleme"
    )
    
    # Section D : Tes priorités et contraintes
    st.markdown('<p class="section-header">Tes priorités pour l\'avenir</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="question-context">
    Soyons réalistes et honnêtes. Chaque choix d'orientation a des implications pratiques.
    Qu'est-ce qui est important pour toi dans ton futur métier ?
    </div>
    """, unsafe_allow_html=True)
    
    priorites_personnelles = st.text_area(
        "Décris ce qui compte vraiment pour toi dans ton futur professionnel",
        height=100,
        placeholder="Par exemple : Je veux un métier qui me passionne mais aussi qui me permette d'aider ma famille. Je suis prêt à étudier longtemps si c'est nécessaire...",
        key="priorites_personnelles"
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        priorite = st.selectbox(
            "Ta priorité principale",
            ["Un bon salaire", "Faire ce qui me passionne", "Équilibre entre passion et salaire",
             "Avoir un impact social", "Avoir un emploi stable"],
            key="priorite"
        )
    
    with col2:
        contraintes = st.multiselect(
            "Tes contraintes actuelles",
            ["Budget limité pour les études", "Besoin de travailler rapidement",
             "Possibilité de faire de longues études", "Préférence pour des études courtes et pratiques"],
            key="contraintes"
        )
    
    st.markdown("---")
    
    col1, col2 = st.columns([1, 4])
    with col1:
        if st.button("Retour"):
            st.session_state.quiz_started = False
            st.rerun()
    
    with col2:
        if st.button("Voir mes recommandations", use_container_width=True):
            if passion_principale and forces_naturelles and impact_souhaite:
                st.session_state.responses = {
                    'passion_principale': passion_principale,
                    'matieres_preferees': matieres_preferees,
                    'activites_favorites': activites_favorites,
                    'forces_naturelles': forces_naturelles,
                    'matieres_fortes': matieres_fortes,
                    'talents': talents,
                    'impact_souhaite': impact_souhaite,
                    'probleme': probleme,
                    'priorites_personnelles': priorites_personnelles,
                    'priorite': priorite,
                    'contraintes': contraintes
                }
                st.session_state.quiz_completed = True
                st.rerun()
            else:
                st.warning("Merci de répondre aux trois questions principales en texte libre pour obtenir des recommandations personnalisées.")

# Page de résultats
def page_resultats():
    st.markdown('<div class="main-header"><h1>Tes résultats personnalisés</h1></div>', unsafe_allow_html=True)
    
    profil = st.session_state.profil
    responses = st.session_state.responses
    
    # Calculer les recommandations
    if profil == "collegien":
        recommandations = calculer_recommandations_texte_libre(responses, SERIES_DATA, profil)
        titre = "Séries recommandées pour toi"
    else:
        recommandations = calculer_recommandations_texte_libre(responses, METIERS_DATA, profil)
        titre = "Métiers et filières recommandés"
    
    st.markdown(f'<p class="section-header">{titre}</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
    Ces recommandations sont basées sur ce que tu nous as partagé. Ce sont des pistes pour t'aider à réfléchir, 
    pas des décisions définitives. Prends le temps d'explorer chaque option.
    </div>
    """, unsafe_allow_html=True)
    
    # Afficher les recommandations
    for i, rec in enumerate(recommandations[:3], 1):
        st.markdown(f"""
        <div class="result-card">
            <h3>{i}. {rec['nom']}</h3>
            <p class="result-score">Correspondance : {rec['score']}%</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Pourquoi cette recommandation ?**")
            st.write(rec['explication'])
            
            st.markdown("**Compétences à développer**")
            for comp in rec['competences'][:3]:
                st.write(f"• {comp}")
        
        with col2:
            st.markdown("**Débouchés au Togo**")
            for debouche in rec['debouches'][:3]:
                st.write(f"• {debouche}")
            
            st.markdown("**Durée d'études**")
            st.write(rec['duree'])
        
        st.markdown("---")
    
    # Bouton recommencer
    if st.button("Recommencer le questionnaire"):
        st.session_state.quiz_completed = False
        st.session_state.quiz_started = False
        st.session_state.responses = {}
        st.rerun()
    
    # Chatbot
    afficher_chatbot(profil)

# Chatbot enrichi
def afficher_chatbot(profil):
    st.markdown('<p class="section-header">Des questions ?</p>', unsafe_allow_html=True)
    
    st.markdown('<div class="chatbot-container">', unsafe_allow_html=True)
    
    st.markdown("""
    Tu peux poser tes questions ici. Je ferai de mon mieux pour t'aider à mieux comprendre tes options.
    """)
    
    # Questions fréquentes enrichies
    questions_frequentes = list(CHATBOT_RESPONSES.keys())
    
    question = st.selectbox(
        "Sélectionne une question",
        ["Choisis une question..."] + questions_frequentes,
        key="chatbot_question"
    )
    
    question_personnalisee = st.text_input("Ou pose ta propre question")
    
    if st.button("Envoyer ma question"):
        reponse = None
        
        if question_personnalisee:
            # Chercher une réponse correspondante
            question_lower = question_personnalisee.lower()
            for q, r in CHATBOT_RESPONSES.items():
                if any(mot in question_lower for mot in q.lower().split()[:3]):
                    reponse = r
                    break
            
            if not reponse:
                reponse = "Je ne suis pas sûr de comprendre ta question. Peux-tu la reformuler ou choisir parmi les questions fréquentes ?"
        
        elif question != "Choisis une question...":
            reponse = CHATBOT_RESPONSES.get(question)
        
        if reponse:
            st.markdown(f'<div class="info-box"><strong>Réponse :</strong><br>{reponse}</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Application principale
def main():
    if not st.session_state.authenticated:
        check_password()
    else:
        if not st.session_state.quiz_started:
            page_accueil()
        elif not st.session_state.quiz_completed:
            page_quiz()
        else:
            page_resultats()

if __name__ == "__main__":
    main()

