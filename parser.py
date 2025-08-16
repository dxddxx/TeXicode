node_type_special_dict = {
    ("sqrt",       ("[", "symbol")): "open_index",
    ("ctr_base",   ("^", "symbol")): "top_script",
    ("ctr_base",   ("_", "symbol")): "btm_script",
    ("limits",     ("^", "symbol")): "top_script",
    ("limits",     ("_", "symbol")): "btm_script",
    ("btm_script", ("^", "symbol")): "top_script",
    ("top_script", ("_", "symbol")): "btm_script",
}

node_type_dict = {
    ("start", "meta"):    "open_root",
    ("end",   "meta"):    "close_root",
    ("^",     "symbol"):  "sup_script",
    ("_",     "symbol"):  "sub_script",
    ("{",     "symbol"):  "open_brac",
    ("}",     "symbol"):  "close_brac",
    ("left",  "command"): "open_delim",
    ("right", "command"): "close_delim",
    ("sqrt",  "command"): "sqrt",
    ("frac",  "command"): "frac",
    ("sum",   "command"): "ctr_base",
    ("prod",  "command"): "ctr_base",
    ("lim",   "command"): "ctr_base",
    ("limits",   "command"): "limits",
    ("iint",     "command"): "ctr_base",
    ("iiint",    "command"): "ctr_base",
    ("iiiiint",  "command"): "ctr_base",
    ("idotsint", "command"): "ctr_base",
}


def get_node_type(prev_node_type: str, token: dict) -> str:
    # gotta turn token into a tuple to hash it
    # maybe tokens should be tuples from the start?
    token_tuple = (token["val"], token["typ"])
    if (prev_node_type, token_tuple) in node_type_special_dict.keys():
        return node_type_special_dict[(prev_node_type, token)]
    elif token_tuple in node_type_dict.keys():
        return node_type_dict[token_tuple]
    else:
        return token["typ"]


only_poppable_by = {
    "open_root":  "close_root",
    "open_brac":  "close_brac",
    "open_index": "close_index",
    "open_delim": "close_delim",
}

only_unpoppable_by = {
    "sqrt": "open_index"
}

always_poppable = {
    "frac",
    "sup_script",
    "sub_script",
    "top_script",
    "btm_script",
}


def can_pop(parent_node_type, node_type):
    if parent_node_type in only_poppable_by.keys():
        if only_poppable_by[parent_node_type] == node_type:
            return True
        else:
            return False
    elif parent_node_type in only_unpoppable_by.keys():
        if only_unpoppable_by[parent_node_type] == node_type:
            return False
        else:
            return True
    elif parent_node_type in always_poppable:
        return True
    else:
        raise ValueError(f"unknown parent {parent_node_type}")


single_child_nodes = {
    "sup_script",
    "sub_script",
    "top_script",
    "btm_script",
    "sqrt",
    "right",
}

double_child_nodes = {
    "frac",
}

multi_child_nodes = only_poppable_by.keys()


def parent_stack_add(node_type, node_id):
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


def can_add(node_type):
    return True # for now


def parse(tokens: list) -> list:
    nodes = []
    parent_stack = []
    node_id = 0

    for i in range(len(tokens)):
        token = tokens[i]

        if nodes:
            prev_node_type = nodes[-1]["typ"]
        else:
            prev_node_type = "none"
        node_type = get_node_type(prev_node_type, token)
        if parent_stack:
            parent_node_id = parent_stack[-1]
            parent_node = nodes[parent_node_id]
            parent_node_type = parent_node["typ"]
            nodes[parent_node_id]["chdrn"].append(node_id)
            if can_pop(parent_node_type, node_type):
                parent_stack.pop()

        added_stack = parent_stack_add(node_type, node_id)
        if added_stack:
            parent_stack += added_stack
        if can_add(node_type):
            node = {"tok": token, "typ": node_type, "chdrn": []}
            nodes.append(node)
            node_id += 1
    return nodes
