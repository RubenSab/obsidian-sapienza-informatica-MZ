# SOP e POS
$f=(\overline a + c)\overline{(a+b)}+c$
- trasformare $\overline{(a+b)}$ in forma normale SOP con De Morgan in modo che la complementazione sia su una sola variabile.
$f=(\overline a + c)(\overline a \overline b)+c$
- applichiamo la proprietà distributiva
$f=\overline a \overline a \overline b + \overline a \overline b c+ c$
- idempotenza + assorbimento
$f=\overline a \overline b + c$ (SOP)
- in forma normale POS
$f=\overline a \overline b + c = (\overline a + c)(\overline b + c)$

# calcolo della forma SOP della duale
$f = \overline a \overline b + c$
- calcolo la duale
$\tilde f=(\overline a \overline b)\bullet c$
- la riscrivo in forma SOP
$\tilde f=(\overline a c)+\overline b c$

# tabella di verità di $f$ e $\tilde f$

| indice | $abc$ | $f$ | $\tilde f$ |
| ------ | ----- | --- | ---------- |
| 0.     | 000   | 1   | 0          |
| 1.     | 001   | 1   | 1          |
| 2.     | 010   | 0   | 0          |
| 3.     | 011   | 1   | 1          |
| 4.     | 100   | 0   | 0          |
| 5.     | 101   | 1   | 1          |
| 6.     | 110   | 0   | 0          |
| 7.     | 111   | 1   | 0          |
## canonica SOP
$f=\overline a \overline b\overline c + \overline a \overline b c + \overline a b c + \overline a b c + a \overline b c + abc$ (guardo dove $f=1$) $= OR(m_{0}, m_{1}, m_{3}, m_{5}, m_{7})$
## canonica POS
$f=(a + \overline b + c)(\overline a + b + c)(\overline a + \overline b + c)=AND(M_2,M_4,M_6)$
## dalla canonica SOP alla forma normale SOP
$f = \overline a \overline b + c = \overline a \overline b (\overline c + c) + c(\overline a + a)(\overline b + b) = \overline a \overline b\overline c + \overline a \overline b c + \overline a b c + \overline a + \overline a b c + a \overline b c + abc$
## dalla canonica POS alla forma normale POS
$f=(\overline a + c)(\overline b + c)=(\overline a + \overline b b + c)(\overline a a + \overline b + c)=(\overline a + \overline b + c)(\overline a + b +c)(\overline a + \overline b + c)(a + \overline b + c)$

