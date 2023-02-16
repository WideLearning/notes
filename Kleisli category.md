# Kleisli category
From [[notes/category]]

## Informal definition
Similar to [[category of sets]], but here the morphism $A \to B$ isn’t just a function. It also produces side effects, which are returned together with the main result. And the composition has to respect this, combining those side effects (as in monads)

## Examples
- Logging: side effect is a string with all the logs produced)
- Partial functions as morphisms: side effect is a flag indicating that the result is valid

