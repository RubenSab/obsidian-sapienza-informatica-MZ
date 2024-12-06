> La ROM è un modulo standard che riceve in ingresso un indirizzo di memoria e passa in uscita i bit contenuti nella posizione a cui si riferisce l'indirizzo.
> è composta da un [[decodificatore (DEC)]] non standard collegato a una matrice di porte OR (ognuna viene usata per produrre un bit in uscita).
# Esempio

| x2  | x1  | x0  |     | y3  | y2  | y1  | y0  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0   | 0   | 0   |     | 1   | 1   | 1   | 0   |
| 0   | 0   | 1   |     | 1   | 1   | 1   | 1   |
| 0   | 1   | 0   |     | 0   | 0   | 0   | 0   |
| 0   | 1   | 1   |     | 0   | 0   | 0   | 1   |
| 1   | 0   | 0   |     | 0   | 0   | 1   | 0   |
| 1   | 0   | 1   |     | 0   | 0   | 1   | 1   |
| 1   | 1   | 0   |     | 0   | 1   | 0   | 0   |
| 1   | 1   | 1   |     | 0   | 1   | 0   | 1   |

![[ROM.svg]]
La ROM si può rappresentare in modo più chiaro usando una *matrice di OR*:
![[ROM.jpg]]