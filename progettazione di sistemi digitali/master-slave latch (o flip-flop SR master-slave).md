```
            ________________               ________________
       s -> | s       y    | -> y ---------| s          y |--->
ck -------> |>             |          ----o|>             |
    |  r -> | r   not y (z)| -> z ----|----| r      not y |--->
    |       |______________|          |    |______________|
    |_________________________________|
```

> N.B.: il secondo flip-flop è recettivo solo sul fronte di discesa del clock, ciò permette di ottenere segnali più veloci. funzionano in tempi diversi.

Consente di dimezzare la frequenza di clock rispetto al latch normale perché appena l'$\overline y$ dell'ultimo latch si stabilizza viene passato immediatamente senza dover aspettare che il clock valga 1.

Il **flip-flop SR Master-Slave** è un'evoluzione del flip-flop SR base. Serve a **eliminare i problemi di stati instabili** e **rendere il circuito più affidabile**, specialmente quando lavoriamo con segnali di clock.  

#AI
## Perché serve il Flip-Flop SR Master-Slave?
Il normale **gated flip-flop SR** ha un problema: **può cambiare stato più volte durante un impulso di clock** (se gli ingressi cambiano rapidamente). Questo crea instabilità.

La soluzione? Il **flip-flop Master-Slave**, che usa **due flip-flop SR collegati in cascata**.  

- **Il primo (Master)** prende gli ingressi quando il **clock è attivo (1)**.  
- **Il secondo (Slave)** aggiorna l’uscita solo quando il **clock torna a 0** (fronte di discesa).  

**Questo significa che l’uscita cambia solo alla discesa del clock**, evitando transizioni indesiderate.

## Come funziona il Flip-Flop SR Master-Slave?
È composto da **due flip-flop SR**:  
- **Master** → Controlla gli ingressi \( S \) e \( R \) quando il clock è **1**.  
- **Slave** → Prende lo stato del Master e lo trasferisce all’uscita quando il clock torna **0**.

**Risultato**: L’uscita cambia **solo sul fronte di discesa del clock** (transizione da 1 a 0).
### **Tabella di Funzionamento**
| Clock | Master (registra)        | Slave (aggiorna)         | Uscita \( y \)         |
| ----- | ------------------------ | ------------------------ | ---------------------- |
| 0     | Non cambia               | Mantiene stato           | \( y \) invariato      |
| ↑ 1   | Riceve \( S \) e \( R \) | Non cambia               | Ancora vecchio \( y \) |
| ↓ 0   | Bloccato                 | Prende valore dal Master | Nuovo \( y \)          |

## Vantaggi del Flip-Flop Master-Slave
**Evita stati instabili** → Non cambia più volte durante il clock.  
**Funziona solo sul fronte di discesa del clock** → Controllo più preciso.  
**Utile nei registri e nei contatori** → Base per memorie digitali e circuiti sequenziali.  

**Limite**: Se gli ingressi cambiano durante il clock alto, il Master può memorizzare valori sbagliati. Per questo, il flip-flop D è spesso preferito.