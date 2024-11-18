> Un'unità aritmetico logica ha SEMPRE:

| bit | prodotti dall'ALU  |
| --- | ------------------ |
| N   | risultato negativo |
| Z   | risultato è 0      |
| W   | overflow           |
| C   | carry in uscita    |

```
          A         B
          |         |
	  ____v_________v____
C1  ->|                 |<- N
C0  ->|       ALU       |<- Z
Rin ->|                 |<- W
      |_________________|<- C
               |
			   v
               R
```
> All'interno dell'ALU è SEMPRE presente un adder.
# esempio semplificato con 3 bit in input
## input:
- $A$
- $B$
- $C_1$:
	- vale 0 -> pone a 0 l'operando $A$
	- vale 1 -> passa $A$
- $C_0$:
	- vale 0 ->  passa $B$
	- vale 1 -> passa $\overline B$
- $R_{in}$ è il riporto in entrata al sommatore
## output:
- $Z$:
	- vale 0 se il risultato è 0
	- vale 1 se il risultato è 1
- $W$: bit di overflow

| $C_1$ | $C_0$ | $R_{in}$ | risultato                 |
| ----- | ----- | -------- | ------------------------- |
| 0     | 0     | 0        | $0+B\ (=B)$               |
| 0     | 0     | 1        | $B+1$                     |
| 0     | 1     | 0        | $\overline B$             |
| 0     | 1     | 1        | $\overline B + 1\ (= -B)$ |
| 1     | 0     | 0        | $A+B$                     |
| 1     | 0     | 1        | $A+B+1$                   |
| 1     | 1     | 0        | $A+\overline B$           |
| 1     | 1     | 1        | $A-B$                     |
