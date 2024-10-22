è un sistema di codifica dei numeri interi relativi, in cui il bit più significativo rappresenta il segno, mentre i bit rimanenti sono interpretati come nel binario.

| 3 bit | bin | modulo e segno |
| ----- | --- | -------------- |
| 000   | 0   | 0              |
| 001   | 1   | 1              |
| 010   | 2   | 2              |
| 011   | 3   | 3              |
| 100   | 4   | -0             |
| 101   | 5   | -1             |
| 110   | 6   | -2             |
| 111   | 7   | -3             |
Esempio con modulo e segno
```
  2-2=0        2-3=-1
1 010 -        010 -
  110 =        111 =
  000          001 = 1 > sbagliato

```
- L'addizione non è efficiente per stabilire il segno.
- C'è il problema della doppia rappresentazione dello zero.