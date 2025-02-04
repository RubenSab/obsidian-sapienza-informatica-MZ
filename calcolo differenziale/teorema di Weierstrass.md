Data $f: [a, b] \rightarrow \mathbb{R}$ continua, allora $$\exists x_{m}, x_{M} \in [a, b]\ |\ m = f(x_{m}) \leq f(x) \leq f(x_{M}) = M\ \ \forall x \in [a, b]$$
> $m$ è il minimo assoluto di $f(x)$
> $M$ è il massimo assoluto di $f(x)$
> $x_{m}$ si dice punto di minimo
> $x_{M}$ si dice punto di massimo

Cioè ogni valore assunto da $f(x)$ è compreso tra il suo massimo e minimo assoluto

Consideriamo un $y=t$ generico. Vale che:
$v_{m}\leq t \leq v_{M} \implies \exists c\ |\ f(c) = t$
invece se $t > v_{M} \land t < v_{m} \implies \nexists c  \in [a, b]\ |\ f(c)=t$

Ciò significa che: $f([a,b])=\{f(x),\ x \in [a, b]\} = [v_{m}, v_{M}]$ per ogni funzione continua.

# teorema di Weierstrass generalizzato
Se $f: [a, b] \rightarrow \mathbb{R}$ è continua, allora
- $\lim_{x\rightarrow a^{+}}f(x)=+\infty = \lim_{x\rightarrow b^{-}}f(x) \implies \exists m$
- $\lim_{x\rightarrow a^{+}}f(x)=-\infty = \lim_{x\rightarrow b^{-}}f(x) \implies \exists M$