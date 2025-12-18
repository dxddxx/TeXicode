TeXicode, short for TeX to Unicode, a CLI that turns TeX math expressions into Unicode art.

# [Webapp](https://texicode.dx512.com)

Posting math equations in Reddit is very annoying, you either have to post a screenshot of rendered LaTeX, or use Reddit's limited markdown features. Using TeXicode in Reddit code blocks makes posting math in Reddit much easier.

<details>
<summary>Quick tutorial NOW</summary>

1. Visit the [TeXicode website](https://texicode.dx512.com), copy output to clipboard
1. Make a new line in Reddit text field (check line spacing, if there is no line spacing above and below the cursor, it means Reddit does not see it as a separate line)
![Reddit1.png](images/Reddit1.png)
1. Add code block
![Reddit2.png](images/Reddit2.png)
1. Paste
![Reddit3.png](images/Reddit3.png)
If the output from TeXicode is a single line, can be placed inline using `Code` instead of `Code Block`
</details>

Also useful for quickly inserting single line equations into Word documents.

# CLI

### Install

```bash
pipx install TeXicode
```

### Basic Usage

- `txc '\LaTeX'` to output Unicode art
    - replace your own TeX equation inside quotes
    - use single quotes
    - if expression contains single quotes like `f'(x)`, replace with `f\'(x)`
    - `\[ \]`, `\( \)`, `$ $`, `$$ $$`, `\begin{...} \end{...}` is optional
- Add `-c` at the end of the command to output in color (black on white)
- Add `-n` at the end of the command to use normal fonts instead of cursive italic
- Unsupported commands will be rendered as `?`, or raise an error. If you see these or other rendering flaws, please post an issue, most can be easily fixed.

### Rendering Math in Markdown

- `txc -f filename.md` to replace latex expressions in markdown files with Unicode art in text blocks.
- Pipe into a markdown renderer like [glow](https://github.com/charmbracelet/glow) for ultimate markdown previewing:

Here is [example.md](example.md) rendered with `txc -f example.md -c | glow`, using the [JuliaMono](https://juliamono.netlify.app/) font.

![Screenshot](images/example.png)

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
    - vertical horizon for &= aligning
    - space saving square roots kinda goes against this, might fix later when I find a better way to draw square roots (found it!)
- Clarity over aesthetics
    - the square root tail is lengthened for clarity
    - all glyphs must connect, sums, square roots, etc
- Fully utilize Unicode features, expressions should look as good as the possibly can

# TODO

- toggled font/artstyle/glyph/legacy/asciimode
- properly implement ampersand
    - change parsing structure, make ampersand and linebreak into parents
    - or just do list of vert horizons (amps), linebreak concats, and \begin splits the lines at the ampersands to insert new paddings before stacking the lines together
    - better align, multi amp, works
    - vectors and matrices
- Better web input field
    - x button
    - code mirror
- comments with %
- macro expansion
- displaystyle
- better error, consistent with LaTeX
- update screenshot
- overline
    - like sqrt, use accent if single char, box drawing if not
- math mode in \text
- \bm \boldsymbol (easy)
- square root with multi line degree
    - with concat and lower
- delimiters
    - tall angle brackets
    - `\middle`
- turn it into a vim plugin

-->
