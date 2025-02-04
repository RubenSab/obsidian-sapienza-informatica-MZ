> Modulo che compara due linee in input $a$ e $b$ e dà come output tre linee che indicano se $a>b$ o $a=b$ o $a<b$.

![[comparatore.svg]]
> Per controllare se $a=b$ bisogna fare gli/lo XOR di tutte le cifre e farli confluire in un OR se sono più di uno (comparatore di uguaglianza).

> Se $a$ e $b$ sono più lunghi di 1 bit e bisogna necessariamente sapere se $a>b$ o $a<b$ (non solo se $a=b$), allora devo eseguire $a-b$ in un [[addizionatori (adder)|adder]] e usare il MSB del risultato:

- $R_{\text{MSb}}=1 \implies a<b$
- $R_{\text{MSb}}=0 \implies a\geq b$ (bisognerà poi controllare se $a=b$ in un comparatore di uguaglianza)