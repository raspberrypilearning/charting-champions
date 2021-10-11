
--- question ---

---
legend: Question 3 of 3
---

A list is created and printed out using the following code:

--- code ---
---
language: python
---

colours = ['red', 'green', 'blue', 'yellow', 'pink', 'brown']

for colour in colours[2:]:
  print(colour)

--- /code ---

Which of these would you expect the program to display?

--- choices ---

- ( ) 
```
red
green
blue
yellow
pink
brown
```
  --- feedback ---
  
  That's not quite right — the list has been sliced, so some items will be skipped.

  --- /feedback ---

- ( ) 
```
blue
```

  --- feedback ---

  Not exactly, `colours[2:]` doesn't select the item at index `2` in the list. Selecting would be `colours[2]`, the `:` makes a big difference! Instead, the items with an index lower than `2` are skipped. This is called slicing the list.

  --- /feedback ---

- (x) 
```
blue
yellow
pink
brown
```

  --- feedback ---
  
  That's correct! The items with an index lower than `2` get skipped, and everything else gets printed out. Even though `blue` is in third position on the list, it has an index of `2` because list indexes start at `0`.

  --- /feedback ---

- ( ) 
```
green
blue
yellow
pink
brown
```

  --- feedback ---
  
  Very close, but although `green` is in second position on the list, its index is `1`, because list indexes start at `0`.

  --- /feedback ---

--- /choices ---

--- /question ---
