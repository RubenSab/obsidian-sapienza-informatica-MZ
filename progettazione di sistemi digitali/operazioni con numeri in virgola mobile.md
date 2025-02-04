# addizione e sottrazione
1. Portiamo gli addendi alla stessa potenza della base (la maggiore). (allineamento degli operandi)
2. Decidere l'operazione (tra somma e sottrazione) e l'ordine degli operandi.
3. Decidere il segno del risultato
4. Eseguire l'operazione
5. Valutare il risultato e aggiustare la potenza portandola allo standard (normalizzazione)
```
Somma tra:

A = < 0; 10011; 1010011010 >
B = < 1; 10100; 0010110101 >

1. Portare allo stesso esponente

eA = 19
eB = 20
portiamo A ad esponente 20 e spostiamo a dx la mantissa di una posizione (1 implicito !!!)

A = 0 10100 0,1101001101
B = 1 10100 1,0010110101 (il primo uno è implicito)


2. Decidere l'operazione
A > 0
B < 0 -> sottrazione


3. Decidere il segno del risultato (ordine degli operandi)
|B|>|A| -> B - A
e il risultato avrà segno meno


4. Esecuzione della sottrazione
B 1,0010110101 (*2^20) -
A 0,1101001101 (*2^20) =
  0,0101101000 (*2^20)


5. Normalizzazione
1,0110100000 (2^-2 * 2^20) = 1,0110100000 (*2^18)


6. Risultato
segno = - (1)
esponente = 18 (10010)
mantissa = 0110100000
<1;10010;0110100000> = 0xC9A0


Verifica:
A = 26,42
B = -37.68
A+B = -11.26
0xC9A0 = -11.25
```

```
Esempio:
A = <1;11101;1110100000>
B = <1;11110;1101100000>

eA = 29
eB = 30

Scorrimento di A di una posizione a destra

mantissa di A: 0,(1)11101
mantissa di B: (1),110110
somma = 10,110011*2^30 = 1,011011*2^31
2^31 = 11111 
11111 è escluso perché è una sequenza speciale dell'esponente per indicare valori speciali
```

```
A = <1;00101;1101000000>
B = <1;10011;1010000000>

eA = 5
eB = 19
eB-eA = 14

la mantissa di A e il suo 1 implicito si perdono per lo scorrimento di 14 posizioni. Ciò succede per tutti gli spostamenti maggiori di 11.

```

# moltiplicazione
- Moltiplica le mantisse degli operandi (1 implicito incluso)
- Somma tra gli esponenti
- Normalizzazione
- Determinare il segno del risultato

>N.B.: gli esponenti si ottengono sommando il bias, ma quando sommo gli esponenti avrei 2 bias, quindi bisogna toglierne 1.

```
A = <0;10001;0101000000>
B = <1;10000;0110000000>


1. Moltiplicazione tra le mantisse (+1 implicito)

     1,0101 * (4 cifre significative dopo la virgola)
     1,0110 = (3 cifre significative dopo la virgola)
     1 0101
-------------
    10 101
   101 01
  0000 0
1 0101
-------------
1,1100 111 (4+3 = 7 cifre significative dopo la virgola)


2. Esponenti

eA+bias = 17 = 2+15
eB+bias = 16 = 1+15
eA+eB+bias = 2+1+15 = 18


3. Normalizzazione
la mantissa è già normalizzata

4. Segno
è meno

A * B = <1;100110;11001111000> = 0xCB38

```