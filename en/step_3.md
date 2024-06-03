## Load data from a file

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
The chart looks good! But, almost 150 nations have competed in the Olympics. To chart them, you're going to load their data from a file. It will save a lot of typing!
</div>
<div>
![A bar chart showing the medal counts of many nations. Information appears when the mouse hovers over a bar. Bars disappear as the names of nations are clicked.](images/adjust_chart.gif){:width="300px"}
</div>
</div>

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
<span style="color: #0faeb0">**Computers and data**</span> You're just starting to learn how to get your computer work with data. Computers can do amazing things with the right data. And they can read more data in minutes than a human could in years. Python is one of the best programming languages there is for data. Python is what the YouTube algorithm, that picks the videos to show you, is made with.
</p>

--- task ---

Open the [second starter project](https://editor.raspberrypi.org/en/projects/charting-champions-second-starter){:target="_blank"}. The Raspberry Pi code editor will open in another browser tab.

If you have a Raspberry Pi account, you can click **Save** to save a copy of the starter code to your library.

--- collapse ---

---
title: Working offline
---

You will need `starter2.py` and the `.csv` files for this step.

--- /collapse ---

--- /task ---

There are several `.csv` files included in this starter project that contain the data you need for your charts.

--- task ---

Open `medals.csv` and look at the data in it. See how each line has a team name and the number of medals they have won, separated by a comma. 

![The Raspberry Pi code editor with medals file highlighted and open, displaying a list of countries and medal numbers seperated with a comma.](images/medals-tab.png)

--- /task ---

<div style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
<span style="color: #0faeb0">**CSV files**</span> are Comma-Separated Values files. They contain data in rows and columns, like a table. Each line is a row, with commas separating that row's values into columns.
![A few lines of a csv file.](images/csv_sample.png){:width="200px"}
</div>

You'll need to turn each line of `medals.csv` into a text string and a number in Python, like in the lists you made.

--- task ---

Click on the `main.py` tab and add code to load the file into a variable by using `with open() as`. Then use a `for` loop to `print` each line from the variable.

The `for` loop will let you repeat code. So you will load hundreds of teams to your chart with just a few lines of code!

[[[generic-python-file-read]]]

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 8 
line_highlights: 9-11
---
# Add data to the chart
with open('medals.csv') as f:
    for line in f:
        print(line)
--- /code ---

--- /task ---

--- task ---

**Test:** Run your code and look at the text it prints out. 

Notice that each line has two values, separated by commas.

![A list of text strings, printed out over many lines.](images/lines.png)

**Debug:** If the code doesn't work, make sure you have indented it under the `with` line, like in the example above.

--- /task ---

Each string that your loop prints is made up of two pieces separated by a comma. Your `chart.add()` function needs each of those pieces as separate inputs.

The `split()` function breaks a string into a list, just like the lists you made earlier. The `split(',')` function makes a new list item every time it sees a comma.

--- task ---

Put a `#` in front of the code that prints `line`. This will turn that code into a comment, so Python will ignore it. 

Use the `split()` method to break up each sting at a `,` and then store the first and second pieces in a new list. Then print those lists out.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 9 
line_highlights: 12-13
---
with open('medals.csv') as f:
    for line in f:
        #print(line)
        pieces = line.split(',') # Breaks the string into a list
        print(pieces) # Print each list
--- /code ---

**Tip:** `split()` can split a string into a list around any text you want. You can split on punctuation, a letter, or even whole words.

--- /task ---

--- task ---

**Test:** Run your code and look at the text it prints out. Each line should be a list with two items. You may notice that the second item has `\n` at the end. `\n` is usually invisible. It tells the computer it has reached the end of the line in a file.

![Many lists, each with two items, printed out.](images/tally.png){:width="400px"}

**Debug:** If your `pieces` are printing out as lists with only one item then check that you have `','` in the `()` of `line.split()`.

**Debug:** If you see a message about `split` being 'not defined', check that you have included `line.` before it.

--- /task ---

--- task ---

Load your data into the chart as part of your `for` loop. `team` is a string so can be used as a label on the chart. `medal` is currently a string, but needs to be converted to a number. You can use the `int()` function to **cast** a string to a number.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 9 
line_highlights: 14-16
---
with open('medals.csv') as f:
    for line in f:
        #print(line)
        pieces = line.split(',')
        #print(pieces)
        team = pieces[0]
        medals = pieces[1]
        chart.add(team, int(medals))  # Make medals a number
--- /code ---

**Tip:** You can now use `#` to turn `print(pieces)` into a comment too.

--- /task ---

--- task ---

**Test:** Run your code and look at the chart it creates. Try hovering over some of the bars, or clicking on the names of teams to add and remove them from the chart.

![A bar chart showing the medal counts of many nations. Information appears when the mouse hovers over a bar. Bars disappear as the names of nations are clicked.](images/adjust_chart.gif){:width="400px"}

**Debug:** If your chart is empty, check that you have `int(medals)` in your `chart.add()`.

**Debug:** If you see a message about an `IndexError`, your code is trying to get a value from a list index that doesn't exist (e.g. `pieces[2]`). To fix this:
 - Check each of your `team` and `medals` variables to be sure you are only using `0` and `1` as indexes.
 - Check the printed `pieces` lists to be sure they have two items: `['Tonga', '1\n']`, not `['Tonga,1\n']`. If they don't, then check that you have `','` in the `()` of `line.split()`.
 - Check you do not have a blank line at the bottom of your .csv file.

--- /task ---

--- save ---
