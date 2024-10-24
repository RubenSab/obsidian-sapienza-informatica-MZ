Inventata da George Boole, l'algebra di Boole fornisce un modo simbolico per manipolare e rappresentare le informazioni logiche.
# Basi dell'algebra booleana
I postulati che definiscono un'algebra, come quella booleana, sono *consistenti* tra loro, *semplici* e *indipendenti*.

L'algebra di Boole può essere costruita a partire da diversi insiemi di postulati, dei quali uno dei più intuitivi è costituito da 6 postulati e 3 definizioni:
## postulati (o assiomi)
1. Se A e B sono due elementi dell'insieme K che deve contenere almeno due elementi, allora A+B appartiene alla classe K.
2. Se A appartiene ala classe K, anche $\overline A$ appartiene alla classe K
3. Se A e B appartengono alla classe K, anche A+B=B+A
4. Se A, B, C appartengono alla classe K allora (A+B)+C=A+(B+C)
5. Se A appartiene alla classe K allora A+A=A
6. Se A e B appartengono alla classe K, allora $\overline {(\overline A + \overline B)}+\overline {(\overline A + B)} = A$
>N.B. Sia l'operatore + che l'operatore $\bullet$ godono della proprietà distributiva
## definizioni
1. $A+\overline A=1$ elemento universale
2. $\overline{A+\overline A}=0$ elemento nullo
3. $A\bullet B = \overline {(\overline A + \overline B)}$ 

L'algebra di Boole può essere interpretata in più modi, ad esempio applicandola alle aree, alla logica proposizionale o alle [[algebra delle porte logiche come interpretazione dell'algebra di Boole]] dei circuiti, avendo cura di mantenere le 
# principio di dualità
> Data un'identità logica si può ottenere una duale scambiando fra loro gli operatori $+$ e $\bullet$, e scambiando fra loro gli 1 e gli 0 avendo cura di mantenere le proprietà esplicite (parentesi) e quelle implicite (ordine delle operazioni NOT, AND, OR).
# identità di base dell'algebra booleana

| identità              | duale dell'identità         | nome             |
| --------------------- | --------------------------- | ---------------- |
| $X+Y=Y+X$             | $XY = XY$                   | Commutatività    |
| $X+(Y+Z)=(X+Y)+Z$     | $X(YZ)=(XY)Z$               | Associatività    |
| $X(Y+Z)=XY+XZ$        | $X+YZ=(X+Y)(X+Z)$           | Distributività   |
| $X + \overline X = 1$ | $X \bullet \overline X = 0$ | Complementazione |
| $X+0=X$               | $X \bullet 1 = X$           | elemento neutro  |
| $X+1=1$               | $X \bullet 0 = 0$           | elemento nullo   |

# proprietà

| espressione                                      | forma duale                                         | nome                           |
| ------------------------------------------------ | --------------------------------------------------- | ------------------------------ |
| $\overline {\overline X}=X$                      |                                                     | involuzione                    |
| $X+X=X$                                          | $X\bullet X=X$                                      | idempotenza                    |
| $x+1=1$                                          | $X\bullet 0 = 0$                                    | elemento nullo / nullificatore |
| $X+XY=X$                                         | $X(X+Y)=X$                                          | assorbimento                   |
| $\overline{X+Y}=\overline X \bullet \overline Y$ | $\overline{X\bullet Y} = \overline X + \overline Y$ | leggi di De Morgan             |
| $XY+YZ+\overline XZ=XY+\overline XZ$             |                                                     | consenso                       |

- [[espressioni booleane]]
