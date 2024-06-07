#!/bin/python3
from pygal import Bar

# Maak een grafiek
grafiek = Bar(title='Olympische medailles')

# Voeg gegevens toe aan de grafiek
with open('medals.csv') as f:
    data = f.read()
    regels = data.splitlines()
    # print(regels)

    for regel in regels:
        totaal = regel.split(',')
        # print(totaal)
        team = totaal[0]
        medailles = totaal[1]
        chart.add(team,int(medailles)) # Maak van medailles een getal

# Toon de grafiek
grafiek.render()
