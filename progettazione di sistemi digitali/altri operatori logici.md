# XOR

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

# NAND e NOR
NAND: $\overline{ab}$ ( #todo aggiungere simbolo)
NOR: $\overline{a+b}$ ( #todo aggiungere simbolo)

NAND e NOR sono operatori universali, quindi posso realizzare NOT, AND e OR usando solo NAND oppure solo NOR (eccetto in casi particolari, quindi bisogna verificare con [[algebra di Boole|De Morgan]]). Dei circuiti così realizzati si chiamano reti all-AND o reti all-OR.
Esempi:
- [[circuito SOP AND-TO-OR all-NAND]]
- [[circuito POS AND-TO-OR all-NOR]]
## all NAND (conveniente per forme SOP)
**NOT** $\overline a = \overline{aa}$
**AND** $ab=\overline{\overline{ab}\bullet\overline{ab}}$
**OR** $a+b=\overline{\overline{aa}\bullet\overline{bb}}$
## all NOR (conveniente per forme POS)
**NOT** $\overline a = \overline{a+a}$
**AND** $ab = \overline{\overline a + \overline b} = \overline{\overline{a+a}+\overline{b+b}}$
**OR** $a+b=\overline{\overline{a+b}}=\overline{\overline{a+b}+\overline{a+b}}$