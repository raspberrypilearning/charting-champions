#!/bin/python3
from pygal import Bar

# Créer un graphique
graphique = Bar(title='Médailles olympiques')

# Ajouter des données au graphique
with open('medals.csv') as f:
    donnees = f.read()
    lignes = donnees.splitlines()
    # print(lignes)

    for ligne in lignes:
        decompte = ligne.split(',')
        # print(decompte)
        equipe = decompte[0]
        medailles = decompte[1]
        graphique.add(equipe, int(medailles))  # Convertir les médailles en nombre

# Afficher le graphique
graphique.render()
