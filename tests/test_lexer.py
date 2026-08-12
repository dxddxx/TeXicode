import pytest

from texicode.lexer import lexer


TOKEN_CASES = [
    ("", []),
    ("   ", []),
    (
        "  a  b",
        [
            ("meta", "start"), ("meta", "startline"),
            ("alph", "a"), ("symb", " "), ("alph", "b"),
            ("meta", "endline"), ("meta", "end"),
        ],
    ),
    (
        "a b",
        [
            ("meta", "start"), ("meta", "startline"),
            ("alph", "a"), ("symb", " "), ("alph", "b"),
            ("meta", "endline"), ("meta", "end"),
        ],
    ),
    (
        "a  b",
        [
            ("meta", "start"), ("meta", "startline"),
            ("alph", "a"), ("symb", " "), ("alph", "b"),
            ("meta", "endline"), ("meta", "end"),
        ],
    ),
    (
        " a",
        [
            ("meta", "start"), ("meta", "startline"),
            ("alph", "a"),
            ("meta", "endline"), ("meta", "end"),
        ],
    ),
    (
        "abc",
        [
            ("meta", "start"), ("meta", "startline"),
            ("alph", "a"), ("alph", "b"), ("alph", "c"),
            ("meta", "endline"), ("meta", "end"),
        ],
    ),
    (
        "123",
        [
            ("meta", "start"), ("meta", "startline"),
            ("numb", "1"), ("numb", "2"), ("numb", "3"),
            ("meta", "endline"), ("meta", "end"),
        ],
    ),
    (
        "+-*/",
        [
            ("meta", "start"), ("meta", "startline"),
            ("symb", "+"), ("symb", "-"), ("symb", "*"), ("symb", "/"),
            ("meta", "endline"), ("meta", "end"),
        ],
    ),
    (
        "x=1",
        [
            ("meta", "start"), ("meta", "startline"),
            ("alph", "x"), ("symb", "="), ("numb", "1"),
            ("meta", "endline"), ("meta", "end"),
        ],
    ),
    (
        "α+β",
        [
            ("meta", "start"), ("meta", "startline"),
            ("alph", "α"), ("symb", "+"), ("alph", "β"),
            ("meta", "endline"), ("meta", "end"),
        ],
    ),
    (
        r"\alpha",
        [
            ("meta", "start"), ("meta", "startline"),
            ("cmnd", "alpha"),
            ("meta", "endline"), ("meta", "end"),
        ],
    ),
    (
        r"\frac12",
        [
            ("meta", "start"), ("meta", "startline"),
            ("cmnd", "frac"), ("numb", "1"), ("numb", "2"),
            ("meta", "endline"), ("meta", "end"),
        ],
    ),
    (
        r"\{",
        [
            ("meta", "start"), ("meta", "startline"),
            ("cmnd", "{"),
            ("meta", "endline"), ("meta", "end"),
        ],
    ),
    (
        r"\}",
        [
            ("meta", "start"), ("meta", "startline"),
            ("cmnd", "}"),
            ("meta", "endline"), ("meta", "end"),
        ],
    ),
    (
        r"\!",
        [
            ("meta", "start"), ("meta", "startline"),
            ("cmnd", "!"),
            ("meta", "endline"), ("meta", "end"),
        ],
    ),
    (
        r"\ ",
        [
            ("meta", "start"), ("meta", "startline"),
            ("cmnd", " "),
            ("meta", "endline"), ("meta", "end"),
        ],
    ),
    (
        r"\\",
        [
            ("meta", "start"), ("meta", "startline"),
            ("cmnd", "\\"),
            ("meta", "endline"), ("meta", "end"),
        ],
    ),
    (
        r"\alpha\ge \beta",
        [
            ("meta", "start"), ("meta", "startline"),
            ("cmnd", "alpha"), ("cmnd", "ge"),
            ("symb", " "), ("cmnd", "beta"),
            ("meta", "endline"), ("meta", "end"),
        ],
    ),
    (
        r"\a1b",
        [
            ("meta", "start"), ("meta", "startline"),
            ("cmnd", "a"), ("numb", "1"), ("alph", "b"),
            ("meta", "endline"), ("meta", "end"),
        ],
    ),
    (
        r"\12",
        [
            ("meta", "start"), ("meta", "startline"),
            ("cmnd", "12"),
            ("meta", "endline"), ("meta", "end"),
        ],
    ),
    (
        r"\sqrt2",
        [
            ("meta", "start"), ("meta", "startline"),
            ("cmnd", "sqrt"), ("numb", "2"),
            ("meta", "endline"), ("meta", "end"),
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
            ("meta", "start"), ("meta", "startline"),
            ("alph", "a"), ("symb", "$"), ("alph", "b"),
            ("meta", "endline"), ("meta", "end"),
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
            ("meta", "start"), ("meta", "startline"),
            ("alph", "x"), ("symb", "%"), ("alph", "y"),
            ("meta", "endline"), ("meta", "end"),
        ],
    ),
    (
        r"\begin{align*} a &= b",
        [
            ("meta", "start"),
            ("cmnd", "begin"), ("symb", "{"),
            ("alph", "a"), ("alph", "l"), ("alph", "i"),
            ("alph", "g"), ("alph", "n"), ("symb", "*"),
            ("symb", "}"),
            ("symb", " "), ("alph", "a"),
            ("symb", " "), ("symb", "&"), ("symb", "="),
            ("symb", " "), ("alph", "b"),
            ("meta", "end"),
        ],
    ),
    (
        "x",
        [
            ("meta", "start"), ("meta", "startline"),
            ("alph", "x"),
            ("meta", "endline"), ("meta", "end"),
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
            ("cmnd", "begin"), ("symb", "{"),
            ("alph", "a"), ("alph", "l"), ("alph", "i"),
            ("alph", "g"), ("alph", "n"), ("symb", "}"),
            ("symb", " "), ("alph", "x"),
            ("symb", " "), ("cmnd", "end"), ("symb", "{"),
            ("alph", "a"), ("alph", "l"), ("alph", "i"),
            ("alph", "g"), ("alph", "n"), ("symb", "}"),
            ("meta", "end"),
        ],
    ),
    (
        "[x]",
        [
            ("meta", "start"), ("meta", "startline"),
            ("symb", "["), ("alph", "x"), ("symb", "]"),
            ("meta", "endline"), ("meta", "end"),
        ],
    ),
    (
        "a\nb",
        [
            ("meta", "start"), ("meta", "startline"),
            ("alph", "a"), ("symb", " "), ("alph", "b"),
            ("meta", "endline"), ("meta", "end"),
        ],
    ),
    (
        r"\text{ a  b }",
        [
            ("meta", "start"), ("meta", "startline"),
            ("cmnd", "text"), ("symb", "{"),
            ("symb", " "), ("alph", "a"),
            ("symb", " "), ("alph", "b"),
            ("symb", " "), ("symb", "}"),
            ("meta", "endline"), ("meta", "end"),
        ],
    ),
    (
        r"\begin x",
        [
            ("meta", "start"),
            ("cmnd", "begin"), ("symb", " "), ("alph", "x"),
            ("meta", "end"),
        ],
    ),
    (
        "©",
        [
            ("meta", "start"), ("meta", "startline"),
            (None, "©"),
            ("meta", "endline"), ("meta", "end"),
        ],
    ),
]


@pytest.mark.parametrize("tex,expected", TOKEN_CASES)
def test_lexer_tokens(tex, expected):
    assert lexer(tex, False) == expected


def test_trailing_backslash_raises():
    with pytest.raises(ValueError, match=r"Unexpected character \\"):
        lexer("x\\", False)
