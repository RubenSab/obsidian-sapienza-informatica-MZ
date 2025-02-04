Inventata da George Boole, l'algebra di Boole fornisce un modo simbolico per manipolare e rappresentare le informazioni logiche.

L'algebra di Boole può essere interpretata in più modi, ad esempio considerandola come
- manipolazione di aree di figure geometriche,
- l'algebra della [[logica proposizionale]]
- l'[[algebra delle porte logiche]] dei circuiti,

ma sempre avendo cura di mantenere la validità e la consistenza degli assiomi.
# Basi dell'algebra booleana
I postulati che definiscono un'algebra, come quella booleana, sono *consistenti* tra loro, *semplici* e *indipendenti*.

L'algebra di Boole può essere costruita a partire da diversi insiemi di postulati, dei quali uno dei più intuitivi è costituito da 6 postulati e 3 definizioni:
## postulati (o assiomi)

Gli assiomi elencati sotto sono quelli dell'algebra booleana pura, ma per l'interpretazione a [[porte logiche]] è utile usare 0 e 1 come A e B, e {0, 1} come classe $K$ (anche chiamata alfabeto di supporto).
1. **Chiusura**  
   - $A + B \in K$
   - $A \cdot B \in K$
2. **Complemento**  
   - $\forall A \in K, \quad \overline{A} \in K$  
3. **Commutatività**  
   - $A + B = B + A$  
   - $A \cdot B = B \cdot A$  
4. **Associatività**  
   - $(A + B) + C = A + (B + C)$  
   - $(A \cdot B) \cdot C = A \cdot (B \cdot C)$  
5. **Distributività**  
   - $A \cdot (B + C) = A \cdot B + A \cdot C$  
   - $A + (B \cdot C) = (A + B) \cdot (A + C)$  
6. **Identità**  
   - $A + 0 = A$  
   - $A \cdot 1 = A$  
7. **Complementazione**  
   - $A + \overline{A} = 1$  
   - $A \cdot \overline{A} = 0$  
8. **Idempotenza**  
   - $A + A = A$  
   - $A \cdot A = A$

Questi sono i principi fondamentali che definiscono un'algebra booleana.

>N.B. A differenza della matematica, sia l'operatore + che l'operatore $\cdot$ godono delle proprietà associativa, commutativa e distributiva (es: $(x+y)\cdot(x+z)=x+y\cdot z$.
## definizioni
(non sono assiomi ma seguono naturalmente dagli assiomi):
1. $A+\overline A=1$ elemento universale
2. $\overline{A+\overline A}=0$ elemento nullo
# principio di dualità
Ogni identità valida nell'Algebra Booleana rimane valida se si scambiano fra loro:
- gli operatori $+$ e $\cdot$
- le costanti 0 e 1,

avendo cura di mantenere le precedenze degli operatori, cioè le proprietà esplicite (parentesi) e quelle implicite (ordine delle operazioni NOT, AND, OR).

>  N.B.: ciò **NON significa** che l'espressione duale assume gli stessi valori di verità dell'originale. 
## osservazioni
- **Se un'espressione è [[logica proposizionale|tautologica]] in Algebra Booleana, anche la sua duale è tautologica**, quindi il principio di dualità è utile per dimostrare identità booleane: invece di dimostrare due relazioni separate (una per OR e una per AND), basta dimostrarne una e ottenere l'altra per dualità.
- **Duale del duale**: Se prendi la duale di un'espressione due volte, ottieni di nuovo l'espressione originale.
# identità di base dell'algebra booleana

| identità              | duale dell'identità       | nome             |
| --------------------- | ------------------------- | ---------------- |
| $X+Y=Y+X$             | $XY = XY$                 | Commutatività    |
| $X+(Y+Z)=(X+Y)+Z$     | $X(YZ)=(XY)Z$             | Associatività    |
| $X(Y+Z)=XY+XZ$        | $X+YZ=(X+Y)(X+Z)$         | Distributività   |
| $X + \overline X = 1$ | $X \cdot \overline X = 0$ | Complementazione |
| $X+0=X$               | $X \cdot 1 = X$           | Elemento neutro  |
| $X+1=1$               | $X \cdot 0 = 0$           | Elemento nullo   |
| $X + X = X$           | $X\cdot X = X$            | Idempotenza      |

# proprietà

| espressione                                    | forma duale                                       | nome                |
| ---------------------------------------------- | ------------------------------------------------- | ------------------- |
| $\overline {\overline X}=X$                    |                                                   | Involuzione         |
| $X+XY=X$                                       | $X(X+Y)=X$                                        | Assorbimento        |
| $X+\overline{X}Y=X+Y$                          | $X(\overline{X}+Y)=XY$                            | Pseudo-assorbimento |
| $\overline{X+Y}=\overline X \cdot \overline Y$ | $\overline{X\cdot Y} = \overline X + \overline Y$ | Leggi di De Morgan  |
| $XY+YZ+\overline{XZ}=XY+\overline{XZ}$         |                                                   | Consenso            |

- [[espressioni booleane]]
