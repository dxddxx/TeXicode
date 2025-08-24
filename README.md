TeXicode
========

TeXicode, short for TeX to Unicode, a CLI that turns TeX math expressions into Unicode art.

# Installation

## Run as Script

1. Have python3 installed, check with `python3 --version`
1. Clone and `cd` into this repo.
1. Make sure this is the correct directory by running `./txc '\Delta'`, should output `Δ`.
1. `pwd` to get the path
1. In `~/.zshrc` or `~/.bashrc`, add line `alias txc="<the_path>/txc"`

## Install form pip

`pip install TeXicode`

# Usage

## Basic Usage

- `txc '\prod_{i=0}^n\ x ~=~ x^n'` to output Unicode art
    - replace your own TeX equation inside quotes
    - use single quotes
    - if expression contains single quotes like `f'(x)`, replace with `f\'(x)`
    - `\[ \]`, `\( \)`, `$ $`, or `$$ $$` is optional, `\begin{} \end{}` is not supported yet
- Add `-c` at the end of the command to output in color (black on white)
- Unsupported commands will be rendered as `?`, or raise an error. If you see these or other rendering flaws, please post an issue, most can be easily fixed.

## Rendering Math in Markdown

- `txc -f filename.md` to replace latex expressions in markdown files with Unicode art in text blocks.
- Pipe into a markdown renderer like [glow](https://github.com/charmbracelet/glow) for ultimate markdown previewing:

Here is [example.md](example.md) rendered with `txr -f example.md -c | glow`, using the [JuliaMono](https://juliamono.netlify.app/) font.

![Screenshot](example.png)

# Features

- Supports most LaTeX math commands
- Uses Unicode
    - Not limited to ASCII characters
    - Unicode italic glyphs are used to differentiate functions from letters, similar to LaTeX
- Works with any good terminal font
    - Does not use any legacy glyphs
    - Go to `src/arts.py`, comment/uncomment some parts if your font support legacy glyphs to get even better symbols

<!--

# Design Principles

- Use box drawing characters for drawing lines and boxes
    - supported in almost all terminal fonts
    - consistent spacing between lines
    - fine tune length with half length glyphs
- Horizon (center line)
    - makes long concatenated expression readable
    - maybe add vertical horizon as well for &= aligning
    - space saving square roots kinda goes against this, might fix later when I find a better way to draw square roots
- Clarity over aesthetics
    - the square root tail is lengthened for clarity
    - all glyphs must connect, sums, square roots, etc
- Fully utilize Unicode features, expressions should look as good as the possibly can

# TODO

- square root with multi line degree
- align equation with \begin{align}, %= ,and \end{align}
- delimiters
    - tall angle brackets
    - `\middle`
- better error, consistent with LaTeX
- turn it into a vim plugin

-->
