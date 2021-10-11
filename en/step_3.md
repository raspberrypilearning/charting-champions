## Load more data

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
The chart looks good, but almost 150 nations have competed in the Olympics. You're going to load that data from a file, instead of having to type it all in!
</div>
<div>
![A column chart showing the medal counts of many nations. Information appears when the mouse hovers over a column. Columns disappear as the names of nations are clicked on.](images/adjust_chart.gif){:width="300px"}
</div>
</div>

--- task ---

Delete the lists and `chart.add()` lines from the previous step — that data is in the file you will be loading.

--- /task ---

--- task ---

The `data.csv` file included in the starter project contains the data you need. You can load the file's contents into a variable by using `with open() as` and `read()`.

[[[generic-python-file-read]]]

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 8 
line_highlights: 9-10
---
# Add data to the chart
with open('data.csv') as f:
  data = f.read()
--- /code ---

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
<span style="color: #0faeb0">**CSV files**</span> are **c**omma-**s**eparted **v**alues files. They contain data in rows and columns, like a table. Each line is a row, with commas seperating that row's values into columns.
</p>

--- task ---

The text in `data` is one long string, which needs to be split into the names of teams and the number of medals they have won. 

Use the string's `splitlines()` function, which splits it into a list of lines. Then `print()` those lines.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 9 
line_highlights: 11-12
---
with open('data.csv') as f:
  data = f.read()
  lines = data.splitlines()
  print('Lines: ', lines)
--- /code ---

--- /task ---

--- task ---

**Test:** Run your code and look at the text it prints out. 

Notice that the list is surrounded by the same square brackets — `[]` — you used to make a list. Also, the items in the list are separted by commas, just like your lists were.

```
Lines:  ['team,medals', 'United States,2399' … 'Liechtenstein,0']
```

**Debug:** Make sure you have indented the code under `with`, like in the example above.

**Debug:** If you see a message about `read` or `splitlines` being 'not defined', then check that you have included `f.` before `read()` or `data` before `splitlines()`, so Python knows which variables have those functions.

--- /task ---

The strings in the `lines` list are all made up of two pieces separated by a comma. Your `chart.add()` function needs each of those pieces separately. 

--- task ---

Use a `for` loop to go through `lines` and use each string's `split()` function to split it into a list — one item for each side of the comma. Then print them out.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 9 
line_highlights: 14-16
---
with open('data.csv') as f:
  data = f.read()
  lines = data.splitlines()
  print('Lines: ', lines)

for line in lines:
  entries = line.split(',')
  print('Entries: ', entries) # Print each entry on its own line
--- /code ---

**Tip:** `split()` can split a string into a list around any text you want. You can split on punctuation, a letter, or even whole words.

--- /task ---

--- task ---

**Test:** Run your code and look at the text it prints out. Each line should be a list of a nation and their medal count.

```
Entries:  ['Tonga', '1']
Entries:  ['United Arab Emirates', '1']
Entries:  ['Virgin Islands', '1']
Entries:  ['Liechtenstein', '0']
```

**Debug:** If your `entries` are printing out as lists with only one item — `Entries:  ['Tonga,1']` instead of `Entries:  ['Tonga', '1']` — then check that you have `','` in the `()` of `line.split()`.

**Debug:** If you see a message about `split` being 'not defined', check that you have included `line.` before it.

--- /task ---

--- task ---

Load your data into the chart using the same `for` loop you just created.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 14 
line_highlights: 17-19
---
for line in lines:
  entries = line.split(',')
  print('Entries: ', entries)
  team = entries[0]
  medals = entries[1]
  chart.add(team, int(medals))  # Make medals a number
--- /code ---

**Tip:** Because they're not part of creating the chart, you can put a `#` in front of the code that prints `lines` and `entries` when you're not using them to debug your program. This will turn that code into comments, so Python will ignore it.

--- /task ---

--- task ---

**Test:** Run your code and see what happens.

You should get an error like this:

```
ValueError: invalid literal for int() with base 10: 'medals' on line 19 in main.py
```

This message means Python can't convert 'medals' into a number with `int()`. This is because the first line of `data.csv` is different to all the others: instead of a team and the number of medals they have won, it is the headings 'team' and 'medals'.

**Debug:** There are some other bugs you might find here:

--- collapse ---
---
title: I don't get an error, but my chart is empty
---

If you get an empty chart instead of this error, check that you have `int(medals)` in your `chart.add()`.

--- /collapse ---

--- collapse ---
---
title: I get a message about an 'IndexError'
---
If you see a message about an `IndexError` instead, it means your code is trying to get a value from a list index (e.g. `entries[2]`) that hasn't had a value stored in it. To fix this:
 - Check each of your `team` and `medals` variables to be sure you are only using `0` and `1` as indexes
 - Check the printed `entries` lists to be sure they have two items — `Entries:  ['Tonga', '1']`, not `Entries:  ['Tonga,1']`. If they don't, then check that you have `','` in the `()` of `line.split()`.

--- /collapse ---

--- /task ---

To fix the bug, you need to skip the first line of `data.csv` — the string at index `0` in `lines`. 

--- task ---

Lists can be **sliced** to skip items at the start by using `my_list[start:]` — where `start` is the index of the item you want to start from, e.g. `my_list[3:]`. Slice `lines` when you use in the `for` loop to skip the first line.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 14 
line_highlights: 14
---
for line in lines[1:]: # Start from the item at index 1
  entries = line.split(',')
  print('Entries: ', entries)
  team = entries[0]
  medals = entries[1]
  chart.add(team, int(medals))  # Make medals a number
--- /code ---

--- /task ---

--- task ---

**Test:** Run your code and look at the chart it creates. Try hovering over some of the bars, or clicking on the names of teams to add and remove them from the chart.

![A column chart showing the medal counts of many nations. Information appears when the mouse hovers over a column. Columns disappear as the names of nations are clicked on.](images/adjust_chart.gif){:width="400px"}

--- /task ---

--- save ---