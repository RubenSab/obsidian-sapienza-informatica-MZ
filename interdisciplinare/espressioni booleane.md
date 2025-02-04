Un'espressione booleana è uno degli infiniti modi (quindi non necessariamente il più semplice) per esprimere una [[funzione]].
Può essere:
- la [[logica proposizionale|variabile atomica]].
- la negazione di una variabile.
- la somma e il prodotto di variabili.

 Per [[induzione sulla struttura del linguaggio]], posso combinare le due definizioni precedenti e usare parentesi per ottenere espressioni booleane più complesse.

## espressione duale
Ogni identità valida nell'Algebra Booleana rimane valida se si scambiano fra loro:

- gli operatori  e 
- le costanti 0 e 1,

avendo cura di mantenere le precedenze degli operatori, cioè le proprietà esplicite (parentesi) e quelle implicite (ordine delle operazioni NOT, AND, OR).

> N.B.: ciò **NON significa** che l'espressione duale assume gli stessi valori di verità dell'originale.
## espressione complementare
> Un'espressione complementare è un'espressione booleana complementata; questa assumerà valori di verità opposti rispetto all'originale per ogni input.

Ci sono due metodi per ottenere la complementare:
- Complementare tutta l'espressione e applicare ripetutamente la [[algebra di Boole|legge di De Morgan]].
- Passare all'espressione duale, poi complementare le singole variabili

## identità
> Un'identità si ottiene eguagliando due diverse espressioni booleane.

L'identità si può verificare:
- Con il ***metodo dell'induzione perfetta***: cioè verificarla per ogni possibile combinazione dei valori delle variabili.
- Con il metodo basato su trasformazioni tramite assiomi e proprietà.
> Esempio: $X+XY=X \rightarrow X(1+Y)=X \rightarrow X(1)=X \rightarrow X=X$
# forme di espressioni
## forme normali (POS e SOP)

### forme normali POS
> Le forme POS (Product Of Sums), o forme congiuntive, sono espressioni nella forma somma $\times$ somma.
### forme normali SOP
> Le forme SOP (Sum of Products), o forme disgiuntive, sono espressioni nella forma prodotto $+$ prodotto.
### procedimento per ottenere una forma normale
1. Applicare De Morgan per "spostare" la complementazione da espressioni più grandi alle singole variabili.o
2. Applicare la **proprietà distributiva** per svolgere le espressioni tra parentesi.
3. Applicare più volte **assorbimento** e **idempotenza** per eliminare termini ridondanti o ripetuti, così otteniamo una forma normale.
- [[esercizio con conversioni tra forme SOP, POS e canoniche]]
## forme canoniche SOP e POS

> Una forma canonica è un'espressione booleana nella quale tutti i termini sono:

- ***mintermini*** ($m_n$), (nella SOP) cioè prodotti logici di variabili, eventualmente complementate, che rappresentano una riga della tabella dove l'uscita vale 1.
- ***maxtermini*** ($M_n$), (nella POS) cioè somme logiche di variabili (eventualmente complementate, che rappresentano una riga della tabella dove l'uscita vale 0.

>N.B.: una forma canonica può essere SOP o POS.
### canoniche SOP

> Possono essere scritte nella forma $\text{OR}(\text{mintermini})$, ad esempio $\text{OR}(m_{0}, m_{3}, m_{6})$, che significa che le righe numero 0 (input: 000), 3 (input: 011) e 6 (input: 110) della tabella di verità valgono **1**. Sono molto adatte per realizzare [[reti AND-TO-OR]].
#### canoniche SOP a partire dalla forma normale
1. Per tutti i termini prodotto della forma normale SOP a cui manca uno o più letterali, bisogna moltiplicare il termine per $(\overline{\text{letterale}}+\text{letterale})$.
>N.B.: non è necessario costruire la tabella di verità.
2. Si applica la **proprietà distributiva** $x(y+z)=xy+xz$
3. Si eliminano i termini uguali grazie **all'idempotenza**.

#### canoniche SOP a partire dalla tabella di verità

- La riga della tabella vale 1 → scrivi il **mintermine** (prodotto tra variabili)
    - Se la variabile è **1**, la scrivi normale.
    - Se la variabile è **0**, la complementi.

Infine sommare tutti i mintermini.

**Esempio**:
input(a,b,c) = 011
output = 1
mintermine = $\overline{a}bc$
### canoniche POS

> Possono essere scritte nella forma $\text{AND}(\text{maxtermini})$, ad esempio $\text{AND}(M_{0}, M_{3}, M_{6})$, che significa che le righe numero 0 (input: 000), 3 (input: 011) e 6 (input: 110) della tabella di verità valgono **0**. Sono molto adatte per realizzare [[reti OR-TO-AND]].
#### canoniche POS a partire dalla forma normale
1. Per tutti i termini somma della forma normale POS a cui manca uno o più letterali, bisogna sommare $(\overline{\text{letterale}}\times \text{letterale})$.
2. Si applica la **proprietà distributiva** $x+yz=(x+y)(x+z)$
3. Si eliminano i termini uguali grazie **all'idempotenza**.
#### canoniche POS a partire dalla tabella di verità
**POS (Product of Sums)** nella tavola di verità:

- **0** nella funzione → scrivi il **maxtermine** (somma tra variabili)
    - Se la variabile è **1**, la complementi.
    - Se la variabile è **0**, la scrivi normale.

Infine moltiplicare  tutti i maxtermini.

**Esempio**:
input(a,b,c) = 011
output = 0
mintermine = $a\overline{b}\overline{c}$

[[esercizio con conversioni tra forme SOP, POS e canoniche]]