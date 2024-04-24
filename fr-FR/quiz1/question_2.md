
--- question ---

---
legend: Question 2 sur 3
---

Ton projet a utilisé des données chargées à partir d'un fichier pour te permettre de présenter des centaines d'informations sous forme de graphique. Lequel de ces morceaux de code chargerait correctement `data.csv` dans une variable sous forme de chaîne de texte ?

--- choices ---

- (x)
```python
with open('data.csv') as f:
  info = f.read()
```
  --- feedback ---

  C'est correct ! Cela chargera `data.csv` comme `f` puis le lira, `read()`, dans `info` sous forme de chaîne de texte.

  --- /feedback ---

- ( )
```python
open('data.csv') as f:
  info = f.read()
```

  --- feedback ---

  Pas tout à fait, tu n'es pas loin, mais il manque quelque chose d'important au début.

  --- /feedback ---

- ( )
```python
with open('data.csv') as f:
info = f.read()
```

  --- feedback ---

  C'est presque ça ! C'est le bon code, mais l'indentation est incorrecte.

  --- /feedback ---

- ( )
```python
with open('data.csv') as f:
  info = read(f)
```

  --- feedback ---

  Pas exactement — la fonction `read()` appartient au fichier stocké dans `f`, tu dois donc l'appeler avec `.` au lieu de lui transmettre `f` .

  --- /feedback ---

--- /choices ---

--- /question ---
