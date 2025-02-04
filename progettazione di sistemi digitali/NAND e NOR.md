>NAND: $\overline{ab}$ ($a \uparrow b$)

>NOR: $\overline{a+b}$ ($a \downarrow b$)

NAND e NOR sono operatori universali, quindi posso realizzare NOT, AND e OR usando solo NAND oppure solo NOR (eccetto in casi particolari, quindi bisogna verificare con [[algebra di Boole|De Morgan]]). Dei circuiti così realizzati si chiamano reti all-AND o reti all-OR.
## all NAND (conveniente per forme SOP)
**NOT** $\overline a = \overline{aa} = a\uparrow a$
**AND** $ab=\overline{a\uparrow b}=(a\uparrow b)\uparrow(a\uparrow b)$
**OR** $a+b=\overline{\overline{aa}\cdot\overline{bb}}=\overline{(a\uparrow a)\cdot(b \uparrow b)}=(a \uparrow a)\uparrow(b\uparrow b)$
## all NOR (conveniente per forme POS)
**NOT** $\overline a = \overline{a+a} = a\downarrow a$
**AND** $ab = \overline{\overline a + \overline b} = \overline{\overline{a+a}+\overline{b+b}} = (a \downarrow a)\downarrow(b\downarrow b)$
**OR** $a+b=\overline{\overline{a+b}}=\overline{\overline{a+b}+\overline{a+b}}=(a \downarrow b)\downarrow(a\downarrow b)$