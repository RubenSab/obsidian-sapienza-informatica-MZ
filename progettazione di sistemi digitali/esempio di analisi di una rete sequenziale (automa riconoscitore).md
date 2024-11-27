![[rete sequenziale 2.svg]]
# 1. espressioni booleane
- $j_{0}=k_{0}=x\oplus y_{1}$
- $j_{1}=k_{1}=\overline{y_{0}}$
- $z=(x\oplus y_{0})y_{1}$

# 2. tavola degli stati futuri

| $x, y_{1}, y_{0}$ | $j_{1}, k_{1}$ | $j_{0}, k_{0}$ | $z$ | $Y_{1}, Y_{0}$ |
| ----------------- | -------------- | -------------- | --- | -------------- |
| 000               | 11             | 00             | 0   | 10             |
| 001               | 00             | 00             | 0   | 01             |
| 010               | 11             | 11             | 0   | 01             |
| 011               | 00             | 11             | 1   | 10             |
| 100               | 11             | 11             | 0   | 11             |
| 101               | 00             | 11             | 0   | 00             |
| 110               | 11             | 00             | 1   | 00             |
| 111               | 00             | 00             | 0   | 11             |
# 3. diagramma della rete
#toadd ![[diagramma della rete 2.png]]
# 4. diagramma della macchina
01 -> $S_I$
00 -> $S_1$
10 -> $S_{10}$
11 -> $S_{11}$

#toadd ![[diagramma della macchina 2.png]]
# 5. descrizione verbale
Automa riconoscitore di 101 e 110 con sovrapposizioni (produce 1 in uscita quando ha queste triple di bit).
Esempio di input e output:

input: 0101101
output 0001011

```
   __v
 __v__v
0101101
   | ||
   v vv
0001011

```