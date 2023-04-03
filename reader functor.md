# reader functor
from [[functors in category theory]]

### implementations
the simplest one:
``` haskell
instance Functor ((->) r) where
	fmap f g = f . g
```
the shortest one:
``` haskell
instance Functor ((->) r) where
	fmap = (.)
```
here the functor takes already a function or what? how it is supposed to work?
``` haskell
newtype Reader e a = Reader (e -> a)
instance Functor (Reader e) where
	fmap f (Reader g) = Reader (\x -> f (g x))
```
probably the right version of it:
``` haskell
type Reader a x = a -> x
instance Functor (Reader a) where
	fmap f h = f . h
```