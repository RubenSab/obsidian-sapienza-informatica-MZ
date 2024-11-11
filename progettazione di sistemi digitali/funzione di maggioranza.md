>Una funzione a $k$ ingressi che vale 1 se la maggioranza degli ingressi valgono 1, sia $k$ un numero dispari. Se $k$ è un numero pari, si può scegliere se la funzione varrà 1 se almeno $\frac{k}{2}$ o $\frac{k}{2}+1$ ingressi valgono 1.

Esempio:
```
abcd f1 f2
0000 0  0
0001 0  0
0010 0  0
0011 1  0

0100 0  0
0101 1  0
0110 1  0
0111 1  1

1000 0  0
1001 1  0
1010 1  0
1011 1  1

1100 1  0
1101 1  1
1110 1  1
1111 1  1

f1 POS ha 5 maxtermini
f2 SOP ha 5 mintermini
```
