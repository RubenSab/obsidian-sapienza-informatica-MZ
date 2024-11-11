```
F = 1111
7 = 0111
A = 1010
0 = 0000

X = <1;11101;1110100000>

F = 1111
B = 1011
6 = 0110
0 = 0000

Y = <1;11110;1101100000>

gli addendi sono entrambi negativi, posso eseguire la somma fra le mantisse con segno negativo.

esponente di X = 29 (la mantissa di X deve shiftare a destra di 1 e l'esponente di X deve diventare uguale a quello di Y)
esponente di Y = 30

somma:
 0,1111010000*2^30 (1 implicito shiftato a dx di 1 con la mantissa)
 1,1101100000*2^30
10,1100110000*2^30

normalizzazione
1,01110011000*2^31

R = <1;11111;0111011000> l'esponente 31 non va bene (non è in [1,30]) perché è riservato a valori infiniti -> overflow dell'esponente
