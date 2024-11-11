> Una funzione non è completamente specificata quando:
- non tutte le combinazioni di input sono definite
- non tutte le combinazioni di output sono definite

In corrispondenza dell'output si scrive $\delta$ (delta), cioè "Don't care".

# esempio
Prendiamo [[dato x contenuto nell'intervallo 0, 7 (compresi) rappresentato in 3 bit CA2 stendere la tavola di verità. y = x-2 rappresentato in CA2 con il minimo numero di bit]] e sostituiamo la richiesta del circuito con la seguente: y = x-2 rappresentato in CA2 con **3 bit** e non con il numero minimo (cioè 4).

Ricaviamo la tabella di verità:
```
bit x2, x1, x2 

    y-2  y2 y1 y0
000 -2   d  d  d
001 -1   1  1  1
010 0    0  0  0
011 1    0  0  1

100 2    0  1  0
101 3    0  1  1
110 4    d  d  d
111 5    d  d  d
```



