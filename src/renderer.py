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

simple_symbols = """`!@#%*()+-=[]|;:'",.<>/?"""


def render_font(font_val: str, children: list) -> tuple:
    sketch, horizon = children[0]
    new_sketch = []
    for row in sketch:
        new_row = ""
        for char in row:
            char = revert_font(char)
            if char not in arts.alphabets["normal"]:
                new_row += char
                continue
            if 'A' <= char <= 'Z':  # Uppercase
                alpha_id = ord(char) - ord('A')
            elif 'a' <= char <= 'z':  # Lowercase
                alpha_id = ord(char) - ord('a') + 26
            new_row += arts.font[font_val][alpha_id]
        new_sketch.append(new_row)
    return new_sketch, horizon


def revert_font(char: str) -> str:
    if char.isascii():
        return char
    for alphabet in arts.alphabets.values():
        if char not in alphabet:
            continue
        for alpha_id in range(26*2):
            if alphabet[alpha_id] == char:
                return arts.alphabets["normal"][alpha_id]
    return char


def unshrink(small_char: str) -> str:
    for char, scripts in arts.unicode_scripts.items():
        if small_char in scripts:
            return char
    return small_char


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
        return render_font("mathnormal", [([token_val], 0)])
    elif token_type == "cmnd":
        if token_val in simple_leaf_commands:
            return [token_val], horizon
        elif token_val in arts.multi_line_leaf_commands.keys():
            return arts.multi_line_leaf_commands[token_val]
        elif token_val in symbols_art.symbols.keys():
            return [symbols_art.symbols[token_val]], horizon
        else:
            # print(f"unknown command {token_val}, rendering as '?'")
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

    shrunk = render_shrink(sketch, script_type_id, False, False)
    if shrunk != []:
        return shrunk, 0
    smart_shrunk = render_shrink(sketch, 1 - script_type_id, True, False)
    if smart_shrunk != []:
        sketch = smart_shrunk

    top = [""]
    btm = [""]
    if script_type_id == 0:
        top = sketch
    elif script_type_id == 1:
        btm = sketch
    return render_vert_pile(top, [arts.bg], 0, btm, "left")
    # shrunk_row = ""
    # for char in sketch[0]:
    #     char = revert_font(char)
    #     if char not in arts.unicode_scripts.keys():
    #         return render_vert_pile(top, [" "], 0, btm, "left")
    #     shrunk_char = arts.unicode_scripts[char][script_type_id]
    #     if shrunk_char == " " and char != " ":
    #         return render_vert_pile(top, [" "], 0, btm, "left")
    #     shrunk_row += shrunk_char


def render_shrink(sketch: list, script_type_id: int,
                  smart: bool, switch: bool) -> list:
    invert_script_type_id = 1 - script_type_id
    if len(sketch) != 1:
        return []
    art = arts.unicode_scripts
    shrunk_row = ""
    for char in sketch[0]:
        char = revert_font(char)
        unshrunk_char = unshrink(char)
        if unshrunk_char not in art.keys():
            return []
        if art[unshrunk_char][script_type_id] == char:
            return []
        if art[unshrunk_char][invert_script_type_id] == char:
            if smart:
                shrunk_row += char
                continue
            if switch:
                shrunk_row += art[unshrunk_char][script_type_id]
                continue
            return []
        shrunk_char = art[unshrunk_char][script_type_id]
        if shrunk_char != " " or char == " ":
            shrunk_row += shrunk_char
            continue
        return []
    return [shrunk_row]


def render_sup_script(children: list) -> tuple:
    return render_script(children, 0)


def render_sub_script(children: list) -> tuple:
    return render_script(children, 1)


def render_top_script(children: list) -> tuple:
    shrunk = render_shrink(children[0][0], 1, True, False)
    if shrunk == []:
        return children[0]
    return shrunk, 0


def render_bottom_script(children: list) -> tuple:
    shrunk = render_shrink(children[0][0], 0, True, False)
    if shrunk == []:
        return children[0]
    return shrunk, 0


def get_pile_center(base_height, base_horizon) -> tuple:
    if base_height == 2:
        # weird hacks but works
        # basically pointing the horizon to the script's paddings
        if base_horizon == 0:
            return [""], 0
        if base_horizon == 1:
            return [""], 1
    if base_height == 1:
        return [], 0
    if base_height == 1:
        return [""], 0
    pile_center_sketch = []
    for _ in range(base_height - 2):
        pile_center_sketch.append(arts.bg)
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
        if sorted_scripts[script_position] != [""]:
            script_type_name = ["super", "sub"][script_position]
            raise ValueError(f"Double {script_type_name}scripts")
        sorted_scripts[script_position] = script_sketch
    top, btm = sorted_scripts
    if base_position == "left":
        ctr, ctr_horizon = get_pile_center(len(base_sketch), base_horizon)
        if ctr == []:
            if top == [""]:
                return render_concat([(base_sketch, base_horizon), (btm, 0)])
            if btm == [""]:
                return render_concat([(base_sketch, base_horizon), (top, len(top)-1)])
            if len(top) > 1:
                top.pop()
                ctr = [""]
                ctr_horizon = 1
            elif len(btm) > 1:
                btm.pop(0)
                ctr = [""]
            elif len(top) == 1 and len(btm) == 1:
                top = render_shrink(top, 1, False, True)
                btm = render_shrink(btm, 0, False, True)
                ctr = [arts.bg]
        piled_scripts = render_vert_pile(top, ctr, ctr_horizon, btm, "left")
        return render_concat([(base_sketch, base_horizon), piled_scripts])
    elif base_position == "center":
        return render_vert_pile(top, base_sketch, base_horizon, btm, "center")


def render_delimiter(delim_type, height: int) -> tuple:
    if delim_type == ".":
        return [""], 0
    art_col = arts.delimiter["sgl"].find(delim_type[0])
    if art_col == -1:
        raise ValueError(f"Invalid delimiter type {delim_type}")
    delim_art = dict()
    for pos in arts.delimiter:
        art = arts.delimiter[pos]
        delim_art[pos] = art[art_col]
    if height == 1:
        return [delim_type], 0
    horizon = height // 2
    sketch = []
    for _ in range(height):
        sketch.append(delim_art["fil"])
    sketch[horizon] = delim_art["ctr"]
    sketch[0] = delim_art["top"]
    sketch[-1] = delim_art["btm"]
    return sketch, horizon


def render_big_delimiter(size: str, children: list) -> tuple:
    delim_type = children[0][0][0]
    height_dict = {"big": 1, "bigl": 1, "bigr": 1,
                   "Big": 3, "Bigl": 3, "Bigr": 3,
                   "bigg": 5, "biggl": 5, "biggr": 5,
                   "Bigg": 7, "Biggl": 7, "Biggr": 7}
    height = height_dict[size]
    return render_delimiter(delim_type, height)


def render_open_delimiter(children: list) -> tuple:
    inside = render_concat(children[1:-1])
    left_delim_type = children[0][0][0]
    right_delim_type = children[-1][0][0]
    height = len(inside[0])
    left = render_delimiter(left_delim_type, height)
    right = render_delimiter(right_delim_type, height)
    return render_concat([left, inside, right])


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


def render_square_root(children: list) -> tuple:
    degree_sketch, degree_horizon = children[0]
    radicand_sketch, radicand_horizon = children[-1]
    # new math vocab learned: radicand

    # clearer square root
    radicand_sketch = render_sup_script([children[-1]])[0]

    art = arts.square_root
    top_bar = art["top_bar"] * len(radicand_sketch[0])
    sqrt_sketch = [top_bar] + radicand_sketch
    for i in range(len(sqrt_sketch)):
        sqrt_sketch[i] = art["left_bar"] + sqrt_sketch[i] + arts.bg
    sqrt_sketch[0] = art["top_angle"] + sqrt_sketch[0][2:-1] + art["top_tail"]
    sqrt_sketch[-1] = art["btm_angle"] + sqrt_sketch[-1][2:]
    if len(children) == 1 or len(degree_sketch) > 1:
        return sqrt_sketch, radicand_horizon + 1

    shrinked_degree = render_shrink(degree_sketch, 1, False, False)
    if shrinked_degree == []:
        shrinked_degree = degree_sketch
    if sqrt_sketch[-2][0] == " ":
        sqrt_sketch[-2] = shrinked_degree[0][-1] + sqrt_sketch[-2][1:]
        shrinked_degree[0] = shrinked_degree[0][:-1]
    left_pad = arts.bg * len(shrinked_degree[0])
    for i in range(len(sqrt_sketch)):
        if i == len(sqrt_sketch) - 2:
            sqrt_sketch[i] = shrinked_degree[0] + sqrt_sketch[i]
            continue
        sqrt_sketch[i] = left_pad + sqrt_sketch[i]
    return sqrt_sketch, radicand_horizon + 1


def render_vert_concat(children: list, sep: list, align: str) -> tuple:
    sketch = children.pop(0)[0]
    horizon = 0
    for child in children:
        top = sketch
        btm = child[0]
        sketch, horizon = render_vert_pile(top, sep, 0, btm, align)
    return sketch, horizon


def render_root(children: list) -> tuple:
    return render_vert_concat(children, [arts.bg], "left")


def render_substack(children: list) -> tuple:
    return render_vert_concat(children, [""], "center")


def render_parent(node_type: str, token_val: str, children: list) -> tuple:
    if node_type == "opn_root":
        return render_root(children)
    elif node_type in {"opn_line", "opn_brak", "opn_pren",
                       "opn_brac", "opn_degr", "opn_stkln",
                       "opn_dllr", "opn_ddlr"}:
        return render_concat(children)
    elif node_type == "opn_dlim":
        return render_open_delimiter(children)
    elif node_type == "cls_dlim":
        return render_close_delimiter(children)
    elif node_type == "big_dlim":
        return render_big_delimiter(token_val, children)
    elif node_type == "sup_scrpt":
        return render_sup_script(children)
    elif node_type == "sub_scrpt":
        return render_sub_script(children)
    elif node_type == "top_scrpt":
        return render_top_script(children)
    elif node_type == "btm_scrpt":
        return render_bottom_script(children)
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
    elif node_type == "stk_lbrk":
        return render_concat(children)
    elif node_type == "cmd_sbstk":
        return render_substack(children)
    else:
        raise ValueError(f"Undefined control sequence {token_val}")


leaf_node_types = {
    "txt_leaf",
    "cmd_leaf",
    "ctr_base",
}


def render(nodes: list, debug: bool) -> list:
    if debug:
        print("Rendering")
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
        # elif node_type in parent_node_types:
        else:
            sketch, horizon = render_parent(node_type, node_token[1], children)

        if scripts:
            sketch, horizon = render_apply_scripts(sketch, horizon, scripts)
        canvas[i] = (sketch, horizon)
        if debug:
            for i in range(len(sketch)):
                print(i, sketch[i])
    return canvas[0][0]
