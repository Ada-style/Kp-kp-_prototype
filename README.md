# Kpékpé - Prototype Interactif (Web App) 🇹🇬

![Kpékpé Logo](assets/img/kpekpe_logo_placeholder.png)

> **"Light on your way"** - L'assistant d'orientation intelligent pour la jeunesse togolaise.

Ce dépôt contient le code source du **Prototype Interactif de Kpékpé**.
Il s'agit d'une **Web App (HTML/CSS/JS)** légère et rapide, conçue pour aider les élèves et étudiants togolais à trouver leur voie grâce à une conversation naturelle.

🔗 **Démo en direct :** [Lien vers votre déploiement (ex: GitHub Pages)]

---

## 🌟 Fonctionnalités Clés

### 1. 🤖 Chatbot Intelligent
Plus de formulaires ennuyeux ! L'utilisateur discute avec **Kpékpé**, un assistant virtuel bienveillant.
- Interface type "WhatsApp" familière.
- Questions ouvertes et naturelles.
- Réponses rapides (Quick Replies).

### 2. 🧠 Test de Personnalité Intégré
Avant de conseiller, Kpékpé apprend à connaître l'utilisateur via un quiz de 15 questions basé sur la psychologie (4 profils) :
- **Analytique** (Logique & Faits)
- **Créatif** (Intuition & Innovation)
- **Méthodique** (Ordre & Rigueur)
- **Social** (Empathie & Contact)

### 3. 🇹🇬 Données 100% Togolaises
L'algorithme de recommandation s'appuie sur une base de données locale riche (`js/data.js`) :
- **50+ Métiers** détaillés (Salaires, Débouchés à Lomé/Kara, Entreprises qui recrutent).
- **Écoles & Universités** (UL, UK, EAMAU, UCAO, ESGIS, etc.).
- **Séries du BAC** (A4, C, D, E, F, G...).

### 4. 🎯 Matching "Ikigaï"
L'application croise :
1.  **Ce que tu aimes** (Analysé via le chat).
2.  **Ce pour quoi tu es doué** (Séries & Notes).
3.  **Ce dont le Togo a besoin** (Marché du travail local).
4.  **Ce qui est payé** (Réalité économique).

---

## 📂 Structure du Projet

```
/
├── index.html          # Page d'accueil (Vitrine)
├── conseiller.html     # APP : L'interface du Chatbot
├── css/
│   └── style.css       # Design System & Styles du Chat
├── js/
│   ├── chat.js         # Cerveau du Chatbot (Logique, State Machine, Matching)
│   ├── data.js         # Base de données (Métiers, Écoles, Profils)
│   └── script.js       # Scripts UI généraux
└── assets/             # Images & Icônes
```

## 🚀 Comment l'utiliser ?

1.  Clonez ce dépôt.
2.  Ouvrez `conseiller.html` dans votre navigateur.
3.  C'est tout ! Aucune installation (Python, Node.js) n'est requise. C'est du pur web.

## 🛠 Technologies

-   **HTML5 / CSS3** (Variables CSS, Flexbox, Grid)
-   **Vanilla JavaScript** (ES6+)
-   **Font Awesome** (Icônes)
-   **Google Fonts** (Outfit & Inter)

---

## 📝 Auteur

Projet développé pour **Kpékpé**.
*Light on your way.*
