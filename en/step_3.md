## Load more data

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
The chart looks good, but almost 150 nations have competed in the Olympics. You're going to load that data from a file, instead of having to type it all in!
</div>
<div>
![A column chart showing the medal counts of many nations](images/completed_preview.png){:width="200px"}
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
with open('data.csv') as file:
  data = file.read()
--- /code ---

--- /task ---

--- task ---

The text in `data` is one long string, which needs to be broken up into the names of nations and the number of medals they have won. Use the string's `splitlines()` function, which breaks it into a list of lines. Then `print()` those lines.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 9 
line_highlights: 11-12
---
with open('data.csv') as file:
  data = file.read()
  lines = data.splitlines()
  print('Lines: ', lines)
--- /code ---

--- /task ---

--- task ---

**Test:** Run your code and look at the text it prints out. Notice how the list is surrounded by the same square brackets — `[]` — you used to make a list. Also, the items in the list are separted by commas, just like your lists were.

```
Lines:  ['team,medals', 'United States,2399', 'Russia,1413', 'Great Britain,1304', 'France,780', 'Germany,671', 'Italy,549', 'Sweden,483', 'Hungary,476', 'China,473', 'Australia,468', 'Japan,398' … 'Sudan,1', 'Togo,1', 'Tonga,1', 'United Arab Emirates,1', 'Virgin Islands,1', 'Liechtenstein,0']
```

--- /task ---

The strings in the `lines` list are all made up of two pieces separated by a comma. Your `chart.add()` function needs each of those pieces separately. 

--- task ---

Loops and lists work really well together, so splitting every string in `lines` apart is very quick: Use a `for` loop and each string's `split()` function to split it into a list — one item for each side of the comma. Then print them out.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 9 
line_highlights: 14-16
---
with open('data.csv') as file:
  data = file.read()
  lines = data.splitlines()
  print('Lines: ', lines)

for line in lines:
  entries = line.split(',')
  print('Entries: ', entries)
--- /code ---

**Tip:** `split()` can split a string into a list around any text you want. You can split on any punctuation, a letter, or even whole words.

--- /task ---

--- task ---

**Test:** Run your code and look at the text it prints out. Each entry should be a list of a nation and their medal count.

```
Entries:  ['Tonga', '1']
Entries:  ['United Arab Emirates', '1']
Entries:  ['Virgin Islands', '1']
Entries:  ['Liechtenstein', '0']
```

**Tip:** Because they're not part of creating the chart, you can place a `#` in front of the code that prints `lines` and `entries` when you're not using them to debug your program. This will turn that code into comments, so Python will ignore it.

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
  chart.add(team, int(medals))  # Convert the medals string to a number for the chart
--- /code ---

--- /task ---

--- task ---

**Test:** Run your code and see what happens.

You should get an error something like this:

```
ValueError: invalid literal for int() with base 10: 'medals' on line 19 in main.py
```

This message means Python can't convert 'medals' into a number with `int()`. This has happened because the first line of `data.csv` is different to all the others: instead of containing a team and the number of medals they have won, it contains the headings 'team' and 'medals'.

--- /task ---

--- task ---

To fix the bug, you need to skip the first line of `data.csv`, which becomes the item at index `0` in `lines`. Lists can be **sliced** to skip items at the start by using `my_list[index:]` where `index` is the index of the item you want to start from. Slice `lines` when you use in the `for` loop to skip the first line.

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
  chart.add(team, int(medals))  # Convert the medals string to a number for the chart
--- /code ---

--- /task ---

--- task ---

**Test:** Run your code and look at the chart it creates. Try hovering over some of the columns, or clicking on the names of teams to add and remove them from the chart.

![A column chart showing the medal counts of many nations](images/completed_preview.png){:width="200px"}

--- /task ---

--- save ---

<mark>Add debug steps</mark>