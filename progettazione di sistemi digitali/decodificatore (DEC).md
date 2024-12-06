> Modulo che riceve $n$ linee in input e restituisce $2^{n}$ linee di output di cui solo una vale 1.

# decodificatore standard

> Un decodificatore che associa 1 alla porta il cui numero è indicato dai bit in entrata, e 0 a tutte le altre.

Il circuito si può rappresentare in modo più chiaro usando una *matrice di OR*: #toadd inserire foto

## Esempio a 2 entrate

| a   | b   | y3  | y2  | y1  | y0  |
| --- | --- | --- | --- | --- | --- |
| 0   | 0   | 0   | 0   | 0   | 1   |
| 0   | 1   | 0   | 0   | 1   | 0   |
| 1   | 0   | 0   | 1   | 0   | 0   |
| 1   | 1   | 1   | 0   | 0   | 0   |
![[decoder.svg]]

# decodificatore non standard
La regola che lega le entrate e le uscite è diversa, come può essere diverso anche il numero di porte di uscita in relazione a quelle di entrata.