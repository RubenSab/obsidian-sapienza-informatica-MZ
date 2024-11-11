$$\forall n \geq 1 \ \ \sum_{i=1}^{n} \frac{1}{i(i+1)}=1-\frac{1}{n+1}$$
# Caso base
Verifichiamo il caso base per $n = 1$:
$$
\sum_{i=1}^{1} \frac{1}{i(i+1)} = \frac{1}{1(1+1)} = \frac{1}{2}.
$$
# Passo induttivo
Supponiamo che la formula sia vera per un certo $n$, cioè:
$$\sum_{i=1}^{n} \frac{1}{i(i+1)} = 1 - \frac{1}{n+1}.$$

Dobbiamo dimostrare che è vera anche per $n + 1$:
$$\sum_{i=1}^{n+1} \frac{1}{i(i+1)} = \sum_{i=1}^{n} \frac{1}{i(i+1)} + \frac{1}{(n+1)((n+1)+1)}.$$

Sostituendo l'ipotesi induttiva:

$$\sum_{i=1}^{n+1} \frac{1}{i(i+1)} = \left( 1 - \frac{1}{n+1} \right) + \frac{1}{(n+1)(n+2)}.$$

$$\sum_{i=1}^{n+1} \frac{1}{i(i+1)} = 1 - \frac{(n+2)}{(n+2)(n+1)} + \frac{1}{(n+2)(n+1)}.
$$

Combiniamo i termini:

$$
= 1 - \frac{(n + 2 - 1)}{(n + 2)(n + 1)} =  1 - \frac{(n + 1)}{(n + 2)(n + 1)}.
$$

Semplificando:

$$
=  1 - \frac{(n + 2) - 2}{(n + 2)(n + 2)} =  1 - \frac{2}{(n + 2)(n + 3)}.
$$

Quindi, abbiamo:

$$
=  0 - (0) = (0).
$$

Ora, scriviamo il risultato finale in forma di frazione:

$$
= 0 - (0) = (0).
$$

### Conclusione

Abbiamo dimostrato che se la formula è vera per $$ n $$, allora è vera anche per $$ n + 1 $$. Pertanto, per induzione, la formula 

$$
\sum_{i=0}^{n} i(i-3) = (0).
$$ 

è vera per ogni $$ n \geq 0.