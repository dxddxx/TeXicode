"""Renderer tests for flat-cell grid assembly."""

import pytest

from texicode import arts
from texicode.pipeline import render_tex


def render_lines(tex):
    """Render and return the output with trailing spaces stripped."""
    result = render_tex(tex, False, False, "raw", {"fonts": "serif"})
    return "\n".join(line.rstrip() for line in result.splitlines())


def art(text):
    """Un-indent 8-space test-art blocks; blank rows stay blank."""
    return "\n".join(line[8:] if line.startswith("        ") else line
                     for line in text.splitlines())


RENDER_CASES = [
    (
        "matrix_2x2",
        r"\begin{matrix} a & b \\ c & d \end{matrix}",
        art("""\
        𝑎 𝑏
        𝑐 𝑑"""),
    ),
    (
        "matrix_in_left_right",
        r"\left( \begin{matrix} a & b \\ c & d \end{matrix} \right)",
        art("""\
        ⎛𝑎 𝑏⎞
        ⎝𝑐 𝑑⎠"""),
    ),
    (
        "matrix_in_curly_braces",
        r"y = \left\{ \begin{matrix} a \\ b \end{matrix} \right\}",
        art("""\
          ⎧𝑎⎫
        𝑦=⎨𝑏⎬
          ⎩ ⎭"""),
    ),
    (
        "matrix_in_double_dollars",
        r"$$ \begin{matrix} a & b \\ c & d \end{matrix} $$",
        art("""\
        𝑎 𝑏
        𝑐 𝑑"""),
    ),
    (
        "matrix_in_brackets",
        r"\[ \begin{matrix} a & b \\ c & d \end{matrix} \]",
        art("""\
        𝑎 𝑏
        𝑐 𝑑"""),
    ),
    (
        "matrix_in_parens",
        r"\( \begin{matrix} a & b \\ c & d \end{matrix} \)",
        art("""\
        𝑎 𝑏
        𝑐 𝑑"""),
    ),
    (
        "matrix_in_dollars",
        r"$ \begin{matrix} a & b \\ c & d \end{matrix} $",
        art("""\
        𝑎 𝑏
        𝑐 𝑑"""),
    ),
    (
        "sum_limits",
        r"\sum\limits_{i=1}^n x",
        art("""\
         ₙ
        ┰─╴
        ▐╸ 𝑥
        ┸─╴
        ⁱ⁼¹"""),
    ),
    (
        "array_in_left_right",
        r"y = \left\{ \begin{array}{cc} 1 & 2 \\ 3 & 4 \end{array} \right\}",
        art("""\
          ⎧1 2⎫
        𝑦=⎨3 4⎬
          ⎩   ⎭"""),
    ),
    (
        "pmatrix",
        r"\begin{pmatrix} a & b \\ c & d \end{pmatrix}",
        art("""\
        ⎛𝑎 𝑏⎞
        ⎝𝑐 𝑑⎠"""),
    ),
    (
        "cases",
        r"y = \begin{cases} x & x>0 \\ -x & x\le 0 \end{cases}",
        art("""\
          ⎧𝑥   𝑥>0
        𝑦=⎨
          ⎩-𝑥  𝑥≤0"""),
    ),
    (
        "bmatrix_2_rows",
        r"y = \begin{Bmatrix} a \\ b \end{Bmatrix}",
        art("""\
          ⎧𝑎⎫
        𝑦=⎨ ⎬
          ⎩𝑏⎭"""),
    ),
    (
        "array_lr",
        r"\begin{array}{lr} 1 & 2 \\ 30 & 4 \end{array}",
        art("""\
        1  2
        30 4"""),
    ),
    (
        "align_right_pad",
        r"\begin{align} 10 &= 5 \\ 1 &= 2 \end{align}",
        art("""\
        10=5
        
         1=2"""),
    ),
    (
        "align_two_ampersands",
        r"\begin{align} a &= b & cc &= d \\ e &= f & g &= h \end{align}",
        art("""\
        𝑎=𝑏𝑐𝑐=𝑑
        
        𝑒=𝑓 𝑔=ℎ"""),
    ),
    (
        "equation_ampersand_columns",
        r"\begin{equation} a & b \end{equation}",
        art("""\
        𝑎𝑏"""),
    ),
    (
        "matrix_of_fractions",
        r"\begin{pmatrix} \frac{1}{2} & \frac{3}{4} \\ \frac{5}{6} & \frac{7}{8} \end{pmatrix}",
        art("""\
        ⎛ 1   3 ⎞
        ⎜╶─╴ ╶─╴⎟
        ⎜ 2   4 ⎟
        ⎜ 5   7 ⎟
        ⎜╶─╴ ╶─╴⎟
        ⎝ 6   8 ⎠"""),
    ),
    (
        "mixed_cell_heights",
        r"\begin{bmatrix} a & \frac{1}{2} \\ \frac{3}{4} & b \end{bmatrix}",
        art("""\
        ⎡     1 ⎤
        ⎢ 𝑎  ╶─╴⎥
        ⎢     2 ⎥
        ⎢ 3     ⎥
        ⎢╶─╴  𝑏 ⎥
        ⎣ 4     ⎦"""),
    ),
    (
        "wide_sum_integral_cells",
        r"\begin{matrix} \sum_{i=1}^{n} x_i & \int_0^\infty e^{-x}\,dx \\ a & b \end{matrix}",
        art("""\
         ₙ     ∞
        ┰─╴   ⌠
        ▐╸ 𝑥ᵢ │ 𝑒⁻ˣ 𝑑𝑥
        ┸─╴   ⌡₀
        ⁱ⁼¹
          𝑎      𝑏"""),
    ),
    (
        "continued_fraction_cell",
        r"\begin{pmatrix} \frac{1}{1+\frac{1}{1+\frac{1}{1+\cdots}}} & x \\ y & z \end{pmatrix}",
        art("""\
        ⎛      1        ⎞
        ⎜╶───────────╴ 𝑥⎟
        ⎜       1       ⎟
        ⎜ 1+╶───────╴   ⎟
        ⎜        1      ⎟
        ⎜    1+╶───╴    ⎟
        ⎜       1+⋯     ⎟
        ⎝      𝑦       𝑧⎠"""),
    ),
    (
        "cases_tall_cells",
        r"\begin{cases} \frac{x}{y} & \text{if } x>0 \\ \int_0^x f(t)\,dt & \text{otherwise} \end{cases}",
        art("""\
        ⎧ 𝑥
        ⎪╶─╴        if 𝑥>0
        ⎪ 𝑦
        ⎨⌠ˣ
        ⎪│ 𝑓(𝑡) 𝑑𝑡  otherwise
        ⎩⌡₀"""),
    ),
    (
        "array_long_text",
        r"\begin{array}{lcr} \text{very long text cell} & x & \text{short} \\ y & \text{even longer text here} & z \end{array}",
        art("""\
        very long text cell           𝑥           short
        𝑦                   even longer text here     𝑧"""),
    ),
    (
        "array_right_aligned",
        r"\begin{array}{rrr} 1 & 22 & 333 \\ 4444 & 5 & 66 \\ 7 & 888 & 9 \end{array}",
        art("""\
           1  22 333
        4444   5  66
           7 888   9"""),
    ),
    (
        "sparse_matrix",
        r"\begin{pmatrix} a & & c \\ & b & \\ d & e & f \end{pmatrix}",
        art("""\
        ⎛𝑎   𝑐⎞
        ⎜  𝑏  ⎟
        ⎝𝑑 𝑒 𝑓⎠"""),
    ),
    (
        "vmatrix_sqrt_exp",
        r"\begin{vmatrix} \sqrt{x^2+1} & \frac{1}{\sqrt{2}} \\ e^{-\frac{x^2}{2}} & \int_0^1 t^2\,dt \end{vmatrix}",
        art("""\
        ⎟ ┌────╴   1    ⎟
        ⎟╰┘𝑥²+1   ╶──╴  ⎟
        ⎟          √2̅   ⎟
        ⎟   𝑥²          ⎟
        ⎟ -╶──╴         ⎟
        ⎟   2    ⌠¹     ⎟
        ⎟𝑒       │ 𝑡² 𝑑𝑡⎟
        ⎟        ⌡₀     ⎟"""),
    ),
    (
        "align_tall_rows",
        r"\begin{align} \frac{a}{b} &= \frac{c}{d} \\ \sum_{i=1}^n i &= \frac{n(n+1)}{2} \end{align}",
        art("""\
          𝑎   𝑐
         ╶─╴=╶─╴
          𝑏   𝑑
        
         ₙ
        ┰─╴   𝑛(𝑛+1)
        ▐╸ 𝑖=╶──────╴
        ┸─╴     2
        ⁱ⁼¹"""),
    ),
    (
        "align_three_columns",
        r"\begin{align} a &= b & c &= d & e &= f \\ g &= h & i &= j & k &= l \end{align}",
        art("""\
        𝑎=𝑏𝑐=𝑑𝑒=𝑓
        
        𝑔=ℎ𝑖=𝑗𝑘=𝑙"""),
    ),
    (
        "raw_linebreak_rows",
        r"a \\ b",
        art("""\
        𝑎
        
        𝑏"""),
    ),
    (
        "display_linebreak_rows",
        r"\[ a \\ b \]",
        art("""\
        𝑎
        
        𝑏"""),
    ),
    (
        "dollar_linebreak_rows",
        r"$ a \\ b $",
        art("""\
        𝑎
        
        𝑏"""),
    ),
    (
        "substack_rows",
        r"\substack{a \\ b}",
        art("""\
        𝑎
        𝑏"""),
    ),
]


@pytest.mark.parametrize("name,tex,expected", RENDER_CASES,
                         ids=[case[0] for case in RENDER_CASES])
def test_render(name, tex, expected):
    assert render_lines(tex) == expected


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


@pytest.mark.parametrize("accent", [
    "tilde", "mathring", "widetilde", "overgroup", "utilde", "undergroup",
    "acute", "vec", "bar", "overleftarrow",
    "overrightarrow", "breve", "underleftarrow", "underrightarrow", "check",
    "overleftharpoon", "overrightharpoon", "dot", "overleftrightarrow",
    "ddot", "underleftrightarrow", "dddot", "overline", "overbracket", "ddddot",
    "underline", "underbracket", "grave", "underbar", "hat", "widecheck", "widehat",
    "'", "~", ".", "H", "`", "=", '"', "v", "^", "u", "r",
    "cancel", "bcancel", "xcancel", "sout", "angl",
])
def test_accent_storage_is_visible_and_rendering_strips_helper_letter(accent):
    stored = arts.accents[accent]
    assert stored.startswith("a")
    assert render_tex(
        rf"\{accent}{{x}}", False, False, "raw", {"fonts": "serif"}
    ) == "𝑥" + stored[1:]


def test_accent_is_applied_to_center_character_rounding_left():
    assert render_tex(
        r"\hat{xyz}", False, False, "raw", {"fonts": "serif"}
    ) == "𝑥𝑦̂𝑧"

    assert render_tex(
        r"\hat{xy}", False, False, "raw", {"fonts": "serif"}
    ) == "𝑥̂𝑦"


def test_text_accents_preserve_combining_marks_through_font_conversion():
    assert render_tex(
        r"\text{\~{xyz}}", False, False, "raw", {"fonts": "serif"}
    ) == "xỹz"


def test_stretchy_accents_use_their_art_rows_at_the_required_widths():
    for accent, accent_art in arts.stretchy_accents.items():
        width_one = render_lines(
            rf"\{accent}{{x}}"
        ).splitlines()
        if (accent_art["combining_width"] == 0
                or "single" in accent_art):
            assert len(width_one) == 2
            if accent_art["placement"] == "top":
                assert width_one == [accent_art["single"], "𝑥"]
            else:
                assert width_one == ["𝑥", accent_art["single"]]
        else:
            assert width_one == ["𝑥" + arts.accents[accent][1:]]

        width_two = render_lines(
            rf"\{accent}{{xy}}"
        ).splitlines()
        uses_row_at_width_two = (
            accent_art["combining_width"] == 0
            or "single" in accent_art
            or accent_art["combining_width"] < 2
        )
        assert len(width_two) == (2 if uses_row_at_width_two else 1)

        width_three = render_lines(
            rf"\{accent}{{xyz}}"
        ).splitlines()
        assert len(width_three) == 2
        if accent_art["placement"] == "top":
            accent_row, base_row = width_three
        else:
            base_row, accent_row = width_three
        assert base_row == "𝑥𝑦𝑧"
        expected_row = ([accent_art["left"]]
                        + [accent_art["fill"]] * (len(base_row) - 2)
                        + [accent_art["right"]])
        if "center" in accent_art:
            expected_row[(len(base_row) - 1) // 2] = accent_art["center"]
        assert accent_row == "".join(expected_row)
