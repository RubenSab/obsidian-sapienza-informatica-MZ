#todo scrivere il procedimento senza fare ogni passaggio manualmente

# tabella di verità
```
x3 x2 x1 x0  y4 y3 y2 y1 y0
0  0  0  0   0  0  1  1  0 (0)
0  0  0  1   0  0  0  1  1 (1)
0  0  1  0   0  0  1  0  1 (2)
0  0  1  1   0  1  0  0  1 (3)

0  1  0  0   0  1  0  1  0 (4)
0  1  0  1   0  1  1  0  0 (5)
0  1  1  0   1  0  0  0  1 (6)
0  1  1  1   1  0  0  1  0 (7)

1  0  0  0   1  0  1  0  0 (8)
1  0  0  1   1  1  0  0  0 (9)
1  0  1  0   don't care
1  0  1  1   don't care

1  1  0  0   don't care
1  1  0  1   don't care
1  1  1  0   don't care
1  1  1  1   don't care
```

# mappa di Karnaugh dalla tabella di verità

| x3 e x2 sotto/x1 e x0 a destra | 00       | 01       | 10       | 11       |
| ------------------------------ | -------- | -------- | -------- | -------- |
| 00                             | 0        | 0        | 0        | 0        |
| 01                             | 0        | 0        | 1        | 1        |
| 11                             | $\delta$ | $\delta$ | $\delta$ | $\delta$ |
| 10                             | 1        | 1        | $\delta$ | $\delta$ |
## SOP
Un'implicante è ($\delta$ $\delta$ $\delta$ $\delta$ 1 1 $\delta$ $\delta$), l'altro è (1 1 $\delta$ $\delta$).
>N.B.: cerca gli implicanti di dimensioni massime

($\delta$ $\delta$ $\delta$ $\delta$ 1 1 $\delta$ $\delta$) va
le $x3$
(1 1 $\delta$ $\delta$) vale $x2\bullet x1$
SOP = $y3 = x_{3}x_{0}+x_{2}\overline{x_{1}}+\overline{x_{2}}{x_1}{x_0}$

## POS
Gli implicanti sono (0 0) (1 1 $\delta$ $\delta$), ($\delta$ $\delta$ 1 $\delta$), (0 0 $\delta$ $\delta$), (0 0 0 $\delta$)
