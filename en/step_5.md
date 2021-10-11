## Upgrade your project

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
In this step, change how your chart looks, or what data it uses.
</div>
<div>
![A pie chart showing the running time of Marvel films](images/mcu_pie.png){:width="300px"}
</div>
</div>

### Use a Pie chart
Try using a pie chart for a different look, or to show how something is divided.

--- task ---

To create a pie chart instead of a bar chart, change the import from `pygal` to `Pie` instead of `Bar`. Do the same for the function you call to create `chart`. 

--- /task ---

### Display the first ten items
<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Try showing only the first ten items on your chart, so it's easier to see and compare them.
</div>
<div>
![A chart showing the carbon dioxide emissions of ten countries](images/10_co2.png){:width="300px"}
</div>
</div>

--- task ---

To display fewer items on the chart, you can slice the `lines` list from the end as well as from the start. You used `lines[1:]` to start from the string at position `1`. If you use `lines[:5]`, Python will skip every item with an index of `5` or higher. 

--- /task ---

### Use a different set of data
You can load and chart any data that's in a `.csv` file with the program you've written.

--- task ---

**Choose:** Pick a different datafile in your project. There are two available:

 - `mcu.csv` is the runtime and gross income from Marvel Cinematic Universe films
 - `carbon.csv` is the total and per-person carbon dioxide emissions of different countries and regions

--- /task ---

--- task ---

Update the code that reads from `data.csv` to read from your new file. 

These files have more than one column of numbers. Use indexes on the `entries` list to choose which to add to your chart. 

The carbon dioxide data uses numbers with decimals. To convert them from text strings, you'll need to use `float()` instead of `int()`.

--- /task ---

--- collapse ---
---
title: Completed project
---

You can view the [completed project here](https://trinket.io/python/1f312ddc4c).

--- /collapse ---

--- save ---