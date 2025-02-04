> *eXclusive Or* è vero solo quando un numero pari di ingressi è vero

| $xy$ | $x\oplus y$ |
| ---- | ----------- |
| 00   | 0           |
| 01   | 1           |
| 10   | 1           |
| 11   | 0           |
$x \oplus y =\overline xy +x\overline y$
- $x \oplus 1 = \overline x$
- $x \oplus 0 = x$

- $\overline{ x \oplus y}= \overline{\overline xy + x\overline y}=(x +\overline y)(\overline x + y)=x\overline x + x y + x\overline y+ y\overline y)=xy+\overline x \overline y$

- $\oplus$ è associativo?
	$x\oplus (y\oplus z) = (x \oplus y)\oplus z$
	$x \oplus (\overline y z + y \overline z)$
	$\overline x (\overline y z + y \overline z)+x\overline{(\overline y z +yz)}$
	$\overline x \overline y z + \overline x y \overline z + x(yz + \overline y \overline z)$
	$\overline x \overline y z + \overline x y \overline z + xyz + x \overline y \overline z$
	$(\overline x \overline y + xy)z+(\overline x y + x\overline y)\overline z$
	$\overline{x\oplus y}z+(x\oplus y)\overline z$
	$(x\oplus y)\oplus z$