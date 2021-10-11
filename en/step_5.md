## Upgrade your project

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
In this step, try changing how your chart appears, or what it displays.
</div>
<div>
![A pie chart showing the running time of Marvel films](images/mcu_pie.png){:width="300px"}
</div>
</div>

### Use a Pie chart
Instead of displaying your data with a bar chart, you can use a pie chart for a different look, or to show how something has been split up.

--- task ---

To create a pie chart instead of a bar chart, change the function you import from `pygal`, and the function call you use to create `chart`, to be `Pie` instead of `Bar`. 

--- /task ---

### Display the first ten items
<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
There's a lot of data displayed on the chart at the moment. Try displaying only the first ten items, so it's easier to see and compare them.
</div>
<div>
![A chart showing the carbon dioxide emissions of ten countries](images/10_co2.png){:width="300px"}
</div>
</div>

--- task ---

To display fewer items on the chart, you can slice the `lines` list from the end as well as from the start. You used `lines[1:]` to start from the string at postion `1`. If you use `lines[:5]`, every string with an index of `5` or higher will be ignored. 

--- /task ---

### Use a different set of data
You can load and chart any data that's in a `.csv` file with the program you've written.

--- task ---

**Choose:** Pick a different datafile in your project. Two have been included for you:

 - `mcu.csv` contains the runtime and gross income from Marvel Cinematic Universe films
 - `carbon.csv` contains the total (in thousands of metric tons) and per-person (in metric tons) carbon dioxide emmisions of a variety of different countries and regions

--- /task ---

--- task ---

Update the code that reads from `data.csv` to read from your new file. These files have more than one set of interesting numbers — use different indexes in the `enteries` list to choose between them. 

The carbon dioxide data uses numbers with decimal places. To convert them from text strings, you'll need to use `float()` instead of `int()`.

--- /task ---

--- collapse ---
---
title: Completed project
---

You can view the [completed project here](https://trinket.io/python/af4b307a5f).

--- /collapse ---