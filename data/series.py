"""
Données complètes des 12 séries du système éducatif togolais
"""

SERIES_DATA = {
    # SÉRIES D'ENSEIGNEMENT GÉNÉRAL
    "A4": {
        "nom": "Série A4 - Lettres et Sciences Sociales",
        "type": "Général",
        "badge": "🎓",
        "matieres_principales": ["Français", "Philosophie", "Histoire-Géographie", "Langues"],
        "profil_ideal": {
            "matieres": ["Français", "Philosophie", "Histoire-Géographie", "Anglais"],
            "activites": ["Lire/Écrire", "Parler/Convaincre", "Aider les autres"],
            "talents": ["Communication", "Créativité", "Empathie", "Organisation"]
        },
        "debouches_post_bac": [
            "Université de Lomé (Lettres, Sociologie, Communication)",
            "Écoles de journalisme",
            "Sciences politiques",
            "Droit",
            "Enseignement"
        ],
        "metiers_accessibles": [
            "Journaliste",
            "Enseignant",
            "Avocat",
            "Diplomate",
            "Communicateur",
            "Sociologue"
        ],
        "difficulte": "Moyen",
        "description": "Pour les passionnés de littérature, langues et sciences humaines. Cette série ouvre vers les métiers de la communication, du droit et de l'enseignement."
    },
    
    "C": {
        "nom": "Série C - Sciences Mathématiques",
        "type": "Général",
        "badge": "🎓",
        "matieres_principales": ["Mathématiques", "Physique-Chimie", "SVT"],
        "profil_ideal": {
            "matieres": ["Mathématiques", "Physique-Chimie"],
            "activites": ["Calculer/Analyser", "Expérimenter", "Utiliser l'ordinateur"],
            "talents": ["Logique/Raisonnement", "Technique"]
        },
        "debouches_post_bac": [
            "Écoles d'ingénieurs (2IE, ESTBA)",
            "Faculté des Sciences (UL)",
            "Écoles d'informatique",
            "Médecine (avec niveau élevé)",
            "Architecture"
        ],
        "metiers_accessibles": [
            "Ingénieur",
            "Développeur informatique",
            "Architecte",
            "Chercheur scientifique",
            "Enseignant de sciences"
        ],
        "difficulte": "Élevé",
        "description": "Série d'excellence pour les matheux ! Idéale pour devenir ingénieur, informaticien ou scientifique. Ouvre toutes les portes des études supérieures."
    },
    
    "D": {
        "nom": "Série D - Sciences de la Nature",
        "type": "Général",
        "badge": "🎓",
        "matieres_principales": ["SVT", "Physique-Chimie", "Mathématiques"],
        "profil_ideal": {
            "matieres": ["SVT", "Physique-Chimie", "Mathématiques"],
            "activites": ["Expérimenter", "Aider les autres", "Calculer/Analyser"],
            "talents": ["Logique/Raisonnement", "Empathie"]
        },
        "debouches_post_bac": [
            "Médecine / Pharmacie (UL, UCAO)",
            "Écoles d'infirmiers/sages-femmes",
            "Agronomie",
            "Sciences biologiques",
            "Environnement"
        ],
        "metiers_accessibles": [
            "Médecin",
            "Pharmacien",
            "Infirmier",
            "Sage-femme",
            "Agronome",
            "Biologiste"
        ],
        "difficulte": "Élevé",
        "description": "Pour les passionnés de biologie et sciences du vivant. Voie royale vers la médecine, pharmacie et professions de santé."
    },
    
    # SÉRIES TECHNIQUES - FILIÈRE INDUSTRIELLE
    "E": {
        "nom": "Série E - Mathématiques et Techniques",
        "type": "Technique-Industriel",
        "badge": "🔧",
        "matieres_principales": ["Mathématiques", "Sciences de l'ingénieur", "Physique"],
        "profil_ideal": {
            "matieres": ["Mathématiques", "Physique-Chimie", "Technologie"],
            "activites": ["Calculer/Analyser", "Construire/Réparer", "Utiliser l'ordinateur"],
            "talents": ["Logique/Raisonnement", "Technique", "Manuel/Pratique"]
        },
        "debouches_post_bac": [
            "Écoles d'ingénieurs (industriel, mécanique)",
            "BTS/DUT techniques",
            "Technicien supérieur",
            "Maintenance industrielle"
        ],
        "metiers_accessibles": [
            "Ingénieur industriel",
            "Technicien supérieur",
            "Responsable production",
            "Automaticien"
        ],
        "difficulte": "Moyen",
        "description": "Maths appliquées + technique ! Parfaite pour ceux qui veulent allier réflexion mathématique et pratique industrielle."
    },
    
    "F1": {
        "nom": "Série F1 - Construction Mécanique",
        "type": "Technique-Industriel",
        "badge": "🔧",
        "matieres_principales": ["Construction mécanique", "Technologie", "Mathématiques"],
        "profil_ideal": {
            "matieres": ["Technologie", "Mathématiques", "Physique-Chimie"],
            "activites": ["Construire/Réparer", "Calculer/Analyser"],
            "talents": ["Manuel/Pratique", "Technique", "Logique/Raisonnement"]
        },
        "debouches_post_bac": [
            "Technicien en mécanique",
            "Maintenance automobile/industrielle",
            "BTS Mécanique",
            "Ateliers de fabrication"
        ],
        "metiers_accessibles": [
            "Mécanicien spécialisé",
            "Technicien maintenance",
            "Chef d'atelier",
            "Dessinateur industriel"
        ],
        "difficulte": "Accessible",
        "description": "Pour les passionnés de mécanique et machines ! Très recherché dans l'industrie togolaise. Insertion professionnelle rapide."
    },
    
    "F2": {
        "nom": "Série F2 - Électronique",
        "type": "Technique-Industriel",
        "badge": "🔧",
        "matieres_principales": ["Électronique", "Électrotechnique", "Mathématiques"],
        "profil_ideal": {
            "matieres": ["Technologie", "Mathématiques", "Physique-Chimie", "Informatique"],
            "activites": ["Construire/Réparer", "Utiliser l'ordinateur", "Calculer/Analyser"],
            "talents": ["Technique", "Logique/Raisonnement", "Manuel/Pratique"]
        },
        "debouches_post_bac": [
            "Technicien électronique",
            "Maintenance télécom",
            "BTS Électronique",
            "Dépannage électronique"
        ],
        "metiers_accessibles": [
            "Technicien électronique",
            "Réparateur téléphones/ordinateurs",
            "Installateur systèmes électroniques",
            "Technicien télécom"
        ],
        "difficulte": "Accessible",
        "description": "Circuits, composants électroniques et nouvelles technologies ! Métier d'avenir avec l'essor du numérique au Togo."
    },
    
    "F3": {
        "nom": "Série F3 - Électrotechnique",
        "type": "Technique-Industriel",
        "badge": "🔧",
        "matieres_principales": ["Électrotechnique", "Installations électriques", "Mathématiques"],
        "profil_ideal": {
            "matieres": ["Technologie", "Mathématiques", "Physique-Chimie"],
            "activites": ["Construire/Réparer", "Calculer/Analyser"],
            "talents": ["Technique", "Manuel/Pratique", "Logique/Raisonnement"]
        },
        "debouches_post_bac": [
            "Électricien qualifié",
            "Installateur réseaux électriques",
            "BTS Électrotechnique",
            "Maintenance électrique industrielle"
        ],
        "metiers_accessibles": [
            "Électricien bâtiment",
            "Technicien maintenance électrique",
            "Installateur solaire",
            "Chef de chantier électrique"
        ],
        "difficulte": "Accessible",
        "description": "Spécialiste des installations électriques ! Très demandé dans le BTP et l'industrie. Possibilité de créer son entreprise facilement."
    },
    
    "F4": {
        "nom": "Série F4 - Génie Civil",
        "type": "Technique-Industriel",
        "badge": "🔧",
        "matieres_principales": ["Construction", "Topographie", "Mathématiques", "Dessin technique"],
        "profil_ideal": {
            "matieres": ["Mathématiques", "Technologie", "Physique-Chimie"],
            "activites": ["Construire/Réparer", "Calculer/Analyser", "Organiser/Gérer"],
            "talents": ["Technique", "Manuel/Pratique", "Organisation", "Logique/Raisonnement"]
        },
        "debouches_post_bac": [
            "Technicien BTP",
            "Conducteur de travaux",
            "BTS Génie Civil",
            "École d'architecture (avec bon niveau)",
            "Métreur"
        ],
        "metiers_accessibles": [
            "Technicien génie civil",
            "Conducteur de travaux",
            "Dessinateur bâtiment",
            "Métreur",
            "Entrepreneur BTP"
        ],
        "difficulte": "Moyen",
        "description": "Construction, routes, bâtiments ! Secteur qui recrute massivement au Togo avec les grands projets d'infrastructure."
    },
    
    "TI": {
        "nom": "Série TI - Chaudronnerie, Tuyauterie",
        "type": "Technique-Industriel",
        "badge": "🔧",
        "matieres_principales": ["Chaudronnerie", "Soudure", "Tuyauterie", "Métallurgie"],
        "profil_ideal": {
            "matieres": ["Technologie", "Mathématiques"],
            "activites": ["Construire/Réparer"],
            "talents": ["Manuel/Pratique", "Technique"]
        },
        "debouches_post_bac": [
            "Chaudronnier professionnel",
            "Soudeur qualifié",
            "Technicien maintenance industrielle",
            "Formations spécialisées"
        ],
        "metiers_accessibles": [
            "Chaudronnier",
            "Soudeur industriel",
            "Tuyauteur",
            "Métallier",
            "Chef d'atelier métallerie"
        ],
        "difficulte": "Accessible",
        "description": "Travail des métaux et soudure ! Métier artisanal très valorisé et bien rémunéré. Forte demande dans l'industrie."
    },
    
    # SÉRIES TECHNIQUES - FILIÈRE TERTIAIRE
    "G1": {
        "nom": "Série G1 - Techniques Administratives",
        "type": "Technique-Tertiaire",
        "badge": "💼",
        "matieres_principales": ["Secrétariat", "Bureautique", "Communication", "Économie"],
        "profil_ideal": {
            "matieres": ["Français", "Économie", "Informatique"],
            "activites": ["Organiser/Gérer", "Utiliser l'ordinateur", "Parler/Convaincre"],
            "talents": ["Organisation", "Communication", "Technique"]
        },
        "debouches_post_bac": [
            "Secrétaire de direction",
            "Assistant administratif",
            "BTS Assistant de gestion",
            "Bureautique avancée"
        ],
        "metiers_accessibles": [
            "Secrétaire",
            "Assistant de direction",
            "Gestionnaire administratif",
            "Employé de bureau"
        ],
        "difficulte": "Accessible",
        "description": "Organisation et gestion administrative ! Débouchés assurés dans toutes les entreprises et administrations togolaises."
    },
    
    "G2": {
        "nom": "Série G2 - Techniques Quantitatives de Gestion",
        "type": "Technique-Tertiaire",
        "badge": "💼",
        "matieres_principales": ["Comptabilité", "Statistiques", "Mathématiques financières", "Économie"],
        "profil_ideal": {
            "matieres": ["Mathématiques", "Économie", "Informatique"],
            "activites": ["Calculer/Analyser", "Organiser/Gérer", "Utiliser l'ordinateur"],
            "talents": ["Logique/Raisonnement", "Organisation", "Technique"]
        },
        "debouches_post_bac": [
            "Comptable",
            "Contrôleur de gestion",
            "BTS Comptabilité-Gestion",
            "Banque/Finance",
            "Audit"
        ],
        "metiers_accessibles": [
            "Comptable",
            "Gestionnaire financier",
            "Contrôleur de gestion",
            "Agent bancaire",
            "Auditeur"
        ],
        "difficulte": "Moyen",
        "description": "Chiffres, comptabilité et finance ! Métier stable et très recherché par toutes les entreprises. Excellentes perspectives de carrière."
    },
    
    "G3": {
        "nom": "Série G3 - Techniques Commerciales",
        "type": "Technique-Tertiaire",
        "badge": "💼",
        "matieres_principales": ["Commerce", "Marketing", "Vente", "Économie"],
        "profil_ideal": {
            "matieres": ["Économie", "Français", "Mathématiques"],
            "activites": ["Parler/Convaincre", "Organiser/Gérer", "Utiliser l'ordinateur"],
            "talents": ["Communication", "Leadership", "Organisation"]
        },
        "debouches_post_bac": [
            "Commercial",
            "Vendeur qualifié",
            "BTS Commerce/Marketing",
            "Gestionnaire de magasin",
            "Marketing digital"
        ],
        "metiers_accessibles": [
            "Commercial",
            "Responsable marketing",
            "Vendeur",
            "Chef de rayon",
            "Entrepreneur commercial"
        ],
        "difficulte": "Accessible",
        "description": "Vente, commerce et relations client ! Parfait pour les communicateurs qui aiment le contact. Possibilité de créer son propre commerce."
    }
}
