## Onderzoek met data

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Nu kan je programma grafieken maken uit gegevensbestanden. Je kunt dit in verschillende bestanden gebruiken om de grafieken te vergelijken en te zien wat je ervan kunt leren.
</div>
<div>
![Een staafdiagram dat de medailletellingen van veel landen weergeeft. Informatie verschijnt wanneer de muis over een balk beweegt. Balken verdwijnen als er op de namen van landen wordt geklikt.](images/adjust_chart.gif){:width="300px"}
</div>
</div>

### Wie heeft de meeste medailles?

--- task ---

Kijk naar de grafiek die je hebt gemaakt. Hoe groter een balk is, hoe meer medailles dat team heeft gewonnen. Beweeg de muis over enkele van de hoogste balken en kijk tot welke teams ze behoren.

![Een staafdiagram dat de bevolking van veel landen weergeeft. Informatie verschijnt wanneer de muis over een balk beweegt. Balken verdwijnen als er op de namen van landen wordt geklikt.](images/adjust_chart.gif){:width="500px"}

Waarom hebben zij misschien wel de meeste medailles?

--- /task ---

Het zou een goed idee kunnen zijn om zowel naar de bevolking als naar de rijkdom van de teams te kijken, om te zien of er een patroon te ontdekken is.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
<span style="color: #0faeb0">**Gegevensanalyse:**</span> Mensen deden dit soort onderzoeken al lang voordat computers werden uitgevonden. In de jaren vijftig van de negentiende eeuw gebruikte Florence Nightingale, een verpleegster, bijvoorbeeld tabellen en grafieken om het belang van ziektepreventie bij de zorg voor zieken aan te tonen. 
![Florence Nightingale's overzicht van doodsoorzaken.](images/nightingale.jpeg){:width="300px"}
</p>

### Bevolkingsgroottes

Een bestand, genaamd `pop.csv`, met gegevens over de bevolking van verschillende landen, maakt deel uit van het startptoject. Omdat de gegevens in `pop.csv` ook uit een tekststring en een getal bestaan, kunt je jouw code met slechts kleine wijzigingen hergebruiken.

--- task ---

Pas de titel van de grafiek aan, de `breedte` van de grafiek, het bestand dat je opent, en de naam van de categorie om een grafiek te maken op basis van de bevolkingsgegevens uit `pop.csv`.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 6
line_highlights: 6, 9, 15, 16
---
chart = Bar(title='Population', width='600')

# Add data to the chart
with open('pop.csv') as f: for line in f: #print(line) pieces = line.split(',') #print(pieces) team = pieces[0] population = pieces[1] chart.add(team, int(population))  # Make population a number --- /code ---

--- /task ---

--- task ---

Voer nu jouw programma uit en kijk naar de grafiek die wordt gemaakt.

![Een staafdiagram dat de bevolking van veel landen weergeeft. Informatie verschijnt wanneer de muis over een balk beweegt. Balken verdwijnen als er op de namen van landen wordt geklikt.](images/pop.gif){:width="500px"}

Beweeg de muis over enkele van de hoogste balken en kijk tot welke landen ze behoren. Klik op de namen van de echt grote om ze uit de grafiek te verwijderen; Zo kun je de anderen beter bekijken. Heeft een van de landen met veel inwoners een groot aantal medailles?

--- /task ---

### Rijkdom

Een bestand met de naam `gdp.csv` maakt deel uit van het startproject. Het bevat gegevens over het jaarlijkse BBP van verschillende landen. Net als bij `pop.csv`hoef je slechts kleine wijzigingen aan te brengen om het te gebruiken.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
<span style="color: #0faeb0">**BBP**</span> is het bruto binnenlands product. Het meet de waarde, in geld, van alles wat in een gebied gedurende een bepaalde periode wordt geproduceerd. Het kan meten hoe rijk een gebied is.
</p>

--- task ---

Pas de titel van de grafiek aan, de breedte van de grafiek, het bestand dat je opent, en de naam van de categorie om een grafiek te maken op basis van de bbp data uit `gdp.csv`.

Het bestand `gdp.csv` slaat het bbp op als decimale getallen. Update het type van `int` naar `float` zodat de getallen de juiste notatie hebben.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 6
line_highlights: 6, 9, 15, 16
---
chart.title = 'GDP'

# Add data to the chart
with open('gdp.csv') as f: for line in f: #print(line) pieces = line.split(',') #print(pieces) team = pieces[0] gdp = pieces[1] chart.add(team, float(gdp))  # Make GDP a number --- /code ---

--- /task ---

--- task ---

Voer nu jouw programma uit en kijk naar de grafiek die wordt gemaakt.

![Een staafdiagram dat het BBP van veel landen weergeeft. Informatie verschijnt wanneer de muis over een balk beweegt. Balken verdwijnen als er op de namen van landen wordt geklikt.](images/gdp.gif){:width="500px"}

Beweeg de muis over enkele van de hoogste balken en kijk tot welke landen ze behoren. Klik op de namen van de echt grote om ze uit de grafiek te verwijderen; Zo kun je de anderen beter bekijken. Had een van de teams van de rijkste landen een zeer groot aantal medailles?

--- /task ---

### Wat heb je gevonden?
Wat heb je ontdekt door je programma te gebruiken om naar deze gegevens te kijken?

 - Er zijn enkele tekenen dat het aantal mensen waaruit een team kan kiezen bijdraagt aan het verdienen van medailles.
 - Maar de bevolking verklaart niet waarom landen als Frankrijk zoveel medailles hebben. Of waarom India niet zoveel medailles heeft als China of de VS.
 - Geld lijkt meer te verklaren. De meeste landen met veel medailles hebben ook een hoog BBP.
 - Geen van beiden legt alles uit. Er zijn teams die dit patroon niet volgen.

--- collapse ---
---
title: Jamaica doet het beter dan grotere en rijkere landen
---
Dit is geen probleem uit een wiskundeboek. Het antwoord is dus niet eenvoudig. Kijk bijvoorbeeld naar Jamaica. Jamaica heeft geen grote bevolking of een groot BBP.

Mexico, Ierland, Portugal, Saoedi-Arabië en Singapore hebben allemaal meer mensen en meer geld. Ze hebben zelfs meer geld per persoon. Maar Jamaica heeft meer medailles gewonnen dan wie dan ook!

--- /collapse ---

Er is dus meer nodig om Olympische medailles te winnen dan alleen mensen en geld. Wat zou het nog meer kunnen zijn? Welke andere ideeën zou je kunnen testen, en wat voor soort gegevens heb je daarvoor nodig?
