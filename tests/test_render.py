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
