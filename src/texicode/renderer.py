from . import node_data, arts, symbols_art


def util_revert_font(char: str) -> str:
    # if char.isascii():
    if ord(char) < 128:
        return char
    for alphabet in arts.alphabets.values():
        if char not in alphabet:
            continue
        for alpha_id in range(26*2):
            if alphabet[alpha_id] == char:
                return arts.alphabets["normal"][alpha_id]
    return char


def util_font(font_val: str, children: list) -> tuple:
    sketch, horizon = children[0]
    new_sketch = []
    for row in sketch:
        new_row = []
        for char in row:
            char = util_revert_font(char)
            if char not in arts.alphabets["normal"]:
                new_row.append(char)
                continue
            if 'A' <= char <= 'Z':
                alpha_id = ord(char) - ord('A')
            elif 'a' <= char <= 'z':
                alpha_id = ord(char) - ord('a') + 26
            new_row.append(arts.font[font_val][alpha_id])
        new_sketch.append(new_row)
    return new_sketch, horizon


def util_unshrink(small_char: str) -> str:
    """No change to logic"""
    for char, scripts in arts.unicode_scripts.items():
        if small_char in scripts:
            return char
    return small_char


def util_concat(children: list, concat_line: bool = False) -> tuple:
    if not children:
        return [[]], 0

    concated_sketch = []
    maxh_sky = 0
    maxh_ocn = 0

    for sketch, horizon in children:
        h_sky = horizon
        h_ocn = len(sketch) - h_sky - 1
        maxh_sky = max(maxh_sky, h_sky)
        maxh_ocn = max(maxh_ocn, h_ocn)

    concated_horizon = maxh_sky
    for _ in range(maxh_sky + 1 + maxh_ocn):
        concated_sketch.append([])

    for sketch, horizon in children:
        h_sky = horizon
        h_ocn = len(sketch) - h_sky - 1
        top_pad_len = maxh_sky - h_sky
        btm_pad_len = maxh_ocn - h_ocn

        top_pad = [[arts.bg] * len(sketch[0]) for _ in range(top_pad_len)]
        btm_pad = [[arts.bg] * len(sketch[0]) for _ in range(btm_pad_len)]

        sketch = top_pad + sketch + btm_pad
        for i in range(len(concated_sketch)):
            concated_sketch[i].extend(sketch[i])

    if concat_line:
        concated_horizon = len(concated_sketch[0])

    return concated_sketch, concated_horizon


def util_vert_pile(top, ctr, ctr_horizon, btm, align) -> tuple:
    piled_sketch = []
    piled_horizon = len(top) + ctr_horizon

    if top == [[]]:
        piled_horizon -= 1
    if ctr == [[]]:
        piled_horizon -= 1

    if piled_horizon < 0:
        piled_horizon = 0

    max_len = max(len(top[0]), len(ctr[0]), len(btm[0]))

    for sketch in (top, ctr, btm):
        if sketch == [[]]:
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

        left_pad = [arts.bg] * left_pad_len
        right_pad = [arts.bg] * right_pad_len

        for row in sketch:
            piled_sketch.append(left_pad + row + right_pad)

    if piled_sketch == []:
        piled_sketch = [[]]

    return piled_sketch, piled_horizon


def util_script(children: list, script_type_id: int) -> tuple:
    sketch, _ = children[0]
    shrunk = util_shrink(sketch, script_type_id, False, False)
    if shrunk != []:
        return shrunk, 0

    smart_shrunk = util_shrink(sketch, 1 - script_type_id, True, False)
    if smart_shrunk != []:
        sketch = smart_shrunk

    top = [[]]
    btm = [[]]

    if script_type_id == 0:
        top = sketch
    elif script_type_id == 1:
        btm = sketch

    return util_vert_pile(top, [[arts.bg]], 0, btm, "left")


def util_shrink(sketch: list, script_type_id: int,
                smart: bool, switch: bool) -> list:
    invert_script_type_id = 1 - script_type_id
    if len(sketch) != 1:
        return []

    art = arts.unicode_scripts
    shrunk_row = []

    for char in sketch[0]:
        char = util_revert_font(char)
        unshrunk_char = util_unshrink(char)

        if unshrunk_char not in art.keys():
            return []

        if art[unshrunk_char][script_type_id] == char:
            return []

        if art[unshrunk_char][invert_script_type_id] == char:
            if smart:
                shrunk_row.append(char)
                continue
            if switch:
                shrunk_row.append(art[unshrunk_char][script_type_id])
                continue
            return []

        shrunk_char = art[unshrunk_char][script_type_id]
        if shrunk_char != " " or char == " ":
            shrunk_row.append(shrunk_char)
            continue

        return []

    return [shrunk_row]


def util_get_pile_center(base_height, base_horizon) -> tuple:
    if base_height == 2:
        if base_horizon == 0:
            return [[]], 0
        if base_horizon == 1:
            return [[]], 1

    if base_height == 1:
        return [[]], 0

    pile_center_sketch = []
    for _ in range(base_height - 2):
        pile_center_sketch.append([arts.bg])

    pile_center_horizon = base_horizon - 1
    return pile_center_sketch, pile_center_horizon


def util_delimiter(delim_type, height: int, horizon: int) -> tuple:
    if delim_type == ".":
        return [[]], 0

    art_col = arts.delimiter["sgl"].find(delim_type[0])
    if art_col == []:
        raise ValueError(f"Invalid delimiter type {delim_type}")

    delim_art = dict()
    for pos in arts.delimiter:
        art = arts.delimiter[pos]
        delim_art[pos] = art[art_col]

    if height == 1:
        return [delim_type], 0

    if height == 2 and delim_type in ["{", "}"]:
        return [delim_art["top"], delim_art["btm"]], horizon

    center = horizon
    if center == 0:
        center = 1
    if center == height - 1:
        center = height - 2

    sketch = []
    for _ in range(height):
        sketch.append([delim_art["fil"]])

    sketch[center] = [delim_art["ctr"]]
    sketch[0] = [delim_art["top"]]
    sketch[-1] = [delim_art["btm"]]

    return sketch, horizon


def util_vert_concat(children: list, sep: list, align: str,
                     pad_left: bool = True) -> tuple:
    if pad_left:
        children = [([[arts.bg] + row for row in sketch], horizon)
                    for sketch, horizon in children]
    sketch = children.pop(0)[0]
    horizon = 0

    for child in children:
        top = sketch
        btm = child[0]
        sketch, horizon = util_vert_pile(top, sep, 0, btm, align)

    return sketch, horizon

# Rendering Functions


def render_font(token: str, children: list) -> tuple:
    return util_font(token[1], children)


def render_text_info(token: tuple, children: list) -> tuple:
    return [[token[1]]], 0


def render_text(token: str, children: list) -> tuple:
    return util_font(token[1], children)


def render_leaf(token: tuple, children: list) -> tuple:
    token_type = token[0]
    token_val = token[1]
    sketch = [[token_val]]
    horizon = 0

    if token_type == "numb":
        return sketch, horizon

    elif token_type == "symb":
        if token_val in arts.special_symbols.keys():
            sketch = arts.special_symbols[token_val]
        return sketch, horizon

    elif token_type == "alph":
        return util_font("mathnormal", [(sketch, 0)])

    elif token_type == "cmnd":
        if token_val in arts.multi_line_leaf_commands.keys():
            sketch, horizon = arts.multi_line_leaf_commands[token_val]
        elif token_val in symbols_art.symbols.keys():
            sketch = [symbols_art.symbols[token_val]]
        else:
            sketch = [["?"]]
        return sketch, horizon


def render_concat(children: list) -> tuple:
    return util_concat(children)


def render_sup_script(children: list) -> tuple:
    return util_script(children, 0)


def render_sub_script(children: list) -> tuple:
    return util_script(children, 1)


def render_top_script(children: list) -> tuple:
    shrunk = util_shrink(children[0][0], 1, True, False)
    if shrunk == []:
        return children[0]
    return shrunk, 0


def render_bottom_script(children: list) -> tuple:
    shrunk = util_shrink(children[0][0], 0, True, False)
    if shrunk == []:
        return children[0]
    return shrunk, 0


def render_apply_scripts(base: list, scripts: list) -> tuple:
    base_sketch, base_horizon = base
    sorted_scripts = [[[]], [[]]]
    base_position = "left"

    for script_type, script_sketch in scripts:
        if script_type in {"top_scrpt", "btm_scrpt"}:
            base_position = "center"
        script_position = 0
        if script_type in {"sub_scrpt", "btm_scrpt"}:
            script_position = 1
        if sorted_scripts[script_position] != [[]]:
            script_type_name = ["super", "sub"][script_position]
            raise ValueError(f"Double {script_type_name}scripts")
        sorted_scripts[script_position] = script_sketch

    top, btm = sorted_scripts
    # base = (base_sketch, base_horizon)

    if base_position == "center":
        return util_vert_pile(top, base_sketch, base_horizon, btm, "center")

    ctr, ctr_horizon = util_get_pile_center(len(base_sketch), base_horizon)
    if ctr != [[]]:
        piled_scripts = util_vert_pile(top, ctr, ctr_horizon, btm, "left")
        return util_concat([base, piled_scripts])

    if top == [[]]:
        return util_concat([base, (btm, 0)])
    if btm == [[]]:
        return util_concat([base, (top, len(top)-1)])

    if len(top) > 1:
        top.pop()
        ctr = [[]]
        ctr_horizon = 1
    elif len(btm) > 1:
        btm.pop(0)
        ctr = [[]]
    elif len(top) == 1 and len(btm) == 1:
        top = util_shrink(top, 1, False, True)
        btm = util_shrink(btm, 0, False, True)
        ctr = [[arts.bg]]

    piled_scripts = util_vert_pile(top, ctr, ctr_horizon, btm, "left")
    return util_concat([base, piled_scripts])


def render_big_delimiter(token: tuple, children: list) -> tuple:
    size = token[1]
    delim_type = children[0][0][0]
    height_dict = {"big": 1, "bigl": 1, "bigr": 1,
                   "Big": 3, "Bigl": 3, "Bigr": 3,
                   "bigg": 5, "biggl": 5, "biggr": 5,
                   "Bigg": 7, "Biggl": 7, "Biggr": 7}
    height = height_dict[size]
    return util_delimiter(delim_type, height, height // 2)


def render_open_delimiter(children: list) -> tuple:
    inside = util_concat(children[1:-1])
    left_delim_type = children[0][0][0][0]
    right_delim_type = children[-1][0][0][0]
    height = len(inside[0])
    horizon = inside[1]
    left = util_delimiter(left_delim_type, height, horizon)
    right = util_delimiter(right_delim_type, height, horizon)
    return util_concat([left, inside, right])


def render_close_delimiter(children: list) -> tuple:
    return children[0]


def render_binomial(children: list) -> tuple:
    n, r = children[0][0], children[1][0]
    sep_space = [arts.bg] * max(len(n[0]), len(r[0]))
    piled = util_vert_pile(n, [sep_space], 0, r, "center")
    return render_open_delimiter([([["("]], 0), piled, ([[")"]], 0)])


def render_fraction(children: list) -> tuple:
    numer, denom = children[0][0], children[1][0]
    art = arts.fraction
    fraction_line = [art[1]] * max(len(numer[0]), len(denom[0]))
    fraction_line = [art[0]] + fraction_line + [art[2]]
    return util_vert_pile(numer, [fraction_line], 0, denom, "center")


def render_accents(token: tuple, children: list) -> tuple:
    accent_val = token[1]
    u_hex = {"acute": "\u0302", "bar": "\u0304", "breve": "\u0306",
             "check": "\u030C", "ddot": "\u0308", "dot": "\u0307",
             "grave": "\u0300", "hat": "\u0302", "mathring": "\u030A",
             "tilde": "\u0303", "vec": "\u20D7", "widehat": "\u0302",
             "widetilde": "\u0360"}[accent_val]
    sketch = children[0][0]
    first_char = sketch[0][0] + u_hex
    # finally fixed ugly ass combining char lets goooo
    first_row = [first_char] + sketch[0][1:]
    sketch = [first_row] + sketch[1:]
    return sketch, children[0][1]


def util_onechar_square_root(children: list) -> tuple:
    # thanks to u/Iron_Pencil for the idea
    radicand_sketch, radicand_horizon = children[-1]
    surd_art = symbols_art.symbols["surd"]

    if len(radicand_sketch[0]) == 1:
        new_radi_row = surd_art + [radicand_sketch[0][0] + "\u0305"]
    if len(radicand_sketch[0]) == 0:
        new_radi_row = surd_art
    new_radi = ([new_radi_row], radicand_horizon)

    if len(children) <= 1:
        return new_radi

    degree = util_script(children, 0)
    return util_concat([degree, new_radi])


def util_multichar_square_root(children: list) -> tuple:
    degree_sketch, _ = children[0]
    radicand_sketch, radicand_horizon = children[-1]

    art = arts.square_root

    top_bar = art["top_bar"] * len(radicand_sketch[0])
    sqrt_sketch = [top_bar] + radicand_sketch

    for i in range(len(sqrt_sketch)):
        sqrt_sketch[i] = art["left_bar"] + sqrt_sketch[i] + [arts.bg]

    sqrt_sketch[0] = art["top_angle"] + sqrt_sketch[0][2:-1] + art["top_tail"]
    sqrt_sketch[-1] = art["btm_angle"] + sqrt_sketch[-1][2:]

    if len(children) == 1 or len(degree_sketch) > 1:
        return sqrt_sketch, radicand_horizon + 1

    shrinked_degree = util_shrink(degree_sketch, 1, False, False)
    if shrinked_degree == []:
        shrinked_degree = degree_sketch

    if sqrt_sketch[-2][0] == " ":
        sqrt_sketch[-2] = [shrinked_degree[0][-1]] + sqrt_sketch[-2][1:]
        shrinked_degree[0] = shrinked_degree[0][:-1]

    left_pad = [arts.bg] * len(shrinked_degree[0])

    for i in range(len(sqrt_sketch)):
        if i == len(sqrt_sketch) - 2:
            sqrt_sketch[i] = shrinked_degree[0] + sqrt_sketch[i]
            continue
        sqrt_sketch[i] = left_pad + sqrt_sketch[i]

    return sqrt_sketch, radicand_horizon + 1


def render_square_root(children: list) -> tuple:
    radicand_sketch, _ = children[-1]

    # if len(radicand_sketch) == 1:
    # someone said parenthesis is uncleaer, agreed.
    if len(radicand_sketch[0]) <= 1 and len(radicand_sketch) == 1:
        return util_onechar_square_root(children)
    else:
        return util_multichar_square_root(children)


def render_concat_line(children: list) -> tuple:
    line_sketch, line_horizon = util_concat(children, True)
    return [[arts.bg] + row for row in line_sketch], line_horizon


def util_env_cells(child_nodes: list, children: list) -> list:
    """Split an environment's flat children into rows of cells.

    & leaves and row_sep children are pure separators: they are not
    included in any cell. Returns a list of rows, each row being a list
    of cells, each cell being a list of (child_node, canvas) pairs.
    """
    rows = []
    row = []
    cell = []
    for child_node, child_canvas in zip(child_nodes, children):
        if child_node[0] == "row_sep":
            row.append(cell)
            cell = []
            rows.append(row)
            row = []
        elif child_node[1] == ("symb", "&"):
            row.append(cell)
            cell = []
        else:
            cell.append((child_node, child_canvas))
    row.append(cell)
    rows.append(row)
    return rows


def render_empty(children: list) -> tuple:
    return [[]], 0


def util_pad_cell(cell: tuple, width: int, align: str) -> tuple:
    sketch, horizon = cell
    pad = width - len(sketch[0])
    if pad <= 0:
        return cell
    if align == "l":
        left, right = 0, pad
    elif align == "r":
        left, right = pad, 0
    else:
        left = pad // 2
        right = pad - left
    padded = [[arts.bg] * left + row + [arts.bg] * right
              for row in sketch]
    return padded, horizon


def util_grid(rows_of_cells: list, aligns: list, gap: int,
              blank_rows: bool, pad_left: bool) -> tuple:
    """Assemble rows of cells into a padded grid.

    Cells in a row are joined at their horizon; cells in a column are
    padded to the column width according to their alignment (l/r/c).
    """
    cell_rows = []
    for row in rows_of_cells:
        cell_rows.append(
            [util_concat([cv for _, cv in cell])
             for cell in row])

    num_cols = max((len(row) for row in cell_rows), default=0)
    if num_cols == 0:
        return [[]], 0

    aligns = (aligns + ["c"] * num_cols)[:num_cols]
    col_widths = []
    for c in range(num_cols):
        col_widths.append(max(
            (len(row[c][0][0]) for row in cell_rows if c < len(row)),
            default=0))

    row_sketches = []
    for row in cell_rows:
        padded = [util_pad_cell(cell, col_widths[c], aligns[c])
                  for c, cell in enumerate(row)]
        if gap:
            sep = ([[arts.bg] * gap], 0)
            concat_children = []
            for i, cell in enumerate(padded):
                if i:
                    concat_children.append(sep)
                concat_children.append(cell)
        else:
            concat_children = padded
        row_sketches.append(util_concat(concat_children))

    sketch = None
    horizon = 0
    for row_sketch in row_sketches:
        if pad_left:
            row_sketch = ([[arts.bg] + row for row in row_sketch[0]],
                          row_sketch[1])
        if sketch is None:
            sketch, horizon = row_sketch[0], row_sketch[1]
            continue
        sep = [[arts.bg]] if blank_rows else [[]]
        sketch, horizon = util_vert_pile(
            sketch, sep, 0, row_sketch[0], "left")

    if not blank_rows:
        horizon = len(sketch) // 2
    return sketch, horizon


def util_env_layout(env: str, num_cols: int) -> tuple:
    """Per-environment grid layout: (aligns, gap, blank_rows, pad_left,
    left_delim, right_delim)."""
    if env in ("align", "align*", "aligned", "split"):
        aligns = (["r", "l"] * ((num_cols + 1) // 2))[:num_cols]
        return aligns, 0, True, False, None, None
    if env == "gathered":
        return ["c"] * num_cols, 0, False, False, None, None
    if env in ("matrix", "pmatrix", "bmatrix", "Bmatrix",
               "vmatrix", "Vmatrix", "smallmatrix"):
        delims = {"pmatrix": ("(", ")"), "bmatrix": ("[", "]"),
                  "Bmatrix": ("{", "}"), "vmatrix": ("|", "|"),
                  "Vmatrix": ("‖", "‖")}
        left_delim, right_delim = delims.get(env, (None, None))
        return ["c"] * num_cols, 1, False, False, left_delim, right_delim
    if env == "cases":
        return ["l"] * num_cols, 2, False, False, "{", None
    return ["c"] * num_cols, 0, True, True, None, None


def util_array_spec(rows: list, nodes: list) -> tuple:
    """Read the {spec} argument of \\begin{array} from the first cell."""
    if not rows or not rows[0] or not rows[0][0] or \
            rows[0][0][0][0][0] != "opn_brac":
        raise ValueError("array requires a column spec")
    first_cell = rows[0][0]
    spec_node = first_cell[0][0]
    spec = "".join(nodes[cid][1][1] for cid in spec_node[2])
    aligns = []
    for char in spec:
        if char in "clr":
            aligns.append(char)
        else:
            raise ValueError(f"Unsupported column spec {spec!r}")
    rest_cell = first_cell[1:]
    first_row = ([rest_cell] if rest_cell else []) + rows[0][1:]
    return aligns, [first_row] + rows[1:]


def render_begin(token: tuple, children: list, child_nodes: list,
                 nodes: list) -> tuple:
    """Render an environment by gridding its flat cells."""
    env = token[1]
    rows = util_env_cells(child_nodes, children)

    if env == "array":
        aligns, rows = util_array_spec(rows, nodes)
        gap, blank_rows, pad_left = 1, False, False
        left_delim = right_delim = None
    else:
        num_cols = max((len(row) for row in rows), default=0)
        aligns, gap, blank_rows, pad_left, left_delim, right_delim = \
            util_env_layout(env, num_cols)

    sketch, horizon = util_grid(rows, aligns, gap, blank_rows, pad_left)
    if left_delim or right_delim:
        left = util_delimiter(left_delim or ".", len(sketch), horizon)
        right = util_delimiter(right_delim or ".", len(sketch), horizon)
        sketch, horizon = util_concat(
            [left, (sketch, horizon), right])
    return sketch, horizon


def render_root(children: list) -> tuple:
    return util_vert_concat(children, [[arts.bg]], "left", pad_left=False)


def render_substack(children: list) -> tuple:
    return util_vert_concat(children, [[]], "center", pad_left=False)


def render_end(token: tuple, children: list) -> tuple:
    return [[]], 0


def render_node(node_type: str, token: tuple, children: list,
                child_nodes: list = None, nodes: list = None) -> tuple:
    if node_type not in node_data.type_info_dict.keys():
        raise ValueError(f"Undefined control sequence {token[1]}")

    rendering_info = node_data.type_info_dict[node_type][4]
    require_token = rendering_info[0]
    function_name = rendering_info[1]
    rendering_function = globals().get(function_name)

    if not callable(rendering_function):
        raise ValueError(f"Unknown Function {function_name} (internal error)")

    if function_name == "render_begin":
        return render_begin(token, children, child_nodes, nodes)
    if require_token:
        return rendering_function(token, children)
    return rendering_function(children)


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
        scripts_ids = node[3]

        children = []
        child_nodes = []
        for j in children_ids:
            children.append(canvas[j])
            child_nodes.append(nodes[j])

        scripts = []
        for j in scripts_ids:
            scripts.append((nodes[j][0], canvas[j][0]))

        sketch, horizon = render_node(
            node_type, node_token, children, child_nodes, nodes)
        child = (sketch, horizon)

        if scripts:
            child = render_apply_scripts(child, scripts)

        canvas[i] = child

        if not debug:
            continue
        print(f"{node_type}")
        for i in range(len(sketch)):
            arrow = ""
            if i == horizon:
                arrow = f"<-- horizon at {horizon}"
            print(i, "".join(sketch[i]), arrow)

    if len(canvas) == 0:
        return [[]]

    return canvas[0][0]
