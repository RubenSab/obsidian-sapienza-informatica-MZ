```
bit x2, x1, x2 

    y-2 y3 y2 y1 y0
000 -2  1  1  1  0
001 -1  1  1  1  1
010 0   0  0  0  0
011 1   0  0  0  1

100 2   0  0  1  0
101 3   0  0  1  1
110 4   0  1  0  0
111 5   0  1  0  1

y0 = x0
y1 = not(x1)
y2 = not(x2) * not(x1) + x2 * x1 = not(xor(x2, x1))
y3 = not(x2) * not(x1) * not(x0) + not(x2) * not(x1) * x0 (mintermini SOP)
y3 = not(x2) * not(x1) * (not(x0) + x0) = not(x2) * not(x1)
```