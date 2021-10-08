## Upgrade your project

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
In this step, try changing how your chart appears, or what it displays.
</div>
<div>
![A column chart showing the medal counts of many nations](images/completed_preview.png){:width="300px"}
</div>
</div>

### Use a Pie chart
Instead of displaying your data with a bar chart, you can use a pie chart for a different look, or to show how something has been split up.

--- task ---

To create a pie chart instead of a bar chart, change the function you import from `pygal`, and the function call you use to create `chart`, to be `Pie` instead of `Bar`. 

--- /task ---

### Display the first ten teams
There's a lot of data displayed on the chart at the moment. Try displaying only the first ten teams, so it's easier to see and compare them.

--- task ---

To display fewer teams on the chart, you can slice the `lines` list from the end as well as from the start. You used `lines[1:]` to start from the string at postion `1`. If you use `lines[:5]`, every string with an index of `5` or higher will be ignored. 

--- /task ---

### Use a different set of data
You can load and chart any data that's in a `.csv` file with the program you've written.

--- task ---

Add another data file to your project by clicking on the 'Create text file' button and giving the file a name that ends in `.csv`.

![A set of buttons, with the + shaped one highlighted](images/completed_preview.png)

Then copy and paste one of the data sets below into your new file.

--- collapse ---
---
title: The MCU Infinity Saga — film length and gross
---

```
Name,Length (mins),Gross ($)
Iron Man,126,585366247
The Incredible Hulk,112,264770996
Iron Man 2,124,623933331
Thor,115,449326618
Captain America: The First Avenger,124,370569774
The Avengers,143,1518812988
Iron Man 3,130,1214811252
Thor: The Dark World,112,644783140
Captain America: The Winter Soldier,136,714421503
Guardians of the Galaxy,121,772776600
Avengers: Age of Ultron,141,1402805868
Ant-Man,117,519311965
Captain America: Civil War,147,1153296293
Doctor Strange ,115,677718395
Guardians of the Galaxy Vol. 2,136,863756051
Spider-Man: Homecoming,133,880166924
Thor: Ragnarok,130,853977126
Black Panther,134,1346913161
Avengers: Infinity War,149,2048359754
Ant-Man and the Wasp,118,622674139
Captain Marvel,123,1128274794
Avengers: Endgame,181,2797501328
Spider-Man: Far From Home,129,1131927996
```

--- /collapse ---

<mark>TODO: Good environmental dataset</mark>

--- /task ---

--- task ---

Update the code that reads from `data.csv` to read from your new file. Some of the files have more than one set of interesting numbers — use different indexes in the `enteries` list to choose between them.

--- /task ---