1. descrizione verbale
2. automa della macchina sequenziale
3. automa della rete (codifiche binarie)
4. tavola degli stati futuri
5. espressioni booleane delle funzioni di eccitazione e uscite
6. disegno della rete

> N.B.: Occorre un passo di [[minimizzazione dell'automa a stati finiti]].

> N.B.: Le espressioni booleane minimali servono per la realizzazione con porte logiche o [[programmable logic array (PLA)]], invece se si usa la [[read only memory (ROM)]] o i [[multiplexer (MUX)]] non serve eplicitare le espressioni booleane.

## esempio

### 1. descrizione verbale 
> Circuito che riceve in ingresso $x$ e produce in uscita 1 se riconosce 1101 con sovrapposizioni.

### 2. stati dell'automa
$S_{in}$: stato iniziale
$S_{1}$: riconoscimento del primo bit
$S_{11}$: riconosciuto due bit


|           | 0           | 1          |
| --------- | ----------- | ---------- |
| $S_{in}$  | $S_{in}/0$  | $S_{1}/0$  |
| $S_{1}$   | $S_{in}/0$  | $S_{11}/0$ |
| $S_{11}$  | $S_{110}/0$ | $S_{11}/0$ |
| $S_{110}$ | $S_{in}/0$  | $S_{1}/1$  |
Quest'automa è minimo, cioè è costruito con meno stati possibili? Si, perché... #todo 
### 3. codifica degli stati
- Input: gli input sono già codificati.
- Stati: In tutto ci sono 4 stati, quindi ci servono 2 bit.

|           | $y_{1}$ | $y_{0}$ |
| --------- | ------- | ------- |
| $S_{0}$   | 0       | 0       |
| $S_{1}$   | 0       | 1       |
| $S_{11}$  | 1       | 0       |
| $S_{110}$ | 1       | 1       |
Scritto ciò, la tabella degli stati dell'automa al passaggio 1 può essere riscritta come:

|      | 0    | 1    |
| ---- | ---- | ---- |
| $00$ | 00/0 | 01/0 |
| $01$ | 00/0 | 10/0 |
| $10$ | 11/0 | 10/0 |
| $11$ | 00/0 | 01/1 |
- Output: gli output sono già codificati.
### 4. tavola degli stati futuri

| $x$ (input) | $y_{1}$ | $y_{0}$ |     | $Y_{1}$ | $Y_{0}$ |     | $z$ (output) |
| ----------- | ------- | ------- | --- | ------- | ------- | --- | ------------ |
| 0           | 0       | 0       |     | 0       | 0       |     | 0            |
| 0           | 0       | 1       |     | 0       | 0       |     | 0            |
| 0           | 1       | 0       |     | 1       | 1       |     | 0            |
| 0           | 1       | 1       |     | 0       | 0       |     | 0            |
| 1           | 0       | 0       |     | 0       | 1       |     | 0            |
| 1           | 0       | 1       |     | 1       | 0       |     | 0            |
| 1           | 1       | 0       |     | 1       | 0       |     | 0            |
| 1           | 1       | 1       |     | 0       | 1       |     | 1            |
## realizzazione con i flip-flop JK

| $x$ | $y_{1}$ | $y_{0}$ |     | $Y_{1}$ | $Y_{0}$ |     | $z$ |     | $j_{1}, k_{1}$ | $j_{0}, k_{0}$ |
| --- | ------- | ------- | --- | ------- | ------- | --- | --- | --- | -------------- | -------------- |
| 0   | 0       | 0       |     | 0       | 0       |     | 0   |     | 0 $\delta$     | 0 $\delta$     |
| 0   | 0       | 1       |     | 0       | 0       |     | 0   |     | 0 $\delta$     | $\delta$ 1     |
| 0   | 1       | 0       |     | 1       | 1       |     | 0   |     | $\delta$ 0     | 1 $\delta$     |
| 0   | 1       | 1       |     | 0       | 0       |     | 0   |     | $\delta$ 1     | $\delta$ 1     |
| 1   | 0       | 0       |     | 0       | 1       |     | 0   |     | 0 $\delta$     | 1 $\delta$     |
| 1   | 0       | 1       |     | 1       | 0       |     | 0   |     | 1 $\delta$     | $\delta$ 1     |
| 1   | 1       | 0       |     | 1       | 0       |     | 0   |     | $\delta$ 0     | 0 $\delta$     |
| 1   | 1       | 1       |     | 0       | 1       |     | 1   |     | $\delta$ 1     | $\delta$ 0     |

### 5JK. espressioni booleane
- $z$ è di immediato riconoscimento: $z = xy_{1}y_{0}$

| $x$ \ $y_{1}y_{0}$ | 00  | 01  | 11       | 10       |
| ------------------ | --- | --- | -------- | -------- |
| 0                  | 0   | 0   | $\delta$ | $\delta$ |
| 1                  | 0   | 1   | $\delta$ | $\delta$ |
$j_{1}=xy_{0}$

| $x$ \ $y_{1}y_{0}$ | 00       | 01       | 11  | 10  |
| ------------------ | -------- | -------- | --- | --- |
| 0                  | $\delta$ | $\delta$ | 1   | 0   |
| 1                  | $\delta$ | $\delta$ | 1   | 0   |
$k_{1}=y_{0}$

| $x$ \ $y_{1}y_{0}$ | 00  | 01       | 11       | 10  |
| ------------------ | --- | -------- | -------- | --- |
| 0                  | 0   | $\delta$ | $\delta$ | 1   |
| 1                  | 1   | $\delta$ | $\delta$ | 0   |
$j_{0}=\overline{x}y_{1}+x\overline{y_1}=x\oplus y_{1}$

| $x$ \ $y_{1}y_{0}$ | 00       | 01  | 11  | 10       |
| ------------------ | -------- | --- | --- | -------- |
| 0                  | $\delta$ | 1   | 1   | $\delta$ |
| 1                  | $\delta$ | 1   | 0   | $\delta$ |
$k_0=\overline{x}+\overline{y_1}$
### 6JK. disegno della rete
#toadd ![[disegno della rete.png]]
## realizzazione con i flip-flop D
Ora realizziamo la stessa rete ma con i flip flop D (più semplice)
### 4D. tavola degli stati futuri

| $x$ | $y_{1}$ | $y_{0}$ |     | $Y_{1}$ | $Y_{0}$ |     | $z$ |     | $d_{1}, d_{0}$ |
| --- | ------- | ------- | --- | ------- | ------- | --- | --- | --- | -------------- |
| 0   | 0       | 0       |     | 0       | 0       |     | 0   |     | 0 0            |
| 0   | 0       | 1       |     | 0       | 0       |     | 0   |     | 0 0            |
| 0   | 1       | 0       |     | 1       | 1       |     | 0   |     | 1 1            |
| 0   | 1       | 1       |     | 0       | 0       |     | 0   |     | 0 0            |
| 1   | 0       | 0       |     | 0       | 1       |     | 0   |     | 0 1            |
| 1   | 0       | 1       |     | 1       | 0       |     | 0   |     | 1 0            |
| 1   | 1       | 0       |     | 1       | 0       |     | 0   |     | 1 0            |
| 1   | 1       | 1       |     | 0       | 1       |     | 1   |     | 0 1            |

### 5D. espressioni booleane
- $z$ è di immediato riconoscimento: $z = xy_{1}y_{0}$

- $d_{1}$

| $x$ \ $y_{1}y_{0}$ | 00  | 01  | 11  | 10  |
| ------------------ | --- | --- | --- | --- |
| 0                  | 0   | 0   | 0   | 1   |
| 1                  | 0   | 1   | 0   | 1   |

- $d_{0}$ 

| $x$ \ $y_{1}y_{0}$ | 00  | 01  | 11  | 10  |
| ------------------ | --- | --- | --- | --- |
| 0                  | 0   | 0   | 0   | 1   |
| 1                  | 0   | 1   | 0   | 1   |

### 6D. disegno della rete
#toadd ![[disegno della rete 2.png]]
## realizzazione con i flip-flop JK combinati alla ROM
> N.B.: Il vantaggio è che non vanno ricavate le espressioni booleane perché i valori degli output possono essere codificati direttamente nella ROM.