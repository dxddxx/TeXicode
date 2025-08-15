def parse(tokens: list) -> list:
    nodes = []
    parent_stack = []

    root_token = {"val":"root", "typ":"meta"}
    root_node = {"tok": root_token, "chdrn": []}
    nodes.append(root_node)
    parent_stack.append(0)
    for token in tokens:
        if parent_stack:
            parent_id = parent_stack[-1]
            parent_token = tokens[parent_id]
            if can_pop(parent_token, token):
                parent_stack.pop()



        parent_stack += []
        nodes.append(node)
    return nodes

# node types include: atomic, function, delimiter, 
# function: rendered with a function, eg frac, concat, leftright

