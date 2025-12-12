"""
Données des métiers et filières accessibles après le BAC
"""

METIERS_DATA = {
    # SANTÉ
    "Médecin": {
        "nom": "Médecin",
        "badge": "⚕️",
        "domaine": "Santé",
        "series_recommandees": ["D", "C"],
        "matieres_importantes": ["SVT", "Physique-Chimie", "Mathématiques"],
        "competences": [
            "Excellence en sciences",
            "Empathie et écoute",
            "Résistance au stress",
            "Rigueur scientifique"
        ],
        "duree_etudes": "7-10 ans (BAC+7 minimum)",
        "debouches_togo": "Très demandé",
        "salaire": "Élevé",
        "niveau_requis": "BAC+7",
        "explication": "Tu as un excellent niveau scientifique et tu veux soigner les gens. La médecine demande beaucoup d'études mais offre un métier gratifiant et respecté.",
        "debouches_concrets": [
            "Hôpitaux publics (CHU Sylvanus Olympio)",
            "Cliniques privées (Biasa, Afia...)",
            "Médecin de brousse (zones rurales)"
        ]
    },
    
    "Pharmacien": {
        "nom": "Pharmacien",
        "badge": "💊",
        "domaine": "Santé",
        "series_recommandees": ["D", "C"],
        "matieres_importantes": ["SVT", "Physique-Chimie", "Mathématiques"],
        "competences": [
            "Bon en chimie et biologie",
            "Rigueur et précision",
            "Sens du commerce",
            "Conseil client"
        ],
        "duree_etudes": "6 ans (BAC+6)",
        "debouches_togo": "Très demandé",
        "salaire": "Élevé",
        "niveau_requis": "BAC+6",
        "explication": "Tu aimes la chimie et tu veux travailler dans le domaine de la santé avec une dimension commerce. Possibilité d'ouvrir ta propre pharmacie.",
        "debouches_concrets": [
            "Pharmacien d'officine (création possible)",
            "Pharmacien hospitalier",
            "Industrie pharmaceutique"
        ]
    },
    
    "Infirmier": {
        "nom": "Infirmier/Infirmière",
        "badge": "🩺",
        "domaine": "Santé",
        "series_recommandees": ["D", "C"],
        "matieres_importantes": ["SVT", "Physique-Chimie"],
        "competences": [
            "Empathie et patience",
            "Résistance physique",
            "Travail d'équipe",
            "Réactivité"
        ],
        "duree_etudes": "3 ans (BAC+3)",
        "debouches_togo": "Très demandé",
        "salaire": "Moyen",
        "niveau_requis": "BAC+3",
        "explication": "Tu veux soigner et aider les gens avec des études plus courtes que médecine. Métier humain avec recrutement garanti au Togo.",
        "debouches_concrets": [
            "Hôpitaux et cliniques",
            "Centres de santé publics",
            "ONG médicales (MSF, Croix-Rouge)"
        ]
    },
    
    "Sage-femme": {
        "nom": "Sage-femme",
        "badge": "🤱",
        "domaine": "Santé",
        "series_recommandees": ["D", "C"],
        "matieres_importantes": ["SVT", "Physique-Chimie"],
        "competences": [
            "Empathie",
            "Gestion du stress",
            "Connaissances médicales",
            "Accompagnement"
        ],
        "duree_etudes": "3-4 ans (BAC+3/4)",
        "debouches_togo": "Très demandé",
        "salaire": "Moyen",
        "niveau_requis": "BAC+3/4",
        "explication": "Tu veux accompagner les femmes et les bébés. Métier gratifiant et très recherché dans les zones rurales togolaises.",
        "debouches_concrets": [
            "Maternités publiques",
            "Cliniques privées",
            "ONG santé maternelle"
        ]
    },
    
    # INGÉNIERIE
    "Ingénieur Génie Civil": {
        "nom": "Ingénieur Génie Civil",
        "badge": "🏗️",
        "domaine": "Construction/Infrastructure",
        "series_recommandees": ["C", "F4", "E"],
        "matieres_importantes": ["Mathématiques", "Physique-Chimie", "Technologie"],
        "competences": [
            "Excellence en maths/physique",
            "Vision spatiale",
            "Gestion de projet",
            "Leadership"
        ],
        "duree_etudes": "5 ans (BAC+5)",
        "debouches_togo": "Très demandé",
        "salaire": "Élevé",
        "niveau_requis": "BAC+5",
        "explication": "Tu excelles en maths/physique et tu aimes construire. Le Togo a d'énormes besoins en infrastructures (routes, ponts, bâtiments).",
        "debouches_concrets": [
            "Bureaux d'études (BNETD, SCET-Togo)",
            "Entreprises BTP (Ebomaf, Maisons du Monde)",
            "Projets gouvernementaux"
        ]
    },
    
    "Ingénieur Informatique": {
        "nom": "Ingénieur Informatique",
        "badge": "💻",
        "domaine": "Technologie/Innovation",
        "series_recommandees": ["C", "E"],
        "matieres_importantes": ["Mathématiques", "Physique-Chimie", "Informatique"],
        "competences": [
            "Logique mathématique",
            "Programmation",
            "Résolution de problèmes",
            "Créativité technique"
        ],
        "duree_etudes": "5 ans (BAC+5)",
        "debouches_togo": "Émergent (forte croissance)",
        "salaire": "Élevé",
        "niveau_requis": "BAC+5",
        "explication": "Tu adores l'informatique et les maths. Secteur en plein boom au Togo avec la digitalisation. Possibilité de travailler à l'international.",
        "debouches_concrets": [
            "Startups tech togolaises (PayDunya, CinetPay)",
            "Banques (développement apps)",
            "Freelance développement"
        ]
    },
    
    "Ingénieur Électrique": {
        "nom": "Ingénieur Électrique/Électrotechnique",
        "badge": "⚡",
        "domaine": "Technologie/Innovation",
        "series_recommandees": ["C", "F3", "E"],
        "matieres_importantes": ["Mathématiques", "Physique-Chimie", "Technologie"],
        "competences": [
            "Maths/physique",
            "Électricité",
            "Résolution problèmes techniques",
            "Innovation"
        ],
        "duree_etudes": "5 ans (BAC+5)",
        "debouches_togo": "Demandé",
        "salaire": "Élevé",
        "niveau_requis": "BAC+5",
        "explication": "Tu es fort en sciences et tu t'intéresses à l'électricité et l'énergie. Secteur d'avenir avec les énergies renouvelables au Togo.",
        "debouches_concrets": [
            "CEET (Compagnie Énergie Électrique)",
            "Projets solaires",
            "Industries"
        ]
    },
    
    # INFORMATIQUE / TECH
    "Développeur Web": {
        "nom": "Développeur Web/Mobile",
        "badge": "👨‍💻",
        "domaine": "Technologie/Innovation",
        "series_recommandees": ["C", "E", "G2"],
        "matieres_importantes": ["Mathématiques", "Informatique"],
        "competences": [
            "Programmation",
            "Logique",
            "Créativité",
            "Autodidacte"
        ],
        "duree_etudes": "2-3 ans (BAC+2/3) ou autodidacte",
        "debouches_togo": "Émergent (forte demande)",
        "salaire": "Moyen à Élevé",
        "niveau_requis": "BAC+2/3",
        "explication": "Tu aimes coder et créer des applications. Métier accessible rapidement, forte demande au Togo. Possibilité de freelance international.",
        "debouches_concrets": [
            "Agences digitales (Lomé)",
            "Création de startups",
            "Freelance (clients internationaux)"
        ]
    },
    
    # COMMERCE / MANAGEMENT
    "Manager Commercial": {
        "nom": "Manager/Responsable Commercial",
        "badge": "📊",
        "domaine": "Commerce/Économie",
        "series_recommandees": ["G3", "G2", "A4"],
        "matieres_importantes": ["Économie", "Français", "Mathématiques"],
        "competences": [
            "Communication",
            "Leadership",
            "Négociation",
            "Gestion d'équipe"
        ],
        "duree_etudes": "3-5 ans (BAC+3/5)",
        "debouches_togo": "Demandé",
        "salaire": "Moyen à Élevé",
        "niveau_requis": "BAC+3/5",
        "explication": "Tu es bon communicant et tu aimes manager. Toutes les entreprises ont besoin de commerciaux qualifiés au Togo.",
        "debouches_concrets": [
            "Grandes entreprises (Ecobank, Togocel)",
            "PME togolaises",
            "Distribution (Carrefour Market, Orca)"
        ]
    },
    
    "Comptable": {
        "nom": "Comptable/Expert-comptable",
        "badge": "📚",
        "domaine": "Commerce/Économie",
        "series_recommandees": ["G2", "C"],
        "matieres_importantes": ["Mathématiques", "Économie"],
        "competences": [
            "Rigueur",
            "Précision",
            "Analyse de chiffres",
            "Organisation"
        ],
        "duree_etudes": "3-5 ans (BAC+3/5)",
        "debouches_togo": "Très demandé",
        "salaire": "Moyen à Élevé",
        "niveau_requis": "BAC+3/5",
        "explication": "Tu es rigoureux et tu aimes les chiffres. Métier stable, toutes les entreprises ont besoin de comptables. Possibilité d'ouvrir son cabinet.",
        "debouches_concrets": [
            "Cabinets comptables (Lomé)",
            "Services comptables entreprises",
            "Cabinet indépendant"
        ]
    },
    
    # DROIT
    "Avocat": {
        "nom": "Avocat",
        "badge": "⚖️",
        "domaine": "Justice/Droit",
        "series_recommandees": ["A4"],
        "matieres_importantes": ["Français", "Philosophie", "Histoire-Géographie"],
        "competences": [
            "Éloquence",
            "Argumentation",
            "Mémoire",
            "Analyse"
        ],
        "duree_etudes": "5-6 ans (BAC+5/6)",
        "debouches_togo": "Demandé",
        "salaire": "Moyen à Élevé",
        "niveau_requis": "BAC+5/6",
        "explication": "Tu aimes débattre et défendre des causes. Métier prestigieux au Togo. Possibilité d'ouvrir son cabinet après quelques années.",
        "debouches_concrets": [
            "Barreau de Lomé",
            "Cabinets d'avocats",
            "Services juridiques entreprises"
        ]
    },
    
    # ENSEIGNEMENT
    "Professeur": {
        "nom": "Professeur (Collège/Lycée)",
        "badge": "👨‍🏫",
        "domaine": "Éducation",
        "series_recommandees": ["A4", "C", "D"],
        "matieres_importantes": ["Varie selon spécialité"],
        "competences": [
            "Pédagogie",
            "Communication",
            "Patience",
            "Passion de transmettre"
        ],
        "duree_etudes": "4-5 ans (BAC+4/5)",
        "debouches_togo": "Très demandé",
        "salaire": "Moyen",
        "niveau_requis": "BAC+4/5",
        "explication": "Tu aimes expliquer et transmettre. Le Togo manque cruellement d'enseignants qualifiés. Métier stable avec vacances scolaires.",
        "debouches_concrets": [
            "Collèges/lycées publics",
            "Établissements privés (bien payés)",
            "Cours particuliers (complément)"
        ]
    },
    
    # ARCHITECTURE
    "Architecte": {
        "nom": "Architecte",
        "badge": "🏛️",
        "domaine": "Construction/Infrastructure",
        "series_recommandees": ["C", "F4"],
        "matieres_importantes": ["Mathématiques", "Arts", "Physique-Chimie"],
        "competences": [
            "Créativité",
            "Vision spatiale",
            "Dessin technique",
            "Maths/physique"
        ],
        "duree_etudes": "5-6 ans (BAC+5/6)",
        "debouches_togo": "Demandé",
        "salaire": "Élevé",
        "niveau_requis": "BAC+5/6",
        "explication": "Tu es créatif et tu aimes dessiner/construire. Boom immobilier au Togo = forte demande d'architectes. Métier valorisant et bien payé.",
        "debouches_concrets": [
            "Cabinets d'architecture (Lomé)",
            "Promotion immobilière",
            "Cabinet indépendant"
        ]
    },
    
    # COMMUNICATION
    "Journaliste": {
        "nom": "Journaliste/Communicateur",
        "badge": "📰",
        "domaine": "Éducation",
        "series_recommandees": ["A4"],
        "matieres_importantes": ["Français", "Histoire-Géographie"],
        "competences": [
            "Écriture",
            "Investigation",
            "Communication",
            "Curiosité"
        ],
        "duree_etudes": "3 ans (BAC+3)",
        "debouches_togo": "Demandé",
        "salaire": "Moyen",
        "niveau_requis": "BAC+3",
        "explication": "Tu aimes écrire et informer. Médias togolais en développement (TV, radio, presse en ligne). Métier dynamique et varié.",
        "debouches_concrets": [
            "Médias nationaux (TVT, Radio Lomé)",
            "Presse en ligne",
            "Communication d'entreprise"
        ]
    },
    
    # AGRICULTURE
    "Agronome": {
        "nom": "Ingénieur Agronome",
        "badge": "🌾",
        "domaine": "Agriculture/Alimentation",
        "series_recommandees": ["D", "C"],
        "matieres_importantes": ["SVT", "Physique-Chimie", "Mathématiques"],
        "competences": [
            "Sciences naturelles",
            "Innovation",
            "Entrepreneuriat",
            "Terrain"
        ],
        "duree_etudes": "5 ans (BAC+5)",
        "debouches_togo": "Très demandé",
        "salaire": "Moyen à Élevé",
        "niveau_requis": "BAC+5",
        "explication": "Tu aimes la nature et l'innovation. Agriculture moderne = secteur d'avenir au Togo. Possibilité de créer son exploitation.",
        "debouches_concrets": [
            "Ministère de l'Agriculture",
            "ONG développement rural",
            "Agribusiness (création ferme moderne)"
        ]
    },
    
    # ENTREPRENEURIAT
    "Entrepreneur": {
        "nom": "Entrepreneur/Chef d'entreprise",
        "badge": "🚀",
        "domaine": "Commerce/Économie",
        "series_recommandees": ["G3", "G2", "Toutes"],
        "matieres_importantes": ["Économie", "Mathématiques"],
        "competences": [
            "Prise de risque",
            "Leadership",
            "Créativité",
            "Persévérance"
        ],
        "duree_etudes": "Variable (0-5 ans)",
        "debouches_togo": "Émergent",
        "salaire": "Variable",
        "niveau_requis": "Variable",
        "explication": "Tu as l'esprit d'initiative et tu veux créer ta propre activité. Le Togo encourage l'entrepreneuriat jeune. Liberté et autonomie.",
        "debouches_concrets": [
            "Startups (tech, services)",
            "Commerce (import/export)",
            "Artisanat valorisé"
        ]
    },
    
    # TECHNICIENS
    "Technicien BTP": {
        "nom": "Technicien BTP",
        "badge": "🔨",
        "domaine": "Construction/Infrastructure",
        "series_recommandees": ["F4", "F1"],
        "matieres_importantes": ["Technologie", "Mathématiques"],
        "competences": [
            "Travail manuel",
            "Lecture de plans",
            "Organisation",
            "Technique"
        ],
        "duree_etudes": "2-3 ans (BAC+2/3)",
        "debouches_togo": "Très demandé",
        "salaire": "Moyen",
        "niveau_requis": "BAC+2/3",
        "explication": "Tu es pratique et tu aimes le terrain. Secteur BTP en forte croissance au Togo. Insertion rapide et possibilité d'évolution.",
        "debouches_concrets": [
            "Entreprises BTP",
            "Chantiers nationaux",
            "Création entreprise artisanale"
        ]
    },
    
    "Technicien Électronique": {
        "nom": "Technicien Électronique/Informatique",
        "badge": "🔌",
        "domaine": "Technologie/Innovation",
        "series_recommandees": ["F2", "E"],
        "matieres_importantes": ["Technologie", "Mathématiques", "Informatique"],
        "competences": [
            "Dépannage",
            "Électronique",
            "Résolution problèmes",
            "Manuel"
        ],
        "duree_etudes": "2-3 ans (BAC+2/3)",
        "debouches_togo": "Très demandé",
        "salaire": "Moyen",
        "niveau_requis": "BAC+2/3",
        "explication": "Tu aimes réparer et comprendre la technologie. Forte demande pour réparation téléphones, ordinateurs, électronique. Possibilité d'ouvrir son atelier.",
        "debouches_concrets": [
            "Ateliers réparation (Grand Marché)",
            "SAV entreprises tech",
            "Atelier indépendant"
        ]
    }
}
