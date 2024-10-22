è un sistema di codifica dei numeri interi relativi, in cui il bit più significativo dà indicazione del segno (0->+, 1->-), mentre i bit rimanenti vengono sottoposti a un'operazione di [[complementazione]] se rappresentano un valore negativo.
# come interpretare il risultato
1. se il MSB è 1 complemento
2. decodifico i bit restanti usando il binario e considero il valore o positivo o negativo

| 3 bit | bin | complemento a 1 |
| ----- | --- | --------------- |
| 000   | 0   | 0               |
| 001   | 1   | 1               |
| 010   | 2   | 2               |
| 011   | 3   | 3               |
| 100   | 4   | -3              |
| 101   | 5   | -2              |
| 110   | 6   | -1              |
| 111   | 7   | -0              |
```
2-2=0                2-3=-1             3-1=2
  v                    v                  v
2+(-2)=0            2+(-3)=-1          3+(-1)=2

010 +               010 +              011 +
101 =               100 =              110 =
111 = -0            110 = -1           001 = 1 > sbagliato
```
Questa rappresentazione ha un problema:
- se il risultato è negativo allora è corretto,
- se il risultato è positivo allora è decrementato di uno e va corretto, quindi serve un controllo ulteriore che impiega più potenza computazionale.
L'addizione quindi non è efficiente perché bisogna verificare se il risultato va corretto.