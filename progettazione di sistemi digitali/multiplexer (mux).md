# multiplexer standard

> Modulo che riceve $n$ linee in ingresso e $n$ linee di selezione (di cui una sola vale 1), e in output ritorna la linea di ingresso scelta dalle linee di selezione.

Viene prodotto con una serie di AND di gating, in cui le linee di ingresso sono il segnale da selezionare, e le linee di selezione le selezionano.

> Espressione booleana: $a\overline{c_{1}}\overline{c_{0}} + b\overline{c_{1}}c_{0} + c c_{1} \overline{c_{0}} + d c_{1} c_{0}$

![[multiplexer.svg]]
# multiplexer con [[decodificatore (dec)]]

#todo aggiungi descrizione

![[multiplexer_con_decodificatore.svg]]

# uso del mux per realizzare funzioni booleane
## esempio
```
abc f      _______
000 0    0-|     |
001 1    1-|     |
010 0    0-|     |
111 0    0-| mux |--> f
100 0    0-|     |
101 1    1-|     |
110 1    1-|     |
111 0    0-|_____|
            ^ ^ ^
            a b c <--- linee di selezione
```
> N.B.: Per funzioni che hanno molte variabili in ingresso si preferisce usare un multiplexer con meno variabili.

```
abc f          _______
000 0        c-|     |
001 1        0-| mux |--> f
010 0        c-|     |
111 0   not(c)-|_____|
100 0            ^ ^
101 1            a b
110 1
111 0
```
Semplificando ancora:
```
abc f             _______
000 0    not(b)  -|     |
001 1    b xor c -| mux |--> f
010 0             |_____|
111 0                ^
100 0                a
101 1
110 1
111 0
```
oppure, cambiando *variabile di selezione*:
*b*:
```
abc f             _______
000 0          c -|     |
001 1   a*not(c) -| mux |--> f
010 0             |_____|
111 0                ^
100 0                b
101 1
110 1
111 0
```
*c*:
```
abc f             _______
000 0         ab -|     |
001 1     not(b) -| mux |--> f
010 0             |_____|
111 0                ^
100 0                c
101 1
110 1
111 0
```

## esempio con due livelli di mux
```
abc f
--- -
000 0
001 1
010 0
111 0
--- -
100 0
101 1
110 1
111 0
--- -
```

![[2mux.svg]]
Che può essere ottimizzato in:
![[demux2.svg]]