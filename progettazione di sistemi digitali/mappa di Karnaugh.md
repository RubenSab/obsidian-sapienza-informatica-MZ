Per [[criterio di minimalità|minimizzare]] le [[espressioni booleane]] si usano le **mappe di Karnaugh** (anche dette **K-mappe**) fino a 4 variabili.
# K-mappa a 3 variabili
Tavola di verità generica a 3 variabili:

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

Mappa di Karnaugh corrispondente:

| a/bc | 00  | 01  | 11  | 10  |
| ---- | --- | --- | --- | --- |
| 0    | M0  | M1  | M3  | M2  |
| 1    | M4  | M5  | M7  | M6  |
# "coordinate" delle K-mappe a n variabili

>N.B.: Notiamo che per la K-mappa generica a 3 variabili, le "coordinate" sull' "asse" bc non sono 00 01 10 11, ma 00 01 11 10, infatti la loro numerazione ***non è in binario*** ma in [[Gray code]].
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
Volendo scrivere una SOP, cerchiamo gli 1 adiacenti in gruppi da 2, 4 o 8: 010 con 011 e 011 con 111. Questi sono gli ***implicanti***.

> Un ***implicante*** è un insieme di mintermini/maxtermini che posso esprimere in forma minima.  

L'espressione corrispondente per l'implicante 010 - 011 è $\overline{a} b$, perché 010 e 011 hanno:
- $a=0$ in comune $\implies \overline{a}$
- $b=1$ in comune $\implies b$
- $c=0$ e $c=1$ non in comune $\implies$ non scrivere $c$

L'espressione corrispondente per l'implicante 011 - 111 è $bc$, perché 011 e 111 hanno:
- $a=0$ e $a=1$ non in comune $\implies$ non scrivere $a$
- $b=1$ in comune $\implies b$
- $c=1$ in comune $\implies$ $c$

L'espressione SOP corrispondente alla K-mappa è $\overline{a}b + bc$

# come ricavare le espressioni SOP

Per ogni **riga della tavola della verità in cui l'output è 1** (mintermini), per ogni variabile in input:
- $x=0$ in comune $\implies \overline{x}$
- $x=1$ in comune $\implies x$
- $x=0$ e $x=1$ non in comune $\implies$ non scrivere $x$

Infine sommare tutti i mintermini.
# come ricavare le espressioni POS
Per ogni **riga della tavola della verità in cui l'output è 0** (maxtermini), per ogni variabile in input:
- $x=0$ in comune $\implies x$
- $x=1$ in comune $\implies \overline{x}$
- $x=0$ e $x=1$ non in comune $\implies$ non scrivere $x$

Infine moltiplicare tutti i maxtermini.
# implicanti
> Si definisce un implicante un insieme di 2, 4 o 8 mintermini / maxtermini che posso esprimere in forma minima. Se un uno o zero non può essere raggruppato e sta da solo, allora è un implicante degenere e verrà rappresentato da una somma / un prodotto di tutti i letterali complementati o meno.

>N.B.: Le caselle ai lati opposti della K-mappa si possono raggruppare in implicanti, infatti le K-mappe sono rappresentate come rettangolari ma in realtà esistono su superfici toroidali.