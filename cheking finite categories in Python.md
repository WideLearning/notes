# cheking finite categories in Python
From [[notes/category theory]]
$\physics$
```python
class Morphism:
    def __init__(self, dom, cod):
        self.dom = dom
        self.cod = cod


def composable(g: Morphism, f: Morphism):
    return g.dom == f.cod


object_names: set[str] = set()
morphisms: dict[str, Morphism] = dict()
ctable: dict[tuple[str, str], str] = dict()


def add_composition(gf_name: str, g_name: str, f_name: str):
    print(gf_name, g_name, f_name)
    assert gf_name in morphisms, f"Unknown gf: {gf_name}"
    assert g_name in morphisms, f"Unknown g: {g_name}"
    assert f_name in morphisms, f"Unknown g: {f_name}"
    assert morphisms[gf_name].dom == morphisms[f_name].dom, f"Wrong domain: {morphisms[gf_name].dom} ≠ {morphisms[f_name].dom}"
    assert morphisms[gf_name].cod == morphisms[g_name].cod, f"Wrong codomain: {morphisms[gf_name].cod} ≠ {morphisms[g_name].cod}"
    if (g_name, f_name) not in ctable:
        ctable[(g_name, f_name)] = gf_name
    else:
        old = ctable[(g_name, f_name)]
        assert old == gf_name, f"Already have: {g_name} ∘ {f_name} = {old} ≠ {gf_name}"


def add_morphism(name: str, dom: str, cod: str):
    assert dom in object_names
    assert cod in object_names
    assert name not in morphisms

    morphisms[name] = Morphism(dom, cod)
    add_composition(name, name, id_name(dom))
    add_composition(name, id_name(cod), name)


def id_name(name: str):
    return f"id_{name}"


def add_object(name: str):
    assert name not in object_names

    object_names.add(name)
    add_morphism(id_name(name), name, name)
    for f_name, f_morphism in morphisms.items():
        if f_morphism.dom == name:
            add_composition(f_name, f_name, id_name(name))
        if f_morphism.cod == name:
            add_composition(f_name, id_name(name), f_name)


def assert_correctness():
    for f_name, f_morphism in morphisms.items():
        for g_name, g_morphism in morphisms.items():
            if not composable(g_morphism, f_morphism):
                continue
            assert (g_name, f_name) in ctable, f"No result for {g_name} ∘ {f_name}"
    for f_name, f_morphism in morphisms.items():
        for g_name, g_morphism in morphisms.items():
            if not composable(g_morphism, f_morphism):
                continue
            for h_name, h_morphism in morphisms.items():
                if not composable(h_morphism, g_morphism):
                    continue
                gf_name = ctable[(g_name, f_name)]
                h_gf_name = ctable[(h_name, gf_name)]
                hg_name = ctable[(h_name, g_name)]
                hg_f_name = ctable[(hg_name, f_name)]
                assert (
                    h_gf_name == hg_f_name
                ), f"No associativity for {h_name} ∘ {g_name} ∘ {f_name}: {h_gf_name} vs {hg_f_name}"


add_object("X")
add_object("Y")

add_morphism("x", "X", "X")
add_morphism("y", "Y", "Y")
add_morphism("p", "X", "Y")
add_morphism("q", "Y", "X")
add_morphism("f", "X", "Y")
add_morphism("f'", "X", "Y")
add_morphism("g", "Y", "X")
add_morphism("g'", "Y", "X")

add_composition("x", "x", "x")
add_composition("p", "f", "x")
add_composition("p", "f'", "x")
add_composition("p", "p", "x")

add_composition("q", "x", "g")
add_composition(id_name("Y"), "f", "g")
add_composition("y", "f'", "g")
add_composition("y", "p", "g")

add_composition("q", "x", "g'")
add_composition("y", "f", "g'")
add_composition(id_name("Y"), "f'", "g'")
add_composition("y", "p", "g'")

add_composition("q", "x", "q")
add_composition("y", "f", "q")
add_composition("y", "f'", "q")
add_composition("y", "p", "q")


add_composition("y", "y", "y")
add_composition("q", "g", "y")
add_composition("q", "g'", "y")
add_composition("q", "q", "y")

add_composition("p", "y", "f")
add_composition(id_name("X"), "g", "f")
add_composition("x", "g'", "f") #?
add_composition("x", "q", "f")

add_composition("p", "y", "f'")
add_composition("x", "g", "f'")
add_composition("x", "g'", "f'")
add_composition("x", "q", "f'")

add_composition("p", "y", "p")
add_composition("x", "g", "p")
add_composition("x", "g'", "p")
add_composition("x", "q", "p")

assert_correctness()

print("Objects:")
print()
for name in object_names:
    print(name)

print()
print("Morphisms:")
print()
for name, morphism in morphisms.items():
    print(f"{name}:\t{morphism.dom}\t→\t{morphism.cod}")

print()
print("Composition:")
print()
for mid in object_names:
    for f_name, f_morphism in morphisms.items():
        if f_morphism.cod != mid:
            continue
        for g_name, g_morphism in morphisms.items():
            if g_morphism.dom != mid:
                continue
            print(f"{g_name}\t∘\t{f_name}\t= {ctable[(g_name, f_name)]}")

```