# monads from algebraic structures
From [[monad]]
$\physics$
## Statement
Consider a [[category]] $\cat{X}$ (of some algebraic structures, for example) which has free functor $F: \cat{Set} \to \cat{X}$ and [[forgetful functor]] $U: \cat{X} \to \cat{Set}$ such that $F \dashv U$. There is a unique [[monad]] in $\cat{Set}$ that corresponds to it.

## Proof
$F$ and $U$ form an [[adjunction]], so we can uniquely build a [[monad from adjunction]].

## Examples
- $\cat{Mon}$: list
- $\cat{CMon}$: multiset
- Idempotent commutative monoids: set
- $\cat{Ab}$: map from the given type to integers
```haskell
module Main (main) where

import Control.Monad
import Data.Functor.Product
import Data.List
import qualified Data.Map.Strict as Map

sumUp :: Ord a => [(a, Int)] -> Map.Map a Int
sumUp = foldl (\m (k, v) -> Map.insertWith (+) k v m) Map.empty

data Ab a = Ab {getList :: [(a, Int)]}
  deriving (Show)

instance (Ord a) => Eq (Ab a) where
  (Ab x) == (Ab y) = sumUp x == sumUp y

instance Functor Ab where
  fmap f (Ab m) = Ab $ [(f a, b) | (a, b) <- m]

instance Applicative Ab where
  pure a = Ab $ [(a, 1)]
  (Ab f) <*> (Ab a) = Ab $ [(fx ax, fy * ay) | (fx, fy) <- f, (ax, ay) <- a]

mu :: Ab (Ab a) -> Ab a
mu (Ab x) = Ab $ (x >>= (\(Ab v, nv) -> [(u, nv * nu) | (u, nu) <- v]))

instance Monad Ab where
  (>>=) :: Ab a -> (a -> Ab b) -> Ab b
  (>>=) x f = (mu . (fmap f)) x

f :: [Char] -> Ab [Char]
f x = Ab $ [(x, 2), (x ++ x, -1)]

main :: IO ()
main = do
  let a = Ab $ [("a", 1), ("aa", 2)]
  print (a >>= f >>= f)
  print (sumUp $ getList (a >>= f >>= f))

```