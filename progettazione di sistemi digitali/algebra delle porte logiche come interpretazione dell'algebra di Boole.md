Il funzionamento di un circuito, visto come struttura sequenziale di porte logiche può essere descritto da un'interpretazione dell'[[algebra di Boole]].
# ottimizzazione dei circuiti
Ciò è particolarmente utile per ottimizzare i circuiti, cioè minimizzare il numero di porte necessarie per creare un circuito che restituisce gli stessi output a partire dagli stessi input del circuito di partenza.
Si ottimizza un circuito codificando la sequenza delle sue porte logiche in un'espressione booleana, poi si semplifica l'espressione in base alle identità dell'algebra Booleana e si decodifica una nuova sequenza di porte logiche.
# porte logiche
![[logic gates.png]]
- Gli input e gli output delle porte logiche possono assumere solo due valori diversi: 0 logico e 1 logico (rispettivamente tensione più alta indicata anche con H e tensione più bassa indicata anche con L nella *logica negativa*). Essi sono dati dalle due fasce di tensione consentite (tra le quali ci sono le *regioni di transizione*).
- La **classe K** è l'insieme dei conduttori caratterizzati dalla possibilità di assumere due stati (1 e 0  *detti alfabeto di supporto*) legati alla tensione.
# porte logiche come operatori booleani
- croce ($+$) (addizione) si indica con **OR**
- soprasegno (complemento) ($\overline A$) si indica con **NOT**
- punto ($\bullet$) (prodotto) si indica con **AND**
## porte a più ingressi
> Una porta AND o OR a n ingressi costa come n-1 porte.
- esempio: and(a, b, c) = and( and(a, b), c )
> Una porta NAND o NOR a più ingressi costa come n o più porte (porte NAND o NOR).
# altri operatori
## XOR

| $xy$ | $x\oplus y$ |
| ---- | ----------- |
| 00   | 0           |
| 01   | 1           |
| 10   | 1           |
| 11   | 0           |
$x \oplus y =\overline xy +x\overline y$
- $x \oplus 1 = \overline x$
- $x \oplus 0 = x$

- $\overline{ x \oplus y}= \overline{\overline xy + x\overline y}=(x +\overline y)(\overline x + y)=x\overline x + x y + x\overline y+ y\overline y)=xy+\overline x \overline y$

- $\oplus$ è associativo?
	$x\oplus (y\oplus z) = (x \oplus y)\oplus z$
	$x \oplus (\overline y z + y \overline z)$
	$\overline x (\overline y z + y \overline z)+x\overline{(\overline y z +yz)}$
	$\overline x \overline y z + \overline x y \overline z + x(yz + \overline y \overline z)$
	$\overline x \overline y z + \overline x y \overline z + xyz + x \overline y \overline z$
	$(\overline x \overline y + xy)z+(\overline x y + x\overline y)\overline z$
	$\overline{x\oplus y}z+(x\oplus y)\overline z$
	$(x\oplus y)\oplus z$

## NAND e NOR
NAND: $\overline{ab}$ ( #todo aggiungere simbolo)
NOR: $\overline{a+b}$ ( #todo aggiungere simbolo)

NAND e NOR sono operatori universali, quindi posso realizzare NOT, AND e OR usando solo NAND oppure solo NOR (eccetto in casi particolari, quindi bisogna verificare con [[algebra di Boole|De Morgan]]). Dei circuiti così realizzati si chiamano reti all-AND o reti all-OR.
Esempi:
- [[circuito SOP AND-TO-OR all-NAND]]
- [[circuito POS AND-TO-OR all-NOR]]
### all NAND (conveniente per forme SOP)
**NOT** $\overline a = \overline{aa}$
**AND** $ab=\overline{\overline{ab}\bullet\overline{ab}}$
**OR** $a+b=\overline{\overline{aa}\bullet\overline{bb}}$
### all NOR (conveniente per forme POS)
**NOT** $\overline a = \overline{a+a}$
**AND** $ab = \overline{\overline a + \overline b} = \overline{\overline{a+a}+\overline{b+b}}$
**OR** $a+b=\overline{\overline{a+b}}=\overline{\overline{a+b}+\overline{a+b}}$
# segnali a onda quadra
Per illustrare concretamente l'output di un circuito partendo da varie casistiche in input, si può disegnare il diagramma del *segnale a onda quadra*.
1. Si disegnano in colonna tutti i segnali per le variabili nell'input, in modo da farli oscillare istantaneamente da 0 a 1 (fronte di salita) e da 1 a 0 (fronte di discesa).
2. Si disegna il segnale dell'output sotto tutti i segnali in input, applicando la *tavola di verità* su tutti gli input del circuito per ogni istante, così si può disegnare il segnale di output per controllare se il circuito si comporta nel modo aspettato.

In questa rappresentazione si può trascurare o meno il ***delay, o ritardo di commutazione*** dell'output rispetto all'input.