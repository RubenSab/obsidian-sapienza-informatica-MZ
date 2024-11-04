Supponiamo che un poligono con $n$ lati abbia $\frac{n(n-3)}{2}$ diagonali e supponiamo di aggiungere un nuovo vertice.
# caso base
$n=4,\ \frac{4(4-3)}{2}=2$ un quadrato di $4$ lati ha $2$ diagonali: il caso base è verificato.
# induzione
Quando aggiungiamo un nuovo vertice, un lato del poligono precedente diventa una diagonale del nuovo, quindi il nuovo vertice genera $n-1$ diagonali.

$\frac{n(n-3)}{2}+n-1=\frac{n^2-n-2}{2}=\frac{n^2+n-2n}{2}=\frac{(n+1)(n-2)}{2}=\frac{(n+1)((n+1)-3)}{2}$
