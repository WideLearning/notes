# writer functor
from [[functors in category theory]]

don’t confuse with [[reader functor]] or it’s opposite, it’s more about logging. types are mapped $a \to (a, string)$ and functions are mapped from $a \to b$ to $(a, string) \to (b, string)$ by composition of first parts and concatenation of second ones (for logging it makes sense).