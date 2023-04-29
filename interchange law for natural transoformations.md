# interchange law for natural transoformations
From [[natural transformation]]
$\physics$
## Statement
Consider the following natural transformations:
```tikz
\usepackage{tikz-cd}
\usetikzlibrary{calc}
\tikzset{curve/.style={settings={#1},to path={(\tikztostart)
    .. controls ($(\tikztostart)!\pv{pos}!(\tikztotarget)!\pv{height}!270:(\tikztotarget)$)
    and ($(\tikztostart)!1-\pv{pos}!(\tikztotarget)!\pv{height}!270:(\tikztotarget)$)
    .. (\tikztotarget)\tikztonodes}},
    settings/.code={\tikzset{quiver/.cd,#1}
        \def\pv##1{\pgfkeysvalueof{/tikz/quiver/##1}}},
    quiver/.cd,pos/.initial=0.35,height/.initial=0}

\begin{document}
\begin{tikzcd}[row sep=huge] {\mathrm{A}} && {\mathrm{B}} && {\mathrm{C}} \arrow[""{name=0, anchor=center, inner sep=0}, curve={height=-18pt}, from=1-1, to=1-3] \arrow[""{name=1, anchor=center, inner sep=0}, curve={height=18pt}, from=1-1, to=1-3] \arrow[""{name=2, anchor=center, inner sep=0}, from=1-1, to=1-3] \arrow[""{name=3, anchor=center, inner sep=0}, curve={height=-18pt}, from=1-3, to=1-5] \arrow[""{name=4, anchor=center, inner sep=0}, curve={height=18pt}, from=1-3, to=1-5] \arrow[""{name=5, anchor=center, inner sep=0}, from=1-3, to=1-5] \arrow["{\alpha_1}"', shorten <=2pt, shorten >=2pt, Rightarrow, from=0, to=2] \arrow["{\alpha_2}"', shorten <=2pt, shorten >=2pt, Rightarrow, from=2, to=1] \arrow["{\beta_1}", shorten <=2pt, shorten >=2pt, Rightarrow, from=3, to=5] \arrow["{\beta_2}", shorten <=2pt, shorten >=2pt, Rightarrow, from=5, to=4] \end{tikzcd}
\end{document}
```
Then the order of composition doesn’t matter:
$$(\beta_{2} \circ \beta_{1}) \bullet (\alpha_{2}\circ \alpha_{1}) = (\beta_{2} \bullet \alpha_{2}) \circ (\beta_{1} \bullet \alpha_{1})$$

## Proof
See [this question](https://math.stackexchange.com/questions/3591835/trying-to-understand-proof-of-interchange-law-of-natural-transformation-composit).