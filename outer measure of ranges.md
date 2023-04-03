# outer measure of ranges
From [[outer measure]]
$\physics$
## Statement
Suppose $m^{*}$ is [[outer measure]], then:
- $m^{*}([l, r]) = r - l$
- $m^{*}((l, r)) = r - l$

## Proof
First, for the closed segment. Upper bound is trivial. For the lower bound we use [[Heine-Borel theorem]] to find finite subcover. Then for each interval from the cover take the part of it that is disjoint from previous intervals. Now we have a disjoint set of intervals that still covers our segment, so we can split our segment into parts that are covered by different intervals and show that the segment is not longer than their sum therefore. And if we add back all removed parts, the inequality still holds.

Now, for open interval or any other range we can simply take closed segments that are smaller and bigger by $\varepsilon$.