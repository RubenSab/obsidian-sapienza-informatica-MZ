> è il tipo di latch più semplice, costruito a partire da due porte NOR

![[latch.svg]]

> N.B.: Lo stato del [[flip-flop]] è determinato dall'uscita superiore (y)

| s   | r   | stato                                                                                                                                                                                                                                                                         |
| --- | --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0   | 0   | memorizzazione (stato set o reset)                                                                                                                                                                                                                                            |
| 0   | 1   | reset (uno dei due stati di funzionamento normale)                                                                                                                                                                                                                            |
| 1   | 0   | set (uno dei due stati di funzionamento normale)                                                                                                                                                                                                                              |
| 1   | 1   | C̶̦̙̤͓̝̾̂̇̅̈́̓͋̕O̶̘̱̰̖̔̔͆̑̎̀̿̕ͅN̴͕̹̖̘͓̿͑F̸͎̺̎Ȋ̴̖͔͕̎̍͝ͅG̴̡̟̜̗͇̖̐̈͋̉́͐̈́̕͠U̵̥͕̟͊͗̒͑̎̕͝͝Ṛ̸̩͌̂͆̏̾̚Á̷̦͕̰̼̥̽ͅͅZ̶͕̽͐̄͂͜Í̴̜̀Ö̶̧̨͔̭͇͎́͝Ņ̸͎̝̙̜̚E̶̝̙̣͕̮͚̮͂ ̷̡̛̘͓͇̦̫̻̈́̍̋͛̂̏̕͠P̴͓̝͇̙̥̜̙̜̦̊́͂̐͌̽̀̀̂Ŗ̴̧͕̲̥͈̲͗̿͝O̷̡̧͇̭̭͕̍͑̑̂̆̄͘̕͜͠Ỉ̸̭͕̠͇̖B̸̫̭̻̏̈́͌͝Ĭ̴̻̣̠͉̓͊̕͝Ṯ̶̛̊̓̄̐̈́͋̏̕A̵̡̗͚̖͔̥͍͌̉́̒͠ |


```
     ________________
s -> | s       y    | -> y
     |              |
r -> | r   not y (z)| -> z
     |______________|
```

$y \text{ nuova}=\overline{r+z}=\overline{r+\overline{s+y \text{ vecchia}}}=\overline{r}\bullet(s+y \text{ vecchia})$
Il tempo $\Delta t$ tra la $y$ nuova e quella vecchia non è indifferente: dipende dal tempo di attraversamento del segnale fra porte NOR.

## analisi del latch
Si taglia la [[reti sequenziali|linea di feedback]]:

![[latch_tagliato.svg]]
#todo capire e formattare il testo
- $r=s=0$
- $A = 1$
- $A=y(t)=y$
- $B=y(t+1)=y$

$B = y = \overline{r}\bullet(s+A)=1(0+1)=1$

$r=s=0$         $A=0$

$B = y = \overline{r}\bullet(s+A)=1(0+0)=0$

- set $s=r=0$            $y=0$
- $s$ diventa $1$
	- $z=\overline{s+y}=\overline{1+0}=0$
	- $y=\overline{r+z}=\overline{0+0}=1$
	stessa cosa partendo da y=1