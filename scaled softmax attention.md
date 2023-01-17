---
date: 2022-07-01
---

# scaled softmax attention
It is a kind of [[attention]] used in [[transformer]], introduced in [[attention is all you need]].

$\physics$
$$\mathrm{Attn}(K, V, q) = \ev{\mathrm{softmax}\qty(\frac{S(K, q)}{\sqrt{n}}), V}$$