> Modulo che ha $n$ linee in input, $m$ linee in output e $p$ prodotti, è usato per implementare facilmente un'insieme di funzioni partendo sempre dallo stesso schema (per funzioni si intendono tutte quelle formule booleane che definiscono i possibili valori di ogni bit di output al variare dei bit di input) usando SOP minimali.

> è realizzato con un circuito integrato che consiste in una matrice di porte AND programmabili seguite da una matrice di porte OR programmabili.
# esempio
## tavola di verità

| $A$ | $B$ | $C$ |     | $Y_{1}$ | $Y_{2}$ |
| --- | --- | --- | --- | ------- | ------- |
| 0   | 0   | 0   |     | 0       | 0       |
| 0   | 0   | 1   |     | 0       | 0       |
| 0   | 1   | 0   |     | 0       | 0       |
| 0   | 1   | 1   |     | 0       | 1       |
| 1   | 0   | 0   |     | 1       | 0       |
| 1   | 0   | 1   |     | 1       | 1       |
| 1   | 1   | 0   |     | 0       | 0       |
| 1   | 1   | 1   |     | 1       | 1       |
## forme SOP delle funzioni degli output
$Y_{1}=A\overline{B}+A\overline{B}C+ABC=A\overline{B}+AC$
$Y_{2}=BC+AC$
## matrice

![[PLA.png]]
## circuito
![[PLA.svg]]
