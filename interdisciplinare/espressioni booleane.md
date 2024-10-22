# espressioni complementari
Data un'espressione booleana, si applica la complementazione all'espressione

# forme di espressioni
## forme normali (POS e SOP)

### forme POS
> Le forme POS (Product Of Sums), o forme congiuntive, sono espressioni nella forma somma $\times$ somma.
### forme SOP
> Le forme SOP (Sum of Products), o forme disgiuntive, sono espressioni nella forma prodotto $+$ prodotto.
### procedimento per ottenere una forma normale
1. Applicare De Morgan per ottenere la complementazione sulle singole variabili.
2. Applicare la proprietà distributiva per svolgere le espressioni tra parentesi.
3. Applicare assorbimento e idempotenza per eliminare termini ridondanti o ripetuti, così otteniamo una forma normale.
- [[esercizio con conversioni tra forme SOP, POS e canoniche]]
## forme canoniche
> Una forma canonica è un'espressione booleana nella quale tutti i termini sono mintermini (contengono tutti i letterali) o maxtermini (contengono tutti i letterali).
### canoniche SOP a partire dalla forma normale
1. Per tutti i termini prodotto della forma normale SOP a cui manca uno o più letterali, bisogna moltiplicare il termine per $(\overline{\text{letterale}}+\text{letterale})$.
>N.B.: non è necessario costruire la tabella di verità.
2. Si applica la proprietà distributiva $x(y+z)=xy+xz$
3. Si eliminano i termini uguali grazie all'idempotenza
### canoniche POS a partire dalla forma normale
1. Per tutti i termini somma della forma normale POS a cui manca uno o più letterali, bisogna sommare $(\overline{\text{letterale}}\times \text{letterale})$.
2. Si applica la proprietà distributiva $x+yz=(x+y)(x+z)$
3. Si eliminano i termini uguali grazie all'idempotenza

[[esercizio con conversioni tra forme SOP, POS e canoniche]]