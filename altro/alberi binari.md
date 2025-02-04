# alberi binari

## 1. definizione
Partiamo definendo un nodo di un albero binario così:

``` python
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
```

In modo che ogni nodo contenga un valore e sia collegato ad altri nodi (il destro e/o il sinistro).

In questo modo l'albero binario seguente

```
            a
          /   \
        b       c
       / \     / \
	  d   e   f   g
```

può essere scritto come:

``` python
tree = Node('a',
	Node('b', 
		Node('d'),
		Node('e')
	),
	Node('c',
		Node('f'),
		Node('g')
	)
)
```

> N.B.: `Node('d')`, `Node('e')`, `Node('f')` e `Node('g')`, possono essere chiamati ***foglie***, cioè nodi senza altri nodi collegati, mentre `Node('a')` è la ***root***, cioè la radice.

## 2. ordinamenti
Prendiamo l'albero binario già visto come esempio.

A partire dall'**albero** (struttura annidata) si può creare una **lista** (struttura lineare) che ha come elementi i valori dei suoi nodi.

Dato che l'albero è una struttura più complessa di una lista, i collegamenti tra i nodi vanno persi, perché valori di ogni nodo devono essere per forza di cose disposti in modo lineare uno dopo l'altro, invece diventa importante l'ordine secondo cui i valori dei nodi vengono inseriti nella nuova lista.

Ci sono **3 tipi di ordinamenti possibili** se si scrive una funzione ricorsiva che agisce su tutto l'albero e prende in considerazione solo il valore del nodo corrente, quello del ramo a destra e quello del ramo a sinistra.

``` python
def inorder(node): # d b e a f c g
    if node is None: # caso base
        return []
    # passo ricorsivo
    return inorder(node.left) + [node.value] + inorder(node.right)

def preorder(node): # a b d e c f g
    if node is None: # caso base
        return []
    # passo ricorsivo
    return [node.value] + preorder(node.left) + preorder(node.right)

def postorder(node): # g f c e d b a
    if node is None: # caso base
        return []
    # passo ricorsivo
    return postorder(node.left) + postorder(node.right) + [node.value]
```

Il caso base di queste funzioni non sono le foglie dell'albero binario, ma sono i nodi delle foglie, i quali per definizione non esistono: infatti `if node is None` si verifica solo se il nodo su cui arriva la funzione non esiste, cioè è `None`.

Se ci si trova su una foglia, `in/pre/postorder(node.left)` e `in/pre/postorder(node.right)`
ritorneranno entrambe una lista vuota perché le foglie non hanno né `node.left` né `node.right` (caso base).
Queste due liste vuote verranno concatenate alla lista `[node.value]`, la quale contiene solo il valore del nodo corrente (in questo caso risultando solo in `[node.value]`).
Poi, subito sopra le foglie, avrà luogo l'ordinamento vero e proprio.

L'ordine con cui queste tre liste (lista con solo il valore corrente, risultato della funzione applicata a destra e risultato della funzione applicata a sinistra) verranno concatenate, è l'unica differenza tra i tre tipi di ordinamento.
- In *inorder* la funzione ritorna la lista: sinistra, nodo corrente, destra;
- in *preorder* la funzione ritorna la lista: nodo corrente, sinistra, destra;
- in *postorder* la funzione ritorna la lista: sinistra, destra, nodo corrente.

## 3. contare i nodi e sommarne i valori
``` python
def count_nodes(node):
    if node is None: # caso base
        return 0
    # passo ricorsivo
    return 1 + count_nodes(node.left) + count_nodes(node.right)

def sum_nodes(node):
    if node is None: # caso base
        return 0
    # passo ricorsivo
    return node.value + sum_nodes(node.left) + sum_nodes(node.right)
```
### contare i nodi

Per contare i nodi basta considerare che il nodo corrente è un singolo nodo, quindi bisogna sommare **1** con **il numero dei nodi contati a destra e a sinistra** del nodo corrente.

Anche qui il caso base avviene nei nodi di una foglia, che sono inesistenti, cioè sono uguali a `None`. Dato che il nodo corrente non esiste in questo caso base, allora la funzione ritornerà 0 nodi.
### sommare i valori dei nodi

Il principio di `sum_nodes` è lo stesso di `count_nodes` e anche il caso base è identico, però qui, nel passo ricorsivo, bisogna sommare **il valore del nodo corrente** con la **somma dei valori dei nodi contati a destra e a sinistra** del nodo corrente.

## 3.1. contare i nodi e sommarne i valori nel range di profondità desiderato

Rispetto a ciò che abbiamo fatto prima per contare tutti i nodi dell'albero o sommarne i valori, ora dobbiamo introdurre un check che controlla se la profondità corrente (da definire come un parametro opzionale uguale a 0 se la funzione viene chiamata sulla root dell'albero) è compresa nell'intervallo $[j,k]$, cioè tra la profondità minima e la profondità massima su cui vogliamo agire.

- Se la profondità corrente è troppo bassa allora la funzione continua a esplorare l'albero con una chiamata ricorsiva a destra e a sinistra senza contare/aggiungere il valore del nodo corrente;
- se è nell'intervallo allora conta/aggiunge il nodo corrente;
- se è oltre l'intervallo si ferma e ritorna 0.

> N.B.: bisogna passare `j`, `k` e `current_depth` anche alle chiamate ricorsive nella definizione della funzione.

``` python
def count_nodes(node, j, k, current_depth=0):

    if node is None:  # caso base
        return 0
        
	if current_depth < j: # continua a esplorare senza contare il nodo corrente
	    return count_nodes(node.left, j, k, current_depth+1) + count_nodes(node.right, j, k, current_depth+1)
	    
    if j <= current_depth <= k: # conta i nodi nell'intervallo [j, k]
        return 1 + count_nodes(node.left, j, k, current_depth+1) + count_nodes(node.right, j, k, current_depth+1)
        
    if current_depth > k: # si ferma quando siamo oltre la profondità massima
        return 0


def sum_nodes(node, j, k, current_depth=0):

    if node is None: # caso base
        return 0

    if current_depth < j: # continua a esplorare senza contare il nodo corrente
        return sum_nodes(node.left, j, k, current_depth + 1) + sum_nodes(node.right, j, k, current_depth + 1)

    if j <= current_depth <= k: # somma i valori dei nodi nell'intervallo [j, k]
        return node.value + sum_nodes(node.left, j, k, current_depth + 1) + sum_nodes(node.right, j, k, current_depth + 1)

    if current_depth > k: # si ferma quando siamo oltre la profondità massima
        return 0
```

## 4. ricerca binaria e profondità del nodo cercato

``` python
def search(node, query):

    if node.value == query: # caso base
        return True

    else: # passo ricorsivo
        if node.left:
            return search(node.left, query)
        if node.right:
            return search(node.right, query)

	return False


def node_depth(node, query, depth=0):

    if not node: # caso base
        return None

    if node.value == query: # caso base
        return depth

    else: # passo ricorsivo

		left_result = node_depth(node.left, query, depth+1)
        if left_result is not None:
            return left_result

        right_result = node_depth(node.right, query, depth+1)
        if right_result is not None:
            return right_result

	return False
```
### ricerca binaria
La ricerca binaria è l'algoritmo di ricerca più veloce per determinare se un determinato valore è contenuto da qualche parte in un albero binario.

Nel caso base, se il valore del nodo è il valore ricercato (`query`), allora la funzione si ferma e restituisce `True`; altrimenti, cerca lo stesso valore a partire dal nodo a destra (se esiste) e a sinistra (se esiste). Dopo tutto il processo, se la funzione è andata avanti senza trovare niente, ritorna `False`.
### profondità del nodo il cui valore è uguale a quello cercato
I casi base di `node_depth` sono gli stessi della ricerca binaria, tranne che se il valore del corrente corrisponde al valore ricercato allora non viene ritornato `True` ma la profondità del nodo corrente.
Se il caso base non si verifica, allora la funzione chiama se stessa a sinistra e a destra del nodo, **ma aumenta di uno il parametro opzionale `depth`** (inizializzato a 0 nel nodo root) per comunicare alla nuova chiamata ricorsiva che è scesa di un livello del nodo precedente.

