from arrays_and_dicts import *

### Lexerizing

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

def combine(left_token_type: str , right_char_token_type: str) -> str:
    combined_token_type = "none"
    if (left_token_type, right_char_token_type) in combine_dict.keys():
        combined_token_type = combine_dict[(left_token_type, right_char_token_type)]
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

### Parsing

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

    #if token_type == "Start":
    #    return [i + 0.1]
    #elif token_type not in ["command", "script", "openbrac", "linebreak"] \
    #    or token_val in ["pm"]:
    #    return []
    #elif token_type == "script" or token_val in ["sqrt"]:
    #    return [i]
    #elif token_type == "openbrac":
    #    return [i + 0.2]
    #elif token_val == "frac":
    #    return [i, i]
    #else:
    #    raise ValueError(f"Unexpected token type: {token_type} with value: {token_val}")

def can_pop(token, parent) -> bool:
    token_type, token_val = token["Type"], token["Val"]
    parent_type, parent_val = parent["Type"], parent["Val"]

    #if parent_type != "Start" and token_type == "End":
    #    raise ValueError("Unexpected end token")
    #elif parent_type == "Start" and token_type == "End":
    #    return True

    #elif parent_type != "openbrac" and token_type == "closebrac":
    #    raise ValueError(f"Unexpected closebrac token under parent {parent}")
    #elif parent_type == "openbrac" and token_type == "closebrac":
    #    return True
    
    if parent_type == "script":
        if token_type == "script":
            raise ValueError("Unexpcted - consecutive script tokens")
        else:
            return True

    elif parent_type == "command":
        if token_val in paired_cmd_vals.values():
            if paired_cmd_vals[parent_val] == token_val:
                return True
            else:
                raise ValueError(f"Unexpected command {token} under parent {parent}")
        elif parent_val in paired_cmd_vals.keys():
            if paired_cmd_vals[parent_val] != token_val:
                return False
        elif parent_val in single_arg_cmd_vals or parent_val in double_arg_cmd_vals:
            return True

    elif token_type in paired_token_types.values():
        print(token)
        if paired_token_types[parent_type] == token_type:
            return True
        else:
            raise ValueError(f"Unexpected token: {token} under parent {parent}")

    else:
        return False

#def pop_from_parent_stack(parent_stack: list, token_type: str) -> tuple:
#    poped_id = parent_stack[-1]
#    poped_id_is_int = int(poped_id) == poped_id
#    if poped_id_is_int and token_type == "closebrac":
#        raise ValueError("Unexpected closing bracket")
#    if poped_id_is_int or token_type == "closebrac":
#        parent_stack = parent_stack[:-1]
#
#    return parent_stack, int(poped_id)

def parse_tokens(tokens: list) -> list:
    parent_stack = []
    for i in range(len(tokens)):
        tokens[i]["Children"] = []
        token = tokens[i]
        # print(i, token, parent_stack)
        #if parent_stack:
        #    parent_stack, parent_id = pop_from_parent_stack(parent_stack, token["Type"])
        #    tokens[parent_id]["Children"].append(i)
        if parent_stack:
            parent_id = parent_stack[-1]
            parent = tokens[parent_id]
            if can_pop(token, parent):
                parent_stack.pop()
            tokens[parent_id]["Children"].append(i)
        parent_stack += add_to_parent_stack(token, i)
        # print(i, token, parent_stack)
    # cleaning closebrac changes token indexes, messes up children list
    #clean_tokens = []
    #for token in tokens:
    #    if token["Type"] == "closebrac":
    #        continue
    #    clean_tokens.append(token)
    #return clean_tokens
    return tokens

### Rendering

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
        else:
            print(f"Unknown command: {token_val}, rendering as is")
            rendered.append(token_val)
            center_line = 0
    else:
        raise ValueError(f"Unknown atomic token {token}")

    return rendered, center_line

def render_frac(numerator: list, denominator: list) -> tuple:
    center_line = len(numerator)
    max_len = max(len(numerator[0]), len(denominator[0]))
    min_len = min(len(numerator[0]), len(denominator[0]))
    left_pad_len = (max_len - min_len) // 2
    right_pad_len = max_len - min_len - left_pad_len
    if len(numerator[0]) == min_len:
        for i in range(len(numerator)):
            numerator[i] = bg_art * left_pad_len + numerator[i] + bg_art * right_pad_len
    elif len(denominator[0]) == min_len:
        for i in range(len(denominator)):
            denominator[i] = bg_art * left_pad_len + denominator[i] + bg_art * right_pad_len
    rendered = numerator + [frac_art * max_len] + denominator
    return rendered, center_line

def render_sqrt(inside: dict) -> tuple:
    rendered = []
    center_line = inside["CenterLine"] + 1
    inside_rendered = inside["Rendered"]
    for row in inside_rendered :
        #rendered.append(" │" + row)
        rendered.append(sqrt_art["left_bar"] + row)
    rendered[-1] = sqrt_art["btm_left_angle"] + rendered[-1][2:]
    top_bar = sqrt_art["top_left_angle"] + sqrt_art["top_bar"] * len(inside_rendered[0])
    rendered = [top_bar] + rendered
    return rendered, center_line

def render_raise(exponent: dict, rows_to_raise: int) -> tuple:
    exponent_len = len(exponent["Rendered"][0])
    rendered = exponent["Rendered"] + [bg_art * exponent_len] * rows_to_raise
    center_line = len(rendered) - 1 # try setting centerline to -1 and see if it works (unconvincing emoji)
    return rendered, center_line

def render_lower(exponent: dict, rows_to_lower: int) -> tuple:
    exponent_len = len(exponent["Rendered"][0])
    rendered =  [bg_art * exponent_len] * rows_to_lower + exponent["Rendered"]
    center_line = 0
    return rendered, center_line

def render_concatenate(children: list) -> tuple:
    rendered = []

    # raise or lower child if it is a script placed
    # after a multiline token (calling it base in this case)
    for i in range(len(children)):
        child = children[i]
        if child["Type"] != "script":
            continue
        if i == 0:
            continue
        if len(children[i-1]["Rendered"]) == 1:
            continue
        # if a script placed after a multi line base
        if child["Val"] == "^":
            base_h_abv = children[i-1]["CenterLine"] # ahh yes, beauty of 0 indexing
            chiled_rendered, child_center_line = render_raise(child, base_h_abv)
            children[i]["Rendered"] = chiled_rendered
            children[i]["CenterLine"] = child_center_line
        if child["Val"] == "_":
            base_h_blw = len(children[i-1]["Rendered"]) - children[i-1]["CenterLine"] - 1
            chiled_rendered, child_center_line = render_lower(child, base_h_blw)
            children[i]["Rendered"] = chiled_rendered
            children[i]["CenterLine"] = child_center_line

    max_h_abv_ctr = 0 # max height above center
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
    left_rendered_before = children[0]["Rendered"][0]
    right_rendered_before = children[-1]["Rendered"][0]
    if height == 1:
        return render_concatenate(children)
    chosen_art_left = left_right_art[left_rendered_before]["left"]
    chosen_art_right = left_right_art[left_rendered_before]["right"]
    for row in inside:
        left_fill = chosen_art_left["fil"]
        right_fill = chosen_art_right["fil"]
        rendered.append(left_fill + row + right_fill)
    rendered[0] = chosen_art_left["top"] + rendered[0][1:-1] + chosen_art_right["top"]
    rendered[-1] = chosen_art_left["btm"] + rendered[-1][1:-1] + chosen_art_right["btm"]
    rendered[center_line] = chosen_art_left["ctr"] + rendered[center_line][1:-1] + chosen_art_right["ctr"]

    return rendered, center_line

def render_right(child: dict) -> tuple:
    return child["Rendered"], 0
    
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
            rendered, center_line = render_parent_token(tokens[i], children_list)
        else:
            rendered, center_line = render_atomic_token(tokens[i])
        tokens[i]["Rendered"] = rendered
        tokens[i]["CenterLine"] = center_line
        #for row in rendered:
        #    print(row)
    return tokens

### Main

def render_latex_expresison(latex_expression: str):
    lexerized = lexer_latex_expression(latex_expression)
    #print("Lexerized")
    #for token in lexerized: print(token)
    parsed = parse_tokens(lexerized)
    #print("Parsed")
    #for i in range(len(parsed)): print(i, parsed[i])
    rendered = render_tokens(parsed)
    #for i in range(len(rendered)):
    #    token = rendered[i]
    #    print(f"...{i}...")
    #    for row in token["Rendered"]:
    #        print(row)
    for i in range(len(rendered[0]["Rendered"])): print(rendered[0]["Rendered"][i])


eqlist = [
    #r"{\frac{1}{\sqrt{n^4 + \frac{1}{n^2}}} + e_{\frac{a^2}{b^3}}}",
    #r"e^\frac{-b \pm \sqrt{b^{2a^4} - 4a c}}{2a}"
    #r"{x^x^x^x^x}",
    #r"{x^{x^{x^{x^{x}}}}}",
    #r"{{{{x^x}^x}^x}^x}",
    #r"\sqrt[\frac{\frac12}{\frac34}+sum_\frac12^{abc}x^2]{2}",
    #r"a(b + c)d + \frac\sqrt{2_{4+4}}{3^{2(x-3)}}",
    #r"\{\ a~\}",
    #r"e^{i\theta} = \cos\theta + i\sin\theta",
    #r"\left|a+\sqrt{\frac12}\right|",
    #r"\frac{{\left(y_{1}-y_{4}-r\,x_{1}+r\,x_{4}-r\,y_{1}+r\,y_{2}-r\,y_{3}+r\,y_{4}+r^2\,x_{1}-r^2\,x_{2}+r^2\,x_{3}-r^2\,x_{4}\right)}^2}{4\,\left(x_{1}-x_{4}-r\,x_{1}+r\,x_{2}-r\,x_{3}+r\,x_{4}\right)\,\left(r\,x_{1}-r\,x_{4}-x_{1}\,y_{4}+x_{4}\,y_{1}-r^2\,x_{1}+r^2\,x_{2}-r^2\,x_{3}+r^2\,x_{4}+r^2\,x_{1}\,y_{3}-r^2\,x_{3}\,y_{1}-r^2\,x_{1}\,y_{4}-r^2\,x_{2}\,y_{3}+r^2\,x_{3}\,y_{2}+r^2\,x_{4}\,y_{1}+r^2\,x_{2}\,y_{4}-r^2\,x_{4}\,y_{2}-r\,x_{1}\,y_{3}+r\,x_{3}\,y_{1}+2\,r\,x_{1}\,y_{4}-2\,r\,x_{4}\,y_{1}-r\,x_{2}\,y_{4}+r\,x_{4}\,y_{2}\right)}",
    #r" \left\{ \frac{a + b}{\sqrt{c}} \right\}^3 ",
    r"F_n = \frac{\phi^n - \psi^n}{\sqrt5}",
    r"\phi = \frac{1+\sqrt5}2, \psi = \frac{1-\sqrt5}2",
    r"F_n = \frac{1}{\sqrt5} \left[ \left( \frac{1+\sqrt5}2 \right) ^n - \left( \frac{1-\sqrt5}2} \right) ^n \right]",
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
