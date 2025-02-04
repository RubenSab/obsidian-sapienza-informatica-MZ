$E \subseteq \mathbb{N}$
> $M$ si dice **maggiorante** di $E$ se $M \geq N\ \ \forall N \in E$

$E \subseteq \mathbb{N}$
>$m$ si dice **minorante** di $E$ se $m \geq n\ \ \forall n \in E$
# Gerarchia degli infiniti
$$log_{x}\leq x^{a} \leq a^{x} (a<1)\leq x! \leq x^{x}$$
# Forme indeterminate
$\frac{0}{0}$, $\frac{\infty}{\infty}$, $0\bullet \infty$, $\infty - \infty$, $0^{0}$, $1^{\infty}$, $\infty^{0}$
# De l'Hopital
$$\lim_{x\to a}{\frac{f(x)}{g(x)}}=0;\pm \infty\to \lim_{x\to a}{\frac{f(x)}{g(x)}}=\frac{f'(x)}{g'(x)}$$
# Limiti notevoli
## Limiti notevoli per $x \to 0$

### Trigonometria
- $\lim_{x \to 0} \frac{\sin x}{x} = 1$
- $\lim_{x \to 0} \frac{1 - \cos x}{x^2} = \frac{1}{2}$
- $\lim_{x \to 0} \frac{1 - \cos x}{x} = 0$
- $\lim_{x \to 0} \frac{\tan x}{x} = 1$
- $\lim_{x \to 0} \frac{\arctan x}{x} = 1$
- $\lim_{x \to 0} \frac{\arcsin x}{x} = 1$
- $\lim_{x \to 0} \frac{\arccos x}{x} = +\infty$
### Logaritmi ed esponenziali
- $\lim_{x \to 0} \frac{e^x - 1}{x} = 1$
- $\lim_{x \to 0} \frac{k^{x} - 1}{x} = \ln{k}$
- $\lim_{x \to 0} \frac{\ln(1 + x)}{x} = 1$
- - $\lim_{x \to 0} \frac{\log(1 + x)}{x} = \frac{1}{\ln{k}}$
- $\lim_{x \to 0} (1 + x)^{\frac{1}{x}} = e$
- $\lim_{x \to 0} (1 + x)^{\frac{k}{x}} = e^{k}$

## Limiti notevoli per $x \to \infty$
- Limite di un rapporto -> usare la gerarchia degli infiniti per vedere se $\lim = 0; \pm\infty; L$.
### Stirling
$$\lim_{n\rightarrow +\infty}{\frac{n!}{n^{n} e^{-n} \sqrt{2 \pi n}}}=1\to n!\approx\sqrt{2\pi n}\left(\frac{n}{e}\right)^n$$
### Trigonometria
- $\lim_{x\to\pm\infty} \arctan{x}=\mp\pi/2$
### Logaritmi ed esponenziali
- $\lim_{x \to \infty} \left( 1 + \frac{1}{x} \right)^x = e$
- $\lim_{x \to \infty} \left( 1 + \frac{k}{x} \right)^x = e^k$
# Serie di Taylor
$$f(x)=f(a)+f^{'}(a)(x−a)+\frac{f^{''}(a)}{2!}(x−a)^{2}+\frac{f^{′′′}(a)}{3!}(x−a)^{3}+⋯$$
- $e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \frac{x^4}{4!} + o(x^5)$  
- $\sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + o(x^9)$  
- $\cos x = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + o(x^8)$  
- $\tan x = x + \frac{x^3}{3} + \frac{2x^5}{15} + \frac{17x^7}{315} + o(x^9)$  
- $\arcsin x = x + \frac{x^3}{6} + \frac{3x^5}{40} + \frac{5x^7}{112} + o(x^9), \quad |x| < 1$  
- $\arccos x = \frac{\pi}{2} - x - \frac{x^3}{6} - \frac{3x^5}{40} - \frac{5x^7}{112} + o(x^9), \quad |x| < 1$  
- $\arctan x = x - \frac{x^3}{3} + \frac{x^5}{5} - \frac{x^7}{7} + o(x^9), \quad |x| < 1$  
- $\ln(1 + x) = x - \frac{x^2}{2} + \frac{x^3}{3} - \frac{x^4}{4} + o(x^5), \quad |x| < 1$  
- $\sqrt{1 + x} = 1 + \frac{x}{2} - \frac{x^2}{8} + \frac{x^3}{16} - \frac{5x^4}{128} + o(x^5), \quad |x| < 1$  
- $(1 + x)^a = 1 + ax + \frac{a(a-1)}{2!}x^2 + \frac{a(a-1)(a-2)}{3!}x^3 + o(x^4), \quad |x| < 1$
> Non si possono calcolare i polinomi di Taylor di grado superiore alla funzione di partenza, infatti l'ordine dell'o piccolo determina l'ordine del polinomio di Taylor più adatto ad approssimare la funzione.
## algebra degli o-piccolo
- Moltiplicazione per una costante (la costante è trascurabile):
$$o(c\bullet g(x))=o(g(x))\text{ per } x\rightarrow x_{0}$$
$$c\bullet o(g(x))=o(g(x))\text{ per } x\rightarrow x_{0}$$
- Potenza di una funzione (stabilità dell'$o$ all'applicazione della potenza):
$$\text{ Se }f(x)=o(g(x))\text{ per }x\rightarrow x_{0}$$
$$\text{ Allora }[f(x)]^{a}=o([g(x)]^{a})\text{ per }a>0$$
- Somma tra o-piccolo
$$o(f(x))+o(f(x))=o(f(x))\text{ per }x\rightarrow x_{0}$$
- Prodotto tra una funzione e un o-piccolo
$$f(x)\bullet o(g(x))=o(f(x)g(x))\text{ per }x\rightarrow x_{0}$$
- O-piccolo di o-piccolo
$$o(o(f(x)))=o(f(x))\text{ per }x\rightarrow x_{0}$$
---

# Derivate
## Regole di derivazione
- $\frac{d}{dx} \left( f(x) \pm g(x) \right) = f'(x) \pm g'(x)$.
- $\frac{d}{dx} \left( f(x) \cdot g(x) \right) = f'(x) \cdot g(x) + f(x) \cdot g'(x)$.
- $\frac{d}{dx} \left( \frac{f(x)}{g(x)} \right) = \frac{f'(x) \cdot g(x) - f(x) \cdot g'(x)}{(g(x))^2}$.
- $\frac{d}{dx} \left( f(g(x)) \right) = f'(g(x)) \cdot g'(x)$.
- $\frac{d}{dx} \left( f(x)^{g(x)} \right) = f(x)^{g(x)} \cdot \left( g'(x) \ln(f(x)) + \frac{g(x) \cdot f'(x)}{f(x)} \right)$
## Derivate prime
- $\frac{d}{dx} (c) = 0$, dove $c$ è una costante.
- $\frac{d}{dx} \left( x^n \right) = n x^{n-1}$  
- $\frac{d}{dx} \left( \sin x \right) = \cos x$  
- $\frac{d}{dx} \left( \cos x \right) = -\sin x$  
- $\frac{d}{dx} \left( \tan x \right) = \sec^2 x$
- $\frac{d}{dx}(\cot{x})=\frac{1}{\sin^2{x}}$
- $\frac{d}{dx} \left( \arcsin x \right) = \frac{1}{\sqrt{1 - x^2}}$  
- $\frac{d}{dx} \left( \arccos x \right) = -\frac{1}{\sqrt{1 - x^2}}$  
- $\frac{d}{dx} \left( \arctan x \right) = \frac{1}{1 + x^2}$
- $\frac{d}{dx} \left(arccot\ x \right) = -\frac{1}{1 + x^2}$
- $\frac{d}{dx} \left( e^x \right) = e^x$
- $\frac{d}{dx} \left( a^x \right) = a^x \cdot \ln a$, dove $a$ è una costante positiva.
- $\frac{d}{dx} \left( \ln x \right) = \frac{1}{x}$, per $x > 0$.
- $\frac{d}{dx} \left( \ln(1 + x) \right) = \frac{1}{1 + x}$
- $\frac{d}{dx} \left( \log_{b}x \right) = \frac{1}{x}\bullet \log_{a}{e}$ oppure $\frac{1}{x\bullet \ln{a}}$
- $\frac{d}{dx} \left( \sqrt{x} \right) = \frac{1}{2\sqrt{x}}$  
- $\frac{d}{dx} \left( (1 + x)^a \right) = a (1 + x)^{a-1}$  
- $\frac{d}{dx} \left( \frac{1}{x} \right) = -\frac{1}{x^2}$
# Teoremi su derivate e funzioni
## teorema degli zeri
Se:
- $f: [a, b] \rightarrow \mathbb{R}$ continua
- $f(a)\bullet f(b) < 0$

Allora $\exists c \in (a, b)|f(c)=0$
## teorema dei valori intermedi
Data $f: [a, b] \rightarrow \mathbb{R}$ continua. La funzione assume tutti i valori tra $f(a)$ e $f(b)$ (e quindi anche tra i massimi e i minimi)
## teorema di Weierstrass
Data $f: [a, b] \rightarrow \mathbb{R}$ continua, allora $f(x)$ ammette (almeno) un punto di massimo assoluto e un punto di minimo assoluto nell'intervallo $[a,b]$.
