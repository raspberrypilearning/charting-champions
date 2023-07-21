## Investigate with data

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Now your program can draw charts from files of data. You can use it on different files to compare their charts to see what you can learn.
</div>
<div>
![A bar chart showing the populations of many nations. Information appears when the mouse hovers over a bar. Bars disappear as the names of nations are clicked.](images/adjust_chart.gif){:width="300px"}
</div>
</div>

### Who has the most medals?

--- task ---

Look at the chart you've made. The taller a bar is, the more medals that team has won. Hover the mouse over some of the tallest bars and notice which teams they belong to. 

![A bar chart showing the populations of many nations. Information appears when the mouse hovers over a bar. Bars disappear as the names of nations are clicked.](images/adjust_chart.gif){:width="500px"}

Why might they have the most medals?

--- /task ---

A good idea might be to look at both the population and wealth of teams, to see if there is any sort of pattern.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
<span style="color: #0faeb0">**Data analysis:**</span> People have done these kinds of investigations since long before computers were invented. For example, in the 1850s, Florence Nightingale, a nurse, used charts and graphs to show the importance of disease prevention in caring for the sick. 
![Florence Nightingale's chart of causes of mortality.](images/nightingale.jpeg){:width="300px"}
</p>

### Population sizes

A file, called `pop.csv`, with data on the populations of different countries, is part of the starter project. Because the data in `pop.csv` is also made up of a text string and a number, you can re-use your code with only small changes.

--- task ---

Change the chart title, the `width` of the chart, the file you are opening, and the category name to draw a chart based on the population data in `pop.csv`.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 6 
line_highlights: 6, 9, 15, 16
---
chart = Bar(title='Population', width='600')

# Add data to the chart
with open('pop.csv') as f:
    for line in f:
        #print(line)
        pieces = line.split(',')
        #print(pieces)
        team = pieces[0]
        population = pieces[1]
        chart.add(team, int(population))  # Make population a number
--- /code ---

--- /task ---

--- task ---

Now run your program and look at the chart it draws. 

![A bar chart showing the populations of many nations. Information appears when the mouse hovers over a bar. Bars disappear as the names of nations are clicked.](images/pop.gif){:width="500px"}

Hover the mouse over the biggest bars and notice which countries they belong to. Click the names of the really big ones to remove them from the chart; that will let you get a closer look at the others. Do any of the countries with lots of people have a large number of medals?

--- /task ---

### Wealth

A file called `gdp.csv` is part of the starter project. It has data on the annual GDP of different countries. Just like with `pop.csv`, you'll only need to make small changes to use it.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
<span style="color: #0faeb0">**GDP**</span> is the Gross Domestic Product. It measures the value, in money, of everything produced in an area over a given time period. It can measure how rich an area is.
</p>

--- task ---

Change the chart title, the file you are opening, and the category name to draw a chart based on the GDP data in `gdp.csv`.

The `gdp.csv` file stores the GDP as decimal numbers. Update the type from `int` to `float` so that the numbers are in the correct format. 

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 6 
line_highlights: 6, 9, 15, 16
---
chart.title = 'GDP'

# Add data to the chart
with open('gdp.csv') as f:
    for line in f:
        #print(line)
        pieces = line.split(',')
        #print(pieces)
        team = pieces[0]
        gdp = pieces[1]
        chart.add(team, float(gdp))  # Make GDP a number
--- /code ---

--- /task ---

--- task ---

Now run your program and look at the chart it draws. 

![A bar chart showing the GDP of many nations. Information appears when the mouse hovers over a bar. Bars disappear as the names of nations are clicked.](images/gdp.gif){:width="500px"}

Hover the mouse over the biggest bars and notice which countries they belong to. Click the names of the really big ones to remove them from the chart; that will let you take a closer look at the others. Did any of the richest countries' teams have very large numbers of medals?

--- /task ---

### What did you find?
What did you discover by using your program to look at this data?

 - There are some signs that the number of people a team has to choose from helps it earn medals.
 - But population doesn't explain how countries like France have so many medals. Or why India doesn't have as many medals as China or the USA.
 - Money seems to explain more. Most of the countries that have lots of medals have high GDPs too.
 - Neither of them explains everything. There are teams that don't follow this pattern.

--- collapse ---
---
title: Jamaica does better than bigger and richer countries
---
This isn't a problem in a maths book. So the answer isn't simple. For example, look at Jamaica. Jamaica doesn't have a large population, or a large GDP. 
 
Mexico, Ireland, Portugal, Saudi Arabia, and Singapore all have more people and more money. They even have more money per person. But Jamaica has won more medals than any of them!

--- /collapse ---

So there's more to what it takes to win Olympic medals than just people and money. What else might it be? What other ideas could you test, and what kind of data would you need to do so?
