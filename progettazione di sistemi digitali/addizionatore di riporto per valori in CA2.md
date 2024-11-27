> è un [[addizionatore a propagazione di riporto (ripple carry adder)|ripple carry adder]] con un [[complementatore]] per ogni bit di $B$ (abilitati da una variabile che indica se sottrarre o aggiungere $A$ e $B$) e due AND finali che controllano i due possibili casi di overflow.

Può fare:
- addizioni tra valori positivi e negativi
- sottrazioni: $A-B = A+(-B) = A+(\overline{B}+1)$

> N.B.: secondo il [[complemento a 2 (CA2)]], i Most Significant Bit di A, B e della somma non sono $2^{\text{numero di bit}-1}$ ma $-2^{\text{numero di bit}-1}$.



![[ripple carry adder CA2.svg]]