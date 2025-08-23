TeXicode
=====
TeXicode, short for TeX to Unicode, a cli tool that turns TeX math expressions into Unicode art.

# Installation

# Usage

## Basic Usage

1. `txc '\prod_{i=0}^n\ x ~=~ x^n'` to output Unicode art
    - replace your own TeX equation inside quotes
    - use single quotes
    - if expression contains single quotes like `f'(x)`, replace with `f\'(x)`
    - `\[ \]`, `\( \)`, `$ $`, or `$$ $$` is optional, `\begin{} \end{}` is not supported yet
1. add `-c` at the end of the command to output in color (black on white)

## Rendering Math in Markdown

1. `txc -f filename.md` to replace latex expressions in markdown files with Unicode art in text blocks.
1. Pipe into a markdown renderer like [glow](https://github.com/charmbracelet/glow) for ultimate markdown previewing:
1. add `-c` at the end of the command to output in color (black on white)
Here is [example.md]() rendered with `txr -f example.md -c | glow`

# Features

1. Unicode characters
    - Prettier than similar projects by fully utilizing Unicode glyphs
1. Unicode *italic texts*
    - Differentiate functions from letters
    - Actual italic glyphs, not italicized text
1. Works with any good terminal font
    - The examples provided here did not use any legacy glyphs
    - Change the header of `renderer.py` if your font support legacy glyphs to get even better symbols
1. Written in python
    - So you can fork it and turn it into a vim plugin

# Design Principles:

- Use box drawing characters when possible
    - supported in almost all terminal fonts
    - consistent spacing between lines
    - fine tune length with half length glyphs
- Horizon (center line)
    - makes long concatenated expression readable
    - space saving square roots kinda goes against this, might fix later
    - maybe add vertical horizon as well for &= aligning
- Aesthetics first, clarity even more first (0th)
    - the square root tail is too long but it makes it clear
    - all glyphs must connect, sums, square roots, etc
- Fully utilize Unicode chars, expressions should look as good as the possibly can

# TODO

- square root with multi line degree
- align equation with \begin{align}, %= ,and \end{align}
- delimiters
    - tall angle brackets
    - `\middle`
- error consistent with LaTeX
