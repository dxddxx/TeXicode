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
    #tokens.append({"Val": "root", "Type": "Start"})
    token_value = ""
    token_type = "none"
    for i in range(len(latex_expression)):
        char = latex_expression[i]
        char_token_type = get_token_type(char)
        combined_token_type = combine(token_type, char_token_type)
        if not combined_token_type == "none":
            token_value += char
            token_type = combined_token_type
            continue
        if token_value:
            tokens.append({"Val": token_value, "Type": token_type})
        token_value = char
        token_type = get_token_type(char)
        if i == len(latex_expression) - 1:
            tokens.append({"Val": token_value, "Type": token_type})
    #tokens.append({"Val": "eof", "Type": "End"})

    clean_tokens = []
    for token in tokens:
        if token["Type"] == "space":
            continue
        if token["Type"] in ("command", "symbolcmd"):
            token["Val"] = token["Val"][1:]
        clean_tokens.append(token)

    return clean_tokens

### Parsing

def add_to_parent_stack(token: list, i: int) -> list:
    token_type = token["Type"]
    token_val = token["Val"]
    if token_type == "Start":
        return [i + 0.1]
    elif token_type not in ["command", "script", "openbrac", "linebreak"] \
        or token_val in ["pm"]:
        return []
    elif token_type == "script" or token_val in ["sqrt"]:
        return [i]
    elif token_type == "openbrac":
        return [i + 0.2]
    elif token_val == "frac":
        return [i, i]
    else:
        raise ValueError(f"Unexpected token type: {token_type} with value: {token_val}")

def pop_from_parent_stack(parent_stack: list, token_type: str) -> tuple:
    poped_id = parent_stack[-1]
    poped_id_is_int = int(poped_id) == poped_id
    if poped_id_is_int and token_type == "closebrac":
        raise ValueError("Unexpected closing bracket")
    if poped_id_is_int or token_type == "closebrac":
        parent_stack = parent_stack[:-1]

    return parent_stack, int(poped_id)

def parse_tokens(tokens: list) -> list:
    parent_stack = []
    for i in range(len(tokens)):
        tokens[i]["Children"] = []
        token = tokens[i]

        if parent_stack:
            parent_stack, parent_id = pop_from_parent_stack(parent_stack, token["Type"])
            tokens[parent_id]["Children"].append(i)

        parent_stack += add_to_parent_stack(token, i)

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

    if token_type in ["letter", "number", "symbol"]:
        rendered.append(token_val)
        center_line = 0
    if token_type == "closebrac":
        rendered.append("")
        center_line = 0
    if token_type == "command":
        if token_val in self_replacement_commands:
            rendered.append(token_val)
            center_line = 0
        elif token_val in single_line_commands_art.keys():
            rendered.append(single_line_commands_art[token_val])
            center_line = 0
        else:
            rendered.append(token_val)
            center_line = 0

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

    # raise or lower child if it is a muiltiline script
    # placed after a multiline token (calling it base in this case)
    for i in range(len(children)):
        child = children[i]
        if child["Type"] != "script":
            continue
        if i == 0:
            continue
        #if len(child["Rendered"]) == 1:
        #    continue
        if len(children[i-1]["Rendered"]) == 1:
            continue
        # if a multi line script placed after a multi line base
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
    
def render_parent_token(token: dict, children: list) -> tuple:
    token_type = token["Type"]
    token_val = token["Val"]
    rendered = []
    center_line = -1
    if token_val == "frac":
        numerator = children[0]["Rendered"]
        denominator = children[1]["Rendered"]
        return render_frac(numerator, denominator)
    if token_val == "sqrt":
        return render_sqrt(children[0])
    if token_type == "openbrac":
        return render_concatenate(children)
    if token_type == "script":
        return render_super_or_sub_script(children[0], token_val)
    else:
        return render_atomic_token(token)


def render_tokens(tokens: list) -> list:
    for i in range(len(tokens)-1, -1, -1):
        children_id_list = tokens[i]["Children"]
        if not children_id_list:
            rendered, center_line = render_atomic_token(tokens[i])
        else:
            children_list = []
            for j in children_id_list:
                children_list.append(tokens[j])
            rendered, center_line = render_parent_token(tokens[i], children_list)
        tokens[i]["Rendered"] = rendered
        tokens[i]["CenterLine"] = center_line
    return tokens

### Main

def render_latex_expresison(latex_expression: str):
    lexerized = lexer_latex_expression(latex_expression)
    parsed = parse_tokens(lexerized)
    #for token in parsed: print(token)
    rendered = render_tokens(parsed)
    #for token in rendered:
    #    print("...")
    #    for row in token["Rendered"]:
    #        print(row)
    for i in range(len(rendered[0]["Rendered"])): print(rendered[0]["Rendered"][i])


quadratic_equation = r"{e^\frac{-b \pm \sqrt{b^{2a^4} - 4a c}}{2a}}"
quadratic_equation = r"{f(x) = 1 + x^2 + x^3 + x^{(1+\frac12)}}"
quadratic_equation = r"{ \frac{\sqrt{a^2 + b^2}}{c^3} }"
quadratic_equation = r"{ \frac{\sqrt{x^4 + 4y^2}}{z^{1/2}} + \frac{y^3}{\sqrt{2x}} }"
quadratic_equation = r"{ \frac{1}{\sqrt{\frac{x^2}{y^2} + \frac{z^3}{w}}} }"
quadratic_equation = r"{ {( \frac{a + b}{\sqrt{c}} )}^3}"
#quadratic_equation = r"{  }"
#quadratic_equation = r"{\frac{{(y_{1}-y_{4}-r\,x_{1}+r\,x_{4}-r\,y_{1}+r\,y_{2}-r\,y_{3}+r\,y_{4}+r^2\,x_{1}-r^2\,x_{2}+r^2\,x_{3}-r^2\,x_{4})}^2}{4\,(x_{1}-x_{4}-r\,x_{1}+r\,x_{2}-r\,x_{3}+r\,x_{4})\,(r\,x_{1}-r\,x_{4}-x_{1}\,y_{4}+x_{4}\,y_{1}-r^2\,x_{1}+r^2\,x_{2}-r^2\,x_{3}+r^2\,x_{4}+r^2\,x_{1}\,y_{3}-r^2\,x_{3}\,y_{1}-r^2\,x_{1}\,y_{4}-r^2\,x_{2}\,y_{3}+r^2\,x_{3}\,y_{2}+r^2\,x_{4}\,y_{1}+r^2\,x_{2}\,y_{4}-r^2\,x_{4}\,y_{2}-r\,x_{1}\,y_{3}+r\,x_{3}\,y_{1}+2\,r\,x_{1}\,y_{4}-2\,r\,x_{4}\,y_{1}-r\,x_{2}\,y_{4}+r\,x_{4}\,y_{2})}}"
#quadratic_equation = r"\sqrt{b^2 - 4ac}"
#quadratic_equation = r"{b^2 - 4ac}"
#quadratic_equation = r"{-4ac}"
#quadratic_equation = r"{b^2}"
#quadratic_equation = r"^2"
#quadratic_equation = r"\frac1\frac21"
#quadratic_equation = r"{\frac{dy}{dx}\sqrt{abc\frac{1}{2a\sqrt2}}}"
#quadratic_equation = r"\frac12"
#quadratic_equation = r"{f(x) = 1 + \frac{x}{1 + x} }"
#quadratic_equation = r"{\sqrt{1 + \sqrt{1 + \frac{x}{2}}} }"
#quadratic_equation = r"{psi = 1 + \frac{1}{1 + \frac{1}{1 + \frac{1}{1 + \frac{1}{1 + ...}}}} }"
render_latex_expresison(quadratic_equation)
eqlist = [
    r"{\frac{1}{\sqrt{n^4 + \frac{1}{n^2}}} + e_{\frac{a^2}{b^3}}}",
    r"{x^x^x^x^x}",
    r"{x^{x^{x^{x^{x}}}}}",
    r"{{{{x^x}^x}^x}^x}",
    r"{}",
    ]
for equation in eqlist:
    print("\n\n")
    render_latex_expresison(equation)
