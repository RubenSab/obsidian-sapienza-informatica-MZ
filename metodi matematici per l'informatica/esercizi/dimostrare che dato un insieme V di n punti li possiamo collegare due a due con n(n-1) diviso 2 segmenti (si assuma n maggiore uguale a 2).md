# Caso base
Collegare il minor numero di punti, cioè 2.
2 punti si possono collegare con 1 segmento, e $1=\frac{2(2-1)}{2}$.
Il caso base è dimostrato direttamente.

# Passo induttivo
Se $n$ punti si possono collegare due a due con $\frac{n(n-1)}{2}=\frac{n^2-n}{2}$ segmenti, allora $n+1$ punti si possono collegare con $\frac{n(n-1)}{2}+n$ segmenti. (intuizione grafica)
- Se $P(n)$ è vera, allora $P(n+1)$ è vera.
$$P(n+1)=\frac{n(n-1)}{2}+n$$
$$P(n+1)=\frac{n(n-1)+2n}{2}$$
$$P(n+1)=\frac{n^2+n}{2}$$
$$P(n+1)=\frac{(n+1)n}{2}$$
$$P(n+1)=\frac{(n+1)(n+1-1)}{2}$$
$P(n+1)$ è nella stessa forma di $P(n)=\frac{(n+1)n}{2}$ $\implies$ L'ipotesi induttiva è verificata.
$\square$
