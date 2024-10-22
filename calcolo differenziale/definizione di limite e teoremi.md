> Si dice che una [[successione]] di [[numeri reali]] $a_n$ ***converge*** a $L \in \mathbb{R}$, *tende* a $L \in \mathbb{R}$ se $$\forall \varepsilon\geq 0\ \ \ \ \ \exists n_{\varepsilon}\in\mathbb{N}\ |\ |a_{n}-L|\leq\ \varepsilon \ \ \ \ \ \forall n \geq n_{\varepsilon}$$

$L$ = valore del limite
# teorema di unicità del limite
> Se il limite esiste, allora è unico.

Esempio: $a_{n}=\frac{1}{{n+1}}$
$\lim_{n\rightarrow+\infty}{\frac{1}{{n+1}}=0}$
Tesi: $\exists n_\varepsilon\in\mathbb{N}|\ \ \ |\frac{1}{{n+1}}-0|\leq\epsilon\ \ \ \ \forall n \geq n_{\varepsilon}$
$n\geq \frac{1}{{\varepsilon}}-1\Longleftrightarrow n_{\varepsilon}=\frac{1}{{\varepsilon}}-1$
# successioni divergenti
> Si dice che $a_{n}$ che diverge a $+\infty$ ***diverge positivamente*** se $$\forall M > 0 \ \ \ \exists n_{M}\in\mathbb{N}|\ a_{n}\geq M\ \ \ \forall n \geq n_{M}$$

> Si dice che $a_{n}$P che diverge a $-\infty$ ***diverge negativamente*** se $$\forall M < 0 \ \ \ \exists n_{M}\in\mathbb{N}|\ a_{n}\leq M\ \ \ \forall n \geq n_{M}$$
# teorema della distributività del limite
Siano
> $a_{n} \rightarrow L \in \mathbb{R}$
$b_{n}\rightarrow M \in \mathbb{R}$

Allora
>$a_n+b_n\rightarrow L+M$
$a_n-b_n\rightarrow L-M$
$a_n\times b_n\rightarrow L\times M$
$a_n/b_n\rightarrow L/M,M\neq0$

# teorema dei carabinieri (o del confronto)
>$$a_{n} \leq b_{n} \leq c_{n}$$
>$$a_{n}\rightarrow L \text{ e } c_{n}\rightarrow L \implies b_{n} \rightarrow L$$
## teorema monocarabiniere
> Date $a_{n}\geq b_{n}$
- Se $b_{n}\rightarrow+\infty\ \implies a_{n}\rightarrow+\infty$
- Se $b_{n}\rightarrow-\infty \implies a_{n}\rightarrow-\infty$
# teorema $(1+h)^{n}\geq1+nh$
> Se $h>0$, si ha $(1+h)^{n}\geq1+nh \ \forall n \in \mathbb{N}$

# generalizzazione dei teoremi sui limiti
$a_n\rightarrow+\infty$
$b_n\rightarrow L$
$a_n+b_n\rightarrow+\infty$
$a_n-b_n\rightarrow+\infty$
$a_{n}b_n\rightarrow$
- $+\infty\text{ se }L>0$
- ***forma indeterminata*** se $L = 0$
- $-\infty \text{ se } L<0$
# forme indeterminate
- $\infty\bullet0$
- $\infty-\infty$

