import streamlit as st
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from data.series import SERIES_DATA
from data.Metier import METIERS_DATA
from data.chatbot_responses import CHATBOT_RESPONSES
from data.universites import UNIVERSITES_PUBLIQUES, UNIVERSITES_PRIVEES_PRINCIPALES, trouver_ecoles_par_domaine
from data.debouches_secteurs import DEBOUCHES_PAR_SECTEUR
from utils.scoring import calculer_recommandations_texte_libre

st.set_page_config(
    page_title="Kpékpé - Light on your way",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS avec couleurs du logo Kpékpé
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
    
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    .main {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
    }
    
    .main-header {
        background: linear-gradient(135deg, #004B87 0%, #0066b3 100%);
        padding: 2.5rem 2rem;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 4px 15px rgba(0, 75, 135, 0.2);
        border: 3px solid #FF6B35;
    }
    
    .main-header h1 {
        color: white;
        font-weight: 700;
        margin-bottom: 0.5rem;
        font-size: 3rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }
    
    .main-header .slogan {
        color: #FDB913;
        font-weight: 500;
        font-size: 1.4rem;
        font-style: italic;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
    }
    
    .stButton>button {
        background: linear-gradient(135deg, #FF6B35 0%, #ff8c5a 100%);
        color: white;
        border-radius: 12px;
        padding: 0.9rem 2.5rem;
        font-weight: 600;
        border: none;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(255, 107, 53, 0.3);
    }
    
    .stButton>button:hover {
        background: linear-gradient(135deg, #e55a2b 0%, #ff6b35 100%);
        box-shadow: 0 6px 20px rgba(255, 107, 53, 0.5);
        transform: translateY(-2px);
    }
    
    .section-header {
        color: #004B87;
        font-weight: 700;
        font-size: 1.8rem;
        margin-top: 2rem;
        margin-bottom: 1.5rem;
        padding-bottom: 0.8rem;
        border-bottom: 3px solid #FF6B35;
        background: linear-gradient(90deg, rgba(255,107,53,0.1) 0%, rgba(253,185,19,0.1) 100%);
        padding-left: 1rem;
        border-radius: 8px;
    }
    
    .question-context {
        background: linear-gradient(135deg, #fff9f0 0%, #fff5e6 100%);
        padding: 1.3rem;
        border-radius: 10px;
        border-left: 4px solid #FDB913;
        margin-bottom: 1.2rem;
        color: #2d3748;
        font-size: 1rem;
        box-shadow: 0 2px 8px rgba(253, 185, 19, 0.15);
    }
    
    .result-card {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        border-left: 6px solid #004B87;
        margin-bottom: 2rem;
        box-shadow: 0 4px 15px rgba(0, 75, 135, 0.15);
    }
    
    .result-card h3 {
        color: #004B87;
        font-weight: 700;
        margin-bottom: 0.8rem;
    }
    
    .result-score {
        background: linear-gradient(135deg, #FF6B35 0%, #FDB913 100%);
        color: white;
        font-weight: 700;
        font-size: 1.3rem;
        padding: 0.5rem 1.5rem;
        border-radius: 25px;
        display: inline-block;
        margin-bottom: 1rem;
    }
    
    .chatbot-container {
        background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-top: 3rem;
        border: 2px solid #004B87;
    }
    
    .info-box {
        background: linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%);
        padding: 1.3rem;
        border-radius: 10px;
        color: #2d3748;
        margin-bottom: 1.5rem;
        border-left: 4px solid #FF6B35;
    }
    
    .welcome-section {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    }
    
    .feature-box {
        background: linear-gradient(135deg, #f0f7ff 0%, #e3f2fd 100%);
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
        border-left: 4px solid #004B87;
    }
    
    .university-box {
        background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%);
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        border-left: 3px solid #2e7d32;
    }
</style>
""", unsafe_allow_html=True)

# Matières officielles du système togolais
MATIERES_TOGO = [
    "Mathématiques",
    "Physique-Chimie-Technologie (PCT)",
    "Sciences de la Vie et de la Terre (SVT)",
    "Français",
    "Anglais",
    "Histoire-Géographie",
    "Philosophie",
    "Économie",
    "Éducation Civique et Morale",
    "Arts",
    "Éducation Physique et Sportive (EPS)",
    "Technologie",
    "Informatique"
]

if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'quiz_started' not in st.session_state:
    st.session_state.quiz_started = False
if 'quiz_completed' not in st.session_state:
    st.session_state.quiz_completed = False
if 'responses' not in st.session_state:
    st.session_state.responses = {}
if 'recommendations' not in st.session_state:
    st.session_state.recommendations = []

def check_password():
    st.markdown("<div class='main-header'><h1>KPÉKPÉ</h1><p class='slogan'>Light on your way</p></div>", unsafe_allow_html=True)
    
    st.info("Cette application est en phase de test. Merci d'entrer le code d'accès.")
    
    password = st.text_input("Code d'accès", type="password")
    
    if st.button("Accéder à l'application"):
        if password == "kpekpe2025":
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("Code incorrect. Contacte l'équipe Kpékpé.")

def page_accueil():
    # Header sans HTML problématique
    st.markdown("<div class='main-header'><h1>KPÉKPÉ</h1><p class='slogan'>Light on your way</p></div>", unsafe_allow_html=True)
    
    # Contenu avec st.container au lieu de HTML
    with st.container():
        st.markdown("## Bienvenue")
        st.write("Kpékpé t'accompagne dans ta réflexion sur ton orientation scolaire ou professionnelle.")
        
        st.info("**Ce qui te passionne vraiment** - Découvre ce qui fait vibrer ton cœur.")
        st.info("**Tes talents naturels** - Identifie les forces que tu possèdes déjà.")
        st.info("**L'impact que tu veux avoir** - Réfléchis au changement que tu souhaites apporter.")
        st.info("**Tes priorités professionnelles** - Définis ce qui compte pour ton avenir.")
    
    st.markdown("---")
    st.subheader("Commençons par te connaître")
    
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

def page_quiz():
    st.markdown("<div class='main-header'><h1>Questionnaire d'orientation</h1><p class='slogan'>Light on your way</p></div>", unsafe_allow_html=True)
    
    profil = st.session_state.profil
    profil_text = "Collégien (3ème)" if profil == "collegien" else "Lycéen/Bachelier"
    
    st.info(f"Profil sélectionné : **{profil_text}**")
    st.write("Prends ton temps pour répondre. Il n'y a pas de bonne ou mauvaise réponse.")
    
    st.subheader("Ce qui te passionne")
    
    st.write("Pense à ces moments où tu es vraiment absorbé par ce que tu fais.")
    
    passion_principale = st.text_area(
        "Décris en quelques phrases ce que tu aimes vraiment faire",
        height=130,
        placeholder="Exemple : J'adore comprendre comment les choses fonctionnent...",
        key="passion_principale"
    )
    st.caption("Sois aussi précis que possible.")
    
    st.write("**Pour t'aider, coche ce qui résonne avec toi :**")
    
    col1, col2 = st.columns(2)
    with col1:
        matieres_preferees = st.multiselect(
            "Matières qui t'intéressent",
            MATIERES_TOGO,
            key="matieres_preferees"
        )
    
    with col2:
        activites_favorites = st.multiselect(
            "Types d'activités",
            ["Lire et écrire", "Créer et dessiner", "Calculer et analyser", "Parler et convaincre",
             "Construire et réparer", "Aider les autres", "Organiser et gérer", 
             "Utiliser l'ordinateur", "Expérimenter et tester"],
            key="activites_favorites"
        )
    
    st.subheader("Tes forces naturelles")
    
    st.write("On a tous des choses qu'on fait plus facilement que d'autres. Qu'est-ce que les gens remarquent chez toi ?")
    
    forces_naturelles = st.text_area(
        "Décris les choses pour lesquelles tu es doué",
        height=130,
        placeholder="Exemple : Mes amis viennent me voir quand ils ont un problème...",
        key="forces_naturelles"
    )
    st.caption("Sois honnête avec tes forces.")
    
    col1, col2 = st.columns(2)
    with col1:
        matieres_fortes = st.multiselect(
            "Matières où tu réussis",
            MATIERES_TOGO,
            key="matieres_fortes"
        )
    
    with col2:
        talents = st.multiselect(
            "Talents que tu reconnais",
            ["Logique et raisonnement", "Créativité", "Communication", "Habileté manuelle",
             "Leadership", "Empathie", "Organisation", "Sens technique"],
            key="talents"
        )
    
    st.subheader("L'impact que tu veux avoir")
    
    st.write("Si tu pouvais améliorer quelque chose, ce serait quoi ?")
    
    impact_souhaite = st.text_area(
        "Décris le changement que tu aimerais créer",
        height=130,
        placeholder="Exemple : Je vois que beaucoup de gens tombent malades...",
        key="impact_souhaite"
    )
    
    probleme = st.selectbox(
        "Domaine prioritaire",
        ["Santé et bien-être", "Éducation et formation", "Environnement et climat", 
         "Technologie et innovation", "Réduction de la pauvreté", "Construction et infrastructure", 
         "Commerce et économie", "Justice et droits", "Agriculture et alimentation"],
        key="probleme"
    )
    
    st.subheader("Tes priorités")
    
    priorites_personnelles = st.text_area(
        "Ce qui compte pour ton futur professionnel",
        height=100,
        placeholder="Exemple : Je veux un métier qui me passionne mais qui aide aussi ma famille...",
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
            "Tes contraintes",
            ["Budget limité pour les études", "Besoin de travailler rapidement",
             "Possibilité de faire de longues études", "Préférence pour des études courtes"],
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
                st.warning("Merci de répondre aux trois questions principales en texte libre.")

def page_resultats():
    st.markdown("<div class='main-header'><h1>Tes résultats</h1><p class='slogan'>Light on your way</p></div>", unsafe_allow_html=True)
    
    profil = st.session_state.profil
    responses = st.session_state.responses
    
    if profil == "collegien":
        recommandations = calculer_recommandations_texte_libre(responses, SERIES_DATA, profil)
        titre = "Séries recommandées"
    else:
        recommandations = calculer_recommandations_texte_libre(responses, METIERS_DATA, profil)
        titre = "Métiers et filières recommandés"
    
    st.session_state.recommendations = recommandations
    
    st.subheader(titre)
    
    st.info("Ces recommandations sont basées sur ton profil. Ce sont des pistes pour t'aider à réfléchir.")
    
    for i, rec in enumerate(recommandations[:3], 1):
        st.markdown(f"### {i}. {rec['nom']}")
        st.success(f"Correspondance : {rec['score']}%")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Pourquoi cette recommandation**")
            st.write(rec['explication'])
            
            st.markdown("**Compétences nécessaires**")
            for comp in rec['competences'][:3]:
                st.write(f"• {comp}")
        
        with col2:
            st.markdown("**Débouchés au Togo**")
            for debouche in rec['debouches'][:3]:
                st.write(f"• {debouche}")
            
            st.markdown("**Durée d'études**")
            st.write(rec['duree'])
            
            # Universités recommandées
            if profil == "lyceen":
                st.markdown("**Où étudier au Togo**")
                domaine_map = {
                    "Santé": ["médecin", "pharmacien", "infirmier", "sage"],
                    "Technologie/Innovation": ["informatique", "ingénieur", "développeur"],
                    "Commerce/Économie": ["comptable", "commercial", "gestion", "finance"],
                    "Construction/Infrastructure": ["génie civil", "btp", "architecte"],
                    "Agriculture/Alimentation": ["agronome", "agriculture"],
                    "Éducation": ["professeur", "enseignant"],
                    "Justice/Droit": ["avocat", "droit"]
                }
                
                nom_lower = rec['nom'].lower()
                ecoles_trouvees = []
                
                for domaine, mots_cles in domaine_map.items():
                    if any(mot in nom_lower for mot in mots_cles):
                        ecoles = trouver_ecoles_par_domaine(domaine)
                        if ecoles:
                            ecoles_trouvees = ecoles[:2]
                            break
                
                if ecoles_trouvees:
                    for ecole in ecoles_trouvees:
                        st.success(f"**{ecole['nom']}** - {ecole['type']} | {ecole['cout']}")
                else:
                    st.success("**Université de Lomé** - Public | 50 000-100 000 FCFA/an")
        
        st.markdown("---")
    
    if st.button("Recommencer le questionnaire"):
        st.session_state.quiz_completed = False
        st.session_state.quiz_started = False
        st.session_state.responses = {}
        st.session_state.recommendations = []
        st.rerun()
    
    afficher_chatbot()

def afficher_chatbot():
    st.subheader("Des questions ?")
    
    st.write("Tu peux poser tes questions ici.")
    
    # Questions contextuelles selon les recommandations
    if st.session_state.recommendations:
        st.write("**Questions sur tes recommandations :**")
        
        for rec in st.session_state.recommendations[:3]:
            nom = rec['nom']
            if st.button(f"Quelles universités pour {nom} ?", key=f"univ_{nom}"):
                st.info(f"Pour {nom}, consulte les établissements affichés ci-dessus.")
    
    st.markdown("---")
    st.write("**Questions générales :**")
    
    questions_frequentes = list(CHATBOT_RESPONSES.keys())
    
    question = st.selectbox(
        "Sélectionne une question",
        ["Choisis une question..."] + questions_frequentes,
        key="chatbot_question"
    )
    
    question_personnalisee = st.text_input("Ou pose ta propre question")
    
    if st.button("Envoyer"):
        reponse = None
        
        if question_personnalisee:
            question_lower = question_personnalisee.lower()
            for q, r in CHATBOT_RESPONSES.items():
                if any(mot in question_lower for mot in q.lower().split()[:3]):
                    reponse = r
                    break
            
            if not reponse:
                reponse = "Je ne comprends pas ta question. Peux-tu la reformuler ou choisir parmi les questions fréquentes ?"
        
        elif question != "Choisis une question...":
            reponse = CHATBOT_RESPONSES.get(question)
        
        if reponse:
            st.info(f"**Réponse :** {reponse}")


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
