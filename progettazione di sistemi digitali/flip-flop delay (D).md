#AI
Il **flip-flop D (Delay o Data)** è un tipo di flip-flop che serve a memorizzare un bit di informazione sincronizzato con un segnale di clock. Risolve il problema degli stati proibiti del flip-flop SR impedendo che S e R siano uguali a 1 contemporaneamente.

### **Come funziona**

Ha due ingressi principali:

- D (Dato): valore da memorizzare
- CLK (Clock): controlla quando l'uscita viene aggiornata

L'uscita y assume il valore dell'ingresso D **solo sul fronte attivo del clock** (in salita o in discesa, a seconda del circuito). Questo significa che y non cambia finché non arriva un impulso di clock.

### **Tabella di verità**

| CLK | D   | y (nuovo)   |
| --- | --- | ----------- |
| ↑   | 0   | 0           |
| ↑   | 1   | 1           |
| 0   | X   | y (vecchio) |

Quando il clock è basso, y rimane invariato. Quando arriva un fronte attivo, y assume il valore di D.

### **Utilizzo**

Il flip-flop D è usato per:

- **Registri di memoria**
- **Sincronizzazione di segnali**
- **Contatori e shift register**


```
         ____________
d -------| s      y |-->
   |     |>         |
   |-not-| r  not y |-->
         |__________|
```

Anche indicato come:

```
      ____________
d ----| d      y |-->
      |          |
      |>  not y  |-->
      |__________|
```

| d   | y(t+1) |
| --- | ------ |
| 0   | 0      |
| 1   | 1      |
