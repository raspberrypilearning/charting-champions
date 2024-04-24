#!/bin/python3
from pygal import Bar

# Maak een grafiek
chart = Bar(title='Olympische medailles')

# Voeg gegevens toe aan de grafiek
with open('medals.csv') as f:
    data = f.read()
    lines = data.splitlines()
    # print(lines)

    for line in lines:
        totaal = line.split(',')
        # print(totaal)
        team = totaal[0]
        medailles = totaal[1]
        chart.add(team,int(medailles)) # Maak van medailles een getal

# Toon de grafiek
chart.render()
