- $(\neg(\neg A))\lor A$ è falsificabile e soddisfacibile
- $(\neg A)\lor (\neg(\neg A))$ è tautologia
- $(\neg (A\lor B))\iff (A\land B)$ è falsificabile e soddisfacibile

| A   | B   | formula |
| --- | --- | ------- |
| V   | V   | V       |
| V   | F   | V       |
| F   | V   | V       |
| F   | F   | F       |
- $(A\implies B)\iff(\neg B \implies \neg A)$ è una tautologia (principio di contrapposizione)
- $(A\land\neg A)\implies B$ è una tautologia.

- Se $\vDash (A\implies B)$ allora $\vDash ((A\land B)\iff A)$
	Tutte le volte che $A$ è vero, $B$ è vero. Quindi tutte le volte che $A$ e $B$ sono veri, $A\land B$ è vero. Tutte le volte che $A \land B$ è vero, $A$ è vero, quindi $((A\land B)\iff A)$ è una tautologia.