Σ = {0, 1} (esempio di alfabeto di codifica).
32bit, 64bit, n_bit = ogni informazione è suddivisa in registri di 32, 64 o n_bit: un valore prefissato che indica il massimo di bit disponibili per comporla.

Questo limita il numero di informazioni possibili che un registro può codificare.

>**ESEMPIO**:
>Dobbiamo comporre una stringa con solo 3 simboli. Quante stringhe possiamo comporre?
>Dipende dalla [[cardinalità (o potenza)]] dell'alfabeto di [[funzioni di codifica e decodifica|codifica]], ad esempio se abbiamo l'alfabeto binario (Σ = {0, 1}) ne possiamo comporre $2^3$, mentre se usiamo l'alfabeto italiano (Σ = {a, b, ..., z}) ne possiamo comporre $21^3$.
>Nel primo caso, dato che il registro usa 3 bit, possiamo rappresentare solo $2^3$ informazioni diverse (in cui dobbiamo comporre/$scomporre tutto il flusso di informazioni).

Il modo naturale di codificare i numeri naturali in binario, è contando usando l'ordine posizionale, proprio dei [[sistemi numerici posizionali]].

0(10) = 0000(2)
1(10) = 0001(2) = 2^0 
2(10) = 0010(2) = 2^1 
... ...
15(10) 1111(2) = 2^3 + 2^2 + 2^1 + 2^0 

>**ESEMPIO**: decodificando 101101 si ottiene 2^0 + 2^2 + 2^3 + 2^5 = 1+4+8+32 = 45
>**ESEMPIO**: non si può decodificare un numero non sapendone la base: 312 sarà al minimo di base 4, perché troviamo il simbolo 3, cioè 4-1 (base-1).
>Supponiamo che sia in base 4 -> 3x4^2 + 1x4^1 +2x4^0 = 54 (base 10)

# come de/codificare i numeri da una base n a una base m
Dividendolo per m e appuntandosi il resto in una colonna a ogni divisione finché si raggiunge l'uno
>**ESEMPIO**: 26(10) = 11010(2)

```
26|0
13|1 (26/base = 13 -> 26/13 non ha resto, scrivo zero)
 6|0 (13/6 ha il resto di 1, scrivo 1)
 3|1
 1|1
```
Leggendo dal basso verso l'alto si legge 11010(b2), cioè 26(b10) in base 2.
Il procedimento è molto più semplice per convertire in una base minore di quella di partenza.