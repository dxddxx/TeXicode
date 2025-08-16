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


def lexer(tex: str) -> list:
    tokens = []
    token_type, token_val = "", ""
    for i in range(len(tex)):
        char = tex[i]
        char_type = get_char_type(char)
        token_val += char
        if len(token_val) > 1:
            if (i == len(tex)-1 or
                    char_type != get_char_type(tex[i+1]) or
                    char_type == "symb"):
                token_val = token_val[1:]
                token_type = "cmnd"
        elif token_val != "\\":
            token_type = char_type
        else:
            token_type = ""

        if token_type:
            if token_type == "symb" and token_val == " ":
                token_val, token_type = "", ""
                continue
            tokens.append((token_type, token_val))
            token_type, token_val = "", ""
    tokens.insert(0, ("meta", "start"))
    tokens.append(("meta", "end"))
    return tokens
