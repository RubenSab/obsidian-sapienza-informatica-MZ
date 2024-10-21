# addizione
```
Esempi:

0110 +                 01111 +
0011 =                 00111 =
1001                   10110
```
>N.B.: Se la macchina ha solo $n$ bit di memoria a disposizione, allora sommare $2^n-1$ a qualsiasi numero intero, essa andrà in [[overflow]].
# sottrazione
```
Esempio:

1010 -
0111 =
0001
```
# moltiplicazione
Per la moltiplicazione si assegnano il doppio dei bit rispetto al moltiplicando e al moltiplicatore (assumendo che abbiano lo stesso numero di bit), in modo che non si vada in overflow. Questo perché il più grande valore che si può ottenere moltiplicando due numeri di $n$ cifre è $(2^n-1)^2$, e vale che:
$$(2^n-1)(2^n-1)<2^{2n}+2^{2n-1}+...+2^{0}\}\forall n$$ $$\text{esempio: } (2^4-1)(2^4-1)=225, 225<255$$
```
Esempi:

    1010 *             0111 *
    0111 =             0111 =
    1010               0111
   1010               0111
  1010               0111
 0000              00110001
01000110
```

>N.B.: Se ho un valore k quanti bit occorrono per rappresentarlo? $\lceil{\log_{2}k}\rceil$
# compiti
convertire 19, 42, 57 in base 2, 3, 5, 8

sommare e moltiplicare in base 2 E 3

verificare i risultati