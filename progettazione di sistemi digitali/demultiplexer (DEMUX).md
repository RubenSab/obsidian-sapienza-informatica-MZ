# demultiplexer standard

> Funzionamento inverso al [[multiplexer (MUX)]].

> Modulo che riceve una linea di ingresso $x$ e $n$ linee di selezione (di cui una sola vale 1), e in output ritorna $n$ linee di uscita, delle quali quella scelta dalla selezione assumerà il valore della linea di ingresso.

Viene prodotto con una serie di [[AND gate con funzione di controllo]], in cui la linea di ingresso è il segnale e le linee di selezione scelgono in quale linea di uscita mandarlo.

![[demultiplexer.svg]]
# demultiplexer con [[decodificatore (DEC)]]

> Riceve una linea di ingresso $x$ e $\log_{2}{n}$ linee di selezione (di cui una sola vale 1), e in output ritorna $n$ linee di uscita, delle quali quella scelta dalla selezione (in base al suo indice) assumerà il valore della linea di ingresso.
> 
> (esempio: selezione = 1 1 -> output del DEC = 0 1 0 0 -> output =  0 $x$ 0 0)
