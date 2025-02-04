> Siano $\{x_{n}\}$ e $\{y_{n}\}, y_{n}\neq 0$ due successioni reali. Si dice che $x_{n}$ è *o piccolo* di $y_{n}$ se
$$\lim_{x\rightarrow +\infty}\frac{x_{n}}{y_{n}}= 0$$
In tal caso si scrive $x_{n} = o(y_{n})$, (o $f(x)=o(g(x))$ se si parla di funzioni).

> N.B.: $o(1)$ indica un [[infiniti e infinitesimi|infinitesimo]] generico, infatti se $\frac{x_{n}}{1}\rightarrow 0$ allora $x_{n}\rightarrow 0$.

Ovviamente tutto ciò espresso sopra è valido anche per le funzioni tramite il [[teorema ponte]], infatti questa notazione viene usata per individuare l'ordine di infinitesimo di una funzione rispetto ad una funzione campione, al tendere di $x$ **ad un determinato valore** o a **infinito**.
$$\lim_{x\rightarrow +\infty}\frac{x_{n}}{y_{n}}= 0$$
Esempi:
- $x^{n+k}=o(x^{n})$ con $k\geq 1$ per $x\rightarrow 0$
- $x^{n}=o(x^{n+k})$ con $k\geq 1$ per $x\rightarrow +\infty$
- $x^{n}o(x^{k})=o(x^{n+k})$ per $x\rightarrow 0$

# proprietà degli o-piccolo
- Moltiplicazione per una costante (la costante è trascurabile):
$$o(c\bullet g(x))=o(g(x))\text{ per } x\rightarrow x_{0}$$
$$c\bullet o(g(x))=o(g(x))\text{ per } x\rightarrow x_{0}$$
- Potenza di una funzione (stabilità dell'$o$ all'applicazione della potenza):
$$\text{ Se }f(x)=o(g(x))\text{ per }x\rightarrow x_{0}$$
$$\text{ Allora }[f(x)]^{a}=o([g(x)]^{a})\text{ per }a>0$$
- Somma tra o-piccolo
$$o(f(x))+o(f(x))=o(f(x))\text{ per }x\rightarrow x_{0}$$
- Prodotto tra una funzione e un o-piccolo
$$o(f(x))o(g(x))=o(f(x)g(x))\text{ per }x\rightarrow x_{0}$$
- O-piccolo di o-piccolo
$$o(o(f(x)))=o(f(x))\text{ per }x\rightarrow x_{0}$$