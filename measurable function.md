# measurable function
From [[measure theory]]
$\physics$
## Definition
A function $f: E \to \mathbb{R}$ where $E$ is a [[measurable set]] is measurable iff one of the following statements holds for all $c \in \mathbb{R}$:
1. $\{ x \in E \mid f(x) > c \}$ is measurable.
2. $\{ x \in E \mid f(x) \geq c \}$ is measurable.
3. $\{ x \in E \mid f(x) < c \}$  is measurable.
4. $\{ x \in E \mid f(x) \leq c \}$ is measurable.

## Proof of equivalence
[[measurable sets are closed under taking complements]]:
$1 \iff 4, 2 \iff 3$

[[measurable sets are closed under countable union]]:
$\{ x \in E \mid f(x) > c \} = \bigcup\limits_{k=1}^{\infty} \{ x \in E \mid f(x) \geq c + \frac{1}{k} \}$
$2 \implies 1$

similarly, with countable intersection:
$1 \implies 2$

## Properties
- [[preimage of measurable function is measurable]]
- [[measurable function in terms of open sets]]
- [[continuous functions are measurable]]
- [[monotone functions on interval are measurable]]
- [[measurable almost everywhere functions are measurable]]
- [[finite measurable functions are an algebra]]
- [[compositon of continuous function with measurable is measurable]]
- [[countable maximum and minimum of measurable functions is measurable]]
- Composition of measurable functions is not necessarily measurable.
- [[simple approximation lemma]], [[simple approximation theorem]]
- [[step approximation lemma]]
- [[semisimple approximation lemma]]
- [[boundedness of finite measurable functions]]