> I bit di parità sono bit aggiunti ***all'inizio*** dell'informazione codificata (nella maggior parte dei casi) per individuare [[errori di trasmissione]]. Se vengono aggiunti più bit, allora si parla di [[codice di Hamming]].
# parità pari/dispari
> Se l'informazione ricevuta è corretta numero di bit uguali a 1 contenuti nella singola porzione di bit considerata (compreso il bit di parità) deve essere pari/dispari.
## vantaggi della parità pari e dispari
- La parità pari è più efficace se l'informazione contiene più 1 che 0.
- La parità dispari è più efficace se l'informazione contiene più 0 che 1.
# funzionamento
- Il mittente aggiunge il bit (o i bit) di parità.
- Il destinatario ricalcola il bit di parità relativo alla porzione di bit considerata (ovviamente escludendo il bit di parità ricevuto).
- Lo confronta con quello ricevuto:
	- se il bit di parità ricevuto e ricalcolato sono diversi allora c'è stato sicuramente un errore.
	- se il bit di parità ricevuto e ricalcolato sono uguali allora non abbiamo la garanzia che non ci siano errori (infatti si potrebbero essere invertiti un numero pari di bit.)