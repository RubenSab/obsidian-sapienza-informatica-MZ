> è il tipo di latch più semplice.

![[latch.svg]]

| s   | r   | stato                   |
| --- | --- | ----------------------- |
| 0   | 0   | memorizzazione          |
| 0   | 1   | reset                   |
| 1   | 0   | set                     |
| 1   | 1   | CONFIGURAZIONE PROIBITA |


```
     ________________
s -> | s       y    | ->
     |              |
r -> | r   not y (z)| ->
     |______________|
```

$y \text{ nuova}=\overline{r+z}=\overline{r+\overline{s+y}}=\overline{r}\bullet(s+y \text{ vecchia})$
Il tempo $\Delta t$ tra la $y$ nuova e quella vecchia non è indifferente: dipende dal tempo di attraversamento tra le porte NOR.

## analisi del latch
Si taglia la [[reti sequenziali|linea di feedback]]:

![[latch_tagliato.svg]]
#todo formattare il testo
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