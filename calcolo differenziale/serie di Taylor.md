> Se la funzione $f$ è [[derivata|derivabile]] $n$ volte $$\implies  P_{n}(x;x_{0})=\sum_{k=0}^{n}\frac{f^{(k)}(x_{0})}{k!}(x-x_{0})^{k}$$
è il [[miglior polinomio]], detto polinomio di Taylor di ordine $n$ centrato in $x_{0}$. è l'UNICO polinomio tale che $$\lim_{x\rightarrow x_{0}}\frac{f(x)-P_{n}(x;x_{0})}{(x-x_{0})^n}=0$$

> La formula si può riscrivere come $$f(a)+f^{'}(a)(x−a)+\frac{f^{''}(a)}{2!}(x−a)^{2}+\frac{f^{′′′}(a)}{3!}(x−a)^{3}+⋯$$
# serie di Taylor per la migliore approssimazione di una funzione esponenziale
$e^{x}=P_{n}(e^{x};0)+o(x^{n})$
>N.B.: $e^{x}=1+x+\frac{x^{2}}{2}+\frac{x^{3}}{6}+...+\frac{x^{n}}{n!}+o(x^{n})$
# serie di Taylor per la migliore approssimazione di  seno e coseno
- $\sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + o(x^9)$  
- $\cos x = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + o(x^8)$  

| derivate                 | $f^{(n)}(1))$ |
| ------------------------ | ------------- |
| $f(x)=\sin(x)$           | 0             |
| $f'(x)=\cos(x)$          | 1             |
| $f''(x)=-\sin(x)$        | 0             |
| $f'''(x)=-\cos(x)$       | -1            |
| $f^{(4)}(x)=\sin(x)$<br> | 0             |
$sin(x)=\frac{0}{1!}x^{0}-\frac{1}{1!}x^{1}+\frac{0}{2!}x^{2}-\frac{1}{3!}x^{3}+\frac{0}{4!}x^{4}-\frac{1}{5!}x^{5}+\frac{0}{6!}x^{6}-\frac{1}{7!}x^{7}$
$$\sin(x)=\sum_{k=0}^{n}\frac{(-1)^{k}x^{2k+1}}{(2k+1)!}+o(x^{2n+2})$$
$$\cos(x)=\sum_{k=0}^{n}\frac{(-1)^{k}x^{2k}}{(2k)!}+o(x^{2n+2})$$

# piccola parentesi su come i calcolatori calcolano i polinomi (non è Taylor)
$P_{n}(x)=a_{n}x^{n}+a_{n-1}x^{n-1}+...+a_{2}x^{2}+a_{1}x+a_{0}$ (polinomio generico)
$x_{0}(x_{0}(a_{n}x_{0}+a_{n-1})+a_{n-2})+a_{n-3}$

Esempio:
$P(x)=3x^{3}+6x^{2}-5x+2$
$x(x(3x+6)-5)+2$

# calcolare i polinomi di Taylor senza derivate

$f(x)=x^{2}e^{x}$
$g(e)=e^{2x}$
$h(x)=e^{3x^{2}}$
$x_{0}=0$

$e^{t}=1+t+\frac{t^{2}}{2}+\frac{t^{3}}{6}+...+\frac{t^{n}}{n!}+o(t^{n})$
$e^{2x}=1+2x+\frac{2x^{2}}{2}+\frac{2x^{3}}{6}+...+\frac{2x^{n}}{n!}+o(2x^{n})$


---

#todo
Esempio:
$f(x)=x^{3}+3x^{2}-6x+8$
Se $f(x)=Q_{n}(x)+o(x^{n})\implies Q_{n}$ è il polinomio di Taylor
Se $g(x)=1+x+o(x)\implies P_{1}(g(x);0)=1+x$
$h(x)=1+2x+o(x^{3})$

$P_{0}(h;0)=1$
$P_{1}(h;0)=1+2x$
$P_{2}(h;0)=1+2x$
$P_{3}(h;0)=1+2x$
$P_{4}(h;0)=1+2x$ (non posso calcolarlo dato che il grado della funzione originale è di $x^{3}$, infatti l'ordine dell'[[infiniti e infinitesimi|infinitesimo]] determina l'ordine del polinomio di Taylor più adatto ad approssimare la funzione, e in questo caso non si può andare più avanti di $3$).


$f(x)=x^{3}+3x^{2}-6x+8$    $f(0)=8$
$f'{1}(x)=3x^{2}+6x-6$    $f^{'}(0)=-6$
$f''(x)=6x+6$    $f^{''}(0)=6$
$f'''(x)=6$    $f^{'''}(0)=6$
$f^{4}(x)=0=f^{(5)}(x)=f^{(6)}(x)=...$


$P_{6}(x^{71}-16x^{45}+32^{8};0)=0$
$P_{92}(-;0)=x^{71}$


$f(x)=e^{x}$


