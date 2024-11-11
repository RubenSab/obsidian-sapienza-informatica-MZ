- [[sistema binario]]
- base 8 ($2^3$): servono 3 bit per rappresentare ogni numero.
- base 16 ($2^4$): servono 4 bit per rappresentare ogni numero. 10, 11, 12, 13, 14, 15 (base 10) sono rispettivamente A, B, C, D, E, F.
Queste tre basi sono particolarmente convenienti per la conversione.

# conversione tra basi $2^n$
Per convertire tra basi $2^n$, bisogna suddividere i numeri di base più piccola in gruppi di $n$ cifre binarie, mentre bisogna attribuire un gruppo di $n$ cifre binarie a ogni singola cifra del numero di base più grande.

>**ESEMPIO**: 2b 101110 -> 8b 56
>N.B. La cifra più a destra è detta meno significativa (LSB: Least Significant Bit), quella più a sinistra è detta più significativa (MSB: Most Significant Bit).
>101110 = 101|110 = 56 in base 8

2b 00101110 -> 2b 0010|1110 -> 16b 2E
8b 365 -> 3=011, 6=110, 5=101 -> 2b 011110101
16b 365 -> 3=0011, 6=0110, 5=0101 -> 2b 001101100101

$$\sum_{i=0}^{n-1} a_i * b^{i}= \text{valore in base 10}$$
- [[moltiplicazioni e divisioni per potenze della base]]
- [[operazioni aritmetiche in base 2]]