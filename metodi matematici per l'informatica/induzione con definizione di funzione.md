Definizione di $f(n)$:
$f(0) = 0$
$f(n+1)=f(n)+2n+2$

Si dimostri che $\forall n, f(n)=n(n+1)$
# Caso base
$f(0)=0$ verificato per definizione
# Passo induttivo
$\forall n, f(n)=n(n+1)$ Si assume vera
$f(n+1)=f(n)+2n+2$ Ipotesi induttiva
$f(n+1)=n(n+1)+2n+2$ Sostituzione di $f(x)$ con l'ipotesi induttiva
$f(n+1)=n(n+1)+2(n+1)=(n+1)(n+2)$, che è nella stessa forma di
$f(n)=n(n+1)$, quindi $f(n+1)$ è dimostrata.