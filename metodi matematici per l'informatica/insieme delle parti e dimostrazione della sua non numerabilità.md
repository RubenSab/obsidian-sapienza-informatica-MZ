>L'insieme della parti è l'insieme di tutti i sottoinsiemi possibili di A.

>N.B.: L'insieme delle parti **CONTIENE l'INSIEME CHE CONTIENE L'INSIEME VUOTO**: $\{ \emptyset \}$.

Si scrive come P(A) = {x|x$\subseteq$A} oppure $2^A$.

# dimostrazione della non [[cardinalità (o potenza)|numerabilità]] di $P(\mathbb{N})$
Tesi: $P(\mathbb{N})$ non è numerabile -> Tesi della dimostrazione per assurdo: $P(\mathbb{N})$ è numerabile

- Sappiamo che ogni insieme (numerabile) è assimilabile a (rappresentato da) una sequenza infinita di 0 e di 1 per mezzo della [[funzione caratteristica di un insieme]] $f(x)$.
- Se l'insieme è numerabile, si può costruire una tabella nella quale ogni colonna rappresenta $f(x)$ di un'elemento $x$ (righe della tabella) di ogni sottoinsieme di $P(\mathbb{N})$.

> QUESTO È ***BASATO*** 🗿💪🗣️🗣️🗣️ 🗣️🗣️🗣️ 🔥🔥🔥🔥🔥🔥 sic(k). *Adolfo Piperno*

|       | 0 $\emptyset$ | 1 $\mathbb{N}$ | 2 $\{1,2,3\}$ | 3 $\{1,3,5..\}$ | 4 $\{0,1,2,4\}$ | 5 ${x\|x\subseteq \mathbb{N}}$ |
| ----- | ------------- | -------------- | ------------- | --------------- | --------------- | ------------------------------ |
| **0** | 0             | 1              | 0             | 0               | 1               | ...                            |
| **1** | 0             | 1              | 1             | 1               | 1               | ...                            |
| **2** | 0             | 1              | 1             | 0               | 1               | ...                            |
| **3** | 0             | 1              | 1             | 1               | 0               | ...                            |
| **4** | 0             | 1              | 0             | 0               | 1               | ...                            |
| n     | ...           | ...            | ...           | ...             | ...             | ...                            |


- Consideriamo la diagonale della tabella

|       | 0 $\emptyset$ | 1 $\mathbb{N}$ | 2 $\{1,2,3\}$ | 3 $\{1,3,5..\}$ | 4 $\{0,1,2,4\}$ | 5 ${x\|x\subseteq \mathbb{N}}$ |
| ----- | ------------- | -------------- | ------------- | --------------- | --------------- | ------------------------------ |
| **0** | (0)           | 1              | 0             | 0               | 1               | ...                            |
| **1** | 0             | (1)            | 1             | 1               | 1               | ...                            |
| **2** | 0             | 1              | (1)           | 0               | 1               | ...                            |
| **3** | 0             | 1              | 1             | (1)             | 0               | ...                            |
| **4** | 0             | 1              | 0             | 0               | (1)             | ...                            |
| n     | ...           | ...            | ...           | ...             | ...             | (...)                          |
- La diagonale è una sequenza infinita di 0 e di 1, quindi è un sottoinsieme di $\mathbb{N}$, quindi per la definizione della tabella, questo insieme è una colonna della tabella.
- [[complementazione|Complementiamo]] il sottoinsieme della diagonale ottenendo $\overline D$, e osserviamo che anch'esso è un'elemento di $P(\mathbb{N})$, rappresentato da una colonna della tabella.
- Essendo $\overline D$ una colonna della tabella, esso è necessariamente attraversato da la diagonale.
- Cosa c'è all'incrocio fra $\overline D$ e la diagonale? Nulla, perché se nella posizione dell'incrocio $D$ avrebbe 0, allora $\overline D$ (il suo complemento) avrebbe 1 e viceversa. Ciò è un'assurdo, quindi il teorema è dimostrato. $\square$