# ipotesi
Per definizione i simboli $A$, $B$, $C$... sono formule (atomiche).
Se $A$ e $B$ sono formule, allora $(>P)$, $(A\land B)$, $(A \lor B)$, $(A\implies B)$, $(A \iff B)$ sono formule
# tesi
Bisogna dimostrare che in ogni formula corretta il numero di parentesi aperte è uguale al numero di parentesi chiuse.
# dimostrazione
Dimostriamo la tesi per [[induzione]] sulla struttura del linguaggio.
## caso base
1. Consideriamo le formule $A$ e $B$.
2. Per definizione se $A$ e $B$ sono formule, allora $(>P)$, $(A\land B)$, $(A \lor B)$, $(A\implies B)$, $(A \iff B)$ sono formule.
3. SI verifica per dimostrazione diretta che $A$ e $B$ hanno tante parentesi aperte quante parentesi chiuse.
## passo induttivo
1. Assumendo che le formule $A$ e $B$ (composte da un solo simbolo) hanno tante parentesi aperte quante parentesi chiuse, allora tutte le formule in forma $(>P)$, $(A\land B)$, $(A \lor B)$, $(A\implies B)$, $(A \iff B)$, che si possono riscrivere come singoli simboli, hanno tante parentesi aperte quante parentesi chiuse.
2. Tutte le formule possibili sono o concatenazioni delle formule precedenti, o formule atomiche. Ciò significa che hanno tante parentesi aperte quante parentesi chiuse. $\square$