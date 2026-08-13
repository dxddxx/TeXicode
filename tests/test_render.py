"""Renderer tests for flat-cell grid assembly."""

import pytest

from texicode.pipeline import render_tex


RENDER_CASES = [
    (
        "matrix_2x2",
        r"\begin{matrix} a & b \\ c & d \end{matrix}",
        "𝑎 𝑏\n𝑐 𝑑",
    ),
    (
        "pmatrix",
        r"\begin{pmatrix} a & b \\ c & d \end{pmatrix}",
        "⎛𝑎 𝑏⎞\n⎝𝑐 𝑑⎠",
    ),
    (
        "cases",
        r"\begin{cases} x & x>0 \\ -x & x\le 0 \end{cases}",
        "⎧𝑥   𝑥>0\n⎩-𝑥  𝑥≤0",
    ),
    (
        "array_lr",
        r"\begin{array}{lr} 1 & 2 \\ 30 & 4 \end{array}",
        "1  2\n30 4",
    ),
    (
        "align_right_pad",
        r"\begin{align} 10 &= 5 \\ 1 &= 2 \end{align}",
        "10=5\n    \n 1=2",
    ),
    (
        "align_two_ampersands",
        r"\begin{align} a &= b & cc &= d \\ e &= f & g &= h \end{align}",
        "𝑎=𝑏𝑐𝑐=𝑑\n       \n𝑒=𝑓 𝑔=ℎ",
    ),
    (
        "equation_ampersand_columns",
        r"\begin{equation} a & b \end{equation}",
        " 𝑎𝑏",
    ),
    (
        "matrix_of_fractions",
        r"\begin{pmatrix} \frac{1}{2} & \frac{3}{4} \\ \frac{5}{6} & \frac{7}{8} \end{pmatrix}",
        "⎛ 1   3 ⎞\n"
        "⎜╶─╴ ╶─╴⎟\n"
        "⎜ 2   4 ⎟\n"
        "⎜ 5   7 ⎟\n"
        "⎜╶─╴ ╶─╴⎟\n"
        "⎝ 6   8 ⎠",
    ),
    (
        "mixed_cell_heights",
        r"\begin{bmatrix} a & \frac{1}{2} \\ \frac{3}{4} & b \end{bmatrix}",
        "⎡     1 ⎤\n"
        "⎢ 𝑎  ╶─╴⎥\n"
        "⎢     2 ⎥\n"
        "⎢ 3     ⎥\n"
        "⎢╶─╴  𝑏 ⎥\n"
        "⎣ 4     ⎦",
    ),
    (
        "wide_sum_integral_cells",
        r"\begin{matrix} \sum_{i=1}^{n} x_i & \int_0^\infty e^{-x}\,dx \\ a & b \end{matrix}",
        " ₙ     ∞      \n"
        "┰─╴   ⌠       \n"
        "▐╸ 𝑥ᵢ │ 𝑒⁻ˣ 𝑑𝑥\n"
        "┸─╴   ⌡₀      \n"
        "ⁱ⁼¹           \n"
        "  𝑎      𝑏    ",
    ),
    (
        "continued_fraction_cell",
        r"\begin{pmatrix} \frac{1}{1+\frac{1}{1+\frac{1}{1+\cdots}}} & x \\ y & z \end{pmatrix}",
        "⎛      1        ⎞\n"
        "⎜╶───────────╴ 𝑥⎟\n"
        "⎜       1       ⎟\n"
        "⎜ 1+╶───────╴   ⎟\n"
        "⎜        1      ⎟\n"
        "⎜    1+╶───╴    ⎟\n"
        "⎜       1+⋯     ⎟\n"
        "⎝      𝑦       𝑧⎠",
    ),
    (
        "cases_tall_cells",
        r"\begin{cases} \frac{x}{y} & \text{if } x>0 \\ \int_0^x f(t)\,dt & \text{otherwise} \end{cases}",
        "⎧ 𝑥                  \n"
        "⎪╶─╴        if 𝑥>0   \n"
        "⎪ 𝑦                  \n"
        "⎨⌠ˣ                  \n"
        "⎪│ 𝑓(𝑡) 𝑑𝑡  otherwise\n"
        "⎩⌡₀                  ",
    ),
    (
        "array_long_text",
        r"\begin{array}{lcr} \text{very long text cell} & x & \text{short} \\ y & \text{even longer text here} & z \end{array}",
        "very long text cell           𝑥           short\n"
        "𝑦                   even longer text here     𝑧",
    ),
    (
        "array_right_aligned",
        r"\begin{array}{rrr} 1 & 22 & 333 \\ 4444 & 5 & 66 \\ 7 & 888 & 9 \end{array}",
        "   1  22 333\n"
        "4444   5  66\n"
        "   7 888   9",
    ),
    (
        "sparse_matrix",
        r"\begin{pmatrix} a & & c \\ & b & \\ d & e & f \end{pmatrix}",
        "⎛𝑎   𝑐⎞\n"
        "⎜  𝑏  ⎟\n"
        "⎝𝑑 𝑒 𝑓⎠",
    ),
    (
        "vmatrix_sqrt_exp",
        r"\begin{vmatrix} \sqrt{x^2+1} & \frac{1}{\sqrt{2}} \\ e^{-\frac{x^2}{2}} & \int_0^1 t^2\,dt \end{vmatrix}",
        "⎟ ┌────╴   1    ⎟\n"
        "⎟╰┘𝑥²+1   ╶──╴  ⎟\n"
        "⎟          √2̅   ⎟\n"
        "⎟   𝑥²          ⎟\n"
        "⎟ -╶──╴         ⎟\n"
        "⎟   2    ⌠¹     ⎟\n"
        "⎟𝑒       │ 𝑡² 𝑑𝑡⎟\n"
        "⎟        ⌡₀     ⎟",
    ),
    (
        "align_tall_rows",
        r"\begin{align} \frac{a}{b} &= \frac{c}{d} \\ \sum_{i=1}^n i &= \frac{n(n+1)}{2} \end{align}",
        "  𝑎   𝑐      \n"
        " ╶─╴=╶─╴     \n"
        "  𝑏   𝑑      \n"
        "             \n"
        " ₙ           \n"
        "┰─╴   𝑛(𝑛+1) \n"
        "▐╸ 𝑖=╶──────╴\n"
        "┸─╴     2    \n"
        "ⁱ⁼¹          ",
    ),
    (
        "align_three_columns",
        r"\begin{align} a &= b & c &= d & e &= f \\ g &= h & i &= j & k &= l \end{align}",
        "𝑎=𝑏𝑐=𝑑𝑒=𝑓\n"
        "         \n"
        "𝑔=ℎ𝑖=𝑗𝑘=𝑙",
    ),
]


@pytest.mark.parametrize("name,tex,expected", RENDER_CASES,
                         ids=[case[0] for case in RENDER_CASES])
def test_render(name, tex, expected):
    assert render_tex(tex, False, False, "raw", {"fonts": "serif"}) == expected


def test_ampersand_outside_env_raises():
    result = render_tex("a & b", False, False, "raw", {"fonts": "serif"})
    assert "parsing error" in result
    assert "got amp_sep" in result


def test_array_requires_column_spec():
    result = render_tex(r"\begin{array} 1 & 2 \end{array}",
                        False, False, "raw", {"fonts": "serif"})
    assert "array requires a column spec" in result


def test_array_unsupported_spec():
    result = render_tex(r"\begin{array}{|c|} 1 \end{array}",
                        False, False, "raw", {"fonts": "serif"})
    assert "Unsupported column spec" in result


def test_nested_environment_raises():
    result = render_tex(
        r"\begin{pmatrix} \begin{matrix} a & b \\ c & d \end{matrix} & e \\ f & g \end{pmatrix}",
        False, False, "raw", {"fonts": "serif"})
    assert "parsing error" in result
