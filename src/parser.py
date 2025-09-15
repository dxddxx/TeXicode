import node_data


def get_node_type(token: tuple, parent_type: str) -> str:
    token_type = token[0]
    if (parent_type, token) in node_data.parent_dependent_type_dict.keys():
        return node_data.parent_dependent_type_dict[(parent_type, token)]
    elif (parent_type, token_type) in node_data.type_dependent_type_dict.keys():
        return node_data.type_dependent_type_dict[(parent_type, token_type)]
    elif token in node_data.type_dict.keys():
        return node_data.type_dict[token]
    elif token_type in node_data.self_dependent_type_dict.keys():
        return node_data.self_dependent_type_dict[token_type]
    # elif token[0] in ("symb", "alph", "numb"):
    #     if parent_type in ("opn_envn"):
    #         return "txt_info"
    #     else:
    #         return "txt_leaf"
    # elif token[0] == "cmnd":
    #     return "cmd_leaf"
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


def can_pop(parent_node_type: str, node_type: str) -> bool:
    if parent_node_type == "none":
        return False
    pop_info = node_data.type_info_dict[parent_node_type][0]
    if pop_info[0]:
        if node_type in pop_info[1]:
            return True
    else:
        if node_type not in pop_info[1]:
            return True
    return False


def parent_stack_add(node_type: str, node_id: int) -> list:
    add_stack = []
    parent_stack_add_info = node_data.type_info_dict[node_type][1]
    add_len = parent_stack_add_info[0]
    for i in range(add_len):
        add_stack.append(node_id)
    return add_stack


def can_add(parent_type: str, node_type: str) -> bool:
    if parent_type == "none":
        if node_type == "opn_root":
            return True
        return False
    add_info = node_data.type_info_dict[node_type][2]
    can_add = add_info[0]
    if add_info[1]:
        if parent_type in add_info[2]:
            raise ValueError(f"Extra {node_type}, under {add_info[2]}")
    else:
        if parent_type not in add_info[2]:
            expected = node_data.type_info_dict[parent_type][0][1]
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
        can_add_to_children_list = node_data.type_info_dict[node_type][3][0]
        can_update_parent_id = node_data.type_info_dict[node_type][3][1]
        can_double_pop = node_data.type_info_dict[node_type][3][2]
        base_id = get_script_base(node_type, nodes, parent_stack)

        # temporary solution to spaces
        if node_type == "txt_invs":
            continue

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
