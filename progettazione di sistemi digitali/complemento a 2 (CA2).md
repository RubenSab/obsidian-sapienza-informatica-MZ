è un sistema di codifica dei numeri interi relativi, in cui il bit più significativo è associato a $-2^{n-1}$, dove n è il numero di bit.

| 3 bit | bin | complemento a 2                                                                                       |
| ----- | --- | ----------------------------------------------------------------------------------------------------- |
| 000   | 0   | 0                                                                                                     |
| 001   | 1   | 1                                                                                                     |
| 010   | 2   | 2                                                                                                     |
| 011   | 3   | 3                                                                                                     |
| 100   | 4   | -4 (oppure non viene considerato, è una scelta di chi costruisce l'[[unità aritmetico logica (ALU)]]) |
| 101   | 5   | -3                                                                                                    |
| 110   | 6   | -2                                                                                                    |
| 111   | 7   | -1                                                                                                    |

> Si osserva che per rendere un numero negativo bisogna [[complementazione|complementarlo]] e aggiungere 1, così si può trasformare A-B in A+(-B), trattandola come un'addizione.

L'intervallo di numeri rappresentabili va da -4 a 0 per 3 bit, e da $[-2^{n-1}, 2^{n-1}-1]$ per $n$ bit.  

$$-a_{n-1}*b^{n-1}+\sum_{i=0}^{n-2} a_i * b^{i}= \text{valore in base 10}$$
```
Esempio:
-2^2 2^1 2^0
1    0   1
```

- L'[[overflow]] si verifica se gli operandi sono concordi ma il segno del risultato dell'addizione è diverso da quello del risultato effettivo.

> N.B.: L'overflow **NON si verifica** se c'è un riporto uscente, al contrario del binario, ma indica semplicemente che il risultato è errato.

```
2-2 = 0 -> 2+(-2) = 0

[1] 010   Il riporto uscente non da problemi di overflow come nel binario
    110
    000

2-3=-1

010
101
111


6 + 7                   

0110 +
0111 =
1101 = -3 > sbagliato


7 = 0111 -> complemento 1000 -> +1 1001


```
# estensione del segno in CA2
Si usa per rappresentare su più bit un valore in CA2.
- Se il bit più significativo è 0, allora a sinistra si aggiungono degli 0, altrimenti si aggiungono degli 1.
```
Esempio:
-3 = 1101
estendiamo la lunghezza del registro di 2 bit
1101 -> 111101

si può verificare che in CA2:
1101 = -2^3 + 2^2 + 2^0 = -3
111101 = -2^5 (MSB) + 2^4 + 2^3 + 2^2 + 2^0 = -3

```