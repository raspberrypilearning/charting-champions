
--- question ---

---
legend: Vraag 2 van 3
---

Jouw project gebruikte gegevens die uit een bestand waren geladen, zodat je honderden stukjes informatie in kaart kon brengen. Welke van deze stukjes code zou `data.csv` correct in een variabele laden als een string?

--- choices ---

- (x)
```python
with open('data.csv') as f:
  info = f.read()
```
  --- feedback ---

  Dat is correct! Hierdoor wordt `data.csv` geladen als `f` en vervolgens ingelezen via `read()` in `info` als string.

  --- /feedback ---

- ( )
```python
open('data.csv') as f:
  info = f.read()
```

  --- feedback ---

  Niet helemaal, dit komt heel dichtbij, maar er ontbreekt in het begin iets belangrijks.

  --- /feedback ---

- ( )
```python
with open('data.csv') as f:
info = f.read()
```

  --- feedback ---

  Heel dichtbij! Dit is allemaal de juiste code, maar de inspringing is verkeerd.

  --- /feedback ---

- ( )
```python
with open('data.csv') as f:
  info = read(f)
```

  --- feedback ---

  Niet precies: de functie `read()` hoort bij het bestand dat is opgeslagen in `f`, dus je moet het aanroepen met `.` in plaats van `f` eraan door te geven.

  --- /feedback ---

--- /choices ---

--- /question ---
