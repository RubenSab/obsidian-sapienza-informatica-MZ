NAND: $\overline{ab}$ ($a \uparrow b$)
NOR: $\overline{a+b}$ ($a \downarrow b$)

NAND e NOR sono operatori universali, quindi posso realizzare NOT, AND e OR usando solo NAND oppure solo NOR (eccetto in casi particolari, quindi bisogna verificare con [[algebra di Boole|De Morgan]]). Dei circuiti così realizzati si chiamano reti all-AND o reti all-OR.
## all NAND (conveniente per forme SOP)
**NOT** $\overline a = \overline{aa}$ (per idempotenza)
**AND** $ab=\overline{\overline{ab}\bullet\overline{ab}}$ (per De Morgan)
**OR** $a+b=\overline{\overline{aa}\bullet\overline{bb}}$ (per idempotenza + De Morgan)
## all NOR (conveniente per forme POS)
**NOT** $\overline a = \overline{a+a}$ (per idempotenza)
**AND** $ab = \overline{\overline a + \overline b} = \overline{\overline{a+a}+\overline{b+b}}$ (per idempotenza + De Morgan)
**OR** $a+b=\overline{\overline{a+b}}=\overline{\overline{a+b}+\overline{a+b}}$ (per De Morgan)