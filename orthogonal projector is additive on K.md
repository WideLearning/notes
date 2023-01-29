# orthogonal projector is additive on K
from [[orthogonal projector]]

## statement
$$\forall x \in H, y \in K: P_{K}(x + y) = P_{K}(x) + y$$

## proof
$$P_{K}(x + y) = \arg\min_{z \in K}(\|z - (x + y)\|)$$
$$P_{K}(x + y) = \arg\min_{(z - y) \in K}(\|(z - y) - x\|)$$
$$P_{K}(x + y) = \arg\min_{z \in K}(\|z - x\|)$$
## proof
$$P_{K}(x + y) = \arg\min_{z \in K}(\|z - (x + y)\|)$$
$$P_{K}(x + y) = \arg\min_{z \in K}(\|(z - y) - x\|)$$
$$P_{K}(x + y) = \arg\min_{z \in K}(\|z - x\|) + y$$
$$P_{K}(x + y) = P_{K}(x) + y$$

