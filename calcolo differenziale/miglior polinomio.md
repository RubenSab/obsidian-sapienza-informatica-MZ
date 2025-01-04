
$$o=\lim_{x\rightarrow x_{0}}[\frac{f(x)-f(x_{0})-f'(x_{0})(x-x_{0})}{(x-x_{0})^1}]$$
$$f(x)=f(x_{0})+f'(x_{0})(x-x_{0})+o((x-x_{0}))$$
> Il "miglior" polinomio è quello che approssima meglio il valore di $f(x_{0})$ in $x_{0}$.

$f(x)=P_{2}(x)+o((x-x_{0})^2)$

- Se $n=0$ e $f$ è continua, $P_{0}(x)=f(x_{0})$
- Se $n=1$ e $f$ è derivabile, $P_{1}=f(x_{0})+f'(x_{0})(x-x_{0})$
- Se $n=2$ e $f'$ è derivabile, $P_{2}=P_{1}+f''(x_{0})(x-x_{0})$

- Se $n=2$ e ... $P_{2}(x)=$
	- $f(x_{0}) + f'(x_{0})(x-x_{0})$ (retta tangente in $x_{0}$)
	- $+ a(x-x_{0})^{2}$ (altro termine)

Cioè 
$$P_{2}(x)=\frac{f^{0}(x_{0})}{1}({x-x_{0}}^{0})+\frac{f^{1}(x_{0})}{1}({x-x_{0}}^{1})+a(x-x_{0})^2$$
Esplicitando gli [[notazione o-piccolo|o piccoli]] e applicando il [[teorema de l'hopital]] più volte:
$$\lim_{x\rightarrow x_{0}}\frac{f(x)-f(x_{0})-f'(x_{0})(x-x_{0})-a(x-x_{0})}{(x-x_{0})^2}=0$$
$$\lim_{x\rightarrow x_{0}}\frac{f'(x)-f'(x_{0})-2a(x-x_{0})}{2(x-x_{0})}=0$$
$$0=\lim_{x\rightarrow x_{0}}\frac{f''(x_{0})-2a}{2}=\lim_{x\rightarrow x_{0}}\frac{f''(x)-2a}{2}$$
$$f''(x_{0})=2a$$
$$a=\frac{f''(x_{0})}{2}$$
Sostituendo $a$:
$$P_{2}(x)=\frac{f^{0}(x_{0})}{1}({x-x_{0}}^{0})+\frac{f^{1}(x_{0})}{1}({x-x_{0}}^{1})+\frac{f''(x_{0})}{2}(x-x_{0})^2$$

#todo per 3

> Da ciò possiamo dedurre il miglior polinomio $n$-esimo che approssima $f(x_{0})$ in $x_{0}$, ricavando le [[serie di Taylor]].