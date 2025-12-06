"""
Algorithme de scoring et recommandation pour Kpékpé
"""

def calculer_score_serie(responses, serie_data):
    """
    Calcule le score de correspondance entre le profil utilisateur et une série
    
    Logique de scoring :
    - Matières (40%) : correspondance entre matières fortes/préférées et matières de la série
    - Talents/Activités (30%) : correspondance avec le profil idéal
    - Problème à résoudre (20%) : adéquation avec les débouchés
    - Contraintes économiques (10%) : favorise séries techniques si budget limité
    """
    score = 0
    
    # 1. MATIÈRES (40 points max)
    matieres_preferees = responses.get('matieres_preferees', [])
    matieres_fortes = responses.get('matieres_fortes', [])
    matieres_serie = serie_data['profil_ideal']['matieres']
    
    # Matières fortes = plus de poids (25 points)
    for matiere in matieres_fortes:
        if matiere in matieres_serie:
            score += 25 / len(matieres_serie)
    
    # Matières préférées (15 points)
    for matiere in matieres_preferees:
        if matiere in matieres_serie:
            score += 15 / len(matieres_serie)
    
    # 2. TALENTS ET ACTIVITÉS (30 points max)
    talents = responses.get('talents', [])
    activites = responses.get('activites_favorites', [])
    talents_serie = serie_data['profil_ideal']['talents']
    activites_serie = serie_data['profil_ideal']['activites']
    
    # Talents (20 points)
    for talent in talents:
        if talent in talents_serie:
            score += 20 / len(talents_serie)
    
    # Activités (10 points)
    for activite in activites:
        if activite in activites_serie:
            score += 10 / len(activites_serie)
    
    # 3. PROBLÈME À RÉSOUDRE / DOMAINE (20 points max)
    probleme = responses.get('probleme', '')
    debouches = ' '.join(serie_data['debouches_post_bac'] + serie_data['metiers_accessibles'])
    
    mapping_problemes = {
        'Santé': ['Médecine', 'Pharmacie', 'Infirmier', 'Sage-femme', 'Sciences biologiques'],
        'Éducation': ['Enseignement', 'Professeur', 'Éducation'],
        'Environnement': ['Environnement', 'Agronomie', 'Sciences'],
        'Technologie/Innovation': ['Informatique', 'Ingénieur', 'Développement', 'Électronique'],
        'Pauvreté/Développement': ['Économie', 'Sociologie', 'Administration', 'Gestion'],
        'Construction/Infrastructure': ['BTP', 'Génie Civil', 'Architecture', 'Construction'],
        'Commerce/Économie': ['Commerce', 'Gestion', 'Économie', 'Commercial'],
        'Justice/Droit': ['Droit', 'Avocat', 'Justice'],
        'Agriculture/Alimentation': ['Agronomie', 'Agriculture', 'Biologie']
    }
    
    mots_cles = mapping_problemes.get(probleme, [])
    for mot in mots_cles:
        if mot.lower() in debouches.lower():
            score += 20 / len(mots_cles)
            break
    
    # 4. CONTRAINTES ÉCONOMIQUES (10 points max)
    contraintes = responses.get('contraintes', [])
    priorite = responses.get('priorite', '')
    
    # Bonus pour séries techniques si contraintes économiques
    if serie_data['type'] in ['Technique-Industriel', 'Technique-Tertiaire']:
        if 'Budget limité pour études' in contraintes:
            score += 3
        if 'Préférence études courtes et pratiques' in contraintes:
            score += 3
        if 'Besoin de travailler rapidement' in contraintes:
            score += 2
        if priorite == 'Stabilité de l\'emploi':
            score += 2
    
    # Bonus pour séries générales si longues études acceptées
    if serie_data['type'] == 'Général':
        if 'Longues études acceptées' in contraintes:
            score += 5
        if priorite in ['Passion avant tout', 'Impact social']:
            score += 3
    
    return min(score, 100)  # Cap à 100


def calculer_score_metier(responses, metier_data):
    """
    Calcule le score de correspondance entre le profil utilisateur et un métier
    """
    score = 0
    
    # 1. MATIÈRES (40 points)
    matieres_preferees = responses.get('matieres_preferees', [])
    matieres_fortes = responses.get('matieres_fortes', [])
    matieres_metier = metier_data['matieres_importantes']
    
    for matiere in matieres_fortes:
        if matiere in matieres_metier:
            score += 25 / len(matieres_metier)
    
    for matiere in matieres_preferees:
        if matiere in matieres_metier:
            score += 15 / len(matieres_metier)
    
    # 2. COMPÉTENCES ET ACTIVITÉS (30 points)
    talents = responses.get('talents', [])
    activites = responses.get('activites_favorites', [])
    competences_metier = ' '.join(metier_data['competences'])
    
    mapping_talents = {
        'Logique/Raisonnement': ['Logique', 'Analyse', 'Raisonnement', 'Mathématiques'],
        'Créativité': ['Créativité', 'Créatif', 'Innovation', 'Dessin'],
        'Communication': ['Communication', 'Éloquence', 'Parler'],
        'Manuel/Pratique': ['Manuel', 'Pratique', 'Travail manuel', 'Construire'],
        'Leadership': ['Leadership', 'Manager', 'Gestion d\'équipe'],
        'Empathie': ['Empathie', 'Écoute', 'Patient', 'Aider'],
        'Organisation': ['Organisation', 'Rigueur', 'Précision'],
        'Technique': ['Technique', 'Technologie', 'Dépannage']
    }
    
    for talent in talents:
        mots = mapping_talents.get(talent, [])
        for mot in mots:
            if mot.lower() in competences_metier.lower():
                score += 20 / len(talents) if talents else 0
                break
    
    # Activités
    mapping_activites = {
        'Lire/Écrire': ['Écriture', 'Investigation', 'Littérature'],
        'Créer/Dessiner': ['Créativité', 'Dessin', 'Vision spatiale'],
        'Calculer/Analyser': ['Analyse', 'Calcul', 'Chiffres'],
        'Parler/Convaincre': ['Communication', 'Éloquence', 'Négociation'],
        'Construire/Réparer': ['Construction', 'Dépannage', 'Manuel'],
        'Aider les autres': ['Empathie', 'Accompagnement', 'Soigner'],
        'Organiser/Gérer': ['Organisation', 'Gestion', 'Management'],
        'Utiliser l\'ordinateur': ['Informatique', 'Programmation', 'Numérique'],
        'Expérimenter': ['Expérimentation', 'Sciences', 'Innovation']
    }
    
    for activite in activites:
        mots = mapping_activites.get(activite, [])
        for mot in mots:
            if mot.lower() in competences_metier.lower():
                score += 10 / len(activites) if activites else 0
                break
    
    # 3. PROBLÈME À RÉSOUDRE / DOMAINE (20 points)
    probleme = responses.get('probleme', '')
    domaine_metier = metier_data['domaine']
    
    mapping_domaines = {
        'Santé': 'Santé',
        'Éducation': 'Éducation',
        'Environnement': 'Environnement',
        'Technologie/Innovation': 'Technologie/Innovation',
        'Pauvreté/Développement': 'Pauvreté/Développement',
        'Construction/Infrastructure': 'Construction/Infrastructure',
        'Commerce/Économie': 'Commerce/Économie',
        'Justice/Droit': 'Justice/Droit',
        'Agriculture/Alimentation': 'Agriculture/Alimentation'
    }
    
    if mapping_domaines.get(probleme) == domaine_metier:
        score += 20
    
    # 4. CONTRAINTES (10 points)
    contraintes = responses.get('contraintes', [])
    priorite = responses.get('priorite', '')
    duree = metier_data['duree_etudes']
    salaire = metier_data['salaire']
    
    # Pénalité si longues études mais budget limité
    if 'Budget limité pour études' in contraintes and 'BAC+5' in duree:
        score -= 5
    
    # Bonus si études courtes souhaitées
    if 'Préférence études courtes et pratiques' in contraintes:
        if 'BAC+2' in duree or 'BAC+3' in duree:
            score += 5
    
    # Bonus salaire
    if priorite == 'Salaire élevé' and salaire == 'Élevé':
        score += 5
    
    # Bonus passion
    if priorite == 'Passion avant tout':
        score += 3
    
    return min(score, 100)


def calculer_recommandations(responses, data_dict, profil):
    """
    Génère les recommandations triées par score
    """
    recommandations = []
    
    for key, data in data_dict.items():
        if profil == 'collegien':
            score = calculer_score_serie(responses, data)
        else:
            score = calculer_score_metier(responses, data)
        
        recommandations.append({
            'nom': data['nom'],
            'badge': data.get('badge', ''),
            'score': round(score),
            'explication': data.get('description', data.get('explication', '')),
            'competences': data.get('profil_ideal', {}).get('talents', []) if profil == 'collegien' else data.get('competences', []),
            'debouches': data.get('debouches_post_bac', []) if profil == 'collegien' else data.get('debouches_concrets', []),
            'duree': f"Parcours : Seconde → Première (BAC 1) → Terminale (BAC 2)" if profil == 'collegien' else data.get('duree_etudes', '')
        })
    
    # Trier par score décroissant
    recommandations.sort(key=lambda x: x['score'], reverse=True)
    
    return recommandations
