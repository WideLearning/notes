
# Obsidian

## Basics

All Obsidian commands are available in the command menu opened by `ctrl+p`. Also you can find files in the `ctrl+o` menu.

## Plugins

There are a lot of community plugins, here are some examples:
![[plugins.png|300x300]]

### Advanced Tables
Not very advanced actually, simplifies editing Markdown tables, including pasting CSV directly.
| x   | y   |
| --- | --- |
| 1   | 1   |
| 2   | 4   |
| 3   | 9   |


### [Excalidraw](https://www.youtube.com/channel/UCC0gns4a9fhVkGkngvSumAQ)
Vector graphics integrated into Obsidian. Also note, that you can set the size when you embed an image (both common image formats and Excalidraw) by adding `|{width}x{height}` as done here:
![[example.excalidraw|500x300]]

### Filename Heading Sync
Ensures that filename matches the first H1 heading.

### Note Auto Creator
You can type "@" and then the name of the note you want to make a link for. If it exists already, it will be suggested, otherwise a new note with that name will be created.

### Obsidian Git
Just type "git" in command menu to see all the commands.

### Quick Latex for Obsidian
Obsidian support Latex by default, this plugin provides some autocompletions. Also you can add custom snippets in settings.
$$a \overset{b}{\underset{c}=} d$$
### Extended MathJax
Adds support for preamble and allows including some LaTeX packages, e.g. `physics`.

### TikZJax
Adds `pgfplots`, `tikzcd` and some other packages.
```tikz
\usepackage{tikz-cd}

\begin{document}
\begin{tikzcd}

    T
    \arrow[drr, bend left, "x"]
    \arrow[ddr, bend right, "y"]
    \arrow[dr, dotted, "{(x,y)}" description] & & \\
    K & X \times_Z Y \arrow[r, "p"] \arrow[d, "q"]
    & X \arrow[d, "f"] \\
    & Y \arrow[r, "g"]
    & Z

\end{tikzcd}
\end{document}
```

## Extras
- [[semantic search through the notes]]