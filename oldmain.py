from arrays_and_dicts import *

# Lexerizing


def get_token_type(char: str) -> str:

    if char in special_char_token_type.keys():
        return special_char_token_type[char]
    elif char in symbols:
        return "symbol"
    elif char.isalpha():
        return "letter"
    elif char.isdigit():
        return "number"
    else:
        return "other"


def combine(left_token_type: str, right_char_token_type: str) -> str:
    combined_token_type = "none"
    if (left_token_type, right_char_token_type) in combine_dict.keys():
        combined_token_type = combine_dict[(
            left_token_type, right_char_token_type)]
    return combined_token_type


def lexer_latex_expression(latex_expression: str) -> list:

    tokens = []
    tokens.append({"Val": "root", "Type": "Start"})
    token_value = ""
    token_type = "none"
    for i in range(len(latex_expression)):
        char = latex_expression[i]
        char_token_type = get_token_type(char)
        combined_token_type = combine(token_type, char_token_type)
        if not combined_token_type == "none":
            token_value += char
            token_type = combined_token_type
            if i == len(latex_expression) - 1:
                tokens.append({"Val": token_value, "Type": token_type})
            continue
        if token_value:
            tokens.append({"Val": token_value, "Type": token_type})
        token_value = char
        token_type = get_token_type(char)
        if i == len(latex_expression) - 1:
            tokens.append({"Val": token_value, "Type": token_type})
    tokens.append({"Val": "eof", "Type": "End"})

    clean_tokens = []
    for token in tokens:
        if token["Type"] == "space":
            continue
        if token["Type"] in ("command", "symbolcmd", "forcedspace"):
            token["Val"] = token["Val"][1:]
        clean_tokens.append(token)

    return clean_tokens

# Parsing


def add_to_parent_stack(token: list, i: int) -> list:
    token_type = token["Type"]
    token_val = token["Val"]
    amount_to_add = 0
    added_list = []
    if token_type == "command":
        if token_val in double_arg_cmd_vals:
            amount_to_add = 2
        elif token_val in single_arg_cmd_vals:
            amount_to_add = 1
        else:
            amount_to_add = 0
    elif token_type in single_arg_token_types:
        amount_to_add = 1
    elif token_type in atomic_token_types:
        amount_to_add = 0

    for j in range(amount_to_add):
        added_list.append(i)
    return added_list


def can_pop(token, parent) -> bool:
    token_type, token_val = token["Type"], token["Val"]
    parent_type, parent_val = parent["Type"], parent["Val"]

    if token_type == "command" and token_val in paired_cmd_vals.values():
        if parent_type != "command":
            raise ValueError(f"Unexpected command {
                             token} under parent {parent}")
        if parent_val not in paired_cmd_vals.keys():
            raise ValueError(f"Unexpected command {
                             token} under parent {parent}")
        if paired_cmd_vals[parent_val] == token_val:
            return True
        else:
            raise ValueError(f"Unexpected command {
                             token} under parent {parent}")

    elif token_type in paired_token_types.values():
        if parent_type not in paired_token_types.keys():
            raise ValueError(f"Unexpected token: {
                             token} under parent {parent}")
        if paired_token_types[parent_type] == token_type:
            return True
        else:
            raise ValueError(f"Unexpected token: {
                             token} under parent {parent}")

    elif parent_type == "script":
        if token_type == "script":
            raise ValueError("Unexpcted - consecutive script tokens")
        else:
            return True

    elif parent_type == "command":
        if parent_val in paired_cmd_vals.keys():
            if paired_cmd_vals[parent_val] != token_val:
                return False
        elif parent_val in single_arg_cmd_vals or parent_val in double_arg_cmd_vals:
            return True

    else:
        return False


def parse_tokens(tokens: list) -> list:
    parent_stack = []
    for i in range(len(tokens)):
        tokens[i]["Children"] = []
        token = tokens[i]
        if parent_stack:
            parent_id = parent_stack[-1]
            parent = tokens[parent_id]
            if can_pop(token, parent):
                parent_stack.pop()
            tokens[parent_id]["Children"].append(i)
        parent_stack += add_to_parent_stack(token, i)
        # print(i, token, parent_stack)
    # cleaning closebrac changes token indexes, messes up children list
    # clean_tokens = []
    # for token in tokens:
    #    if token["Type"] == "closebrac":
    #        continue
    #    clean_tokens.append(token)
    # return clean_tokens
    return tokens

# Rendering


def render_atomic_token(token: dict) -> tuple:
    token_type = token["Type"]
    token_val = token["Val"]
    rendered = []
    center_line = -1

    if token_type in self_replacement_token_types:
        rendered.append(token_val)
        center_line = 0
    elif token_type in paired_token_types.values():
        rendered.append("")
        center_line = 0
    elif token_type == "nonbreakingspace":
        rendered.append(" ")
        center_line = 0
    elif token_type in ("command", "symbolcmd"):
        if token_val in self_replacement_commands:
            rendered.append(token_val)
            center_line = 0
        elif token_val in single_line_commands_art.keys():
            rendered.append(single_line_commands_art[token_val])
            center_line = 0
        elif token_val in ("sum"):
            return render_sum()
        else:
            print(f"Unknown command: {token_val}, rendering as is")
            rendered.append(token_val)
            center_line = 0
    else:
        raise ValueError(f"Unknown atomic token {token}")

    return rendered, center_line


def render_vert_pile(top: list, bottom: list, sep_art: str, align: str) -> tuple:
    center_line = len(top)
    max_len = max(len(top[0]), len(bottom[0]))
    min_len = min(len(top[0]), len(bottom[0]))
    if align == "left":
        left_pad_len = 0
        right_pad_len = (max_len - min_len)
    elif align == "right":
        left_pad_len = (max_len - min_len)
        right_pad_len = 0
    elif align == "center":
        left_pad_len = (max_len - min_len) // 2
        right_pad_len = max_len - min_len - left_pad_len
    left_pad = bg_art * left_pad_len
    right_pad = bg_art * right_pad_len
    if len(top[0]) == min_len:
        for i in range(len(top)):
            top[i] = left_pad + top[i] + right_pad
    elif len(bottom[0]) == min_len:
        for i in range(len(bottom)):
            bottom[i] = left_pad + bottom[i] + right_pad
    rendered = top + [sep_art * max_len] + bottom
    return rendered, center_line


def render_frac(numerator: list, denominator: list) -> tuple:
    return render_vert_pile(numerator, denominator, frac_art, "center")


def render_sqrt(inside: dict) -> tuple:
    rendered = []
    center_line = inside["CenterLine"] + 1
    inside_rendered = inside["Rendered"]
    for row in inside_rendered:
        # rendered.append(" │" + row)
        rendered.append(sqrt_art["left_bar"] + row)
    rendered[-1] = sqrt_art["btm_left_angle"] + rendered[-1][2:]
    top_bar = sqrt_art["top_left_angle"] + \
        sqrt_art["top_bar"] * len(inside_rendered[0])
    rendered = [top_bar] + rendered
    return rendered, center_line


def render_raise(exponent: dict, rows_to_raise: int) -> tuple:
    exponent_len = len(exponent["Rendered"][0])
    rendered = exponent["Rendered"] + [bg_art * exponent_len] * rows_to_raise
    # try setting centerline to -1 and see if it works (unconvincing emoji)
    center_line = len(rendered) - 1
    return rendered, center_line


def render_lower(exponent: dict, rows_to_lower: int) -> tuple:
    exponent_len = len(exponent["Rendered"][0])
    rendered = [bg_art * exponent_len] * rows_to_lower + exponent["Rendered"]
    center_line = 0
    return rendered, center_line


def render_switch_script(script_rendered: list) -> list:
    script_switched_rendered = ""
    for char in script_rendered[0]:
        switched_char = switch_script_dict[char]
        if switched_char == " ":
            return script_rendered
        script_switched_rendered += switched_char
    return [script_switched_rendered]


def render_pile_scripts(super_script_rendered: list, sub_script_rendered: list) -> tuple:
    if len(sub_script_rendered) == 1:
        sub_script_rendered = render_switch_script(sub_script_rendered)
    if len(super_script_rendered) == 1:
        super_script_rendered = render_switch_script(super_script_rendered)

    if len(sub_script_rendered) > 1:
        sub_script_rendered = sub_script_rendered[1:]
    if len(super_script_rendered) > 1:
        super_script_rendered = super_script_rendered[:-1]
    return render_vert_pile(super_script_rendered, sub_script_rendered, bg_art, "left")


def render_format_scripts(children: list) -> list:

    for i in range(len(children)):
        child = children[i]
        child_type = child["Type"]
        child_val = child["Val"]
        if child_type != "script" or i == 0:
            continue
        base_id = i-1
        base = children[base_id]
        is_pile_script_needed = False

        if base["Type"] == "script":
            if base["Val"] == child_val:
                raise ValueError(f"Double {child_val} script")
            is_pile_script_needed = True
            neighbor_script = base
            base_id = i-2
            base = children[base_id]
            if i == 1:
                placeholder = {"Val": "none", "Type": "placeholder",
                               "Rendered": [""], "CenterLine": 0}
                base = placeholder
            if base["Type"] == "script":
                raise ValueError(f"Double {child_val} script")

        if base["Type"] == "command" and base["Val"] in ("sum"):
            is_pile_script_needed = False
            if child_val == "^":
                top = child["Rendered"]
                bottom = base["Rendered"]
                keep_center = "bottom"
            elif child_val == "_":
                top = base["Rendered"]
                bottom = child["Rendered"]
                keep_center = "top"
            base["Rendered"], base["CenterLine"] = render_new_vert_pile(
                top, bottom, keep_center, base["CenterLine"], "center")
            child["Rendered"] = [""]
            child["CenterLine"] = 0

        elif child_val == "^":
            base_h_abv = base["CenterLine"]  # ahh yes, beauty of 0 indexing
            child["Rendered"], child["CenterLine"] = render_raise(
                child, base_h_abv)
            if is_pile_script_needed:
                super_script = child
                sub_script = neighbor_script

        elif child_val == "_":
            base_h_blw = len(base["Rendered"]) - base["CenterLine"] - 1
            child["Rendered"], child["CenterLine"] = render_lower(
                child, base_h_blw)
            if is_pile_script_needed:
                sub_script = child
                super_script = neighbor_script

        if is_pile_script_needed:
            child["Rendered"], child["CenterLine"] = render_pile_scripts(
                super_script["Rendered"], sub_script["Rendered"])
            children[i-1]["Rendered"] = [""]

        children[i]["Rendered"] = child["Rendered"]
        children[i]["CenterLine"] = child["CenterLine"]
    return children


def render_concatenate(children: list) -> tuple:
    rendered = []

    children = render_format_scripts(children)

    max_h_abv_ctr = 0  # max height above center
    max_h_blw_ctr = 0

    for child in children:
        h_abv_ctr = child["CenterLine"]
        if h_abv_ctr > max_h_abv_ctr:
            max_h_abv_ctr = h_abv_ctr
        h_blw_ctr = len(child["Rendered"]) - h_abv_ctr - 1
        if h_blw_ctr > max_h_blw_ctr:
            max_h_blw_ctr = h_blw_ctr

    for i in range(max_h_abv_ctr + 1 + max_h_blw_ctr):
        rendered.append("")

    for child in children:
        h_abv_ctr = child["CenterLine"]
        h_blw_ctr = len(child["Rendered"]) - h_abv_ctr - 1
        top_pad_len = max_h_abv_ctr - h_abv_ctr
        btm_pad_len = max_h_blw_ctr - h_blw_ctr
        top_pad = [bg_art * len(child["Rendered"][0])] * top_pad_len
        btm_pad = [bg_art * len(child["Rendered"][0])] * btm_pad_len
        padded_child = top_pad + child["Rendered"] + btm_pad
        for row_num in range(len(rendered)):
            rendered[row_num] += padded_child[row_num]
    center_line = max_h_abv_ctr
    return rendered, center_line


def render_super_or_sub_script(exponent: dict, script_type: str) -> tuple:
    if script_type == "^":
        dict_id = 0
    elif script_type == "_":
        dict_id = 1

    cannot_use_unicode_scripts = False
    if len(exponent["Rendered"]) == 1:
        for char in exponent["Rendered"][0]:
            if char not in super_sub_script_art.keys():
                cannot_use_unicode_scripts = True
                break
            if super_sub_script_art[char][dict_id] == " ":
                cannot_use_unicode_scripts = True
                break
    else:
        cannot_use_unicode_scripts = True
    if cannot_use_unicode_scripts:
        if script_type == "^":
            return render_raise(exponent, 1)
        if script_type == "_":
            return render_lower(exponent, 1)

    rendered = []
    rendered.append("")
    for char in exponent["Rendered"][0]:
        rendered[0] += super_sub_script_art[char][dict_id]
    center_line = 0
    return rendered, center_line


def render_left(children: list) -> tuple:
    rendered = []
    inside, center_line = render_concatenate(children[1:-1])
    height = len(inside)
    if height == 1:
        return render_concatenate(children)
    left_rendered_before = children[0]["Rendered"][0]
    right_rendered_before = children[-1]["Rendered"][0]
    chosen_art_left = left_right_art[left_rendered_before]["left"]
    chosen_art_right = left_right_art[left_rendered_before]["right"]
    # special case when curly brac around expression with height 2
    if (left_rendered_before == "{" or right_rendered_before == "}") and height == 2:
        if center_line == 0:
            inside = [bg_art * len(inside[0])] + inside
        elif center_line == 1:
            inside = inside + [bg_art * len(inside[0])]
    for row in inside:
        left_fill = chosen_art_left["fil"]
        right_fill = chosen_art_right["fil"]
        rendered.append(left_fill + row + right_fill)
    rendered[center_line] = chosen_art_left["ctr"] + \
        rendered[center_line][1:-1] + chosen_art_right["ctr"]
    rendered[0] = chosen_art_left["top"] + \
        rendered[0][1:-1] + chosen_art_right["top"]
    rendered[-1] = chosen_art_left["btm"] + \
        rendered[-1][1:-1] + chosen_art_right["btm"]

    return rendered, center_line


def render_right(child: dict) -> tuple:
    return child["Rendered"], 0

# def render_sandwich(top: list, middle: list, bottom: list, align) -> tuple:
#     center_line = len(top) + len(center)//2
#     rendered = []
#     max_len = max(len(top[0]), len(middle[0]), len(bottom[0]))
#     for element in [top, middle, bottom]:
#         element_len = len(element[0])
#         if element_len == max_len:
#             continue
#         if align == "left":
#             left_pad_len = 0
#             right_pad_len = max_len - element_len
#         elif align == "right":
#             left_pad_len = max_len - element_len
#             right_pad_len = 0
#         elif align == "center":
#             left_pad_len = (max_len - element_len) // 2
#             right_pad_len = max_len - element_len - left_pad_len
#         left_pad = bg_art * left_pad_len
#         right_pad = bg_art * right_pad_len
#         for i in range(len(rendered)):
#             element[i] = left_pad + element[i] + right_pad
#             rendered.append(element)
#
#     return rendered, center_line


def render_new_vert_pile(top: list, bottom: list, keep_center: str, kept_center_line: int, align: str) -> tuple:
    rendered = []
    max_len = max(len(top[0]), len(bottom[0]))
    for element in [top, bottom]:
        element_len = len(element[0])
        if align == "left":
            left_pad_len = 0
            right_pad_len = max_len - element_len
        elif align == "right":
            left_pad_len = max_len - element_len
            right_pad_len = 0
        elif align == "center":
            left_pad_len = (max_len - element_len) // 2
            right_pad_len = max_len - element_len - left_pad_len
        left_pad = bg_art * left_pad_len
        right_pad = bg_art * right_pad_len
        for row in element:
            rendered.append(left_pad + row + right_pad)
    if keep_center == "bottom":
        kept_center_line += len(top)

    return rendered, kept_center_line


def render_sum() -> tuple:
    return sum_art, len(sum_art) // 2


def render_parent_token(token: dict, children: list) -> tuple:
    token_type = token["Type"]
    token_val = token["Val"]
    rendered = []
    center_line = -1
    if token["Children"]:
        if token_type == "openbrac" or token_type == "Start":
            return render_concatenate(children)
        if token_type == "script":
            return render_super_or_sub_script(children[0], token_val)
        if token_type == "command":
            if token_val == "frac":
                numerator = children[0]["Rendered"]
                denominator = children[1]["Rendered"]
                return render_frac(numerator, denominator)
            if token_val == "sqrt":
                return render_sqrt(children[0])
            if token_val == "left":
                return render_left(children)
            if token_val == "right":
                return render_right(children[0])
        else:
            raise ValueError(f"Unexpected parent token {token}")
    else:
        return render_atomic_token(token)


def render_tokens(tokens: list) -> list:
    for i in range(len(tokens)-1, -1, -1):
        children_id_list = tokens[i]["Children"]
        if children_id_list:
            children_list = []
            for j in children_id_list:
                children_list.append(tokens[j])
            rendered, center_line = render_parent_token(
                tokens[i], children_list)
        else:
            rendered, center_line = render_atomic_token(tokens[i])
        tokens[i]["Rendered"] = rendered
        tokens[i]["CenterLine"] = center_line
        # for row in rendered:
        #    print(row)
    return tokens

# Main


def render_latex_expresison(latex_expression: str):
    lexerized = lexer_latex_expression(latex_expression)
    # print("Lexerized")
    # for token in lexerized: print(token)
    parsed = parse_tokens(lexerized)
    print("Parsed")
    for i in range(len(parsed)):
        print(i, parsed[i])
    rendered = render_tokens(parsed)
    # for i in range(len(rendered)):
    #    token = rendered[i]
    #    print(f"...{i}...")
    #    for row in token["Rendered"]:
    #        print(row)
    for i in range(len(rendered[0]["Rendered"])):
        print(rendered[0]["Rendered"][i])


eqlist = [
    # r"{\frac{1}{\sqrt{n^4 + \frac{1}{n^2}}} + e_{\frac{a^2}{b^3}}}",

    # r"e^\frac{-b \pm \sqrt{b^{2a^4} - 4a c}}{2a}",
    r"\frac{-b \pm \sqrt{b^2- 4a c}}{2a}",

    # r"{x^{x^{x^{x^{x}}}}}",
    # r"{{{{x^x}^x}^x}^x}",

    # r"\frac{{\left(y_{1}-y_{4}-r\,x_{1}+r\,x_{4}-r\,y_{1}+r\,y_{2}-r\,y_{3}+r\,y_{4}+r^2\,x_{1}-r^2\,x_{2}+r^2\,x_{3}-r^2\,x_{4}\right)}^2}{4\,\left(x_{1}-x_{4}-r\,x_{1}+r\,x_{2}-r\,x_{3}+r\,x_{4}\right)\,\left(r\,x_{1}-r\,x_{4}-x_{1}\,y_{4}+x_{4}\,y_{1}-r^2\,x_{1}+r^2\,x_{2}-r^2\,x_{3}+r^2\,x_{4}+r^2\,x_{1}\,y_{3}-r^2\,x_{3}\,y_{1}-r^2\,x_{1}\,y_{4}-r^2\,x_{2}\,y_{3}+r^2\,x_{3}\,y_{2}+r^2\,x_{4}\,y_{1}+r^2\,x_{2}\,y_{4}-r^2\,x_{4}\,y_{2}-r\,x_{1}\,y_{3}+r\,x_{3}\,y_{1}+2\,r\,x_{1}\,y_{4}-2\,r\,x_{4}\,y_{1}-r\,x_{2}\,y_{4}+r\,x_{4}\,y_{2}\right)}",

    # r"e^{i\theta} = \cos\theta + i\sin\theta",

    # r"F_n = \frac{\phi^n - \psi^n}{\sqrt5}",
    # r"\phi = \frac{1+\sqrt5}2, \psi = \frac{1-\sqrt5}2",
    # r"F_n = \frac{1}{\sqrt5} \left[ \left( \frac{1+\sqrt5}2 \right) ^n - \left( \frac{1-\sqrt5}2 \right) ^n \right]",

    # r"_\LaTeX^\TeXtR",
    # r"\sum^{n=0}_k x~-~\sqrt{x}-1",
    # r"\sum^{n=0} x~-~\sqrt{x}-1",
    # r"\left\{\sqrt2\right\}",
    # r"\left( \sqrt2 \right)",
    # r"\left\{ \sqrt2 \right\}",
]
for equation in eqlist:
    print("\n\n")
    render_latex_expresison(equation)

# todo:
# - start and end tokens - done
# - \left, \right
#    - parsing done
#    - rendering done
# - \lim, \int, \sum - handled by rendering
# - \sqrt[n]{a} - change token_type of "[" after \sqrt during post lexing
# - \big
