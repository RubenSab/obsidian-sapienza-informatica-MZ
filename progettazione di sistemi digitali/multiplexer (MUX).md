# multiplexer standard

> Modulo che riceve $n$ linee in ingresso e $n$ linee di selezione (di cui una sola vale 1), e in output ritorna le linee di ingresso scelte dalle linee di selezione.

Viene prodotto con una serie di [[AND gate con funzione di controllo]], in cui le linee di ingresso sono il segnale da selezionare, e le linee di selezione le selezionano.

> Espressione booleana: $x_{3}s_{3}+x_{2}s_{2}+x_{1}s_{1}+x_{0}s_{0}$

![[multiplexer.svg]]
# multiplexer con [[decodificatore (DEC)]]

> Riceve $n$ linee in ingresso e $\log_{2}{n}$ linee di selezione (di cui una sola vale 1) che scelgono il segnale da mandare in output in base al suo indice (esempio: selezione = 10 -> output = valore dell'ingresso numero 2), e in output ritorna la linea di ingresso scelta dalle linee di selezione.

> Espressione booleana: $x_{3}\overline{c_{1}}\cdot\overline{c_{0}}+x_{2}\overline{c_{1}}\cdot{c_{0}}+x_{1}{c_{1}}\cdot\overline{c_{0}}+x_{0}{c_{1}}\cdot{c_{0}}$

![[multiplexer_con_decodificatore.svg]]

# uso del mux per realizzare funzioni booleane
## esempio
```
abc f      _______
000 0    0-|     |
001 1    1-|     |
010 0    0-|     |
011 0    0-| mux |--> f
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
011 0   not(c)-|_____|
100 0            ^ ^
101 1            a b
110 1
111 0
```
Semplificando ancora:
```
abc f             _______
000 0   not(b)*c -|     |
001 1    b xor c -| mux |--> f
010 0             |_____|
011 0                ^
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
011 0                ^
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
011 0
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