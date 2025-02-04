Per codificare in binario la parte decimale di un numero, bisogna moltiplicare ripetutamente la parte dopo la virgola per per la base (=2 nel codice binario).
```
Esempio:
17,36

17 = 16 + 1 = 10001

0,36*2=[0],72 |
0,72*2=[1],44 |
0,44*2=[0],88 |
0,88*2=[1],76 |
0,76*2=[1],52 v   da ripetere tante volte quanto sono i bit disponibili

0,36 = 01011

17,36 = 10001,01011
```
Ma quanti bit si devono allocare per la parte intera e per la parte decimale?
# virgola fissa
Usa $n$ bit totali:
- $k$ bit per la parte intera
- $n-k$ bit per la parte frazionaria
# virgola mobile
Come nella notazione scientifica esprimiamo il valore usando una potenza della base adeguata.
Lo standard odierno della rappresentazione dei numeri decimali in virgola mobile è "**l'IEEE 754**" (*I triple E*), in cui gli $n$ bit della rappresentazione si dividono in:
- segno (a cui è dedicato un singolo bit $s$, negativo se $s=1$ e positivo se $s=0$)
- esponente (del $*2^n$ della notazione scientifica)
- mantissa (i bit dopo la virgola, l'1 della parte intera è sempre implicito)
>N.B.: la parte intera del numero **non** viene codificata in dei bit dedicati. Anche se in base 10 può sembrare strano, in base binaria basta scegliere l'esponente in modo che la cifra più significativa sia sempre un 1 per ogni numero.

>esempio:
>$1011,011 = 1,011011*2^3$
>$0,001001 = 1,001*2^-2$

## codifiche con livelli di precisione diversi

| n   |                  | s (segno) | e (esponente) | m (mantissa) |
| --- | ---------------- | --------- | ------------- | ------------ |
| 16  | half precision   | 1         | 5             | 10           |
| 32  | single precision | 1         | 8             | 23           |
| 64  | double precision | 1         | 11            | 53           |
## esponente
- Si considera la rappresentazione in [[complemento a 2 (CA2)]], con $e$ bit rappresento un'intervallo di valori possibili di $[-2^{e-1};2^{e-1}-1]$.
- Si aggiunge il bias $2^{e-1}-1$ in modo che l'esponente sia positivo.
>esempio: se $e=5$ il bias è $15$
>se $e=8$ il bias è $127$
- Si ottiene l'intervallo $[-2^{e-1}+2^{e-1}-1;2^{e-1}-1+2^{e-1}] \rightarrow  [-1;2^e-2]$.
- Si eliminano i due valori più piccoli, cioè -1 e 0, ottenendo $[1;2^e-2]$, in binario $[0..01;1..10]$
## rappresentazione
Nello standard IEEE 754, il segno, l'esponente e l mantissa di un numero in virgola mobile viene rappresentato mettendo vicini i bit del segno, dell'esponente e della mantissa; talvolta si usa la base esadecimale (base 16,, più compatta del binario) in cui ogni numero rappresenta 4 bit.
```
Esempio: 26,42 = <0;10011;1010011010> = 0100111010011010
0100 = 4
1110 = E
1001 = 9
1010 = A
26,42 = 0x4E9A
```
## tipi di valori diversi

| tipo                                              | esponente   | mantissa  | segno |
| ------------------------------------------------- | ----------- | --------- | ----- |
| zero                                              | 0           | 0         | +/-   |
| numeri denormalizzati/subnormal (prossimi allo 0) | 0           | $\neq$ 0  | +/-   |
| numeri normali                                    | $[1;2^e-2]$ | qualunque | +/-   |
| infiniti                                          | $2^e-1$     | 0         | +/-   |
| NaN (Not A Number)                                | $2^e-1$     | $\neq$ 0  | +/-   |
>Esempio con $n=16$

| overflow negativi        | $<-(2-2^{-10})*2^{15}$          |
| ------------------------ | ------------------------------- |
| negativi rappresentabili | $[-(2-2^{-10})*2^{15};-2^{14}]$ |
| underflow negativi       | $[-2^{-14}; 0]$                 |
| underflow positivi       | $[0;2^{-14}]$                   |
| positivi rappresentabili | $[2^{-14}; (2-2^{-10})*2^{15}]$ |
| overflow positivi        | $> 2^{15}$                      |
- [[operazioni con numeri in virgola mobile]]


esempi di rappresentazione in virgola mobile:
```
Esempio: n = 16 bit, segno = 1 bit, esponente = 5 bit, mantissa = 10, bias = 15

A = 26,84

26 | 0 ^
13 | 1 ^
 6 | 0 ^
 3 | 1 ^
 1 | 1 ^

26 = 11010

0,42*2 | 0,84 v
0,84*2 | 1,68 v
0,68*2 | 1,36 v
0,36*2 | 0,72 v
0,72*2 | 1,44 v
0,44*2 | 0,88 v

0,84 = 011010

26,84 = 11010,011010 = 1,1010011010*2^4

esponente = 4+15 (bias) = 19(base 10) = 10011

26,42 = <0;10011;1010011010> (approssimazione)

il computer userà 0100111010011010, in esadecimale (0x) sarà:
0100 | 4
1110 | E
1001 | 9
1010 | A
-> 0x4E9A

```

```
Esempio: Dato C9A0 nello standard IEEE 754 half precision convertilo in base 10

C = 1100
9 = 1001
A = 1010
0 = 0000

<1.10010.0110100000>
^      ^      ^
segno  exp.   mantissa

10010 = exp+bias (18)
- bias (15) = 3 (exp) = 2^3 = 100 (base 2)

numero = -1*2^3*1.40625 (1.0110100000) = -11.25
```

```
Esempio in half precision (n = 16 bit, segno = 1 bit, esponente = 5 bit, mantissa = 10, bias = 15)

-37.68

37 | 1
18 | 0
 9 | 1
 4 | 0
 2 | 0
 1 | 1 ^

.68 | 1.36 v
.36 | 0.72
.72 | 1.44
.44 | 0.88
.88 | 1.76

100101.10101 = 1.0010110101*2^5
esponente + bias = 5+15 = 20(base 10) = 10100
20 | 0
10 | 0
 5 | 1
 2 | 0
 1 | 1 ^

37.68 = <1;10100;0010110110> = 0xD0B5

1101 = D
0000 = 0
1011 = B
0110 = 5
```