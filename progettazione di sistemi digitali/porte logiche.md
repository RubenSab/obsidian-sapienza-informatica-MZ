
![[logic gates.png]]
- Gli input e gli output delle porte logiche possono assumere solo due valori diversi: 0 logico e 1 logico (rispettivamente tensione più alta indicata anche con H e tensione più bassa indicata anche con L nella *logica negativa*). Essi sono dati dalle due fasce di tensione consentite (tra le quali ci sono le *regioni di transizione*).
- La **classe K** è l'insieme dei conduttori caratterizzati dalla possibilità di assumere due stati (1 e 0  *detti alfabeto di supporto*) legati alla tensione.
# porte logiche come operatori booleani
- croce ($+$) (addizione) si indica con **OR**
- soprasegno (complemento) ($\overline A$) si indica con **NOT**
- punto ($\bullet$) (prodotto) si indica con **AND**
- [[altri operatori logici]]
## porte a più ingressi

> Una porta AND o OR a n ingressi costa come n-1 porte.

- esempio: and(a, b, c) = and( and(a, b), c )

> Una porta NAND o NOR a più ingressi costa come n o più porte (porte NAND o NOR).
