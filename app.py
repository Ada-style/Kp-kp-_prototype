import streamlit as st
import sys
from pathlib import Path

# Ajouter le dossier parent au path pour les imports
sys.path.append(str(Path(__file__).parent))

from data.series import Serie
from data.Metier import Metier
from data.chatbot_responses import chatbot_responses
from utils.scoring import calculer_recommandations
from utils.ikigai import calculer_score_ikigai

# Configuration de la page
st.set_page_config(
    page_title="Kpékpé - Ton guide d'orientation",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS personnalisé
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #2E7D32 0%, #FDD835 100%);
        padding: 2rem;
        border-radius: 10px;
        text-align: center;
        color: white;
        margin-bottom: 2rem;
    }
    .stButton>button {
        background-color: #FF6B35;
        color: white;
        border-radius: 20px;
        padding: 0.5rem 2rem;
        font-weight: bold;
        border: none;
    }
    .stButton>button:hover {
        background-color: #E55A2B;
    }
    .result-card {
        background-color: #f0f8ff;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #2E7D32;
        margin-bottom: 1rem;
    }
    .chatbot-container {
        background-color: #f5f5f5;
        padding: 1rem;
        border-radius: 10px;
        margin-top: 2rem;
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
    st.markdown('<div class="main-header"><h1>🎓 Bienvenue sur Kpékpé</h1><p>Ton guide d\'orientation scolaire et professionnelle</p></div>', unsafe_allow_html=True)
    
    password = st.text_input("🔒 Mot de passe d'accès", type="password")
    
    if st.button("Accéder"):
        if password == "kpekpe2025":
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("❌ Accès réservé à l'équipe Kpékpé. Contacte-nous pour obtenir l'accès.")

# Page d'accueil
def page_accueil():
    st.markdown('<div class="main-header"><h1>🎓 Kpékpé</h1><h3>Trouve ta voie, construis ton avenir !</h3></div>', unsafe_allow_html=True)
    
    st.markdown("""
    ### 👋 Bienvenue !
    
    **Kpékpé** t'aide à choisir la bonne orientation scolaire ou professionnelle grâce à un quiz personnalisé basé sur tes passions, tes talents et tes aspirations.
    
    ✨ **Ce que nous allons découvrir ensemble :**
    - 💚 Ce que tu **AIMES** faire
    - 🌟 Ce dans quoi tu es **DOUÉ(E)**
    - 🌍 L'**IMPACT** que tu veux avoir
    - 💼 Tes **PRIORITÉS** professionnelles
    
    🎯 À la fin, tu recevras des recommandations personnalisées adaptées au contexte togolais !
    """)
    
    st.markdown("---")
    st.markdown("### 🎯 Qui es-tu ?")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🎒 Je suis en 3ème (Collégien)", use_container_width=True):
            st.session_state.profil = "collegien"
            st.session_state.quiz_started = True
            st.rerun()
    
    with col2:
        if st.button("🎓 Je suis Lycéen/Bachelier", use_container_width=True):
            st.session_state.profil = "lyceen"
            st.session_state.quiz_started = True
            st.rerun()

# Quiz Ikigaï
def page_quiz():
    st.markdown('<div class="main-header"><h1>📝 Quiz d\'Orientation Kpékpé</h1></div>', unsafe_allow_html=True)
    
    profil = st.session_state.profil
    profil_text = "Collégien (3ème)" if profil == "collegien" else "Lycéen/Bachelier"
    
    st.info(f"🎯 Profil sélectionné : **{profil_text}**")
    
    # Section A : Ce que tu AIMES
    st.markdown("## 💚 A. Ce que tu AIMES")
    
    matieres_preferees = st.multiselect(
        "📚 Quelles sont tes matières préférées ?",
        ["Mathématiques", "Physique-Chimie", "SVT", "Français", "Anglais", 
         "Histoire-Géographie", "Philosophie", "Économie", "Arts", "Sport", 
         "Technologie", "Informatique"],
        key="matieres_preferees"
    )
    
    activites_favorites = st.multiselect(
        "🎨 Quelles sont tes activités favorites ?",
        ["Lire/Écrire", "Créer/Dessiner", "Calculer/Analyser", "Parler/Convaincre",
         "Construire/Réparer", "Aider les autres", "Organiser/Gérer", 
         "Utiliser l'ordinateur", "Expérimenter"],
        key="activites_favorites"
    )
    
    # Section B : Ce dans quoi tu es BON
    st.markdown("## 🌟 B. Ce dans quoi tu es BON(NE)")
    
    matieres_fortes = st.multiselect(
        "💪 Dans quelles matières as-tu les meilleures notes ?",
        ["Mathématiques", "Physique-Chimie", "SVT", "Français", "Anglais", 
         "Histoire-Géographie", "Philosophie", "Économie", "Arts", "Sport", 
         "Technologie", "Informatique"],
        key="matieres_fortes"
    )
    
    talents = st.multiselect(
        "✨ Quels sont tes talents naturels ?",
        ["Logique/Raisonnement", "Créativité", "Communication", "Manuel/Pratique",
         "Leadership", "Empathie", "Organisation", "Technique"],
        key="talents"
    )
    
    # Section C : Ce dont le monde a besoin
    st.markdown("## 🌍 C. Ce dont le MONDE a besoin")
    
    probleme = st.selectbox(
        "🎯 Quel problème veux-tu contribuer à résoudre ?",
        ["Santé", "Éducation", "Environnement", "Technologie/Innovation",
         "Pauvreté/Développement", "Construction/Infrastructure", 
         "Commerce/Économie", "Justice/Droit", "Agriculture/Alimentation"],
        key="probleme"
    )
    
    # Section D : Ce pour quoi tu peux être payé
    st.markdown("## 💼 D. Ce pour quoi tu peux être PAYÉ(E)")
    
    priorite = st.selectbox(
        "💰 Quelle est ta priorité principale ?",
        ["Salaire élevé", "Passion avant tout", "Équilibre salaire-passion",
         "Impact social", "Stabilité de l'emploi"],
        key="priorite"
    )
    
    contraintes = st.multiselect(
        "⚠️ Quelles sont tes contraintes ?",
        ["Budget limité pour études", "Besoin de travailler rapidement",
         "Longues études acceptées", "Préférence études courtes et pratiques"],
        key="contraintes"
    )
    
    st.markdown("---")
    
    col1, col2 = st.columns([1, 4])
    with col1:
        if st.button("⬅️ Retour"):
            st.session_state.quiz_started = False
            st.rerun()
    
    with col2:
        if st.button("✅ Voir mes recommandations", use_container_width=True):
            if len(matieres_preferees) > 0 and len(activites_favorites) > 0:
                st.session_state.responses = {
                    'matieres_preferees': matieres_preferees,
                    'activites_favorites': activites_favorites,
                    'matieres_fortes': matieres_fortes,
                    'talents': talents,
                    'probleme': probleme,
                    'priorite': priorite,
                    'contraintes': contraintes
                }
                st.session_state.quiz_completed = True
                st.rerun()
            else:
                st.warning("⚠️ Merci de répondre au moins aux questions sur tes matières préférées et activités favorites !")

# Page de résultats
def page_resultats():
    st.markdown('<div class="main-header"><h1>🎉 Tes Résultats</h1></div>', unsafe_allow_html=True)
    
    profil = st.session_state.profil
    responses = st.session_state.responses
    
    # Calculer les recommandations
    if profil == "collegien":
        recommandations = calculer_recommandations(responses, SERIES_DATA, profil)
        titre = "📚 Séries recommandées pour toi"
    else:
        recommandations = calculer_recommandations(responses, METIERS_DATA, profil)
        titre = "💼 Métiers/Filières recommandés pour toi"
    
    st.markdown(f"## {titre}")
    st.success("✨ Voici les meilleures options basées sur ton profil Ikigaï !")
    
    # Afficher les recommandations
    for i, rec in enumerate(recommandations[:3], 1):
        with st.container():
            st.markdown(f"""
            <div class="result-card">
                <h3>#{i} - {rec['nom']} {rec.get('badge', '')}</h3>
                <p><strong>🎯 Correspondance : {rec['score']}%</strong></p>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown(f"**💡 Pourquoi ça te correspond :**")
                st.write(rec['explication'])
                
                st.markdown(f"**✨ Compétences nécessaires :**")
                for comp in rec['competences']:
                    st.write(f"• {comp}")
            
            with col2:
                st.markdown(f"**🎓 Débouchés au Togo :**")
                for debouche in rec['debouches']:
                    st.write(f"• {debouche}")
                
                st.markdown(f"**⏱️ Durée d'études :**")
                st.write(rec['duree'])
            
            st.markdown("---")
    
    # Bouton recommencer
    if st.button("🔄 Recommencer le quiz"):
        st.session_state.quiz_completed = False
        st.session_state.quiz_started = False
        st.session_state.responses = {}
        st.rerun()
    
    # Chatbot
    afficher_chatbot(profil)

# Chatbot
def afficher_chatbot(profil):
    st.markdown("---")
    st.markdown("## 💬 Des questions ? Chatbot Kpékpé")
    
    st.markdown('<div class="chatbot-container">', unsafe_allow_html=True)
    
    questions_frequentes = list(CHATBOT_RESPONSES.keys())
    
    question = st.selectbox(
        "🤔 Choisis une question ou pose la tienne :",
        ["Sélectionne une question..."] + questions_frequentes,
        key="chatbot_question"
    )
    
    question_personnalisee = st.text_input("✍️ Ou écris ta propre question :")
    
    if st.button("Envoyer"):
        reponse = None
        
        if question_personnalisee:
            # Chercher une réponse correspondante
            question_lower = question_personnalisee.lower()
            for q, r in CHATBOT_RESPONSES.items():
                if any(mot in question_lower for mot in q.lower().split()):
                    reponse = r
                    break
            
            if not reponse:
                reponse = "Je ne comprends pas encore cette question. Peux-tu la reformuler ou choisir parmi les questions fréquentes ? 🤔"
        
        elif question != "Sélectionne une question...":
            reponse = CHATBOT_RESPONSES.get(question)
        
        if reponse:
            st.info(f"🤖 **Kpékpé Bot :** {reponse}")
    
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




