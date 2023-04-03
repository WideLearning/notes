# random access machine
From [[formal languages]]
$\physics$
## Definition
It has read-only input tape, write-only output tape, and countably infinite number of registers: $c(0), c(1), c(2), \dots$. All registers can store natural numbers, $c(0)$ can also store symbols of tape alphabet. Also there is a program, which is a list of instructions, and a command counter $\kappa$, that points to which instruction is executed now.

## Commands
- `load i`: $c(0) := c(i), \kappa := \kappa + 1$
- `store i`: $c(i) := c(0), \kappa := \kappa + 1$
- `add i`: $c(0) := c(0) + c(i), \kappa := \kappa + 1$
- `sub i`: $c(0) := \max(0, c(0) - c(i)), \kappa := \kappa + 1$
- `read`: $c(0) := x_{h_{r}}, h_{r} := h_{r} + 1, \kappa := \kappa + 1$
- `print`: $y := yc(0), \kappa := \kappa + 1$
- `shift`: $c(0) = \lfloor c(0) / 2 \rfloor, \kappa := \kappa + 1$
- `goto i`: $\kappa = i$
- `goto`: $\kappa = c(0)$
- `if a = i goto j`: …
- `ind load i`: $a = c(c(i)), \kappa := \kappa + 1$
- `ind store i`: $c(c(i)) := c(0), \kappa := \kappa + 1$
- `ind add i`
- `ind sub i`
- `load const i`: $c(0) := i, \kappa := \kappa + 1$
- `add const i`
- `sub const i`
- `end`

## Properties
- [[RAM and TM are equivalent]]