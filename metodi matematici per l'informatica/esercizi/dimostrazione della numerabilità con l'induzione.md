$A_n={0,...,n}$
$\mathbb{N}-A_n$ è numerabile
# Caso base
$n = 0 \rightarrow A_n=\{0\}$
$\mathbb{N}-A_{n}=\mathbb{N}-\{0\}$ è numerabile per dimostrazione diretta:
infatti se per ogni elemento di indice $i$ di $\mathbb{N}$, corrisponde l'elemento di indice $i+1$ di $\mathbb{N}-A_0$, allora esiste una corrispondenza biunivoca tra $\mathbb{N}$ e $\mathbb{N}-\{0\}$, quindi $\mathbb{N}-A_{0}$ è numerabile.
# Passo induttivo
- $\mathbb{N}-A_n$ è numerabile, cioè è in relazione biunivoca con $\mathbb{N}$
A ogni elemento di $\mathbb{N}$ di indice $i$ corrisponde l'elemento di $\mathbb{N}-A_{n}$ di indice $i+n+1$, perché gli elementi di $\mathbb{N}-A_n$ sono spostati a sinistra di $n+1$ posizioni rispetto a $\mathbb{N}$, essendo che $\mathbb{N}-A_n$ non ha i primi $n+1$ elementi di $\mathbb{N}$. Quindi $\mathbb{N}-A_n$ è numerabile.

A ogni elemento di $\mathbb{N}$ di indice $i$ corrisponde l'elemento di $\mathbb{N}-A_{n+1}$ di indice $i+n+1+1$, perché gli elementi di $\mathbb{N}-A_n+1$ sono spostati a sinistra di $n+1+1$ posizioni rispetto a $\mathbb{N}$, essendo che $\mathbb{N}-A_n+1$ non ha i primi $n+1+1$ elementi di $\mathbb{N}$. Quindi $\mathbb{N}-A_{n+1}$ è numerabile.




# seconda dimostrazione
$A_{n}=\{0,...,n\}$
Quanti elementi di $P(A_n)$ hanno l'elemento $0$?

# Caso base
$A_0=\{0\}$
$P(A_0)=\{\{0\},\emptyset\}$
1 insieme di $P(A_0)$ contiene 0.
# ipotesi
$2^n$ insiemi di $P(A_n)$ contengono 0.
# passo induttivo
$P(A_n)$ ha $2^n$ elementi che contengono $0$ $\implies$ $P(A_{n+1})$ ha $2^{n+1}$ elementi che contengono $0$
# dimostrazione
Chi è $P(A_{n+1})$ rispetto a $P(A_n)$?
$P(A_{n+1}) = P(A_{n}) \cup \{X\cup\{n+1\}|X\in P(A_n)\}$

$P(A_n)$ ha $2^n$ elementi che contengono $0$ per ipotesi induttiva.
anche $\{X\cup\{n+1\}|X\in P(A_n)\}$ ha $2^n$ elementi perché prende semplicemente ogni insieme di $P(A_n)$ e gli aggiunge $\{n+1\}$.
$P(A_{n+1})$ ha $2^n+2^n=2^{n+1}$ che contengono $0$.

$\square$