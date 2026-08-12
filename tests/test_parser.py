from texicode.lexer import lexer
from texicode.parser import parse


def parsed(tex):
    return parse(lexer(tex, False), False)


def types_of(nodes, node_ids):
    return [nodes[i][0] for i in node_ids]


def test_align_rows_are_children_of_env():
    nodes = parsed(r"\begin{align*} a &= b \\ c &= d \end{align*}")
    root = nodes[0]
    assert types_of(nodes, root[2]) == ["cmd_bgin"]

    env = nodes[root[2][0]]
    assert env[1] == ("env_bgin", "align*")
    assert types_of(nodes, env[2]) == [
        "txt_leaf", "txt_leaf", "txt_leaf", "txt_leaf",
        "cmd_lbrk",
    ]
    assert [nodes[i][1] for i in env[2][:4]] == [
        ("alph", "a"), ("symb", "&"), ("symb", "="), ("alph", "b"),
    ]

    row2 = nodes[env[2][4]]
    assert [nodes[i][1] for i in row2[2]] == [
        ("alph", "c"), ("symb", "&"), ("symb", "="), ("alph", "d"),
    ]


def test_trailing_row_break_parses():
    nodes = parsed(r"\begin{equation*} f(x) \\ \end{equation*}")
    env = nodes[nodes[0][2][0]]
    assert types_of(nodes, env[2]) == [
        "txt_leaf", "txt_leaf", "txt_leaf", "txt_leaf", "cmd_lbrk",
    ]
    assert nodes[env[2][-1]][2] == []


def test_matrix_rows_keep_ampersands():
    nodes = parsed(r"\begin{matrix} a & b \\ c & d \end{matrix}")
    env = nodes[nodes[0][2][0]]
    assert env[1] == ("env_bgin", "matrix")
    assert types_of(nodes, env[2]) == [
        "txt_leaf", "txt_leaf", "txt_leaf", "cmd_lbrk",
    ]
    assert nodes[env[2][1]][1] == ("symb", "&")

    row2 = nodes[env[2][3]]
    assert types_of(nodes, row2[2]) == [
        "txt_leaf", "txt_leaf", "txt_leaf",
    ]
    assert nodes[row2[2][1]][1] == ("symb", "&")
