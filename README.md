# 🎓 Kpékpé - Application d'Orientation Scolaire et Professionnelle

**Kpékpé** est une application web d'orientation destinée aux jeunes togolais (collégiens et lycéens) pour les aider à choisir leur série ou leur métier grâce à un quiz personnalisé basé sur le concept Ikigaï.

---

## 📋 Table des matières

1. [Description](#description)
2. [Fonctionnalités](#fonctionnalités)
3. [Installation](#installation)
4. [Utilisation](#utilisation)
5. [Structure du projet](#structure-du-projet)
6. [Déploiement](#déploiement)
7. [Exemples de profils](#exemples-de-profils)
8. [Contribuer](#contribuer)

---

## 🎯 Description

### Objectif
Aider les jeunes togolais à choisir leur orientation scolaire ou professionnelle en se basant sur :
- 💚 Ce qu'ils **AIMENT** faire
- 🌟 Ce dans quoi ils sont **DOUÉS**
- 🌍 L'**IMPACT** qu'ils veulent avoir
- 💼 Leurs **PRIORITÉS** professionnelles

### Public cible
- **Collégiens de 3ème** : Choix de série pour le lycée (parmi 12 séries)
- **Lycéens/Bacheliers** : Choix de métier/filière post-BAC

### Concept Ikigaï
L'application utilise le concept japonais **Ikigaï** (raison d'être) qui croise 4 dimensions pour trouver la voie idéale.

---

## ✨ Fonctionnalités

### 1. Authentification sécurisée
- Mot de passe d'accès : `kpekpe2025`
- Accès réservé à l'équipe de test

### 2. Sélection du profil
- Collégien (3ème)
- Lycéen/Bachelier

### 3. Quiz Ikigaï (4 dimensions)
**A. Ce que tu AIMES**
- Matières préférées (12 choix)
- Activités favorites (9 choix)

**B. Ce dans quoi tu es BON**
- Matières fortes (12 choix)
- Talents naturels (8 choix)

**C. Ce dont le monde a BESOIN**
- Problème à résoudre (9 choix)

**D. Ce pour quoi tu peux être PAYÉ**
- Priorité professionnelle (5 choix)
- Contraintes (4 choix multiples)

### 4. Recommandations personnalisées

**Pour Collégiens - 12 séries togolaises :**

**Séries Générales (🎓) :**
- A4 (Lettres/Sciences Sociales)
- C (Sciences Mathématiques)
- D (Sciences de la Nature)

**Séries Techniques - Industrielles (🔧) :**
- E (Mathématiques et Techniques)
- F1 (Construction Mécanique)
- F2 (Électronique)
- F3 (Électrotechnique)
- F4 (Génie Civil)
- TI (Chaudronnerie, Tuyauterie)

**Séries Techniques - Tertiaires (💼) :**
- G1 (Techniques Administratives)
- G2 (Techniques Quantitatives de Gestion)
- G3 (Techniques Commerciales)

**Pour Lycéens - 18+ métiers/filières** incluant :
- Santé (Médecin, Pharmacien, Infirmier, Sage-femme)
- Ingénierie (Génie Civil, Informatique, Électrique)
- Commerce/Management
- Droit
- Enseignement
- Architecture
- Communication
- Agriculture
- Entrepreneuriat
- Métiers techniques

### 5. Affichage des résultats
Chaque recommandation inclut :
- Score de correspondance (%)
- Badge visuel (🎓 Général / 🔧 Technique-Industriel / 💼 Technique-Tertiaire)
- Explication personnalisée (pourquoi ça correspond)
- Compétences nécessaires
- Débouchés concrets au Togo
- Durée d'études

### 6. Chatbot FAQ
Répond à 13+ questions fréquentes :
- Différences entre séries C et D
- Différences entre séries F et G
- Meilleure série pour devenir ingénieur
- Débouchés de la série A4
- Durée d'études pour médecin
- Possibilité de changer de série
- Meilleures écoles au Togo
- Financement des études
- BAC 1 vs BAC 2
- Valorisation des séries techniques
- Et plus encore...

---

## 🚀 Installation

### Prérequis
- Python 3.11 ou supérieur
- pip (gestionnaire de paquets Python)

### Étapes d'installation

1. **Cloner ou télécharger le projet**
```bash
# Créer le dossier du projet
mkdir kpekpe_prototype
cd kpekpe_prototype
```

2. **Créer la structure des dossiers**
```bash
mkdir data utils
```

3. **Créer les fichiers** (copier le contenu des artifacts Claude) :
- `app.py`
- `data/series.py`
- `data/metiers.py`
- `data/chatbot_responses.py`
- `utils/scoring.py`
- `utils/ikigai.py`
- `requirements.txt`

4. **Créer un environnement virtuel (recommandé)**
```bash
python -m venv venv

# Activer l'environnement
# Sur Windows :
venv\Scripts\activate
# Sur Mac/Linux :
source venv/bin/activate
```

5. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

---

## 💻 Utilisation

### Lancer l'application en local

```bash
streamlit run app.py
```

L'application s'ouvrira automatiquement dans votre navigateur à l'adresse : `http://localhost:8501`

### Tester l'application

1. **Entrer le mot de passe** : `kpekpe2025`
2. **Choisir un profil** : Collégien ou Lycéen
3. **Répondre au quiz** : Sélectionner au minimum les matières préférées et activités favorites
4. **Voir les recommandations** : Top 3 séries ou métiers adaptés
5. **Poser des questions** au chatbot si besoin

---

## 📁 Structure du projet

```
kpekpe_prototype/
│
├── app.py                          # Application principale Streamlit
│   ├── Authentification
│   ├── Page d'accueil
│   ├── Quiz Ikigaï
│   ├── Affichage des résultats
│   └── Chatbot FAQ
│
├── data/                           # Données de l'application
│   ├── series.py                   # 12 séries togolaises (A4, C, D, E, F1-F4, TI, G1-G3)
│   ├── metiers.py                  # 18+ métiers/filières post-BAC
│   └── chatbot_responses.py        # 13+ réponses FAQ chatbot
│
├── utils/                          # Algorithmes et logique métier
│   ├── scoring.py                  # Algorithme de recommandation
│   │   ├── calculer_score_serie()
│   │   ├── calculer_score_metier()
│   │   └── calculer_recommandations()
│   │
│   └── ikigai.py                   # Logique Ikigaï (4 dimensions)
│       ├── calculer_score_ikigai()
│       ├── interpreter_ikigai()
│       └── get_recommendations_par_dimension()
│
├── requirements.txt                # Dépendances Python
└── README.md                       # Documentation (ce fichier)
```

---

## 🌐 Déploiement sur Streamlit Cloud

### Étapes pour déployer gratuitement

1. **Créer un compte sur GitHub** (si pas déjà fait) : https://github.com

2. **Créer un nouveau repository** :
   - Nom : `kpekpe-prototype`
   - Public ou Private
   - Uploader tous les fichiers du projet

3. **Créer un compte sur Streamlit Cloud** : https://streamlit.io/cloud
   - Se connecter avec GitHub

4. **Déployer l'application** :
   - Cliquer sur "New app"
   - Sélectionner le repository `kpekpe-prototype`
   - Main file : `app.py`
   - Cliquer sur "Deploy"

5. **L'application sera accessible via une URL publique** du type :
   ```
   https://kpekpe-prototype-xxxxx.streamlit.app
   ```

6. **Partager le lien** avec ton équipe pour tester !

### Mettre à jour l'application
Pousser les changements sur GitHub → Streamlit Cloud redéploie automatiquement.

---

## 🧪 Exemples de profils testés

### Profil 1 : Futur Médecin
**Réponses :**
- Matières préférées : SVT, Physique-Chimie
- Matières fortes : SVT, Mathématiques
- Activités : Aider les autres, Expérimenter
- Talents : Empathie, Logique/Raisonnement
- Problème : Santé
- Priorité : Impact social

**Résultat attendu :** Série D (Sciences de la Nature) → Métier Médecin/Pharmacien

---

### Profil 2 : Futur Ingénieur BTP
**Réponses :**
- Matières préférées : Mathématiques, Technologie
- Matières fortes : Mathématiques, Physique-Chimie
- Activités : Construire/Réparer, Calculer/Analyser
- Talents : Logique/Raisonnement, Technique, Manuel/Pratique
- Problème : Construction/Infrastructure
- Priorité : Salaire élevé

**Résultat attendu :** Série F4 (Génie Civil) ou C → Métier Ingénieur Génie Civil

---

### Profil 3 : Futur Entrepreneur Commercial
**Réponses :**
- Matières préférées : Économie, Français
- Matières fortes : Économie, Mathématiques
- Activités : Parler/Convaincre, Organiser/Gérer
- Talents : Communication, Leadership
- Problème : Commerce/Économie
- Priorité : Équilibre salaire-passion
- Contraintes : Préférence études courtes et pratiques

**Résultat attendu :** Série G3 (Techniques Commerciales) → Métier Manager Commercial/Entrepreneur

---

### Profil 4 : Futur Développeur Web
**Réponses :**
- Matières préférées : Mathématiques, Informatique
- Matières fortes : Mathématiques, Informatique
- Activités : Utiliser l'ordinateur, Calculer/Analyser, Créer/Dessiner
- Talents : Logique/Raisonnement, Créativité, Technique
- Problème : Technologie/Innovation
- Priorité : Passion avant tout

**Résultat attendu :** Série C ou E → Métier Développeur Web/Ingénieur Informatique

---

### Profil 5 : Futur Avocat
**Réponses :**
- Matières préférées : Français, Philosophie, Histoire-Géographie
- Matières fortes : Français, Philosophie
- Activités : Lire/Écrire, Parler/Convaincre
- Talents : Communication, Empathie
- Problème : Justice/Droit
- Priorité : Impact social

**Résultat attendu :** Série A4 (Lettres et Sciences Sociales) → Métier Avocat

---

## 🎨 Design et UX

### Couleurs
- **Vert et Jaune** : Couleurs du drapeau togolais
- **Bleu/Violet** : Modernité et technologie
- **Orange** : Call-to-action (boutons)

### Ton
- Encourageant et bienveillant
- Adapté aux jeunes (15-20 ans)
- **Valorise TOUTES les séries** (techniques = aussi importantes que générales)
- Utilisation d'émojis pour rendre ludique

### Responsive
- L'application fonctionne parfaitement sur mobile, tablette et desktop
- Interface claire et intuitive

---

## 📊 Algorithme de Scoring

### Logique de calcul (100 points max)

**Pour les séries (Collégiens) :**
1. **Matières (40%)** : Correspondance matières fortes/préférées avec séries
   - Matières fortes : 25 points
   - Matières préférées : 15 points

2. **Talents/Activités (30%)** : Correspondance avec profil idéal
   - Talents : 20 points
   - Activités : 10 points

3. **Problème à résoudre (20%)** : Adéquation avec débouchés

4. **Contraintes économiques (10%)** : Favorise séries techniques si budget limité

**Bonus séries techniques :**
- Budget limité : +3 points
- Études courtes souhaitées : +3 points
- Besoin de travailler rapidement : +2 points

**Pour les métiers (Lycéens) :** Logique similaire adaptée aux métiers.

---

## 🔒 Sécurité

### Mot de passe
- Mot de passe unique : `kpekpe2025`
- Accès réservé à l'équipe de test
- Pas de stockage de données utilisateur (tout en mémoire)

### Données personnelles
- **Aucune donnée n'est stockée** en base de données
- Les réponses restent en mémoire pendant la session
- Respect de la vie privée des utilisateurs

---

## 🛠️ Technologies utilisées

- **Python 3.11+** : Langage de programmation
- **Streamlit 1.29.0** : Framework web pour prototypage rapide
- **Pandas 2.1.4** : Manipulation de données (si nécessaire)

---

## 🐛 Dépannage

### L'application ne démarre pas
```bash
# Vérifier que Streamlit est bien installé
pip install --upgrade streamlit

# Vérifier la version de Python
python --version  # Doit être >= 3.11
```

### Erreur d'import
```bash
# Vérifier que tous les fichiers sont présents
ls data/
ls utils/

# Réinstaller les dépendances
pip install -r requirements.txt --force-reinstall
```

### L'application est lente
- Streamlit peut être lent au premier lancement
- Rafraîchir la page si besoin
- Sur Streamlit Cloud, l'app se met en veille après inactivité (normal)

---

## 📈 Évolutions futures (post-MVP)

### Fonctionnalités avancées
- [ ] Graphique radar visualisant le profil Ikigaï
- [ ] Export des résultats en PDF
- [ ] Comparaison de plusieurs profils
- [ ] Statistiques anonymisées (nombre d'utilisateurs par série)
- [ ] Mode clair/sombre
- [ ] Intégration d'une vraie base de données
- [ ] Système de comptes utilisateurs
- [ ] Historique des quiz passés
- [ ] Notifications et rappels
- [ ] Version mobile native (iOS/Android)

### Données enrichies
- [ ] Plus de métiers (30+)
- [ ] Témoignages d'anciens élèves
- [ ] Vidéos métiers
- [ ] Grille salariale détaillée
- [ ] Carte des écoles togolaises
- [ ] Bourses disponibles

---

## 👥 Contribuer

Pour contribuer au projet :
1. Fork le repository
2. Créer une branche (`git checkout -b feature/amelioration`)
3. Commit les changements (`git commit -m 'Ajout fonctionnalité X'`)
4. Push vers la branche (`git push origin feature/amelioration`)
5. Ouvrir une Pull Request

---

## 📞 Contact

Pour toute question ou suggestion sur **Kpékpé**, contacte l'équipe via :
- Email : adadossi24@gmail.com
- Téléphone : 71162394

---

## 📄 Licence

Ce projet est développé dans le cadre de l'initiative **Kpékpé** pour l'orientation des jeunes togolais.

© 2025 Kpékpé - Tous droits réservés.

---

## 🙏 Remerciements

Merci à tous ceux qui contribuent à améliorer l'orientation des jeunes togolais !


**Ensemble, construisons l'avenir du Togo ! 🇹🇬🚀**
