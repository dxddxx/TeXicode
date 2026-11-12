"""Renderer tests for flat-cell grid assembly."""

import re
from pathlib import Path

import pytest

from texicode import arts
from texicode import symbols_art
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


CHECKLIST_SYMBOL_SECTIONS = {
    "Greek Letters",
    "Other Letters",
    "Logic and Set Theory",
    "Relations",
    "Negated Relations",
    "Arrows",
    "Binary Operators",
    "Math Operators",
    "Symbols and Punctuation",
}


def _checked_simple_symbol_commands():
    """Return checked one-token commands grouped by checklist section.

    Keeping this list derived from the checklist makes it difficult to add a
    checkmark without also adding a rendering assertion for the command.
    Structured commands and text-wrapped entries have dedicated tests below.
    """
    commands_by_section = {}
    section = None
    checklist = Path(__file__).parents[1] / "katex-supported.md"
    for line in checklist.read_text(encoding="utf-8").splitlines():
        if line.startswith("## ") or line.startswith("### ") \
                or line.startswith("#### "):
            section = line.split(" ", 1)[1]
        match = re.match(r"- \[x\] `([^`]*)`", line)
        if not match or section not in CHECKLIST_SYMBOL_SECTIONS:
            continue
        expression = match.group(1)
        if any(char in expression for char in "{}[]"):
            continue
        found = re.findall(r"\\([A-Za-z]+|[^\s])", expression)
        if not found or not all(command in symbols_art.symbols
                                for command in found):
            continue
        commands = commands_by_section.setdefault(section, [])
        for command in found:
            if command not in commands:
                commands.append(command)
    return list(commands_by_section.items())


CHECKED_SYMBOL_CATEGORIES = _checked_simple_symbol_commands()


@pytest.mark.parametrize(
    "section,commands",
    CHECKED_SYMBOL_CATEGORIES,
    ids=[section for section, _ in CHECKED_SYMBOL_CATEGORIES],
)
def test_checked_symbol_category_renders_single_and_multiline(
        section, commands):
    expression = " ".join(rf"\{command}" for command in commands)
    expected = "".join(
        "".join(symbols_art.symbols[command]) for command in commands
    )
    assert render_tex(
        expression, False, False, "raw", {"fonts": "serif"}
    ) == expected, section
    assert render_lines(expression + MULTILINE_BLOCK) == (
        " " * len(expected) + "𝑎\n" + expected + "𝑏"
    ), section


def _checked_text_symbols():
    entries_by_section = {}
    section = None
    checklist = Path(__file__).parents[1] / "katex-supported.md"
    for line in checklist.read_text(encoding="utf-8").splitlines():
        if line.startswith("## ") or line.startswith("### ") \
                or line.startswith("#### "):
            section = line.split(" ", 1)[1]
        match = re.match(r"- \[x\] `([^`]*)`", line)
        if not match or section not in {"Other Letters",
                                        "Symbols and Punctuation"}:
            continue
        expression = match.group(1)
        inner = re.fullmatch(r"\\text\{([^{}]+)\}", expression)
        if inner is None:
            continue
        content = inner.group(1)
        if content.startswith("\\"):
            command = content[1:]
            if command not in symbols_art.symbols:
                continue
            expected = "".join(symbols_art.symbols[command])
        else:
            expected = content
        entries_by_section.setdefault(section, []).append(
            (expression, expected)
        )
    return list(entries_by_section.items())


CHECKED_TEXT_SYMBOL_CATEGORIES = _checked_text_symbols()


@pytest.mark.parametrize(
    "section,entries",
    CHECKED_TEXT_SYMBOL_CATEGORIES,
    ids=[section for section, _ in CHECKED_TEXT_SYMBOL_CATEGORIES],
)
def test_checked_text_symbol_category_renders_single_and_multiline(
        section, entries):
    expression = " ".join(entry[0] for entry in entries)
    expected = "".join(entry[1] for entry in entries)
    assert render_tex(
        expression, False, False, "raw", {"fonts": "serif"}
    ) == expected, section
    assert render_lines(expression + MULTILINE_BLOCK) == (
        " " * len(expected) + "𝑎\n" + expected + "𝑏"
    ), section


DELIMITER_SYMBOLS = [
    ("lparen", "("), ("rparen", ")"),
    ("lceil", "⌈"), ("rceil", "⌉"), ("uparrow", "↑"),
    ("lbrack", "["), ("rbrack", "]"), ("downarrow", "↓"),
    ("lbrace", "{"), ("rbrace", "}"),
    ("lmoustache", "⎰"), ("rmoustache", "⎱"),
    ("updownarrow", "↕"), ("langle", "⟨"), ("rangle", "⟩"),
    ("lgroup", "⟮"), ("rgroup", "⟯"), ("Uparrow", "⇑"),
    ("vert", "∣"), ("ulcorner", "⌜"), ("urcorner", "⌝"),
    ("Downarrow", "⇓"), ("|", "∥"), ("Vert", "∥"),
    ("llcorner", "⌞"), ("lrcorner", "⌟"), ("Updownarrow", "⇕"),
    ("lvert", "|"), ("rvert", "|"),
    ("lVert", "∥"), ("rVert", "∥"), ("backslash", "\\"),
    ("lang", "⟨"), ("rang", "⟩"), ("lt", "⟨"), ("gt", "⟩"),
    ("llbracket", "⟦"), ("rrbracket", "⟧"),
    ("lBrace", "⦃"), ("rBrace", "⦄"),
]

MULTILINE_BLOCK = r"\begin{matrix}a \\ b\end{matrix}"


@pytest.mark.parametrize("command,glyph", DELIMITER_SYMBOLS)
def test_delimiter_commands_render_single_character(command, glyph):
    assert render_tex(
        rf"\{command} a", False, False, "raw", {"fonts": "serif"}
    ) == glyph + "𝑎"


@pytest.mark.parametrize("command,glyph", DELIMITER_SYMBOLS)
def test_delimiter_commands_compose_with_multiline_blocks(command, glyph):
    assert render_lines(rf"\{command}{MULTILINE_BLOCK}") == (
        " 𝑎\n" + glyph + "𝑏"
    )


SIZED_DELIMITER_PAIRS = [
    ("big", "big", "(𝑎)", " 𝑎\n(𝑏)"),
    ("bigl", "bigr", "(𝑎)", " 𝑎\n(𝑏)"),
    ("Big", "Big", "⎛ ⎞\n⎜𝑎⎟\n⎝ ⎠", "⎛𝑎⎞\n⎜𝑏⎟\n⎝ ⎠"),
    ("Bigl", "Bigr", "⎛ ⎞\n⎜𝑎⎟\n⎝ ⎠", "⎛𝑎⎞\n⎜𝑏⎟\n⎝ ⎠"),
    ("bigg", "bigg", "⎛ ⎞\n⎜ ⎟\n⎜𝑎⎟\n⎜ ⎟\n⎝ ⎠", "⎛ ⎞\n⎜𝑎⎟\n⎜𝑏⎟\n⎜ ⎟\n⎝ ⎠"),
    ("biggl", "biggr", "⎛ ⎞\n⎜ ⎟\n⎜𝑎⎟\n⎜ ⎟\n⎝ ⎠", "⎛ ⎞\n⎜𝑎⎟\n⎜𝑏⎟\n⎜ ⎟\n⎝ ⎠"),
    ("Bigg", "Bigg", "⎛ ⎞\n⎜ ⎟\n⎜ ⎟\n⎜𝑎⎟\n⎜ ⎟\n⎜ ⎟\n⎝ ⎠", "⎛ ⎞\n⎜ ⎟\n⎜𝑎⎟\n⎜𝑏⎟\n⎜ ⎟\n⎜ ⎟\n⎝ ⎠"),
    ("Biggl", "Biggr", "⎛ ⎞\n⎜ ⎟\n⎜ ⎟\n⎜𝑎⎟\n⎜ ⎟\n⎜ ⎟\n⎝ ⎠", "⎛ ⎞\n⎜ ⎟\n⎜𝑎⎟\n⎜𝑏⎟\n⎜ ⎟\n⎜ ⎟\n⎝ ⎠"),
]


@pytest.mark.parametrize(
    "left_command,right_command,single_expected,multiline_expected",
    SIZED_DELIMITER_PAIRS,
)
def test_sized_delimiters_render_single_and_multiline(
        left_command, right_command, single_expected, multiline_expected):
    single = rf"\{left_command}(a\{right_command})"
    multiline = rf"\{left_command}({MULTILINE_BLOCK}\{right_command})"

    assert render_lines(single) == single_expected
    assert render_lines(multiline) == multiline_expected


def test_combined_delimiter_sizes_render_single_and_multiline():
    expression = r"( \big( \Big( \bigg( \Bigg("
    assert render_lines(expression) == (
        "    ⎛\n   ⎛⎜\n  ⎛⎜⎜\n((⎜⎜⎜\n"
        "  ⎝⎜⎜\n   ⎝⎜\n    ⎝"
    )
    assert render_lines(expression + MULTILINE_BLOCK) == (
        "    ⎛\n   ⎛⎜\n  ⎛⎜⎜𝑎\n((⎜⎜⎜𝑏\n"
        "  ⎝⎜⎜\n   ⎝⎜\n    ⎝"
    )


@pytest.mark.parametrize(
    "tex,single_expected,multiline_expected",
    [
        (r"\left. a \right)", "𝑎)", "𝑎⎞\n𝑏⎠"),
        (r"\left( a \right.", "(𝑎", "⎛𝑎\n⎝𝑏"),
    ],
)
def test_invisible_delimiters_render_single_and_multiline(
        tex, single_expected, multiline_expected):
    assert render_lines(tex) == single_expected

    if "\\begin" in tex:
        multiline = tex.replace("a", "a \\ b")
    else:
        multiline = tex.replace("a", MULTILINE_BLOCK)
    assert render_lines(multiline) == multiline_expected


def test_raw_floor_delimiters_render_single_and_multiline():
    assert render_lines("⌊a⌋") == "⌊𝑎⌋"
    assert render_lines("⌊" + MULTILINE_BLOCK + "⌋") == " 𝑎\n⌊𝑏⌋"


def test_raw_slash_delimiters_render_single_and_multiline():
    assert render_lines("/a/") == "/𝑎/"
    assert render_lines("/" + MULTILINE_BLOCK + "/") == " 𝑎\n/𝑏/"


def test_unchecked_plain_math_symbols_render_together():
    expression = "+ a/b \""
    expected = "+𝑎/𝑏\""
    assert render_lines(expression) == expected
    assert render_lines(expression + MULTILINE_BLOCK) == (
        " " * len(expected) + "𝑎\n" + expected + "𝑏"
    )


def test_apostrophe_renders_as_prime():
    assert render_lines("a'") == "𝑎′"
    assert render_lines("a'" + MULTILINE_BLOCK) == "  𝑎\n𝑎′𝑏"


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


@pytest.mark.parametrize(("tex", "expected"), [
    (r"\text{$a\text{b}$}", "ab"),
    (r"\text{$\text{a}$}", "a"),
    (r"\text{$$a\text{b}$$}", "ab"),
    (r"\text{$$\text{a}\text{$b$}$$}", "ab"),
    (r"\text{a$\text{b}$c$$d\text{e}$$}", "abcde"),
])
def test_nested_text_and_dollar_math(tex, expected):
    assert render_tex(
        tex, False, False, "raw", {"fonts": "serif"}
    ) == expected


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


BIG_OPERATOR_CASES = [
    ("sum", "┰─╴\n▐╸ 𝑎\n┸─╴", "┰─╴𝑎\n▐╸ 𝑏\n┸─╴"),
    ("prod", "┰─┰\n┃ ┃𝑎\n┸ ┸", "┰─┰𝑎\n┃ ┃𝑏\n┸ ┸"),
    ("bigotimes", "╭───╮\n│ × │𝑎\n╰───╯", "╭───╮𝑎\n│ × │𝑏\n╰───╯"),
    ("bigvee", "╲╱𝑎", "  𝑎\n╲╱𝑏"),
    ("int", "⌠\n│𝑎\n⌡", "⌠𝑎\n│𝑏\n⌡"),
    ("coprod", "┰ ┰\n┃ ┃𝑎\n┸─┸", "┰ ┰𝑎\n┃ ┃𝑏\n┸─┸"),
    ("bigoplus", "╭───╮\n│ + │𝑎\n╰───╯", "╭───╮𝑎\n│ + │𝑏\n╰───╯"),
    ("bigwedge", "╱╲𝑎", "  𝑎\n╱╲𝑏"),
    ("iint", "⌠⌠\n││𝑎\n⌡⌡", "⌠⌠𝑎\n││𝑏\n⌡⌡"),
    ("intop", "⌠\n│𝑎\n⌡", "⌠𝑎\n│𝑏\n⌡"),
    ("bigodot", "╭───╮\n│ ⋅ │𝑎\n╰───╯", "╭───╮𝑎\n│ ⋅ │𝑏\n╰───╯"),
    ("bigcap", "╭─╮\n│ │𝑎", "╭─╮𝑎\n│ │𝑏"),
    ("iiint", "⌠⌠⌠\n│││𝑎\n⌡⌡⌡", "⌠⌠⌠𝑎\n│││𝑏\n⌡⌡⌡"),
    ("smallint", "∫𝑎", " 𝑎\n∫𝑏"),
    ("biguplus", "│+│𝑎\n╰─╯", "   𝑎\n│+│𝑏\n╰─╯"),
    ("bigcup", "│ │𝑎\n╰─╯", "   𝑎\n│ │𝑏\n╰─╯"),
    ("oint", " ⌠\n╶╪╴𝑎\n ⌡", " ⌠ 𝑎\n╶╪╴𝑏\n ⌡"),
    ("oiint", " ⌠⌠\n╶╪╪╴𝑎\n ⌡⌡", " ⌠⌠ 𝑎\n╶╪╪╴𝑏\n ⌡⌡"),
    ("oiiint", " ⌠⌠⌠\n╺╪╪╪╸𝑎\n ⌡⌡⌡", " ⌠⌠⌠ 𝑎\n╺╪╪╪╸𝑏\n ⌡⌡⌡"),
]


@pytest.mark.parametrize("command,single_expected,multiline_expected",
                         BIG_OPERATOR_CASES)
def test_big_operator_commands_render_single_and_multiline(
        command, single_expected, multiline_expected):
    assert render_lines(rf"\{command} a") == single_expected
    assert render_lines(rf"\{command}{MULTILINE_BLOCK}") == multiline_expected


SPACING_CASES = [
    (r"\, a", 1), (r"\thinspace a", 1), (r"\> a", 1),
    (r"\: a", 1), (r"\medspace a", 1), (r"\; a", 1),
    (r"\thickspace a", 1), (r"\enspace a", 1),
    (r"\quad a", 2), (r"\qquad a", 4), (r"\! a", 0),
    ("~a", 1), (r"\ a", 1),
    (r"\negthinspace a", 0), (r"\negmedspace a", 0),
    (r"\negthickspace a", 0), (r"\nobreakspace a", 1),
    (r"\space a", 1),
]


@pytest.mark.parametrize("tex,space_width", SPACING_CASES)
def test_spacing_commands_render_single_and_multiline(tex, space_width):
    prefix = " " * space_width
    assert render_tex(
        tex, False, False, "raw", {"fonts": "serif"}
    ) == prefix + "𝑎"
    command = tex[:-1] if tex.endswith(" a") else tex[:-1]
    if tex == "~a":
        multiline = tex[0] + MULTILINE_BLOCK
    elif tex == r"\ a":
        multiline = tex[0:2] + MULTILINE_BLOCK
    else:
        multiline = command + MULTILINE_BLOCK
    assert render_lines(multiline) == prefix + "𝑎\n" + prefix + "𝑏"


FRACTION_CASES = [
    (r"\frac{a}{b}", " 𝑎\n╶─╴\n 𝑏", " 𝑎 𝑎\n╶─╴𝑏\n 𝑏"),
    (r"\tfrac{a}{b}", " 𝑎\n╶─╴\n 𝑏", " 𝑎 𝑎\n╶─╴𝑏\n 𝑏"),
    (r"\dfrac{a}{b}", " 𝑎\n╶─╴\n 𝑏", " 𝑎 𝑎\n╶─╴𝑏\n 𝑏"),
    (r"\cfrac{a}{1 + \cfrac{1}{b}}",
     "   𝑎\n╶─────╴\n    1\n 1+╶─╴\n    𝑏",
     "   𝑎   𝑎\n╶─────╴𝑏\n    1\n 1+╶─╴\n    𝑏"),
    (r"\binom{n}{k}", "⎛𝑛⎞\n⎜ ⎟\n⎝𝑘⎠", "⎛𝑛⎞𝑎\n⎜ ⎟𝑏\n⎝𝑘⎠"),
    (r"\dbinom{n}{k}", "⎛𝑛⎞\n⎜ ⎟\n⎝𝑘⎠", "⎛𝑛⎞𝑎\n⎜ ⎟𝑏\n⎝𝑘⎠"),
]


@pytest.mark.parametrize("tex,single_expected,multiline_expected",
                         FRACTION_CASES)
def test_fraction_and_binomial_commands_render_single_and_multiline(
        tex, single_expected, multiline_expected):
    assert render_lines(tex) == single_expected
    assert render_lines(tex + MULTILINE_BLOCK) == multiline_expected


@pytest.mark.parametrize(
    "tex,expected",
    [
        (r"\sqrt{x}", "√𝑥̅"),
        (r"\sqrt[3]{x}", "³√𝑥̅"),
    ],
)
def test_square_root_commands_render_single_characters(tex, expected):
    assert render_lines(tex) == expected


@pytest.mark.parametrize(
    "tex,expected",
    [
        (r"\sqrt{\begin{matrix}a \\ b\end{matrix}}",
         " ┌─╴\n │𝑎\n╰┘𝑏"),
        (r"\sqrt[3]{\begin{matrix}a \\ b\end{matrix}}",
         " ┌─╴\n₃│𝑎\n╰┘𝑏"),
    ],
)
def test_square_root_commands_render_multiline_blocks(tex, expected):
    assert render_lines(tex) == expected


ENVIRONMENT_CASES = [
    ("matrix", r"\begin{matrix}a\end{matrix}", "𝑎",
     r"\begin{matrix}a\\b\end{matrix}", "𝑎\n𝑏"),
    ("array", r"\begin{array}{c}a\end{array}", "𝑎",
     r"\begin{array}{c}a\\b\end{array}", "𝑎\n𝑏"),
    ("pmatrix", r"\begin{pmatrix}a\end{pmatrix}", "(𝑎)",
     r"\begin{pmatrix}a\\b\end{pmatrix}", "⎛𝑎⎞\n⎝𝑏⎠"),
    ("bmatrix", r"\begin{bmatrix}a\end{bmatrix}", "[𝑎]",
     r"\begin{bmatrix}a\\b\end{bmatrix}", "⎡𝑎⎤\n⎣𝑏⎦"),
    ("vmatrix", r"\begin{vmatrix}a\end{vmatrix}", "|𝑎|",
     r"\begin{vmatrix}a\\b\end{vmatrix}", "⎟𝑎⎟\n⎟𝑏⎟"),
    ("Vmatrix", r"\begin{Vmatrix}a\end{Vmatrix}", "‖𝑎‖",
     r"\begin{Vmatrix}a\\b\end{Vmatrix}", "║𝑎║\n║𝑏║"),
    ("Bmatrix", r"\begin{Bmatrix}a\end{Bmatrix}", "{𝑎}",
     r"\begin{Bmatrix}a\\b\end{Bmatrix}", "⎧𝑎⎫\n⎨ ⎬\n⎩𝑏⎭"),
    ("smallmatrix", r"\begin{smallmatrix}a\end{smallmatrix}", "𝑎",
     r"\begin{smallmatrix}a\\b\end{smallmatrix}", "𝑎\n𝑏"),
    ("cases", r"\begin{cases}a\end{cases}", "{𝑎",
     r"\begin{cases}a\\b\end{cases}", "⎧𝑎\n⎨\n⎩𝑏"),
    ("align", r"\begin{align}a\end{align}", "𝑎",
     r"\begin{align}a\\b\end{align}", "𝑎\n\n𝑏"),
    ("align*", r"\begin{align*}a\end{align*}", "𝑎",
     r"\begin{align*}a\\b\end{align*}", "𝑎\n\n𝑏"),
    ("gather", r"\begin{gather}a\end{gather}", "𝑎",
     r"\begin{gather}a\\b\end{gather}", "𝑎\n\n𝑏"),
    ("gather*", r"\begin{gather*}a\end{gather*}", "𝑎",
     r"\begin{gather*}a\\b\end{gather*}", "𝑎\n\n𝑏"),
    ("aligned", r"\begin{aligned}a\end{aligned}", "𝑎",
     r"\begin{aligned}a\\b\end{aligned}", "𝑎\n\n𝑏"),
    ("gathered", r"\begin{gathered}a\end{gathered}", "𝑎",
     r"\begin{gathered}a\\b\end{gathered}", "𝑎\n𝑏"),
    ("equation*", r"\begin{equation*}a\end{equation*}", "𝑎",
     r"\begin{equation*}a\\b\end{equation*}", "𝑎\n\n𝑏"),
]


@pytest.mark.parametrize(
    "name,single_tex,single_expected,multiline_tex,multiline_expected",
    ENVIRONMENT_CASES,
)
def test_supported_environments_render_single_and_multiline(
        name, single_tex, single_expected, multiline_tex, multiline_expected):
    assert render_lines(single_tex) == single_expected
    assert render_lines(multiline_tex) == multiline_expected


@pytest.mark.parametrize("command,expected_single,expected_multi", [
    ("mathrm", "a", "a\nb"),
    ("mathbf", "𝐚", "𝐚\n𝐛"),
    ("mathsf", "𝖺", "𝖺\n𝖻"),
    ("mathnormal", "𝑎", "𝑎\n𝑏"),
    ("mathit", "𝑎", "𝑎\n𝑏"),
    ("mathtt", "𝚊", "𝚊\n𝚋"),
    ("mathfrak", "𝖆", "𝖆\n𝖇"),
    ("mathcal", "𝓪", "𝓪\n𝓫"),
    ("mathbb", "𝕒", "𝕒\n𝕓"),
    ("mathscr", "𝓪", "𝓪\n𝓫"),
])
def test_supported_font_commands_render_single_and_multiline(
        command, expected_single, expected_multi):
    assert render_lines(rf"\{command}{{a}}") == expected_single
    assert render_lines(
        rf"\{command}{{\substack{{a \\ b}}}}"
    ) == expected_multi


@pytest.mark.parametrize("command,combining", [
    ("cancel", "̸"), ("bcancel", "⃥"), ("xcancel", "̸⃥"),
    ("sout", "̶"), ("angl", "⃧"),
])
def test_annotation_accents_render_single_and_multiline(command, combining):
    assert render_tex(
        rf"\{command}{{x}}", False, False, "raw", {"fonts": "serif"}
    ) == "𝑥" + combining
    assert render_lines(rf"\{command}{{{MULTILINE_BLOCK}}}") == (
        "𝑎" + combining + "\n𝑏"
    )


def test_xcancel_checklist_example_renders_all_characters():
    assert render_tex(
        r"\xcancel{ABC}", False, False, "raw", {"fonts": "serif"}
    ) == "𝐴𝐵̸⃥𝐶"


def test_sout_inside_text_renders():
    assert render_tex(
        r"\text{\sout{abc}}", False, False, "raw", {"fonts": "serif"}
    ) == "ab̶c"


@pytest.mark.parametrize("command,expected", [
    ("overbrace", "╭─┴─╮\n𝑎+𝑏+𝑐ⁿᵒᵗᵉ"),
    ("underbrace", "𝑎+𝑏+𝑐ₙₒₜₑ\n╰─┬─╯"),
    ("overbracket", "┌───┐\n𝑎+𝑏+𝑐ⁿᵒᵗᵉ"),
    ("underbracket", "𝑎+𝑏+𝑐ₙₒₜₑ\n└───┘"),
])
def test_annotation_stretchy_accents_support_scripts(command, expected):
    if command.startswith("under"):
        tex = rf"\{command}{{a+b+c}}_{{\text{{note}}}}"
    else:
        tex = rf"\{command}{{a+b+c}}^{{\text{{note}}}}"
    assert render_lines(tex) == expected


def test_annotation_stretchy_accents_support_multiline_blocks():
    assert render_lines(
        rf"\overbrace{{{MULTILINE_BLOCK}}}^{{\text{{n}}}}"
    ) == "⏞ⁿ\n𝑎\n𝑏"
    assert render_lines(
        rf"\underbrace{{{MULTILINE_BLOCK}}}_{{\text{{n}}}}"
    ) == "𝑎\n𝑏\n⏟ₙ"


@pytest.mark.parametrize("glyph", ["=", "<", ">"])
def test_raw_relations_render_single_and_multiline(glyph):
    assert render_tex(
        glyph + "a", False, False, "raw", {"fonts": "serif"}
    ) == glyph + "𝑎"
    assert render_lines(glyph + MULTILINE_BLOCK) == (
        " 𝑎\n" + glyph + "𝑏"
    )


def test_operatorname_renders_single_and_multiline():
    assert render_lines(r"\operatorname{f}") == "f"
    assert render_lines(
        r"\operatorname{f}" + MULTILINE_BLOCK
    ) == " 𝑎\nf𝑏"


def test_newline_command_renders_single_and_multiline():
    assert render_lines(r"a\newline b") == "𝑎\n\n𝑏"
    assert render_lines(r"a\newline b\newline c") == "𝑎\n\n𝑏\n\n𝑐"


@pytest.mark.parametrize("tex,expected", [(r"x_n", "𝑥ₙ"), (r"e^x", "𝑒ˣ")])
def test_basic_vertical_scripts_render(tex, expected):
    assert render_lines(tex) == expected


def test_prime_script_renders_single_and_multiline():
    assert render_lines(r"a^{\prime}") == " ′\n𝑎"
    assert render_lines(r"a^{\prime}" + MULTILINE_BLOCK) == (
        " ′𝑎\n𝑎 𝑏"
    )


def test_scripts_without_a_base_render():
    assert render_lines(r"_u^o") == "ᵤᵒ"
    assert render_lines(r"_u^o" + MULTILINE_BLOCK) == "  𝑎\nᵤᵒ𝑏"


def test_substack_sum_renders_single_and_multiline():
    expression = r"\sum_{\substack{0<i<m\\0<j<n}}"
    expected = " ┰─╴\n ▐╸\n ┸─╴\n0<𝑖<𝑚\n0<𝑗<𝑛"
    assert render_lines(expression) == expected
    assert render_lines(expression + MULTILINE_BLOCK) == (
        " ┰─╴ 𝑎\n ▐╸  𝑏\n ┸─╴\n"
        "0<𝑖<𝑚\n0<𝑗<𝑛"
    )


def test_dollar_math_environment_renders_single_and_multiline():
    assert render_lines(r"$a$") == "𝑎"
    assert render_lines(r"$" + MULTILINE_BLOCK + r"$") == "𝑎\n𝑏"


def test_grouped_expression_renders_single_and_multiline():
    expression = r"{F=ma}"
    expected = "𝐹=𝑚𝑎"
    assert render_lines(expression) == expected
    assert render_lines(expression + MULTILINE_BLOCK) == (
        " " * len(expected) + "𝑎\n" + expected + "𝑏"
    )


def test_limits_modifier_renders_on_an_operator():
    expression = r"\lim\limits_x"
    assert render_lines(expression) == "lim\n ˣ"
    assert render_lines(expression + MULTILINE_BLOCK) == (
        "   𝑎\nlim𝑏\n ˣ"
    )


def test_text_font_command_renders_single_and_multiline_composition():
    assert render_lines(r"\text{Ab0}") == "Ab0"
    assert render_lines(r"\text{Ab0}" + MULTILINE_BLOCK) == (
        "   𝑎\nAb0𝑏"
    )


def test_nested_supported_fonts_render():
    assert render_lines(r"\mathsf{\mathbf{H}}") == "𝖧"
    assert render_lines(
        r"\mathsf{\mathbf{\substack{H \\ H}}}"
    ) == "𝖧\n𝖧"


def test_superscript_expression_renders():
    assert render_lines(r"A^{2+3}") == "𝐴²⁺³"
