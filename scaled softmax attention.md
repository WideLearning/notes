# scaled softmax attention
From [[attention]]

$$\mathrm{Attn}(K, V, q) = \ev{\mathrm{softmax}\qty(\frac{S(K, q)}{\sqrt{n}}), V}$$