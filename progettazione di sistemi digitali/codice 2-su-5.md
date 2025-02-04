>è una codifica ridondante utile per trasmettere le informazioni permettendo di controllare se si sono verificati [[errori di trasmissione]]. In questa codifica solo 2 bit su 5 valgono 1, e a ogni bit si associa un peso.

```
Esempio: pesi 6 3 2 1 0 (ma potrebbero essere diversi) 

  63210
0 00110 (0=1+2 perché 1 con 2 non è usato da nessun'altra parte)
1 00011 (1=1+0)
2 00101 (2=2+0)
3 01001 (3=3+0)
4 10010 (4=3+1)
5 01100 (5=3+2)
6 10001 (6=6+0)
7 10010 (7=6+1)
8 10100 (8=7+1)
9 11000 (9=6+3)
```

