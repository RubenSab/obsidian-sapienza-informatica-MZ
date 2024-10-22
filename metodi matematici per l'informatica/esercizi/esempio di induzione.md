$$\forall n \geq 1 \ \ \sum_{i=1}^{n} \frac{1}{i(i+1)}=1-\frac{1}{n+1}$$
# Caso base
$n=1$
per $n=1$, $P(1)$ varrà $\frac{1}{2}$.

# induzione
- Se $P(n)$ è vera, allora $P(n+1)$ è vera.
Aggiungendo un $n$ si ottiene che:
$$P(n+1)=\sum_{i=1}^{n}(\frac{1}{i(i+1)})+\frac{1}{(n+1)(n+2)}=P(n)+\frac{1}{(n+1)(n+2)}$$

$$\forall n \geq 1\ \ P(n+1)=\sum_{i=1}^{n+1} \frac{1}{i(i+1)}=1-\frac{1}{n+2}$$
$$\forall n \geq 1\ \ P(n+1)=\sum_{i=1}^{n} \frac{1}{i(i+1)}+\frac{1}{(n+1)(n+2)}=1-\frac{1}{n+2}$$
$$\sum_{i=1}^{n} \frac{1}{i(i+1)}=1-\frac{1}{n+2}-\frac{1}{(n+1)(n+2)}$$
$$\sum_{i=1}^{n} \frac{1}{i(i+1)}=1-\frac{1}{(n+1)}$$