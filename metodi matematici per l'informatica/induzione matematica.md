$$[P(0)\wedge(P(n)\implies P(n))]\implies \forall n, P(n)$$
- sul libro è *proprietà dei numeri naturali*.

> L'induzione è un metodo di dimostrazione che si può applicare in moltissimi contesti.

Per tutto quello che può essere scritto come $\forall n \in \mathbb{N}$ esiste almeno una proprietà $P(n)$.

- Esempio: la somma degli angoli interni di un poligono di $n$ lati $\forall n \geq 3$ è $180(n-2)$.

>Una proprietà dei numeri naturali è che $n$ o è $0$ o è $n+1$, cioè il successivo di un altro numero.

# esempio con la formula di Gauss

Quanto vale $\sum_{i=0}^{k} i$?
## tentativi iniziali
$0+1 = 1$
$0+1+2 = 3$
$0+1+2+3 = 6$
$0+1+2+3+4 = 10$
## intuizione
$$0+...+k = \sum_{i=0}^{k} i=\frac{k(k+1)}{2} = P(k), k \in \mathbb{N}$$

| 0   | 1   | 2   | 3   | 4   | 5   |
| --- | --- | --- | --- | --- | --- |
| 5   | 4   | 3   | 2   | 1   | 0   |
## dimostrazione rigorosa dell'intuizione
- Questa è semplicemente un intuizione, dobbiamo dimostrare la proprietà per ogni numero naturale per avere  una dimostrazione rigorosa.
- Sfruttiamo la proprietà dei numeri naturali che dice che $n$ o è $0$ o è $n+1$, cioè il successivo di un altro numero.
1. Nel **caso base**, il numero più piccolo per cui la proprietà si può dimostrare, cioè $0$, $P(0)$ vale.
2. Ora cerchiamo di dimostrare $P(n+1)$ ipotizzando durante la dimostrazione che valga $P(n)$. -> **IPOTESI INDUTTIVA**. Per la *proprietà associativa della somma* vale che:
$$P(n)=\sum_{i=0}^{n+1} i=(\sum_{i=0}^{n} i)+(n+1)$$
3. Se $P(n)=\sum_{i=0}^{n+1} i$ è vera, allora $(\sum_{i=0}^{n} i)+(n+1)$ è vera. (ipotesi induttiva)
$$(\sum_{i=0}^{n} i)+(n+1) = \frac{{n(n+1)}}{2}+n+1$$
4. Riscriviamo l'espressione e verifichiamo la veridicità dell'tesi iniziale.
$$\frac{{n(n+1)}}{2}+n+1=\frac{{(n+1)(n+2)}}{2}=\sum_{i=0}^{n-1} i$$
# perché l'induzione funziona
- Abbiamo dimostrato che $P(k)$ è vero, ma supponiamo per assurdo che $\exists k\ |\ P(k)$  sia falso, (sia $k$ il più piccolo intero per cui $P(k)$ è falso) e $P(k)$ valga almeno per $0$ (per dimostrazione diretta).
- Ma se $P(k) \implies P(k-1)$ è vero, allora se $P(k)$ è falso allora anche $P(k-1)$ è falso.
- Questo significa che si arriverà a dire che $P(0)$ è falso, ma ciò è un assurdo.



# esempio con la somma degli angoli interni dei poligoni
TESI: Per ogni $n \geq 3$ la somma degli angoli interni di un poligono di $n$ lati è uguale a $180(n-2)$
1. Caso base: per $3$ lati, un poligono ha $180$ gradi.
2. Consideriamo un poligono di $n$ lati, assumiamo che un poligono 


$\forall n\ n^{3}+5n$ è multiplo di $6$.

$P(0)=0$ -> vero


$n^{3}+5n = 6k$ PER IPOTESI

$(n+1)^{3}+5(n+1)$
$n^3+3n^2+3n+5n+6$
$(n^3+5n)+3n^2+3n+6$ 
$3n^2+3n+6+3n(n+1)$
$3n^2+3n$ è multiplo di 6 per ipotesi induttiva
$6$ è multiplo di 6
$3n(n+1)$ è multiplo di 3, ma è anche un multiplo di 2, perché è il prodotto di due numeri consecutivi, quindi un numero pari per un numero dispari. un multiplo di 3 e di 2 è anche un multiplo di 6.

la somma di n multipli di 6 è un multiplo di 6.