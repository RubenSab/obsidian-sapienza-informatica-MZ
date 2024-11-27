![[automa contatore.svg]]
# 1. espressioni booleane
## funzioni di eccitazione
$d_{1}=xy_{0}+\overline{x}y_{1}$
$d_{0}=\overline{x}y_{0}+x\overline{y_{1}}$

## uscite
$z_{1}=d_{1}$
$z_{0}=d_{0}$

# 2. tavola stati futuri

| $x, (y_1, y_0)\text{ stato attuale}$ | $d_1, d_0$ | $z_1,z_0$ | $(y_1,y_0)\text{ stato futuro}$ |
| ------------------------------------ | ---------- | --------- | ------------------------------- |
| 000                                  | 00         | 00        | 00                              |
| 001                                  | 01         | 01        | 01                              |
| 010                                  | 10         | 10        | 10                              |
| 011                                  | 11         | 11        | 11                              |
| 100                                  | 01         | 01        | 01                              |
| 101                                  | 11         | 11        | 11                              |
| 110                                  | 00         | 00        | 00                              |
| 111                                  | 10         | 10        | 10                              |
# 3. diagramma della rete ([[automa a stati finiti]])
#toadd ![[diagramma della rete.png]]
# 4. diagramma della macchina
Astraiamo il diagramma della rete per produrre il diagramma della macchina, che prescinde dai valori di memoria negli stati.

Diamo un nome agli stati:

00 -> $S_0$
01 -> $S_1$
10 -> $S_2$
11 -> $S_3$

#toadd ![[diagramma della macchina.png]]
# 5. descrizione verbale
Intuiamo il funzionamento generale dell'automa a partire dal diagramma della macchina, poi descriviamolo verbalmente:

Contatore (a modulo 4, cioè da 0 a 3) di input uguali a 1.