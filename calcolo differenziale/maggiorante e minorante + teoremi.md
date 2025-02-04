
# maggiorante
$E \subseteq \mathbb{N}$
> $M$ si dice **maggiorante** di $E$ se $M \geq N\ \ \forall N \in E$

- Se $M$ è un maggiorante di $E$, allora $M+1, M+2, M+k$ sono maggioranti.
- Non esiste negli insiemi illimitati a destra.

# minorante
$E \subseteq \mathbb{N}$
>$m$ si dice **minorante** di $E$ se $m \geq n\ \ \forall n \in E$

- Se $m$ è un minorante di $E$, allora $M-1, M-2, M-k$ sono minoranti.
- Non esiste negli insiemi illimitati a sinistra.

## differenza tra max/min e maggiorante/minorante

>N.B.: il [[massimo e minimo]] di un insieme sono maggiorante e minorante dell'insieme, ma non vale l'implicazione inversa, ciò significa che **il maggiorante e il minorante non appartengono necessariamente all'insieme**.

&nbsp;

# teorema di esistenza del massimo per $E \subseteq \mathbb{N}$
Sia $E \subseteq \mathbb N$, $E \neq \emptyset$
H: esiste almeno un maggiorante di $E$ (insieme dei maggioranti di $E$: $M(E)=\{{n\in\mathbb{N}:n\geq m}\ \ \forall m \in E\}$)
T: esiste un massimo
se $M(E) = \{n \in \mathbb{N}: n\geq m\ \ \forall m \in E\} \neq \emptyset$
$\implies \exists min(M(E)) = max(E)$
$\square$
# teorema di esistenza del minimo di $E \subseteq \mathbb{N}$
se $E \subseteq \mathbb{N}, E\neq \emptyset$
H: esiste almeno un maggiorante di $E$ (insieme dei maggioranti di $E$:
(insieme dei minoranti di $E$: $m(E) = \{n \in \mathbb{N}: n\leq m\ \ \forall m \in E\} \neq \emptyset$
$\implies \exists max(m(E))=min(E)$
$\square$
# teorema di esistenza del massimo e del minimo di $E \subseteq \mathbb{Z}$
se $E \subseteq \mathbb{Z} \neq \emptyset$
- $\exists min(E) ?$
- $\exists max(E) ?$

Se $E \subseteq \mathbb{Z}$:
$m(E)\neq \emptyset \implies \exists min(E) = max(m(E))$
$M(E)\neq \emptyset \implies \exists max(E) = min(M(E))$
$\square$
# teorema di esistenza del massimo e del minimo di per $E \subseteq \mathbb{Q}$
$E \subseteq \mathbb{Q} \neq \emptyset$
Sia $E | m(E)\neq\emptyset$
- $\exists max(m(E)) = min(E)?$
- $\exists min(M(E))=max(E) ?$

$E = \{x\in\mathbb{Q}\ |\ 0<x<1\}$
$m(E)\neq\emptyset=\{x\in\mathbb{Q}\ |\ x\leq0\}$
$max(m(E))=0=min(E)$
$\exists max(m(E))\neq min(E) (\nexists min(E))$
$M(E)=\{x\in\mathbb{Q}\ |\ x\geq1\}$
$\exists min(M(E))=1,\nexists max(E)$

# teorema (per $E \subseteq \mathbb{Q}$)
$E\neq\emptyset, E\subseteq\mathbb{Q}$
- se $m(E)\neq\emptyset\implies E\max(m(E))$? falso
- se $m(E)\neq\emptyset\implies E\min(M(E))$? falso

esempio:
$E= \{x\in\mathbb{Q}:x\geq0\text{ e }x^2\leq2\}$
$M(E)\neq\emptyset \implies \exists min(M(E))$?
**Non sempre!** Se esistesse $L=min(M(E)), L\in\mathbb{Q}$, esisterebbe $L^2=2, L\in\mathbb{Q}$

# teorema (per $E \subseteq \mathbb{R}$)
$E= \{x\in\mathbb{R}:x\geq0\text{ e }x^2\leq2\}$
$M(E)\neq\emptyset \implies \exists min(M(E))$?
**Sì!** $\sqrt{2} = min(M(E)) \implies max(E) = \sqrt{2}$

# definizione (per $E\neq\emptyset\subseteq \mathbb{R}$)
- Se $M(E) = \{x\in\mathbb{R}|x\geq y \forall y \in E\}\neq \emptyset \implies \exists min(M(E)) \in \mathbb{R}$
- Se $m(E) = \{x\in\mathbb{R}|x\leq y \forall y \in E\}\neq \emptyset \implies \exists max(m(E)) \in \mathbb{R}$

>estremo superiore: $sup(E)=min(M((E)))$
>estremo inferiore: $inf(E)=max(m(E)))$

# definizione (per $E\subseteq \mathbb{R}$)
- $\sup(E)=min(M((E)))$ se $M(E)\neq\emptyset$ o $+\infty$ se $M(E)=\emptyset$
- $\inf(E)=max(m((E)))$ se $m(E)\neq\emptyset$ o $-\infty$ se $m(E)=\emptyset$
- **TUTTI** i sottoinsiemi (limitati) di $\mathbb{R}$ hanno superiore e inferiore

Se $sup(E)\in E \implies sup(E) = max(E)$
Se $inf(E)\in E \implies inf(E) = min(E)$

>Queste definizioni ci permettono di definire gli [[intervalli in R]].

