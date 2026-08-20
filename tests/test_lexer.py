import pytest

from texicode.lexer import lexer


TOKEN_CASES = [
    ("", []),
    ("   ", []),
    (
        "  a  b",
        [
            ("meta", "start"),
            ("alph", "a"), ("symb", " "), ("alph", "b"),
            ("meta", "end"),
        ],
    ),
    (
        "a b",
        [
            ("meta", "start"),
            ("alph", "a"), ("symb", " "), ("alph", "b"),
            ("meta", "end"),
        ],
    ),
    (
        "a  b",
        [
            ("meta", "start"),
            ("alph", "a"), ("symb", " "), ("alph", "b"),
            ("meta", "end"),
        ],
    ),
    (
        " a",
        [
            ("meta", "start"),
            ("alph", "a"),
            ("meta", "end"),
        ],
    ),
    (
        "abc",
        [
            ("meta", "start"),
            ("alph", "a"), ("alph", "b"), ("alph", "c"),
            ("meta", "end"),
        ],
    ),
    (
        "123",
        [
            ("meta", "start"),
            ("numb", "1"), ("numb", "2"), ("numb", "3"),
            ("meta", "end"),
        ],
    ),
    (
        "+-*/",
        [
            ("meta", "start"),
            ("symb", "+"), ("symb", "-"), ("symb", "*"), ("symb", "/"),
            ("meta", "end"),
        ],
    ),
    (
        "x=1",
        [
            ("meta", "start"),
            ("alph", "x"), ("symb", "="), ("numb", "1"),
            ("meta", "end"),
        ],
    ),
    (
        "α+β",
        [
            ("meta", "start"),
            ("alph", "α"), ("symb", "+"), ("alph", "β"),
            ("meta", "end"),
        ],
    ),
    (
        r"\alpha",
        [
            ("meta", "start"),
            ("cmnd", "alpha"),
            ("meta", "end"),
        ],
    ),
    (
        r"\frac12",
        [
            ("meta", "start"),
            ("cmnd", "frac"), ("numb", "1"), ("numb", "2"),
            ("meta", "end"),
        ],
    ),
    (
        r"\{",
        [
            ("meta", "start"),
            ("cmnd", "{"),
            ("meta", "end"),
        ],
    ),
    (
        r"\}",
        [
            ("meta", "start"),
            ("cmnd", "}"),
            ("meta", "end"),
        ],
    ),
    (
        r"\!",
        [
            ("meta", "start"),
            ("cmnd", "!"),
            ("meta", "end"),
        ],
    ),
    (
        r"\ ",
        [
            ("meta", "start"),
            ("cmnd", " "),
            ("meta", "end"),
        ],
    ),
    (
        r"\\",
        [
            ("meta", "start"),
            ("cmnd", "\\"),
            ("meta", "end"),
        ],
    ),
    (
        r"\alpha\ge \beta",
        [
            ("meta", "start"),
            ("cmnd", "alpha"), ("cmnd", "ge"),
            ("symb", " "), ("cmnd", "beta"),
            ("meta", "end"),
        ],
    ),
    (
        r"\a1b",
        [
            ("meta", "start"),
            ("cmnd", "a"), ("numb", "1"), ("alph", "b"),
            ("meta", "end"),
        ],
    ),
    (
        r"\12",
        [
            ("meta", "start"),
            ("cmnd", "12"),
            ("meta", "end"),
        ],
    ),
    (
        r"\sqrt2",
        [
            ("meta", "start"),
            ("cmnd", "sqrt"), ("numb", "2"),
            ("meta", "end"),
        ],
    ),
    (
        "$x$",
        [
            ("meta", "start"),
            ("symb", "$"), ("alph", "x"), ("symb", "$"),
            ("meta", "end"),
        ],
    ),
    (
        "$$x$$",
        [
            ("meta", "start"),
            ("symb", "$$"), ("alph", "x"), ("symb", "$$"),
            ("meta", "end"),
        ],
    ),
    (
        "$$$",
        [
            ("meta", "start"),
            ("symb", "$$"), ("symb", "$"),
            ("meta", "end"),
        ],
    ),
    (
        "a$b",
        [
            ("meta", "start"),
            ("alph", "a"), ("symb", "$"), ("alph", "b"),
            ("meta", "end"),
        ],
    ),
    (
        "$",
        [
            ("meta", "start"),
            ("symb", "$"),
            ("meta", "end"),
        ],
    ),
    (
        "x%y",
        [
            ("meta", "start"),
            ("alph", "x"), ("symb", "%"), ("alph", "y"),
            ("meta", "end"),
        ],
    ),
    (
        r"\begin{align*} a &= b",
        [
            ("meta", "start"),
            ("env_bgin", "align*"),
            ("symb", " "), ("alph", "a"),
            ("symb", " "), ("symb", "&"), ("symb", "="),
            ("symb", " "), ("alph", "b"),
            ("meta", "end"),
        ],
    ),
    (
        r"\begin{matrix} a & b \\ c & d \end{matrix}",
        [
            ("meta", "start"),
            ("env_bgin", "matrix"),
            ("symb", " "), ("alph", "a"),
            ("symb", " "), ("symb", "&"),
            ("symb", " "), ("alph", "b"),
            ("symb", " "), ("cmnd", "\\"),
            ("symb", " "), ("alph", "c"),
            ("symb", " "), ("symb", "&"),
            ("symb", " "), ("alph", "d"),
            ("symb", " "), ("env_end", "matrix"),
            ("meta", "end"),
        ],
    ),
    (
        r"\begin{array}{cc} 1 & 2 \end{array}",
        [
            ("meta", "start"),
            ("env_bgin", "array"),
            ("symb", "{"), ("alph", "c"), ("alph", "c"),
            ("symb", "}"),
            ("symb", " "), ("numb", "1"),
            ("symb", " "), ("symb", "&"),
            ("symb", " "), ("numb", "2"),
            ("symb", " "), ("env_end", "array"),
            ("meta", "end"),
        ],
    ),
    (
        r"\begin {matrix}",
        [
            ("meta", "start"),
            ("env_bgin", "matrix"),
            ("meta", "end"),
        ],
    ),
    (
        "x",
        [
            ("meta", "start"),
            ("alph", "x"),
            ("meta", "end"),
        ],
    ),
    (
        r"\[x\]",
        [
            ("meta", "start"),
            ("cmnd", "["), ("alph", "x"), ("cmnd", "]"),
            ("meta", "end"),
        ],
    ),
    (
        r"\(x\)",
        [
            ("meta", "start"),
            ("cmnd", "("), ("alph", "x"), ("cmnd", ")"),
            ("meta", "end"),
        ],
    ),
    (
        r"\begin{align} x \end{align}",
        [
            ("meta", "start"),
            ("env_bgin", "align"),
            ("symb", " "), ("alph", "x"),
            ("symb", " "), ("env_end", "align"),
            ("meta", "end"),
        ],
    ),
    (
        "[x]",
        [
            ("meta", "start"),
            ("symb", "["), ("alph", "x"), ("symb", "]"),
            ("meta", "end"),
        ],
    ),
    (
        """a
b""",
        [
            ("meta", "start"),
            ("alph", "a"), ("symb", " "), ("alph", "b"),
            ("meta", "end"),
        ],
    ),
    (
        r"\text{ a  b }",
        [
            ("meta", "start"),
            ("cmnd", "text"), ("symb", "{"),
            ("symb", " "), ("alph", "a"),
            ("symb", " "), ("alph", "b"),
            ("symb", " "), ("symb", "}"),
            ("meta", "end"),
        ],
    ),
    (
        "©",
        [
            ("meta", "start"),
            (None, "©"),
            ("meta", "end"),
        ],
    ),
]


@pytest.mark.parametrize("tex,expected", TOKEN_CASES)
def test_lexer_tokens(tex, expected):
    assert lexer(tex, False) == expected


def test_trailing_backslash_raises():
    with pytest.raises(ValueError, match=r"Unexpected character \\"):
        lexer("x\\", False)


@pytest.mark.parametrize("tex", [r"\begin x", r"\begin", r"\end"])
def test_begin_end_require_brace(tex):
    with pytest.raises(ValueError, match=r"Expected \{ after \\"):
        lexer(tex, False)


def test_unclosed_begin_raises():
    with pytest.raises(ValueError, match=r"Unclosed \{ after \\begin"):
        lexer(r"\begin{matrix", False)
