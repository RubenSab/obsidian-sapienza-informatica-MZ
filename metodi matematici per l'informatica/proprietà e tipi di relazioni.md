Definiamo una relazione $R \subseteq A \bigtimes A$

>Una relazione è **riflessiva** se $\forall a \in A, (a,a) \in R$
Esempio: $\{(a,b) \in \mathbb{N} \times \mathbb{N} \mid a \leq b\}$

>Una relazione è **antiriflessiva** se $\forall a \in A, (a,a) \notin R$

>Una relazione è **simmetrica** se $\forall a,b \in A , (a,b)\in R\implies (b,a) \in R$

>Una relazione è **antisimmetrica** se $\forall a,b \in A , (a,b)\in R \land (b,a)\in R\implies a = b$

>Una relazione è **transitiva** se $\forall a,b,c \in A, (a,b)\in R \land (b,c)\in R \implies (a,c )\in R$

# tipi di relazioni
## equivalenza
>Una relazione è un'**equivalenza** se è:
- riflessiva
- simmetrica
- transitiva
Esempio: $R\in \mathbb{N} \times \mathbb{N}$   $R={(a,b)|a=b}$ 
Esempio di equivalenza con $A = \{0,1,2,3\}$:
$A = {(0,0); (1,1); (2,2); (3,3); (0,1); (1,0); (2,3); (3, 2)}$
### classe di equivalenza
>La classe di equivalenza di un elemento di A è l'insieme di tutti gli elementi in relazione con l'elemento di A.
$$[a]=\{x\in A|(a,x)\in R\}$$
$$a\in [b] \leftrightarrow b \in [a]$$
### insieme quoziente
>L'insieme di tutte le classi di equivalenza di tutti gli elementi di A.

$$Q=\{[a]|a\in A\}$$
Ogni elemento di A è in una e una sola classe di A. Le classi sono disgiunte e la loro unione è l'insieme A.
## chiusura transitiva
>Dato un'insieme R, la chiusura transitiva di R è la più piccola relazione transitiva che contiene R.

Esempio: A = {0, 1, 2}  R = {(0,1),(1,2)} $\hat R$={(0,1),(1,2),(2,0)}

## ordini
### ordine (largo)
>Una relazione riflessiva, antisimmetrica e transitiva è un'**ordine largo**.
### ordine stretto
>Una relazione antiriflessiva, antisimmetrica e transitiva è un'**ordine stretto**.
### ordine totale
>Una relazione d'ordine (largo o stretto) in cui per ogni coppia di elementi $a$ e $b$ si verifica che $(a,b)\in R$ o $(b,a)\in R$ si dice di **ordine totale**.
### ordine parziale
>Una relazione d'ordine (largo o stretto) in cui per ogni coppia di elementi $a$ e $b$ ***non*** si verifica che $(a,b)\in R$ o $(b,a)\in R$ si dice di **ordine totale**.
### preordine
>Una relazione di inclusione riflessiva e transitiva è un **preordine**.
