- [[sintesi di reti sequenziali]]
# 1. descrizione verbale
> Circuito che somma due numeri sommando due bit alla volta ($a_{i}$,$b_{i}$) e produce gli output $c_{i}$, $s_{i}$

# 2. stati dell'automa
- $S_{0}$ = riporto 0
- $S_{1}$ = riporto 1

|         | 00        | 01        | 10        | 11        |
| ------- | --------- | --------- | --------- | --------- |
| $C_{0}$ | $C_{0}/0$ | $C_{0}/1$ | $C_{0}/1$ | $C_{1}/0$ |
| $C_{1}$ | $C_{1}/1$ | $C_{1}/0$ | $C_{1}/0$ | $C_{1}/1$ |
#toadd ![[automa sommatore.png]]
# 3. codifica degli stati

|         | $y$ (riporto) |
| ------- | ------------- |
| $C_{0}$ | 0             |
| $C_{1}$ | 1             |
> N.B.: Il riporto è codificato negli stati, la somma $s_{i}$ è l'output

# 4. tabella degli stati futuri realizzata con [[flip-flop (JK)]]

| $a_{i}b_{i}y_{i}$ | $Y$ (stato futuro) | $s_{i}$ | $jk$       |
| ----------------- | ------------------ | ------- | ---------- |
| 000               | 0                  | 0       | 0 $\delta$ |
| 001               | 0                  | 1       | $\delta$ 1 |
| 010               | 0                  | 1       | 0 $\delta$ |
| 011               | 1                  | 0       | $\delta$ 0 |
| 100               | 1                  | 1       | 0 $\delta$ |
| 101               | 1                  | 0       | $\delta$ 0 |
| 110               | 1                  | 0       | 1 $\delta$ |
| 111               | 1                  | 1       | $\delta$ 0 |
- kmappa

#todo