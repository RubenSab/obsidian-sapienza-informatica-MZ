# 22 gen 2019
## 1
A F
B F
C F
D V
## 2
A F
B V
C V
D F
## 3
A F
B V
C V
D V
## 4

| (0,0) | (0,1) |       |       |
| ----- | ----- | ----- | ----- |
| (1,0) | (1,1) |       |       |
|       |       | (2,2) | (2,3) |
|       |       | (3,2) | (3,3) |
classi di equivalenza = {0, 1} e {2, 3}
insieme quoziente = {{0, 1}, {2, 3}}
## 5
$$\sum_{i=1}^{n}\frac{1}{i(i+1)}=1-\frac{1}{n+1}\ \ \forall n \geq 1$$
### caso base
$$n = 1 \rightarrow \sum_{i=1}^{1}\frac{1}{2}=\frac{1}{2}=1-\frac{1}{2} \ \ \square$$
### passo induttivo
Si vuole dimostrare che:
$$\sum_{i=1}^{n+1}\frac{1}{i(i+1)}=1-\frac{1}{n+2}\ \ \forall n \geq 1$$
$$\sum_{i=1}^{n+1}\frac{1}{i(i+1)}=\sum_{i=1}^{n}\frac{1}{i(i+1)}+\frac{1}{(n+1)(n+2)}\ \ \forall n \geq 1$$
Per ipotesi induttiva, abbiamo che:
$$\sum_{i=1}^{n+1}\frac{1}{i(i+1)}=1-\frac{1}{n+1}+\frac{1}{(n+1)(n+2)}$$
$$\frac{(n+1)(n+2)-(n+2)+1}{(n+1)(n+2)}=\frac{n^2+3n+2-n-2+1}{(n+1)(n+2)}=\frac{(n+1)^2}{(n+1)(n+2)}=\frac{n+1}{n+2}=1-\frac{1}{n+2}$$
$$\sum_{i=1}^{n+1}\frac{1}{i(i+1)}=1-\frac{1}{n+2}\ \ \forall n \geq 1\ \ \square$$
# 20 gen 2020
## 1
A F
B F
C V
D F
E V
## 2
A 
B 
C 
D 
## 3
A 
B 
C 
D 
## 4
A 
B 
C 
D 
## 5
A 
B 
C 
D 
## 6
A 
B 
C 
D
## 7
$$f(1)=1, f(n+1)=f(n)+3n+1$$
$$f(n)=\frac{n(3n-1)}{2}\ \ \forall n \geq 2$$
### caso base
$$f(2)=\frac{2(3\bullet 2-1)}{2}=5$$
$$f(1)=1,f(2)=1+3\bullet 1 + 1=5$$
### passo induttivo
Si vuole dimostrare che $$f(n+1)=\frac{(n+1)(3(n+1)-1)}{2}\ \ \forall n \geq 2$$$$f(n+1)=\frac{(n+1)(3n+2)}{2}=\frac{3n^2+5n+2}{2}\ \ \forall n \geq 2$$
Per definizione:
$$f(n+1)=f(n)+3n+1$$
Per ipotesi induttiva:
$$f(n+1)=\frac{n(3n-1)}{2}+3n+1=\frac{3n^{2}+5n+2}{2}\ \ \square$$

# 15 gen 2018
## 1A (V)
Se l'intersezione tra A e B contiene degli elementi, questi saranno contenuti in A ma non in C, quindi C è diverso da A, quindi è incluso propriamente in A.
## 1B (F)
C non ha nessun elemento dell'intersezione tra A e B, e nemmeno B - A ha elementi in comune tra A e B, quindi l'unione tra C e A - B non ha elementi appartenenti all'intersezione tra A e B.
## 2A (V)
## 2B (F)
## 3
$$\sum_{k=0}^{n-1}x^k=\frac{1-x^n}{1-x}\ \ \forall n \geq 2$$
### caso base
$n = 2$
$$\sum_{k=0}^{1}x^k=\frac{1-x^2}{1-x}$$
$$\sum_{k=0}^{1}x^k=x+x^0=x+1$$
$$\frac{1-x^{2}}{1-x}=x+1\ \ \square$$
### passo induttivo:
Si vuole dimostrare che:
$$\sum_{k=0}^{n}x^k=\frac{1-x^{n+1}}{1-x}\ \ \forall n \geq 2$$
$$\sum_{k=0}^{n}x^k=\sum_{k=0}^{n-1}x^k+x^n$$
Per l'ipotesi induttiva vale che:
$$\sum_{k=0}^{n}x^k=\frac{1-x^{n}}{1-x}+x^{n}=\frac{1-x^{n}+x^{n}-x^{n+1}}{1-x}=\frac{1-x^{n}}{1-x}\ \ \square$$
## 4
Si può parlare di numerabilità di un insieme se esso è finito. Un'insieme si dice numerabile se ha una corrispondenza biunivoca con $\mathbb{N}$.