#todo
Il cancello si apre se
- si usa il telecomando
- si usa la chiave
- ma non entrambi
e
- non ci sono intralci

# procedimento
1. tavola di verità

| T   | C   | O   | risultato |
| --- | --- | --- | --------- |
| 0   | 0   | 0   | 0         |
| 0   | 0   | 1   | 0         |
| 0   | 1   | 0   | 1         |
| 0   | 1   | 1   | 0         |
| 1   | 0   | 0   | 1         |
| 1   | 0   | 1   | 0         |
| 1   | 1   | 0   | 0         |
| 1   | 1   | 1   | 0         |
$f=(T\oplus C)\overline O$
## da SOP a all NAND
- espressione SOP:
	$f=(T\overline C + \overline T C)\overline O=T\overline C \overline O + \overline T C \overline O$
- espressione POS:
	$f=(T\overline C + \overline T C)\overline O=(T \overline C + \overline T)(T\overline C+C)\overline O=(T+\overline T)(\overline C+\overline T)(T+C)(\overline C+C)\overline O = (\overline C + \overline T)(T+C)\overline O$
	>N.B.: Per ottenere la canonica basta sommare alle combinazioni parziali di  $T$ $C$ $O$ la variabile mancante moltiplicata alla sua complementare (che è uguale a 1) (esempio: $T+\overline C = T+\overline C + O\overline O = (T+\overline C + O)(T+\overline C + \overline O)$
	
	
	

- da espressione SOP a circuito AND to OR:
	OR(AND(T, NOT(C), O), AND(NOT(T),C, O))
	![[AND TO OR.png]]
- all NAND:
	$f=T\overline CO+\overline T CO = (\overline T C + T)(\overline T C + C)\overline O =$

## da POS a all NOR
- ricaviamo la POS dalla SOP con gli assiomi: $$
# variabili
T = telecomando
C = chiave
O = ostacoli

