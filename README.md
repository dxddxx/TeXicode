TexTR
=====
TeX Terminal Renderer, a terminal TeX renderer in the terminal that renders TeX into your terminal by rendering the TeX.

# Usage

1. Clone and `cd` into repo
1. run in terminal: `./textr '\prod_{i=0}^n\ x ~=~ x^n'`, replace your own TeX equation inside quotes
    - use single quotes!
    - `\[ \]` or `\( \)` is optional, `\begin` and `$` is not supported yet
1. Enjoy beautiful Unicode art

```text
 ₙ        
┰─┰       
┃ ┃ 𝑥 = 𝑥ⁿ
┸ ┸       
ⁱ⁼⁰       
```
> [!IMPORTANT]
> omg github can't even render in monospace and box glyphs don't even line up, go try yourself, all equations on this page look horrible

inline equation $\frac{1}{2}$
big equation
$$
\frac{1}{2}
$$
big equation
\[
\frac{1}{2}
\]
latex block
```latex
\frac{1}{2}
```

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

# Examples

`e^{i\theta} = \cos\theta + i\sin{\theta}`:
```text
𝑒ⁱᶿ=cosθ+𝑖sinθ
```
`r = \sqrt{a^2+b^2}`:
```text
   ┌─────╴
𝑟= │𝑎²+𝑏² 
  ╰┘      
```
`(x+y)^n ~=~ \sum_{k=0}^n \binom{n}k x^n y^{n-k}`:
```text
          ₙ          
         ┰─╴⎛𝑛⎞      
(𝑥+𝑦)ⁿ = ▐╸ ⎜ ⎟𝑥ⁿ𝑦ⁿ⁻ᵏ
         ┸─╴⎝𝑘⎠      
         ᵏ⁼⁰         
```
`\arctan\left(-\frac1{\sqrt 3}\right) = \frac\pi6`:
```text
      ⎛   1   ⎞  π 
arctan⎜-╶────╴⎟=╶─╴
      ⎜   ┌─╴ ⎟  6 
      ⎝  ╰┘³  ⎠    
```

Notice the 3 under the square root is shrunk to save space, below is the same equation with full size 3
```text
      ⎛   1   ⎞  π 
arctan⎜-╶────╴⎟=╶─╴
      ⎜   ┌─╴ ⎟  6 
      ⎜   │3  ⎟    
      ⎝  ╰┘   ⎠    

```
`x = \frac{-b\pm\sqrt{b^2-4ac}}{2a}`:
```text
       ┌──────╴ 
   -𝑏± │𝑏²-4𝑎𝑐  
      ╰┘        
𝑥=╶────────────╴
        2𝑎      

```

# Design Principles:

- Use box drawing characters
    - supported in most fonts
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
- align equation with begin align, %= , end align
- delimiters
    - tall angle brackets
    - `\middle`
- error consistent with LaTeX
