# per le [[ottimizzazione delle reti combinatorie|reti]]

> La **complessità** di una rete combinatoria è proporzionale al numero di porte (che anche dipende dal numero di ingressi (**fan-in**) in ogni porta, se il circuito è dotato di porte a più ingressi) e al tempo di attraversamento del circuito.

le [[reti AND-TO-OR]] ( o [[reti OR-TO-AND|OR-TO-AND]]) sono minimali se tra tutte le reti possibili AND-TO-OR (o OR-TO-AND) ha:
- il minimo numero di porte AND (o OR)
- il minimo numero di ingressi per ogni porta
# per le [[espressioni booleane]]
Un'espressione SOP (o POS) è minimale se tra tutte le espressioni booleane possibili SOP (o POS) ha:
- Il minimo numero di prodotti (o somme)
- il minimo numero di letterali per ogni prodotto (o somma)

# per gli [[automi a stati finiti (finite state automata) con output]]
Un'automa è minimale se è realizzato con il minor numero di [[flip-flop]] possibili, cioé non ha stati equivalenti.