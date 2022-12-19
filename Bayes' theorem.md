# Bayes' theorem

from [[terms commonly used in Bayesian statistics]]

If $X$ is the variable we are interested in and $D$ is the data we have:
$$ P(X \mid D) =
\frac{P(XD)}{P(D)} =
\frac{P(X)P(D \mid X)}{P(D)} \sim
P(X)P(D \mid X) $$
In the equation above $X$ and $D$ were considered as events, but only notation changes if we take them to be discrete or continuous random variables. For example, in case of continuous variables we just replace all probabilities with densities:
$$ f_{X \mid D = d}(x) =
\frac{f_{X}(x)f_{D\mid X=x}(d)}{f_{D}(d)} \sim
f_{X}(x)f_{D\mid X=x}(d) $$
The last transformation shows that $P(D)$ is just a normalization constant. It means that we can ignore it, until we want to get the normalized probabilities. But if we actually need it, it is trivial (though not always computable in a reasonable time) to find:
$$P(D) = P(D\mid X) + P(D \mid \bar X)$$
$$f_{D}(d) = \int_{X} f_{D\mid X=x}(d) dx$$