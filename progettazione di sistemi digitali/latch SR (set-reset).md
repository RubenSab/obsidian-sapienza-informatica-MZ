> è il tipo di latch più semplice, costruito a partire da due porte NOR.

![[latch.svg]]

> N.B.: Lo stato del [[flip-flop]] è determinato dall'uscita superiore (y). Il flip-flop si può pensare come un meccanismo bi-stabile che può trovarsi solo negli stati 0 e 1.  

| s   | r   | stato                                                                                                                                                                                                                                                                         |
| --- | --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0   | 0   | y: memorizzazione (stato set o reset)                                                                                                                                                                                                                                         |
| 0   | 1   | 0: reset (uno dei due stati di funzionamento normale)                                                                                                                                                                                                                         |
| 1   | 0   | 1: set (uno dei due stati di funzionamento normale)                                                                                                                                                                                                                           |
| 1   | 1   | C̶̦̙̤͓̝̾̂̇̅̈́̓͋̕O̶̘̱̰̖̔̔͆̑̎̀̿̕ͅN̴͕̹̖̘͓̿͑F̸͎̺̎Ȋ̴̖͔͕̎̍͝ͅG̴̡̟̜̗͇̖̐̈͋̉́͐̈́̕͠U̵̥͕̟͊͗̒͑̎̕͝͝Ṛ̸̩͌̂͆̏̾̚Á̷̦͕̰̼̥̽ͅͅZ̶͕̽͐̄͂͜Í̴̜̀Ö̶̧̨͔̭͇͎́͝Ņ̸͎̝̙̜̚E̶̝̙̣͕̮͚̮͂ ̷̡̛̘͓͇̦̫̻̈́̍̋͛̂̏̕͠P̴͓̝͇̙̥̜̙̜̦̊́͂̐͌̽̀̀̂Ŗ̴̧͕̲̥͈̲͗̿͝O̷̡̧͇̭̭͕̍͑̑̂̆̄͘̕͜͠Ỉ̸̭͕̠͇̖B̸̫̭̻̏̈́͌͝Ĭ̴̻̣̠͉̓͊̕͝Ṯ̶̛̊̓̄̐̈́͋̏̕A̵̡̗͚̖͔̥͍͌̉́̒͠ |
Astrazione a *blackbox* del latch:
```
     ________________
s -> | s       y    | -> y
     |              |
r -> | r   not y (z)| -> z
     |______________|
```

$y_{\text{ nuova}}=\overline{r+z}=\overline{r+\overline{s+y_{\text{ vecchia}}}}=\overline{r}\bullet(s+y_{\text{ vecchia}})$
Il tempo $\Delta t$ tra la $y$ nuova e quella vecchia non è indifferente: dipende dal tempo di attraversamento del segnale fra porte NOR.

## analisi del latch #AI
Un **latch** è un **elemento di memoria**: può **memorizzare un valore** finché non viene modificato dagli ingressi di **Set (S) e Reset (R)**. L’analisi serve a **capire come si evolve l’uscita nel tempo** rispetto agli ingressi.

Il metodo di **tagliare la linea di feedback** aiuta a trattare il latch **come una rete combinatoria** in un singolo istante, semplificando lo studio del suo comportamento.

Normalmente, un latch ha un ciclo di feedback, cioè un'uscita che ritorna come ingresso. Questo rende difficile analizzarlo direttamente.
L’idea è **sostituire l’uscita vecchia con una variabile temporanea** e poi esprimere la nuova uscita in funzione degli ingressi e della vecchia uscita.

In pratica, stiamo **scomponendo il funzionamento del latch passo dopo passo** invece di osservarlo come un sistema che cambia continuamente.

Si taglia la [[reti sequenziali|linea di feedback]]:

![[latch_tagliato.svg]]
1. **Scrivi l’equazione della nuova uscita BBB in termini della vecchia uscita $y_{\text{vecchia}}$ e degli ingressi.**

- Se il latch ha un NOR o NAND, usa la formula corrispondente.

1. **Usa De Morgan e semplifica l’equazione per esprimere $y_{\text{nuova}}$ in funzione degli ingressi.**

2. **Studia caso per caso (tabelle di verità parziali):**

- **Quando il reset è attivo?** → L'uscita deve diventare 0.
- **Quando il set è attivo?** → L'uscita deve diventare 1.
- **Quando entrambi sono 0?** → L'uscita deve mantenere il valore precedente.

3. **Verifica che il comportamento corrisponda a un latch (memorizzazione di stato).**