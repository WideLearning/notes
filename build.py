from os import chdir, listdir

names = []
for name in listdir():
    if ".md" not in name or "compiled" in name:
        continue
    names.append(name)
names.sort(key=lambda x: x.lower())

def read_note(name):
    with open(name) as f:
        return f.read()

with open("compiled.md", "w") as f:
    print("# compiled\n", file=f)
    for name in names:
        print(read_note(name), file=f)
        print(file=f)
