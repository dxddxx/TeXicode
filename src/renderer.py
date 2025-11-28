import node_data
import arts
import symbols_art

def util_revert_font(char: str) -> str:
    """No change to logic, operates on single character strings"""
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
        new_row = []  # Changed: list instead of string
        for char in row:
            char = util_revert_font(char)
            if char not in arts.alphabets["normal"]:
                new_row.append(char)  # Changed: append instead of +=
                continue
            if 'A' <= char <= 'Z':
                alpha_id = ord(char) - ord('A')
            elif 'a' <= char <= 'z':
                alpha_id = ord(char) - ord('a') + 26
            new_row.append(arts.font[font_val][alpha_id])  # Changed: append
        new_sketch.append(new_row)
    return new_sketch, horizon

def util_unshrink(small_char: str) -> str:
    """No change to logic"""
    for char, scripts in arts.unicode_scripts.items():
        if small_char in scripts:
            return char
    return small_char

def util_concat(children: list, concat_line: bool, align_amp: bool) -> tuple:
    concated_sketch = []
    maxh_sky = 0
    maxh_ocn = 0
    contain_amp = False
    
    for sketch, horizon in children:
        if horizon == -1:
            contain_amp = True
            if not align_amp:
                raise ValueError(f"Unexpected {sketch}")
            continue
        h_sky = horizon
        h_ocn = len(sketch) - h_sky - 1
        if h_sky > maxh_sky:
            maxh_sky = h_sky
        if h_ocn > maxh_ocn:
            maxh_ocn = h_ocn
            
    concated_horizon = maxh_sky
    for i in range(maxh_sky + 1 + maxh_ocn):
        concated_sketch.append([])  # Changed: empty list instead of string
        
    for sketch, horizon in children:
        if horizon == -1:
            if not align_amp:
                raise ValueError(f"Unexpected {sketch}")
            concated_horizon = len(concated_sketch[0])
            continue
            
        h_sky = horizon
        h_ocn = len(sketch) - h_sky - 1
        top_pad_len = maxh_sky - h_sky
        btm_pad_len = maxh_ocn - h_ocn
        
        # Changed: create list of background cells
        top_pad = [[arts.bg] * len(sketch[0]) for _ in range(top_pad_len)]
        btm_pad = [[arts.bg] * len(sketch[0]) for _ in range(btm_pad_len)]
        
        sketch = top_pad + sketch + btm_pad
        for i in range(len(concated_sketch)):
            concated_sketch[i].extend(sketch[i])  # Changed: extend instead of +=
            
    if concat_line and not contain_amp:
        concated_horizon = len(concated_sketch[0])
    return concated_sketch, concated_horizon

def util_vert_pile(top, ctr, ctr_horizon, btm, align) -> tuple:
    piled_sketch = []
    piled_horizon = len(top) + ctr_horizon
    
    # Changed: compare to list with empty list
    if top == [[]]:
        piled_horizon -= 1
    if ctr == [[]]:
        piled_horizon -= 1
        
    if piled_horizon < 0:
        piled_horizon = 0
        
    max_len = max(len(top[0]), len(ctr[0]), len(btm[0]))
    
    for sketch in (top, ctr, btm):
        if sketch == [[]]:  # Changed: compare to list with empty list
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
            
        # Changed: create list of background cells
        left_pad = [arts.bg] * left_pad_len
        right_pad = [arts.bg] * right_pad_len
        
        for row in sketch:
            piled_sketch.append(left_pad + row + right_pad)

    if piled_sketch == []:
        piled_sketch = [[]]
            
    return piled_sketch, piled_horizon

def util_script(children: list, script_type_id: int) -> tuple:
    sketch, horizon = children[0]
    shrunk = util_shrink(sketch, script_type_id, False, False)
    if shrunk != []:
        return shrunk, 0
        
    smart_shrunk = util_shrink(sketch, 1 - script_type_id, True, False)
    if smart_shrunk != []:
        sketch = smart_shrunk
        
    top = [[]]  # Changed: list with empty list
    btm = [[]]  # Changed: list with empty list
    
    if script_type_id == 0:
        top = sketch
    elif script_type_id == 1:
        btm = sketch
        
    return util_vert_pile(top, [[arts.bg]], 0, btm, "left")  # Changed: wrap bg in list

def util_shrink(sketch: list, script_type_id: int,
                smart: bool, switch: bool) -> list:
    invert_script_type_id = 1 - script_type_id
    if len(sketch) != 1:
        return []
        
    art = arts.unicode_scripts
    shrunk_row = []  # Changed: list instead of string
    
    for char in sketch[0]:
        char = util_revert_font(char)
        unshrunk_char = util_unshrink(char)
        
        if unshrunk_char not in art.keys():
            return []
            
        if art[unshrunk_char][script_type_id] == char:
            return []
            
        if art[unshrunk_char][invert_script_type_id] == char:
            if smart:
                shrunk_row.append(char)  # Changed: append
                continue
            if switch:
                shrunk_row.append(art[unshrunk_char][script_type_id])  # Changed: append
                continue
            return []
            
        shrunk_char = art[unshrunk_char][script_type_id]
        if shrunk_char != " " or char == " ":
            shrunk_row.append(shrunk_char)  # Changed: append
            continue
            
        return []
        
    return [shrunk_row]

def util_get_pile_center(base_height, base_horizon) -> tuple:
    if base_height == 2:
        if base_horizon == 0:
            return [[]], 0  # Changed: list with empty list
        if base_horizon == 1:
            return [[]], 1  # Changed: list with empty list
            
    if base_height == 1:
        return [], 0
        
    # Note: This second condition is unreachable in original code (bug)
    if base_height == 1:
        return [[]], 0  # Changed: list with empty list
        
    pile_center_sketch = []
    for _ in range(base_height - 2):
        pile_center_sketch.append([arts.bg])  # Changed: wrap in list
        
    pile_center_horizon = base_horizon - 1
    return pile_center_sketch, pile_center_horizon

def util_delimiter(delim_type, height: int, horizon: int) -> tuple:
    if delim_type == ".":
        return [[]], 0  # Changed: list with empty list
        
    art_col = arts.delimiter["sgl"].find(delim_type[0])
    if art_col == -1:
        raise ValueError(f"Invalid delimiter type {delim_type}")
        
    delim_art = dict()
    for pos in arts.delimiter:
        art = arts.delimiter[pos]
        delim_art[pos] = art[art_col]  # Single character
        
    if height == 1:
        return [delim_type], 0  # Changed: wrap in list
        
    if height == 2 and delim_type in ["{", "}"]:
        height = 3
        if horizon == 0:
            horizon = 1
            
    center = horizon
    if center == 0:
        center = 1
    if center == height - 1:
        center = height - 2
        
    sketch = []
    for _ in range(height):
        sketch.append([delim_art["fil"]])  # Changed: wrap in list
        
    sketch[center] = [delim_art["ctr"]]  # Changed: wrap in list
    sketch[0] = [delim_art["top"]]  # Changed: wrap in list
    sketch[-1] = [delim_art["btm"]]  # Changed: wrap in list
    
    return sketch, horizon

def util_add_ampersand_padding(children: list) -> tuple:
    padded_children = []
    max_amp_pos = 0
    
    for sketch, amp_pos in children:
        if amp_pos > max_amp_pos:
            max_amp_pos = amp_pos
            
    for sketch, amp_pos in children:
        padded_sketch = []
        pad_len = max_amp_pos - amp_pos
        padding = [arts.bg] * pad_len  # Changed: list multiplication
        
        for row in sketch:
            padded_sketch.append(padding + row)  # Changed: list concatenation
            
        padded_children.append((padded_sketch, amp_pos))
        
    return padded_children

def util_vert_concat(children: list, sep: list, align: str) -> tuple:
    if children[0][1] != -2:
        children = util_add_ampersand_padding(children)
        
    sketch = children.pop(0)[0]
    horizon = 0
    
    for child in children:
        top = sketch
        btm = child[0]
        sketch, horizon = util_vert_pile(top, sep, 0, btm, align)
        
    return sketch, horizon

# Rendering functions - minimal changes, just wrapping literals
def render_font(token: str, children: list) -> tuple:
    return util_font(token[1], children)

def render_text_info(token: tuple, children: list) -> tuple:
    return [[token[1]]], 0  # Changed: wrap in list

def render_text(token: str, children: list) -> tuple:
    return util_font(token[1], children)

def render_leaf(token: tuple, children: list) -> tuple:
    token_type = token[0]
    token_val = token[1]
    horizon = 0
    
    if token_type == "numb":
        return [[token_val]], horizon  # Changed: wrap in list
        
    elif token_type == "symb":
        if token_val == "&":
            return [["&"]], -1  # Changed: wrap in list
        if token_val in arts.simple_symbols:
            return [[token_val]], horizon  # Changed: wrap in list
        elif token_val in arts.special_symbols.keys():
            return arts.special_symbols[token_val], horizon  # Already a list
            
    elif token_type == "alph":
        return util_font("mathnormal", [([[token_val]], 0)])  # Changed: wrap in list
        
    elif token_type == "cmnd":
        if token_val in arts.multi_line_leaf_commands.keys():
            return arts.multi_line_leaf_commands[token_val]  # Already converted
        elif token_val in symbols_art.symbols.keys():
            return [symbols_art.symbols[token_val]], horizon  # Changed: wrap in list
        else:
            return [["?"]], 0  # Changed: wrap in list

def render_concat(children: list) -> tuple:
    return util_concat(children, False, False)

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

def render_apply_scripts(base_sketch, base_horizon, scripts: list) -> tuple:
    sorted_scripts = [[[]], [[]]]  # Changed: lists with empty lists
    base_position = "left"
    
    for script_type, script_sketch in scripts:
        if script_type in {"top_scrpt", "btm_scrpt"}:
            base_position = "center"
        script_position = 0
        if script_type in {"sub_scrpt", "btm_scrpt"}:
            script_position = 1
        if sorted_scripts[script_position] != [[]]:  # Changed: compare to [[]]
            script_type_name = ["super", "sub"][script_position]
            raise ValueError(f"Double {script_type_name}scripts")
        sorted_scripts[script_position] = script_sketch
        
    top, btm = sorted_scripts
    base = (base_sketch, base_horizon)
    
    if base_position == "center":
        return util_vert_pile(top, base_sketch, base_horizon, btm, "center")
        
    ctr, ctr_horizon = util_get_pile_center(len(base_sketch), base_horizon)
    if ctr != []:
        piled_scripts = util_vert_pile(top, ctr, ctr_horizon, btm, "left")
        return util_concat([base, piled_scripts], False, False)
        
    if top == [[]]:  # Changed: compare to [[]]
        return util_concat([base, (btm, 0)], False, False)
    if btm == [[]]:  # Changed: compare to [[]]
        return util_concat([base, (top, len(top)-1)], False, False)
        
    if len(top) > 1:
        top.pop()
        ctr = [[]]  # Changed: list with empty list
        ctr_horizon = 1
    elif len(btm) > 1:
        btm.pop(0)
        ctr = [[]]  # Changed: list with empty list
    elif len(top) == 1 and len(btm) == 1:
        top = util_shrink(top, 1, False, True)
        btm = util_shrink(btm, 0, False, True)
        ctr = [[arts.bg]]  # Changed: wrap in list
        
    piled_scripts = util_vert_pile(top, ctr, ctr_horizon, btm, "left")
    return util_concat([base, piled_scripts], False, False)

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
    inside = util_concat(children[1:-1], False, False)
    left_delim_type = children[0][0][0]
    right_delim_type = children[-1][0][0]
    height = len(inside[0])
    horizon = inside[1]
    left = util_delimiter(left_delim_type, height, horizon)
    right = util_delimiter(right_delim_type, height, horizon)
    return util_concat([left, inside, right], False, False)

def render_close_delimiter(children: list) -> tuple:
    return children[0]

def render_binomial(children: list) -> tuple:
    n, r = children[0][0], children[1][0]
    sep_space = [arts.bg] * max(len(n[0]), len(r[0]))  # Changed: list comprehension
    piled = util_vert_pile(n, [sep_space], 0, r, "center")
    return render_open_delimiter([(["("], 0), piled, ([")"], 0)])

def render_fraction(children: list) -> tuple:
    numer, denom = children[0][0], children[1][0]
    art = arts.fraction
    fraction_line = [art[1]] * max(len(numer[0]), len(denom[0]))  # Changed: list
    fraction_line = [art[0]] + fraction_line + [art[2]]  # Changed: list concatenation
    return util_vert_pile(numer, [fraction_line], 0, denom, "center")

def render_accents(token: tuple, children: list) -> tuple:
    accent_val = token[1]
    # import unicodedata
    u_hex = {"acute": "\u0302", "bar": "\u0304", "breve": "\u0306",
             "check": "\u030C", "ddot": "\u0308", "dot": "\u0307",
             "grave": "\u0300", "hat": "\u0302", "mathring": "\u030A",
             "tilde": "\u0303", "vec": "\u20D7", "widehat": "\u0302",
             "widetilde": "\u0360"}[accent_val]
    sketch = children[0][0]
    first_char = sketch[0][0] + u_hex
    # first_char = unicodedata.normalize("NFKC", first_char)
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

    if len(children) <= 1:
        return [new_radi_row], radicand_horizon

    degree = util_script(children, 0)
    sketch_degreed, horizon_degreed = util_concat([degree, ([new_radi_row], 0)], False, False)

    return sketch_degreed, horizon_degreed


def util_multichar_square_root(children: list) -> tuple:
    degree_sketch, degree_horizon = children[0]
    radicand_sketch, radicand_horizon = children[-1]

    art = arts.square_root
    
    top_bar = art["top_bar"] * len(radicand_sketch[0])
    sqrt_sketch = [top_bar] + radicand_sketch
    
    for i in range(len(sqrt_sketch)):
        sqrt_sketch[i] = art["left_bar"] + sqrt_sketch[i] + [arts.bg]  # Changed
    
    sqrt_sketch[0] = art["top_angle"] + sqrt_sketch[0][2:-1] + art["top_tail"]  # Changed
    sqrt_sketch[-1] = art["btm_angle"] + sqrt_sketch[-1][2:]  # Changed
    
    if len(children) == 1 or len(degree_sketch) > 1:
        return sqrt_sketch, radicand_horizon + 1
        
    shrinked_degree = util_shrink(degree_sketch, 1, False, False)
    if shrinked_degree == []:
        shrinked_degree = degree_sketch
        
    if sqrt_sketch[-2][0] == " ":
        sqrt_sketch[-2] = [shrinked_degree[0][-1]] + sqrt_sketch[-2][1:]  # Changed
        shrinked_degree[0] = shrinked_degree[0][:-1]
        
    left_pad = [arts.bg] * len(shrinked_degree[0])  # Changed
    
    for i in range(len(sqrt_sketch)):
        if i == len(sqrt_sketch) - 2:
            sqrt_sketch[i] = shrinked_degree[0] + sqrt_sketch[i]  # Changed
            continue
        sqrt_sketch[i] = left_pad + sqrt_sketch[i]  # Changed
        
    return sqrt_sketch, radicand_horizon + 1


def render_square_root(children: list) -> tuple:
    degree_sketch, degree_horizon = children[0]
    radicand_sketch, radicand_horizon = children[-1]

    # if len(radicand_sketch) == 1:
    # someone said parenthesis is uncleaer, agreed.
    if len(radicand_sketch[0]) <= 1 and len(radicand_sketch) == 1:
        return util_onechar_square_root(children)
    else:
        return util_multichar_square_root(children)

def render_concat_line_align_amp(children: list) -> tuple:
    return util_concat(children, True, True)

def render_concat_line_no_align_amp(children: list) -> tuple:
    line_sketch = util_concat(children, True, False)[0]
    return line_sketch, -2

def render_begin(children: list):
    if children[0][0] in ([['a', 'l', 'i', 'g', 'n']], [['a', 'l', 'i', 'g', 'n', '*']]):
        return util_concat(children[1:], True, True)
    else:
        return render_concat_line_no_align_amp(children[1:])

def render_root(children: list) -> tuple:
    return util_vert_concat(children, [[arts.bg]], "left")  # Changed: wrap bg

def render_substack(children: list) -> tuple:
    return util_vert_concat(children, [[]], "center")  # Changed: empty list

def render_end(children: list):
    return children[0]

def render_node(node_type: str, token: tuple, children: list) -> tuple:
    if node_type not in node_data.type_info_dict.keys():
        raise ValueError(f"Undefined control sequence {token[1]}")
        
    rendering_info = node_data.type_info_dict[node_type][4]
    require_token = rendering_info[0]
    function_name = rendering_info[1]
    rendering_function = globals().get(function_name)
    
    if not callable(rendering_function):
        raise ValueError(f"Unknown Function {function_name} (internal error)")
        
    if require_token:
        return rendering_function(token, children)
    else:
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
        children = []
        for j in children_ids:
            children.append(canvas[j])
            
        scripts_ids = node[3]
        scripts = []
        for j in scripts_ids:
            scripts.append((nodes[j][0], canvas[j][0]))
            
        sketch, horizon = render_node(node_type, node_token, children)
        
        if scripts:
            sketch, horizon = render_apply_scripts(sketch, horizon, scripts)
            
        canvas[i] = (sketch, horizon)
        
        if debug:
            print(f"{node_type}, horizon at {horizon}")
            for i in range(len(sketch)):
                arrow = ""
                if i == horizon:
                    arrow = "<--"
                # Changed: join list into string for display
                print(i, sketch[i], arrow)
                print(i, "".join(sketch[i]), arrow)
                
    if len(canvas) == 0:
        return [[]]  # Changed: return list with empty list
        
    return canvas[0][0]  # Now returns list[list[str]]
