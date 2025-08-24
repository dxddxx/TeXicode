node_type_parent_dependent_dict = {
    ("cmd_sqrt",  ("symb", "[")):  "opn_degr",
    ("opn_degr",  ("symb", "]")):  "cls_degr",
    ("cmd_sbstk", ("symb", "{")):  "opn_stkln",
    ("opn_stkln", ("symb", "}")):  "cls_stkln",
    ("stk_lbrk",  ("symb", "}")):  "cls_stkln",
    ("opn_stkln", ("cmnd", "\\")): "stk_lbrk",
    ("stk_lbrk",  ("cmnd", "\\")): "stk_lbrk",
    ("opn_stkln", ("cmnd", "newline")): "stk_lbrk",
    ("stk_lbrk",  ("cmnd", "newline")): "stk_lbrk",
    ("opn_dllr",  ("symb", "$")):  "cls_dllr",
    ("opn_ddlr",  ("symb", "$$")): "cls_ddlr",
    ("cmd_lbrk",  ("symb", "$")):  "cls_dllr",
    ("cmd_lbrk",  ("symb", "$$")): "cls_ddlr",
}

node_type_dict = {
    ("meta",     "start"): "opn_root", ("meta",     "end"): "cls_root",
    ("meta", "startline"): "opn_line", ("meta", "endline"): "cls_line",
    ("symb",         "^"): "sup_scrpt", ("symb",      "_"): "sub_scrpt",
    ("symb", "$"): "opn_dllr",  ("symb",  "$$"): "opn_ddlr",
    ("cmnd", "["): "opn_brak",  ("cmnd",  "]"): "cls_brak",
    ("cmnd", "("): "opn_pren",  ("cmnd",  ")"): "cls_pren",
    ("symb", "{"): "opn_brac",  ("symb",  "}"): "cls_brac",

    ("cmnd",  "left"): "opn_dlim", ("cmnd", "right"): "cls_dlim",
    ("cmnd",  "bigl"): "big_dlim", ("cmnd",   "big"): "big_dlim",
    ("cmnd",  "bigr"): "big_dlim", ("cmnd",  "Bigl"): "big_dlim",
    ("cmnd",   "Big"): "big_dlim", ("cmnd",  "Bigr"): "big_dlim",
    ("cmnd", "biggl"): "big_dlim", ("cmnd",  "bigg"): "big_dlim",
    ("cmnd", "biggr"): "big_dlim", ("cmnd", "Biggl"): "big_dlim",
    ("cmnd",  "Bigg"): "big_dlim", ("cmnd", "Biggr"): "big_dlim",

    ("cmnd",  "sqrt"): "cmd_sqrt",

    ("cmnd",  "frac"): "cmd_frac", ("cmnd", "tfrac"): "cmd_frac",
    ("cmnd", "dfrac"): "cmd_frac", ("cmnd", "cfrac"): "cmd_frac",

    ("cmnd",   "sum"): "ctr_base", ("cmnd", "prod"): "ctr_base",
    ("cmnd",   "lim"): "ctr_base",

    ("cmnd", "binom"): "cmd_binom", ("cmnd", "dbinom"): "cmd_binom",

    ("cmnd",  "limits"): "cmd_lmts", ("cmnd",     "acute"): "cmd_acnt",
    ("cmnd",     "bar"): "cmd_acnt", ("cmnd",     "breve"): "cmd_acnt",
    ("cmnd",   "check"): "cmd_acnt", ("cmnd",      "ddot"): "cmd_acnt",
    ("cmnd",     "dot"): "cmd_acnt", ("cmnd",     "grave"): "cmd_acnt",
    ("cmnd",     "hat"): "cmd_acnt", ("cmnd",  "mathring"): "cmd_acnt",
    ("cmnd",   "tilde"): "cmd_acnt", ("cmnd",       "vec"): "cmd_acnt",
    ("cmnd", "widehat"): "cmd_acnt", ("cmnd", "widetilde"): "cmd_acnt",

    ("cmnd",  "mathrm"): "cmd_font", ("cmnd",     "mathbf"): "cmd_font",
    ("cmnd",  "mathsf"): "cmd_font", ("cmnd",     "mathtt"): "cmd_font",
    ("cmnd",  "mathit"): "cmd_font", ("cmnd", "mathnormal"): "cmd_font",
    ("cmnd", "mathcal"): "cmd_font", ("cmnd",   "mathfrak"): "cmd_font",
    ("cmnd",  "mathbb"): "cmd_font", ("cmnd",       "text"): "cmd_font",
    ("cmnd", "mathscr"): "cmd_font",

    ("cmnd", "\\"): "cmd_lbrk",
    ("cmnd",  "newline"): "cmd_lbrk",
    ("cmnd", "substack"): "cmd_sbstk",

}


def get_node_type(token: tuple, parent_type: str) -> str:
    if (parent_type, token) in node_type_parent_dependent_dict.keys():
        return node_type_parent_dependent_dict[(parent_type, token)]
    elif token in node_type_dict.keys():
        return node_type_dict[token]
    elif token[0] in ("symb", "alph", "numb"):
        return "txt_leaf"
    elif token[0] == "cmnd":
        return "cmd_leaf"
    else:
        raise ValueError(f"Unknown token {token}")
        return token[0]  # token type


def get_script_base(node_type, nodes: list, parent_stack: list) -> int:
    script_types = {"sup_scrpt", "sub_scrpt", "top_scrpt", "btm_scrpt"}
    if not (bool(parent_stack) and node_type in script_types):
        return -1
    base_id = -1
    sibling_list = nodes[parent_stack[-1]][2]
    if len(sibling_list) >= 1:
        base_id = sibling_list[-1]
    else:
        return base_id
    if nodes[base_id][0] in script_types:
        if len(sibling_list) >= 2:
            base_id = sibling_list[-2]
        else:
            base_id = -1
    return base_id


def update_node_type(base_node_type: str, script_node_type) -> str:
    if base_node_type == "ctr_base":
        return {"sup_scrpt": "top_scrpt",
                "sub_scrpt": "btm_scrpt",
                "cmd_lmts": "cmd_lmts"}[script_node_type]
    else:
        return script_node_type


# parent_node_info( ("only/only_not", popable_by["node_type"])
#                   (add_amount)
#                   (can_add, "err if/if_not", under[])
#                   (can_be_children, can_break_parent, can_double_pop)
# ) can double pop is a bit of a hack for cls_stkln
node_type_info = {
    "opn_root":  ((True,  ["cls_root"
                           ]), (1,), (True,  True, []), (False, False, False)),
    "opn_brac":  ((True,  ["cls_brac"
                           ]), (1,), (True,  True,  []), (True, False, False)),
    "opn_degr":  ((True,  ["cls_degr"
                           ]), (1,), (True,  True,  []), (True, False, False)),
    "opn_dlim":  ((True,  ["cls_dlim"
                           ]), (1,), (True,  True,  []), (True, False, False)),
    "cmd_sqrt":  ((False, ["opn_degr"
                           ]), (1,), (True,  True,  []), (True, False, False)),
    "cmd_frac":  ((False, []), (2,), (True,  True,  []), (True, False, False)),
    "cmd_binom": ((False, []), (2,), (True,  True,  []), (True, False, False)),
    "big_dlim":  ((False, []), (1,), (True,  True,  []), (True, False, False)),
    "sup_scrpt": ((False, []), (1,), (True,  True,  []), (True, False, False)),
    "sub_scrpt": ((False, []), (1,), (True,  True,  []), (True, False, False)),
    "top_scrpt": ((False, []), (1,), (True,  True,  []), (True, False, False)),
    "btm_scrpt": ((False, []), (1,), (True,  True,  []), (True, False, False)),
    "cls_dlim":  ((False, []), (1,), (True,  True,  []), (True, False, False)),
    "cmd_acnt":  ((False, []), (1,), (True,  True,  []), (True, False, False)),
    "cmd_font":  ((False, []), (1,), (True,  True,  []), (True, False, False)),
    "cmd_lmts":  ((True,  []), (0,), (True,  True,  []), (True, False, False)),
    "ctr_base":  ((True,  []), (0,), (True,  True,  []), (True, False, False)),
    "txt_leaf":  ((True,  []), (0,), (True,  True,  []), (True, False, False)),
    "cmd_leaf":  ((True,  []), (0,), (True,  True,  []), (True, False, False)),
    "cls_root":  ((True, []), (0,), (False, False, ["opn_root"
                                                    ]), (False, False, False)),
    "cls_brac":  ((True, []), (0,), (False, False, ["opn_brac"
                                                    ]), (False, False, False)),
    "cls_degr":  ((True, []), (0,), (False, False, ["opn_degr"
                                                    ]), (False, False, False)),
    "cls_line":  ((True, []), (0,), (False, False, ["opn_line", "cmd_lbrk"
                                                    ]), (False, False, False)),
    "cls_brak":  ((True, []), (0,), (False, False, ["opn_brak", "cmd_lbrk"
                                                    ]), (False, False, False)),
    "cls_pren":  ((True, []), (0,), (False, False, ["opn_pren", "cmd_lbrk"
                                                    ]), (False, False, False)),
    "cls_dllr":  ((True, []), (0,), (False, False, ["opn_dllr", "cmd_lbrk"
                                                    ]), (False, False, False)),
    "cls_ddlr":  ((True, []), (0,), (False, False, ["opn_ddlr", "cmd_lbrk"
                                                    ]), (False, False, False)),
    "cls_stkln": ((True, []), (0,), (False, False, ["opn_stkln", "stk_lbrk"
                                                    ]), (False, True,  True)),
    "opn_line":  ((True, ["cls_line", "cmd_lbrk"
                          ]), (1,), (True,  True,  []), (True,  False, False)),
    "opn_brak":  ((True, ["cls_brak", "cmd_lbrk"
                          ]), (1,), (True,  True,  []), (True,  False, False)),
    "opn_pren":  ((True, ["cls_pren", "cmd_lbrk"
                          ]), (1,), (True,  True,  []), (True,  False, False)),
    "opn_dllr":  ((True, ["cls_dllr", "cmd_lbrk"
                          ]), (1,), (True,  True,  []), (True,  False, False)),
    "opn_ddlr":  ((True, ["cls_ddlr", "cmd_lbrk"
                          ]), (1,), (True,  True,  []), (True,  False, False)),
    "stk_lbrk":  ((True, ["cls_stkln", "stk_lbrk"
                          ]), (1,), (True,  False, ["opn_stkln", "stk_lbrk"
                                                    ]), (True,  True,  False)),
    "opn_stkln": ((True, ["cls_stkln", "stk_lbrk"
                          ]), (1,), (True,  False, ["cmd_sbstk"
                                                    ]), (True,  False, False)),
    "cmd_sbstk": ((True, ["cls_stkln"
                          ]), (1,), (True,  True,  []), (True,  False, False)),
    "cmd_lbrk":  ((True, ["cmd_lbrk", "cls_line", "cls_brak", "cls_pren",
                          "cls_dllr", "cls_ddlr"
                          ]), (1,), (True,  False, ["cmd_lbrk", "opn_line",
                                                    "opn_brak", "opn_pren",
                                                    "opn_dllr", "opn_ddlr"
                                                    ]), (True,  True,  False)),
}


def can_pop(parent_node_type: str, node_type: str) -> bool:
    if parent_node_type == "none":
        return False
    pop_info = node_type_info[parent_node_type][0]
    if pop_info[0]:
        if node_type in pop_info[1]:
            return True
    else:
        if node_type not in pop_info[1]:
            return True
    return False


def parent_stack_add(node_type: str, node_id: int) -> list:
    add_stack = []
    parent_stack_add_info = node_type_info[node_type][1]
    add_len = parent_stack_add_info[0]
    for i in range(add_len):
        add_stack.append(node_id)
    return add_stack


def can_add(parent_type: str, node_type: str) -> bool:
    if parent_type == "none":
        if node_type == "opn_root":
            return True
        return False
    add_info = node_type_info[node_type][2]
    can_add = add_info[0]
    if add_info[1]:
        if parent_type in add_info[2]:
            raise ValueError(f"Extra {node_type}, under {add_info[2]}")
    else:
        if parent_type not in add_info[2]:
            expected = node_type_info[parent_type][0][1]
            raise ValueError(f"Expected {expected}, got {node_type}")
    return can_add


def parse(tokens: list, debug: bool) -> list:
    if debug:
        print("Parsing")
    nodes = []
    parent_stack = []
    node_id = 0
    for i in range(len(tokens)):
        token = tokens[i]
        parent_type = "none"
        if parent_stack:
            parent_id = parent_stack[-1]
            parent_type = nodes[parent_id][0]
        node_type = get_node_type(token, parent_type)
        can_add_to_nodes = can_add(parent_type, node_type)
        can_pop_parent = can_pop(parent_type, node_type)
        can_add_to_children_list = node_type_info[node_type][3][0]
        can_update_parent_id = node_type_info[node_type][3][1]
        can_double_pop = node_type_info[node_type][3][2]
        base_id = get_script_base(node_type, nodes, parent_stack)

        if base_id != -1:
            base_node = nodes[base_id]
            node_type = update_node_type(base_node[0], node_type)
            base_node[3].append(node_id)
            can_add_to_children_list = False
            can_pop_parent = False
        if can_pop_parent:
            parent_stack.pop()
        if can_update_parent_id:
            parent_id = parent_stack[-1]
            parent_type = nodes[parent_id][0]
        # double pop is only true for cls_sbstk
        if can_double_pop:
            parent_stack.pop()
            parent_id = parent_stack[-1]
            parent_type = nodes[parent_id][0]
        if can_add_to_children_list:
            nodes[parent_id][2].append(node_id)
        parent_stack += parent_stack_add(node_type, node_id)
        if can_add_to_nodes:
            node = (node_type, token, [], [])
            nodes.append(node)
            node_id += 1
        if debug:
            print(i, token, node_type, node, parent_type, parent_stack)
    if debug:
        for i in range(len(nodes)):
            print(i, nodes[i])
    return nodes
