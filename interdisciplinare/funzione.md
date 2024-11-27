$f:\mathbb{R}\rightarrow\mathbb{R}, \ \ x\rightarrow f(x)$
$f: A \rightarrow B$
- $f$ è la legge che associa ad ogni elemento di $A$ un'elemento di $B$
- $A$ è il dominio
- $B$ è il codominio

>Una **funzione** è una [[relazione]] ($F\subseteq A\times B$, $\forall a \in A\ \exists !\ b\in B\ |\ (a,b)\in F$) che associa (l'[[teoria degli insiemi|insieme]] A) il dominio e (B) il codominio.
>Esempio: $f(a)=a^2\rightarrow\{(a,b)\in\mathbb{N}\times\mathbb{N}\ |\ b=a^2\}=(0,0)(1,1)(2,4)(3,9)..(a,a^2)$
>

>Per quantificare il numero di elementi di un insieme si usa il concetto di [[cardinalità (o potenza)]].

>L'**immagine** di $f(x)$ è $im(A)=\{f(x),x\in A\}$, oppure $im(A)=\{b\ |\ (a,b)\in F\}$, $F\subseteq A\times B$


# proprietà delle funzioni
>$f: A \rightarrow B$ si dice **suriettiva** se $f(A)=B$, cioè se l'insieme delle immagini coincide con B.

>N.B.: per rendere una funzione suriettiva si restringe il dominio.

>$f:A\rightarrow B$ si dice **iniettiva** se $x\neq y \implies f(x)\neq f(y)$, cioè se non esistono due argomenti con lo stesso valore.

>N.B.: per rendere una funzione iniettiva si restringe il di codominio.

>$f: A \rightarrow B$ si dice **biiettiva** o **corrispondenza biunivoca** se $\forall b \in B\ \exists\ !a\in A\ |\ f(a)=b$. Solo le funzioni biettive sono invertibili.

>Data $f:A\rightarrow B$ iniettiva e suriettiva esiste la funzione inversa $f^-1:B\rightarrow A$, che ha la proprietà: $$f^{-1}(f(x))=x\ \forall x \in A$$$$f(f^{-1}(x))=x\ \forall x \in A$$

# composizione delle funzioni
$f: A \rightarrow B$
$g: B  \rightarrow C$

$g \circ f: A \rightarrow B \rightarrow C$
$g \circ f: A \rightarrow C$
$x\rightarrow g(f(x))$

# teoremi delle funzioni
- [[teorema dell'esistenza degli zeri]]
- [[teorema dei valori intermedi]]
- [[teorema di Weierstrass]]
- [[teorema di Weierstrass + Valori Intermedi generalizzati]]
