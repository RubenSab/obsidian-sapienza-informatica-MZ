#todo
> Modulo standard che riceve $n$ linee di ingresso e da $m$ linee di uscita; è formato da un decodificatore seguito da un insieme di porte OR, ognuna per produrre un bit di uscita.

- decodificatore
- insieme di porte OR (possibilmente rappresentate da una matrice #toadd) ognuna per produrre un bit di uscita
# Esempio

| x2  | x1  | x0  |     | y3  | y2  | y1  | y0  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0   | 0   | 0   |     | 1   | 1   | 1   | 0   |
| 0   | 0   | 1   |     | 1   | 1   | 1   | 1   |
| 0   | 1   | 0   |     | 0   | 0   | 0   | 0   |
| 0   | 1   | 1   |     | 0   | 0   | 0   | 1   |
| 1   | 0   | 0   |     | 0   | 0   | 1   | 0   |
| 1   | 0   | 1   |     | 0   | 0   | 1   | 1   |
| 1   | 1   | 0   |     | 0   | 1   | 0   | 0   |
| 1   | 1   | 1   |     | 0   | 1   | 0   | 1   |

## y3

| x2/x1,x0 | 00  | 01  | 11  | 10  |
| -------- | --- | --- | --- | --- |
| 0        | 1   | 1   | 0   | 0   |
| 1        | 0   | 0   | 0   | 0   |
$y_{3}=\overline{x_{2}}\bullet\overline{x_{1}}$
## y2

| x2/x1,x0 | 00  | 01  | 11  | 10  |
| -------- | --- | --- | --- | --- |
| 0        | 1   | 1   | 0   | 0   |
| 1        | 0   | 0   | 1   | 1   |
$y_{2}=\overline{x_{2}}\bullet\overline{x_{1}} + x_{2}\bullet x_{1}$
## y1

| x2/x1,x0 | 00  | 01  | 11  | 10  |
| -------- | --- | --- | --- | --- |
| 0        | 1   | 1   | 0   | 0   |
| 1        | 1   | 1   | 0   | 0   |
$y=\overline{x_{1}}$

## y0

| x2/x1,x0 | 00  | 01  | 11  | 10  |
| -------- | --- | --- | --- | --- |
| 0        | 0   | 1   | 1   | 0   |
| 1        | 0   | 1   | 1   | 0   |
$y=x_{0}$
#todo 