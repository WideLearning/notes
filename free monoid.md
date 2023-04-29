# free monoid
from [[constructions and operations in category theory]]

in a nutshell, it’s a [[free construction]] of [[monoid]]. we start with a set of objects, add [[unit element]], than add all cartesian products and so on. also it must respect [[associativity]], so we don’t care about internal brackets. finally, we end up with all possible (including infinite) lists of the given elements (and the unit element corresponds to an empty list). 

### universal construction
suppose we have a set of generators $x$. consider the [[category of monoids]] and a functor $U$ from it to [[category of sets]] ([[forgetful functor]]) which maps each monoid to the set of its elements. the objects we want to consider are pairs like $(m, x \to U\ m)$ where $m$ is some monoid and the second element is to select which elements in that monoid correspond to the generators.

some of these functions may collapse a few generators into one element, so to get rid ot these we will form a category of these pairs and find an [[initial object]] there. let’s add a morphism from $m, p)$ to $(n, q)$ if there is a unique morphism $h :: m \to n$  such that $q = (U\ h) \circ p$. 

why this construction should work? the reasoning is quite similar to universal constructions from [[categorical product]] and [[categorical limit]]. suppoes that $m$ is actually the free monoid and now what are the cases for $n$. 
first, it can have some extra elements (but also everything from $m$). in that case $h$ is obvious, we just don’t map anything to those extra objects (and we can’t find another $h$, because we know where we must map all the generators and then all other elements from $m$ are determined by it). and if we try to find morphism from $n$ to $m$ then it would get ambiguous, because this time we are free to map extra elements (those of them which aren’t defined as a product of others) to any of the generators.

second, $n$ might be less (by collapsing several elements into one or something like that). but again, we know where to map each generator (even though some of them will collapse after it) and it determines the other mappings. and if we tried to find $n \to m$ morphism the ambiguity would arise when choosing where to map collapsed generators (any of those who collapsed to it would be a viable choice).