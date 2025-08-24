special_chars = r" ^_{}[]~"

symbol_chars = """`!@#$%&*()+-=|;:'",.<>/?"""

symbols = special_chars + symbol_chars


def get_char_type(char: str) -> str:
    if char.isalpha():
        return "alph"
    elif char.isdigit():
        return "numb"
    elif char in symbols:
        return "symb"
    elif char == "\\":
        return "backslash"


def lexer(tex: str, debug: bool) -> list:
    tex = tex.replace('\n', ' ').replace('\r', ' ')
    if debug:
        print("Lexerizing")
        print(tex)
    tokens = []
    token_type, token_val = "", ""
    for i in range(len(tex)):
        char = tex[i]
        char_type = get_char_type(char)
        token_val += char
        is_final_char = i == len(tex) - 1
        if len(token_val) > 1 and token_val[0] == "\\":
            if not is_final_char and (
                    char_type == get_char_type(tex[i+1]) and
                    char_type != "symb"):
                continue
            else:
                token_val = token_val[1:]
        elif token_val == "\\":
            token_type = "cmnd"
            if is_final_char:
                raise ValueError(f"Unexpexted character {char}")
            continue
        elif token_val == "$":
            token_type = "symb"
            if (not is_final_char) and tex[i+1] == "$":
                continue
        else:
            token_type = char_type
        if token_type == "symb" and token_val == " ":
            token_val, token_type = "", ""
            continue
        tokens.append((token_type, token_val))
        token_type, token_val = "", ""
        if debug and tokens:
            print(i, tokens[-1])
    if tokens[0] not in (("cmnd", "["), ("cmnd", "("),
                         ("symb", "$"), ("symb", "$$")):
        tokens.insert(0, ("meta", "startline"))
        tokens.append(("meta", "endline"))
    tokens.insert(0, ("meta", "start"))
    tokens.append(("meta", "end"))
    if debug:
        for i in range(len(tokens)):
            print(i, tokens[i])
    return tokens
