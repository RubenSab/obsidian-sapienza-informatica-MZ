> Modulo che riceve $2^{n}$ linee in input e restituisce $n$ linee di output di cui solo una vale 1.

# decodificatore standard

> Funzionamento inverso al [[decodificatore (dec)]].

Il circuito si può rappresentare in modo più chiaro usando una *matrice di AND*: #todo inserire foto

## Esempio a 2 entrate

| x3  | x2  | x1  | x0  | z1  | z0  |
| --- | --- | --- | --- | --- | --- |
| 0   | 0   | 0   | 1   | 0   | 0   |
| 0   | 0   | 1   | 0   | 1   | 0   |
| 0   | 1   | 0   | 0   | 0   | 1   |
| 1   | 0   | 0   | 0   | 1   | 1   |
![[encoder.svg]]
# decodificatore non standard
La regola che lega le entrate e le uscite è diversa, come può essere diverso anche il numero di porte di uscita in relazione a quelle di entrata.