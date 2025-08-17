node_type_parent_dependent_dict = {
    ("cmd_sqrt", ("symb", "[")): "opn_degr",
    ("opn_degr", ("symb", "]")): "cls_degr",
}

node_type_dict = {
    ("meta", "start"): "opn_root",
    ("meta",   "end"): "cls_root",
    ("symb",     "^"): "sup_scrpt",
    ("symb",     "_"): "sub_scrpt",
    ("symb",     "{"): "opn_brac",
    ("symb",     "}"): "cls_brac",
    ("cmnd",  "left"): "opn_dlim",
    ("cmnd", "right"): "cls_dlim",
    ("cmnd",  "sqrt"): "cmd_sqrt",
    ("cmnd",  "frac"): "cmd_frac",
    ("cmnd",   "sum"): "ctr_base",
    ("cmnd",  "prod"): "ctr_base",
    ("cmnd",   "lim"): "ctr_base",
    ("cmnd",   "limits"): "cmd_lmts",
    ("cmnd",     "iint"): "ctr_base",
    ("cmnd",    "iiint"): "ctr_base",
    ("cmnd",  "iiiiint"): "ctr_base",
    ("cmnd", "idotsint"): "ctr_base",
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
    if not (bool(parent_stack) and node_type in {"sup_scrpt", "sub_scrpt"}):
        return -1
    base_id = -1
    sibling_list = nodes[parent_stack[-1]][2]
    if len(sibling_list) >= 1:
        base_id = sibling_list[-1]
    if nodes[base_id][0] in {"sup_scrpt", "sub_scrpt"}:
        if len(sibling_list) >= 2:
            base_id = sibling_list[-2]
        else:
            base_id = -1
    return base_id


only_poppable_by = {
    "opn_root": "cls_root",
    "opn_brac": "cls_brac",
    "opn_degr": "cls_degr",
    "opn_dlim": "cls_dlim",
}

only_unpoppable_by = {
    "cmd_sqrt": "opn_degr"
}

always_poppable = {
    "cmd_frac",
    "sup_scrpt",
    "sub_scrpt",
    "cls_dlim",
}


def can_pop(parent_node_type: str, node_type: str) -> bool:
    if parent_node_type == "none":
        return False
    elif parent_node_type in only_poppable_by.keys():
        if only_poppable_by[parent_node_type] == node_type:
            return True
    elif parent_node_type in only_unpoppable_by.keys():
        if only_unpoppable_by[parent_node_type] != node_type:
            return True
    elif parent_node_type in always_poppable:
        return True
    else:
        raise ValueError(f"unknown parent {parent_node_type}")
    return False


single_child_nodes = {
    "sup_scrpt",
    "sub_scrpt",
    "cmd_sqrt",
    "cls_dlim",
}

double_child_nodes = {
    "cmd_frac",
}


def parent_stack_add(node_type: str, node_id: int) -> list:
    multi_child_nodes = only_poppable_by.keys()
    add_len = 0
    add_stack = []
    if node_type in single_child_nodes:
        add_len = 1
    elif node_type in double_child_nodes:
        add_len = 2
    elif node_type in multi_child_nodes:
        add_len = 1
    else:
        add_len = 0
    for i in range(add_len):
        add_stack.append(node_id)
    return add_stack


cannot_add = {
    "cls_root",
    "cls_brac",
    "cls_degr",
    }


def can_add(parent_type: str, node_type: str) -> bool:
    if parent_type == "none":
        if node_type == "opn_root":
            return True
        return False
    can_add = True
    if node_type in only_poppable_by.values():
        if parent_type not in only_poppable_by.keys():
            raise ValueError(f"parse error: Extra {node_type} under {parent_type}")
        expected = only_poppable_by[parent_type]
        if expected != node_type:
            raise ValueError(f"parse error: Expected {expected}, got {node_type}")
        can_add = True
    if node_type in cannot_add:
        can_add = False
    return can_add


def parse(tokens: list) -> list:
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
        can_add_to_children_list = can_add_to_nodes and bool(parent_stack)
        can_pop_parent = can_pop(parent_type, node_type)
        base_id = get_script_base(node_type, nodes, parent_stack)

        if base_id != -1:
            nodes[base_id][3].append(node_id)
            can_add_to_children_list = False
            can_pop_parent = False
        if can_pop_parent:
            parent_stack.pop()
        if can_add_to_children_list:
            nodes[parent_id][2].append(node_id)
        parent_stack += parent_stack_add(node_type, node_id)
        if can_add_to_nodes:
            node = (node_type, token, [], [])
            nodes.append(node)
            node_id += 1
        print(i, parent_stack)
    return nodes
