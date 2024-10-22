# Caso base
Collegare il minor numero di punti, cioè 2.
2 punti si possono collegare con 1 segmento, e $1=\frac{2(2-1)}{2}$.
Il caso base è dimostrato direttamente.

# Ipotesi induttiva
Se $n$ punti si possono collegare due a due con $\frac{n(n-1)}{2}=\frac{n^2-n}{2}$ segmenti, allora $n+1$ punti si possono collegare con $\frac{(n+1)n}{2}=\frac{n^2+n}{2}$ segmenti.
- Se $P(n)$ è vera, allora $P(n+1)$ è vera.
Se si considera un numero $n$ di punti, essi sono collegati ($P(n)$) due a due con $\frac{n(n-1)}{2}$ segmenti.
Se si aggiunge un punto, i punti saranno collegati da $\frac{n(n-1)}{2}+n$ punti, quindi da $\frac{n(n-1)+2n}{2}$
Rimuovendo un punto, i punti saranno collegati ($P(n)$) due a due con $\frac{n(n-1)}{2}$ punti.
- L'ipotesi induttiva è verificata.
$\square$
