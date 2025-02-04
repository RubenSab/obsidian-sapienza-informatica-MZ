Il fatto che un circuito, può essere descritto dall'interpretazione a [[porte logiche]] dell'[[algebra di Boole]] è particolarmente utile per ottimizzare i circuiti, cioè [[criterio di minimalità|minimizzare il numero di porte necessarie]] per creare un circuito che restituisce gli stessi output a partire dagli stessi input del circuito di partenza.

Si ottimizza un circuito codificando la sequenza delle sue porte logiche in un'espressione booleana, poi si semplifica l'espressione in base alle identità dell'algebra Booleana e si decodifica una nuova sequenza di porte logiche.

# come si ottimizza un circuito: sintesi
- leggere la descrizione verbale
- espressioni booleane (opzionale)
- tavola di verità
- ottenere le espressioni minimali tramite K mappe
- disegno del circuito

# come si vede se un circuito è [[criterio di minimalità|minimale]]: analisi
- vedere la rappresentazione del circuito
- scrivere un'espressione booleana di ogni uscita
- compilare la tavola di verità
- fare la descrizione verbale del funzionamento del circuito
- caratterizzare le condizioni che danno uscita 1 (attivare qualcosa) (se ci sono più uscite 1 usare SOP, se ci sono più uscite 0 usare POS).
- ottenere le espressioni minimali tramite K mappe
- confrontare il circuito ottenuto con il circuito originale.