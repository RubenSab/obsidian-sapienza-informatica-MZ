#AI 
Il flip-flop T (Toggle) è un tipo di flip-flop che cambia stato a ogni impulso di clock quando l'ingresso \( T \) è alto. È una variante del flip-flop D e viene usato principalmente nei contatori binari.  

### Come funziona  
Ha due ingressi principali:  
- \( T \) (Toggle): determina se l'uscita deve cambiare stato  
- \( CLK \) (Clock): controlla il momento in cui il cambiamento avviene  

Se \( T = 0 \), l'uscita \( y \) rimane invariata. Se \( T = 1 \), \( y \) inverte il suo valore a ogni impulso di clock.  

### Tabella di verità  
| CLK | T   | y (nuovo)       |     |
| --- | --- | --------------- | --- |
| ↑   | 0   | y (vecchio)     |     |
| ↑   | 1   | not y (vecchio) |     |

### Equazione caratteristica  
$y(t+1) = T \oplus y(t)$
### Utilizzo  
Il flip-flop T è usato per:  
- **Contatori binari** (divide la frequenza del clock per 2)  
- **Divisori di frequenza**  
- **Generatori di sequenze digitali**  

È spesso realizzato modificando un flip-flop JK con \( J = K = T \).  

```
      ____________
t ----| T      y |-->
   |  |>         |
   |__| k  not y |-->
      |__________|
```

| $t$ | $y(t+1)$          |
| --- | ----------------- |
| 0   | $y(t)$            |
| 1   | $\overline{y(t)}$ |
