> Questo componente del processore effettua calcoli e operazioni logiche. Riceve in input due [[bus]] (a 64 bit nelle architetture moderne) accompagnati da un bus parallelo detto ***opcode*** (Operation Code) per configurarla (scegliere l'operazione da effettuare tra i due bus) e ritorna in output il risultato dell'operazione tra i due bus, cioè un bus altrettanto lungo.

> All'interno delle ALU è SEMPRE presente un [[full adder (FA)]].

# esempio di ALU semplice a 3 bit

| bit | prodotti dell'ALU (stato) |
| --- | ------------------------- |
| N   | risultato negativo        |
| Z   | risultato è 0             |
| W   | overflow                  |
| C   | carry in uscita           |

```
          A (input) B  
(opcode)  |         |
	  ____v_________v____   (stato/status)
C1  ->|                 |-> N
C0  ->|       ALU       |-> Z
Rin ->|                 |-> W
      |_________________|-> C
               |
			   v
               R (risultato)
```
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

## funzionamento:

| $C_1$ | $C_0$ | $R_{in}$ | risultato                  |
| ----- | ----- | -------- | -------------------------- |
| 0     | 0     | 0        | $0+B\ (=B)$                |
| 0     | 0     | 1        | $B+1\ (=\overline{B})$     |
| 0     | 1     | 0        | $\overline B$              |
| 0     | 1     | 1        | $\overline B + 1\ (= B)$   |
| 1     | 0     | 0        | $A+B$                      |
| 1     | 0     | 1        | $A+B+1\ (=\overline{A+B})$ |
| 1     | 1     | 0        | $A+\overline B$            |
| 1     | 1     | 1        | $A-B$                      |
![[ALU 2.svg]]
# altro esempio di ALU

![[ALU.svg]]
