Ipotesi:
- Se la Roma ha vinto la partita allora il Brescia e il Genoa retrocedono.
$$R \implies (\neg B \land \neg G)$$
- Se almeno uno tra il Brescia e il Genoa retrocede, allora la Sampdoria di salva.
$$\neg B \lor \neg G \implies S$$
Tesi:
- Quindi, se la Sampdoria non si salva, allora la Roma non ha vinto la partita.
$$\neg S \implies \neg R$$
Dimostrare la tesi vuol dire dimostrare $(\neg B \lor \neg G \implies S)\implies (\neg S \implies \neg R)\ \ \forall R, B, G, S$


| $R$ | $B$ | $G$ | $S$ | $R \implies (\neg B \land \neg G)$ | $\neg B \lor \neg G \implies S$ | $\neg S \implies \neg R$ |
| --- | --- | --- | --- | ---------------------------------- | ------------------------------- | ------------------------ |
| V   | V   | V   | V   | F                                  | V                               | V                        |
| V   | V   | V   | F   | F                                  | V                               | F                        |
| V   | V   | F   | V   | F                                  | V                               | V                        |
| V   | V   | F   | F   | F                                  | F                               | F                        |
| V   | F   | V   | V   | F                                  | V                               | V                        |
| V   | F   | V   | F   | F                                  | F                               | F                        |
| V   | F   | F   | V   | F                                  | V                               | V                        |
| V   | F   | F   | F   | G                                  | F                               | F                        |
| F   | V   | V   | V   | V                                  | V                               | V                        |
| F   | V   | V   | F   | V                                  | V                               | V                        |
| F   | V   | F   | V   | V                                  | ...                             | V                        |
| F   | V   | F   | F   | V                                  | ...                             | F                        |
| F   | F   | V   | V   | V                                  | ...                             | V                        |
| F   | F   | V   | F   | V                                  | ...                             | F                        |
| F   | F   | F   | V   | V                                  | ...                             | V                        |
| F   | F   | F   | F   | V                                  | ...                             | F                        |
$(\neg B \lor \neg G \implies S)\implies (\neg S \implies \neg R)\ \ \forall R, B, G, S\ \ \square$
