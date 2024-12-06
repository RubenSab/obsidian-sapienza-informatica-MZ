# [[latch SR (set-reset)]]

| $y, Y$ | $s, r$                                                                |
| ------ | --------------------------------------------------------------------- |
| 00     | 0 $\delta$ (se si passa da 0 a 0 o si memorizza 0 o si resetta)       |
| 01     | 10 (funzione di set)                                                  |
| 10     | 01 (funzione di reset)                                                |
| 11     | $\delta$ 0 (se si passa da 1 a 1 o si memorizza 1 o non si fa niente) |

# [[flip-flop delay (D)]]

| $y, Y$ | $d$ |
| ------ | --- |
| 00     | 0   |
| 01     | 1   |
| 10     | 0   |
| 11     | 1   |
# [[flip-flop (JK)]]

| $y, Y$ | $j, k$     |
| ------ | ---------- |
| 00     | 0 $\delta$ |
| 01     | 1 $\delta$ |
| 10     | $\delta$ 0 |
| 11     | $\delta$ 1 |