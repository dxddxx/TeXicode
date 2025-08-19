import arts
import symbols_art

# from https://latexref.xyz/Math-functions.html
simple_leaf_commands = {
    " ", "_", "$", "{", "}", "#", "&",
    "arccos", "arcsin", "arctan", "arg", "bmod", "cos", "cosh", "cot", "coth",
    "csc", "deg", "det", "dim", "exp", "gcd", "hom", "inf", "ker", "lg", "lim",
    "liminf", "limsup", "ln", "log", "max", "min", "pmod",
    # "mod",  # \mod creates leading spaces, not simple
    "Pr", "sec", "sin", "sinh", "sup", "tan", "tanh", "%",
}

simple_symbols = """`!@#$%*()+-=[]|;:'",.<>/?"""


def render_leaf(token: tuple) -> tuple:
    token_type = token[0]
    token_val = token[1]
    horizon = 0
    if token_type == "numb":
        return [token_val], horizon
    elif token_type == "symb":
        if token_val in simple_symbols:
            return [token_val], horizon
        elif token_val in arts.special_symbols.keys():
            return [arts.special_symbols[token_val]], horizon
    elif token_type == "alph":
        return render_font("mathnormal", [token_val])
    elif token_type == "cmnd":
        if token_val in simple_leaf_commands:
            return [token_val], horizon
        elif token_val in arts.multi_line_leaf_commands.keys():
            return arts.multi_line_leaf_commands[token_val]
        elif token_val in symbols_art.symbols.keys():
            return [symbols_art.symbols[token_val]], horizon
        else:
            print(f"unknown command {token_val}, rendering as '?'")
            return ["?"], 0


def render_concat(children: list) -> tuple:
    concated_sketch = []
    maxh_sky = 0  # max height above horizon - max height of sky
    maxh_ocn = 0
    for sketch, horizon in children:
        h_sky = horizon
        h_ocn = len(sketch) - h_sky - 1
        if h_sky > maxh_sky:
            maxh_sky = h_sky
        if h_ocn > maxh_ocn:
            maxh_ocn = h_ocn
    for i in range(maxh_sky + 1 + maxh_ocn):
        concated_sketch.append("")
    for sketch, horizon in children:
        h_sky = horizon
        h_ocn = len(sketch) - h_sky - 1
        top_pad_len = maxh_sky - h_sky
        btm_pad_len = maxh_ocn - h_ocn
        top_pad = [arts.bg * len(sketch[0])] * top_pad_len
        btm_pad = [arts.bg * len(sketch[0])] * btm_pad_len
        sketch = top_pad + sketch + btm_pad
        for i in range(len(concated_sketch)):
            concated_sketch[i] += sketch[i]
    concated_horizon = maxh_sky
    return concated_sketch, concated_horizon


def render_vert_pile(top, ctr, ctr_horizon, btm, align) -> tuple:
    piled_sketch = []
    piled_horizon = len(top) + ctr_horizon
    if top == [""]:
        piled_horizon -= 1
    if ctr == [""]:
        piled_horizon -= 1
    if piled_horizon < 0:
        piled_horizon = 0
    max_len = max(len(top[0]), len(ctr[0]), len(btm[0]))
    for sketch in (top, ctr, btm):
        if sketch == [""]:
            continue
        sketch_len = len(sketch[0])
        left_pad_len = 0
        right_pad_len = 0
        if align == "left":
            right_pad_len = max_len - sketch_len
        elif align == "right":
            left_pad_len = max_len - sketch_len
        elif align == "center":
            left_pad_len = (max_len - sketch_len) // 2
            right_pad_len = max_len - sketch_len - left_pad_len
        left_pad = arts.bg * left_pad_len
        right_pad = arts.bg * right_pad_len
        for row in sketch:
            piled_sketch.append(left_pad + row + right_pad)
    return piled_sketch, piled_horizon


def render_script(children: list, script_type_id: int) -> tuple:
    sketch, horizon = children[0]
    top = [""]
    btm = [""]
    if script_type_id == 0:
        top = sketch
    elif script_type_id == 1:
        btm = sketch
    if len(sketch) != 1:
        return render_vert_pile(top, [" "], 0, btm, "left")
    shrinked_row = ""
    for char in sketch[0]:
        char = revert_font(char)
        if char not in arts.unicode_scripts.keys():
            return render_vert_pile(top, [" "], 0, btm, "left")
        shrinked_char = arts.unicode_scripts[char][script_type_id]
        if shrinked_char == " " and char != " ":
            return render_vert_pile(top, [" "], 0, btm, "left")
        shrinked_row += shrinked_char
    return [shrinked_row], 0


def render_sup_script(children: list) -> tuple:
    return render_script(children, 0)


def render_sub_script(children: list) -> tuple:
    return render_script(children, 1)


def get_pile_center(base_height, base_horizon) -> tuple:
    if base_height in {1, 2}:
        return [""], 0
    pile_center_sketch = []
    for _ in range(base_height - 2):
        pile_center_sketch.append(" ")
    pile_center_horizon = base_horizon - 1
    return pile_center_sketch, pile_center_horizon


def render_apply_scripts(base_sketch, base_horizon, scripts: list) -> tuple:
    sorted_scripts = [[""], [""]]
    base_position = "left"
    for script_type, script_sketch in scripts:
        if script_type in {"top_scrpt", "btm_scrpt"}:
            base_position = "center"
        script_position = 0
        if script_type in {"sub_scrpt", "btm_scrpt"}:
            script_position = 1
        sorted_scripts[script_position] = script_sketch
    top, btm = sorted_scripts
    if base_position == "left":
        ctr, ctr_horizon = get_pile_center(len(base_sketch), base_horizon)
        piled_scripts = render_vert_pile(top, ctr, ctr_horizon, btm, "left")
        return render_concat([(base_sketch, base_horizon), piled_scripts])
    elif base_position == "center":
        return render_vert_pile(top, base_sketch, base_horizon, btm, "center")


def render_open_delimiter(children: list) -> tuple:
    inside, horizon = render_concat(children[1:-1])
    left_delim = children[0][0]
    right_delim = children[-1][0]
    height = len(inside)
    if height == 1:
        return render_concat([(left_delim, 0), (inside, 0), (right_delim, 0)])

    left_art_col = arts.delimiter["left"]["sgl"].find(left_delim[0])
    right_art_col = arts.delimiter["right"]["sgl"].find(right_delim[0])
    if left_art_col == -1:
        raise ValueError(f"Invalid delimiter type {left_delim}")
    if right_art_col == -1:
        raise ValueError(f"Invalid delimiter type {right_delim}")
    left_art = dict()
    right_art = dict()
    for pos in arts.delimiter["left"]:
        art = arts.delimiter["left"][pos]
        left_art[pos] = art[left_art_col]
    for pos in arts.delimiter["right"]:
        art = arts.delimiter["right"][pos]
        right_art[pos] = art[right_art_col]
    sketch = []
    for row in inside:
        sketch.append(left_art["fil"] + row + right_art["fil"])
    sketch[horizon] = left_art["ctr"] + sketch[horizon][1:-1] + right_art["ctr"]
    sketch[0] = left_art["top"] + sketch[0][1:-1] + right_art["top"]
    sketch[-1] = left_art["btm"] + sketch[-1][1:-1] + right_art["btm"]
    return sketch, horizon


def render_close_delimiter(children: list) -> tuple:
    return children[0]


def render_binomial(children: list) -> tuple:
    n, r = children[0][0], children[1][0]
    sep_space = max(len(n[0]), len(r[0])) * arts.bg
    piled = render_vert_pile(n, [sep_space], 0, r, "center")
    return render_open_delimiter([("("), piled, (")")])


def render_fraction(children: list) -> tuple:
    numer, denom = children[0][0], children[1][0]
    art = arts.fraction
    fraction_line = max(len(numer[0]), len(denom[0])) * art[1]
    fraction_line = art[0] + fraction_line + art[2]
    return render_vert_pile(numer, [fraction_line], 0, denom, "center")


def render_accents(accent_val: str, children: list) -> tuple:
    import unicodedata
    u_hex = {"acute": "\u0302", "bar": "\u0304", "breve": "\u0306",
             "check": "\u030C", "ddot": "\u0308", "dot": "\u0307",
             "grave": "\u0300", "hat": "\u0302", "mathring": "\u030A",
             "tilde": "\u0303", "vec": "\u20D7", "widehat": "\u0302",  # fix
             "widetilde": "\u0360"}[accent_val]
    sketch = children[0][0]
    first_char = sketch[0][0] + u_hex
    first_char = unicodedata.normalize("NFKC", first_char)
    # pls fix this, pre composed font looks like ass
    first_row = first_char + sketch[0][1:]
    sketch = [first_row] + sketch[1:]
    return sketch, children[0][1]


def render_font(font_val: str, children: list) -> tuple:
    alpha_val = children[0][0][0]
    if alpha_val not in arts.font["mathrm"]:
        return [alpha_val], 0
    if 'A' <= alpha_val <= 'Z':  # Uppercase
        alpha_id = ord(alpha_val) - ord('A')
    elif 'a' <= alpha_val <= 'z':  # Lowercase
        alpha_id = ord(alpha_val) - ord('a') + 26
    return [arts.font[font_val][alpha_id]], 0


def revert_font(char: str) -> str:
    if char.isascii():
        return char
    for alphabet in arts.font.values():
        if char not in alphabet:
            continue
        for alpha_id in range(26):
            if alphabet[alpha_id] != char:
                return arts.font["mathrm"][alpha_id]
    return char


def render_square_root(children: list) -> tuple:
    degree_sketch, degree_horizon = children[0]
    radicand_sketch, radicand_horizon = children[-1]
    # new math vocab learned: radicand
    radicand_sketch = render_sup_script(children)[0]
    art = arts.square_root
    top_bar = art["top_bar"] * len(radicand_sketch[0])
    sqrt_sketch = [top_bar] + radicand_sketch
    for i in range(len(sqrt_sketch)):
        sqrt_sketch[i] = art["left_bar"] + sqrt_sketch[i] + arts.bg
    sqrt_sketch[0] = art["top_angle"] + sqrt_sketch[0][2:-1] + art["top_tail"]
    sqrt_sketch[-1] = art["btm_angle"] + sqrt_sketch[-1][2:]
    return sqrt_sketch, radicand_horizon + 1


def render_root(children: list) -> tuple:
    sketch = children.pop(0)[0]
    horizon = 0
    for child in children:
        top = sketch
        btm = child[0]
        sketch, horizon = render_vert_pile(top, [" "], 0, btm, "center")
    return sketch, horizon


def render_parent(node_type: str, token_val: str, children: list) -> tuple:
    if node_type == "opn_root":
        return render_root(children)
    if node_type in {"opn_line", "opn_brac", "opn_degr"}:
        return render_concat(children)
    elif node_type == "opn_dlim":
        return render_open_delimiter(children)
    elif node_type == "cls_dlim":
        return render_close_delimiter(children)
    elif node_type == "sup_scrpt":
        return render_sup_script(children)
    elif node_type == "sub_scrpt":
        return render_sub_script(children)
    # top/btm script uses the same fn as sup/sub script
    # so that top/btm scripts stick to their ctr base
    elif node_type == "top_scrpt":
        return render_sub_script(children)
    elif node_type == "btm_scrpt":
        return render_sup_script(children)
    elif node_type == "cmd_sqrt":
        return render_square_root(children)
    elif node_type == "cmd_frac":
        return render_fraction(children)
    elif node_type == "cmd_binom":
        return render_binomial(children)
    elif node_type == "cmd_acnt":
        return render_accents(token_val, children)
    elif node_type == "cmd_font":
        return render_font(token_val, children)
    elif node_type == "cmd_lbrk":
        return render_concat(children)
    else:
        raise ValueError(f"Undefined node {node_type}")


parent_node_types = {
    "opn_root",
    "opn_brac",
    "opn_dlim",
    "cls_dlim",
    "sup_scrpt",
    "sub_scrpt",
    "top_scrpt",
    "btm_scrpt",
    "cmd_sqrt",
    "cmd_frac",
    "cmd_binom",
    "cmd_acnt",
    "cmd_font",
    "opn_line",
    "cls_line",
    "cmd_lbrk",
}

leaf_node_types = {
    "txt_leaf",
    "cmd_leaf",
    "ctr_base",
}


def render(nodes: list) -> list:
    canvas = []
    for i in range(len(nodes)):
        canvas.append(())
    for i in range(len(nodes)-1, -1, -1):
        node = nodes[i]
        node_type = node[0]
        node_token = node[1]
        children_ids = node[2]
        children = []
        for j in children_ids:
            children.append(canvas[j])
        scripts_ids = node[3]
        scripts = []
        for j in scripts_ids:
            # scripts is a list of tuple(node_type, sketch)
            scripts.append((nodes[j][0], canvas[j][0]))

        if node_type in leaf_node_types:
            sketch, horizon = render_leaf(node_token)
        elif node_type in parent_node_types:
            sketch, horizon = render_parent(node_type, node_token[1], children)
        else:
            raise ValueError(f"Undefined control sequence {node_token[1]}")

        if scripts:
            sketch, horizon = render_apply_scripts(sketch, horizon, scripts)
        canvas[i] = (sketch, horizon)
    return canvas[0][0]
