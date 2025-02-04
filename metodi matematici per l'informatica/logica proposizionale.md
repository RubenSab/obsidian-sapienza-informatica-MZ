Chiamiamo $LP$ la logica proposizionale, cioè l'insieme di tutte le formule rappresentabili in logica proposizionale (una delle interpretazioni dell'[[algebra di Boole]]) e chiamiamo $S$ il suo insieme di simboli (simboli proposizionali).

$X \in S \rightarrow X \in LP$
$P, Q \in LP$

# operatori logici

- not: $(\neg P) \in LP$
- and: $(P \land Q)\in LP$
- or: $(P\lor Q)\in LP$
- [[implicazione materiale]] $(P\implies Q) \in LP$
- se e solo se: $(P\iff Q)\in LP$

# definizioni

> Le formule sono definite per [[induzione sulla struttura del linguaggio]].

> L'interpretazione di una formula è l'attribuzione del suo valore a *vero* o *falso*. Questo valore dipende dall'interpretazione dei simboli dell'espressione, su cui operano i gli *operatori* o *connettivi logici*.

> Un'interpretazione che soddisfa la formula è detta ***modello***.
> Un'interpretazione che non soddisfa la formula è detta ***contromodello***.

- [[esempio di formula logica]]

> Il valore di verità di un'espressione si determina con le tavole di verità.

- Se esiste almeno un modo di rendere la formula vera, la formula si chiama ***soddisfacibile***.
- Se esiste non esiste un modo di rendere la formula vera, la formula si chiama ***insoddisfacibile***.
- Se esiste almeno un modo di rendere la formula falsa, la formula si chiama ***falsificabile***.
- Se non esiste un modo di rendere la formula falsa, la formula si chiama ***tautologia***, ***valida***, ***verità logica***, o ***proprietà del linguaggio***.
	$$\vDash P_{1}$$

> Se una di queste caratteristiche di una formula è definita con "esiste almeno un valore che rende la formula vera/falsa", allora è definita tramite un ***esistenziale***.
> Se una di queste caratteristiche di una formula è definita con "per ogni valore la formula vera/falsa", allora è definita tramite un ***universale***.

> Due formule si dicono ***logicamente equivalenti*** quando tutte le implicazioni che rendono vera una rendono vera anche l'altra e viceversa.
> $$P_{1}\equiv P_{2}$$

> Se le formule $P_{1},...,P_{k}$ (premesse) sono vere e allora è vera anche $Q$ (conclusione), si dice che $Q$ è ***conseguenza logica*** di $P_{1},...,P_{k}$.
> $$P_{1},...,P_{k} \vDash\ Q$$

> N.B.: La conseguenza logica è violata solo quando tutte le premesse sono vere, ma la conclusione è falsa.

> N.B.: Se la premessa è falsa/insoddisfacibile, allora la conclusione è vera/tautologica, ciò è detto *Principio di esplosione* o *verità vacua*

- [[esempi di formule]]
- [[esempi con situazioni reali]]


