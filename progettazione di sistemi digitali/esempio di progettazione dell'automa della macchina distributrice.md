>Progettare l'automa per una macchina distributrice che può ricevere 10€ e 20€ e fornisce il prodotto con 50€ e memorizza l'eventuale resto.
# tabella dell'automa
Bisogna partire dalla tabella, specificando il significato di ogni stato, usando anche i nomi.

|          | 10 €       | 20 €       |
| -------- | ---------- | ---------- |
| $S_{i}$  | $S_{10}/0$ | $S_{20}/0$ |
| $S_{10}$ | $S_{20}/0$ | $S_{30}/0$ |
| $S_{20}$ | $S_{30}/0$ | $S_{i}/0$  |
| $S_{30}$ | $S_{40}/0$ | $S_{i}/1$  |
| $S_{40}$ | $S_{i}/1$  | $S_{10}/1$ |

# diagramma con il modello di Moore
#toadd
![[caffè moore.png]]
# diagramma con il modello di Mealy
![[caffè mealy.png]]
#toadd 