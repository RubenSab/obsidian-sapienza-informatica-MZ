Per [[criterio di minimalità|minimizzare]] le [[espressioni booleane]] si usano le **mappe di Karnaugh** (anche dette K-mappe**) fino a 4 variabili.
# K-mappa a 3 variabili
La tavola di verità

| a b c | output |
| ----- | ------ |
| 000   | M0     |
| 001   | M1     |
| 010   | M2     |
| 011   | M3     |
| 100   | M4     |
| 101   | M5     |
| 110   | M6     |
| 111   | M7     |

diventa

| a/bc | 00  | 01  | 11  | 10  |
| ---- | --- | --- | --- | --- |
| 0    | M0  | M1  | M3  | M2  |
| 1    | M4  | M5  | M7  | M6  |
In questo modo possiamo individuare i termini adiacenti.
## esempio
| a b c | output |
| ----- | ------ |
| 000   | 0      |
| 001   | 0      |
| 010   | 1      |
| 011   | 1      |
| 100   | 0      |
| 101   | 0      |
| 110   | 0      |
| 111   | 1      |
diventa

| ab/c | 0   | 1   |
| ---- | --- | --- |
| 00   | 0   | 0   |
| 01   | 1   | 1   |
| 10   | 0   | 1   |
| 11   | 0   | 0   |
Cerchiando i mintermini 010 con 011 e 011 con 111, otteniamo gli ***implicanti***.
L'espressione corrispondente per l'implicante 010 - 011 è $\overline{a} b$, perché 010 e 011 hanno:
- $a=0$ in comune $\implies \overline a$
- $b=1$ in comune $\implies b$
- $c=0$ e $c=1$ non in comune $\implies$ non scrivere $c$

L'espressione corrispondente per l'implicante 011 - 111 è $bc$, perché 011 e 111 hanno:
- $a=0$ e $a=1$ non in comune $\implies$ non scrivere $a$
- $b=1$ in comune $\implies b$
- $c=1$ in comune $\implies$ $c$

L'espressione SOP è $\overline{a}b + bc$

Per ricavare l'espressione POS le regole sono:
- $x=0$ in comune $\implies \overline x$
- $x=1$ in comune $\implies x$
- $x=0$ e $x=1$ non in comune $\implies$ non scrivere $x$
# implicanti
> Si definisce un implicante un insieme di 2, 4 o 8 mintermini / maxtermini che posso esprimere in forma minima. Se un uno o zero non può essere raggruppato e sta da solo è un implicante degenere

#todo 
>P.S.: c'è una probabilità superiore al 50% che tutto quello qui scritto sia completamente falso.