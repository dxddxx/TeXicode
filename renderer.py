

def render_leaf(token: tuple) -> tuple:
    ...


def render_concat(node: list) -> tuple:
    ...


def render_square_root(node: list) -> tuple:
    ...


def render_sup_script(node: list) -> tuple:
    ...


def render_sub_script(node: list) -> tuple:
    ...


def render_fraction(node: list) -> tuple:
    ...


def render_apply_scripts(scripts: list) -> tuple:
    ...


def render_parent(node_type: str, children: list) -> tuple:
    if node_type == "cmd_sqrt":
        return render_square_root(children)
    elif node_type == "cmd_frac":
        return render_fraction(children)
    elif node_type == "sup_scrpt":
        return render_sup_script(children)
    elif node_type == "sub_scrpt":
        return render_sup_script(children)
    else:
        raise ValueError(f"Undefined node {node_type}")


parent_node_types = {
    "opn_root",
    "opn_brac",
    "opn_dlim",
    "cls_dlim",
    "sup_scrpt",
    "sub_scrpt",
    "cmd_sqrt",
    "cmd_frac",
}

leaf_node_types = {
    "txt_leaf",
    "cmd_leaf",
    "ctr_base",
}


def render(nodes: list) -> list:
    canvas = []
    for i in range(len(nodes)-1, -1, -1):
        node = nodes[i]
        node_type = node[0]
        node_token = node[1]
        children_ids = node[2]
        children = []
        for i in children_ids:
            children.append(canvas[i])
        scripts_ids = node[3]
        scripts = []
        for i in scripts_ids:
            scripts.append(canvas[i])

        if node_type in leaf_node_types:
            sketch, horizon = render_leaf(node_token)
        elif node_type in parent_node_types:
            sketch, horizon = render_parent(node_type, children)
        else:
            raise ValueError(f"Undefined control sequence {node_token[1]}")

        if scripts:
            sketch, horizon = render_apply_scripts(scripts)
        canvas.append(sketch)
    return canvas[0][0]
