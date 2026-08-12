from texicode.lexer import lexer
from texicode.parser import parse


def parsed(tex):
    return parse(lexer(tex, False), False)


def types_of(nodes, node_ids):
    return [nodes[i][0] for i in node_ids]


def test_align_children_are_flat():
    nodes = parsed(r"\begin{align*} a &= b \\ c &= d \end{align*}")
    root = nodes[0]
    assert types_of(nodes, root[2]) == ["cmd_bgin"]

    env = nodes[root[2][0]]
    assert env[1] == ("env_bgin", "align*")
    assert types_of(nodes, env[2]) == [
        "txt_leaf", "amp_sep", "txt_leaf", "txt_leaf",
        "row_sep",
        "txt_leaf", "amp_sep", "txt_leaf", "txt_leaf",
    ]
    assert [nodes[i][1] for i in env[2][:4]] == [
        ("alph", "a"), ("symb", "&"), ("symb", "="), ("alph", "b"),
    ]
    row_sep = nodes[env[2][4]]
    assert row_sep[1] == ("cmnd", "\\")
    assert row_sep[2] == []
    assert [nodes[i][1] for i in env[2][5:]] == [
        ("alph", "c"), ("symb", "&"), ("symb", "="), ("alph", "d"),
    ]


def test_trailing_row_break_is_flat_separator():
    nodes = parsed(r"\begin{equation*} f(x) \\ \end{equation*}")
    env = nodes[nodes[0][2][0]]
    assert types_of(nodes, env[2]) == [
        "txt_leaf", "txt_leaf", "txt_leaf", "txt_leaf", "row_sep",
    ]
    row_sep = nodes[env[2][-1]]
    assert row_sep[2] == []


def test_matrix_children_are_flat_with_ampersands():
    nodes = parsed(r"\begin{matrix} a & b \\ c & d \end{matrix}")
    env = nodes[nodes[0][2][0]]
    assert env[1] == ("env_bgin", "matrix")
    assert types_of(nodes, env[2]) == [
        "txt_leaf", "amp_sep", "txt_leaf", "row_sep",
        "txt_leaf", "amp_sep", "txt_leaf",
    ]
    assert nodes[env[2][1]][1] == ("symb", "&")
    assert nodes[env[2][3]][1] == ("cmnd", "\\")
    assert nodes[env[2][5]][1] == ("symb", "&")


def test_standalone_linebreak_still_uses_cmd_lbrk():
    nodes = parsed(r"\[ a \\ b \]")
    root = nodes[0]
    assert types_of(nodes, root[2]) == ["opn_brak", "cmd_lbrk"]
    lbrk = nodes[root[2][1]]
    assert types_of(nodes, lbrk[2]) == ["txt_leaf"]
