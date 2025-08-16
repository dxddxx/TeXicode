special_chars = r" ^_{}[]~"

symbol_chars = """`!@#$%&*()+-=|;:'",.<>/?"""

symbols = special_chars + symbol_chars


def get_char_type(char: str) -> str:
    if char.isalpha():
        return "letter"
    elif char.isdigit():
        return "number"
    elif char in symbols:
        return "symbol"
    elif char == "\\":
        return "backslash"


def lexer(tex: str) -> list:
    tokens = []
    token_val, token_type = "", ""
    for i in range(len(tex)):
        char = tex[i]
        char_type = get_char_type(char)
        token_val += char
        if len(token_val) > 1:
            if (i == len(tex)-1 or
                    char_type != get_char_type(tex[i+1]) or
                    char_type == "symbol"):
                token_val = token_val[1:]
                token_type = "command"
        elif token_val != "\\":
            token_type = char_type
        else:
            token_type = ""
        print(i, char, token_type)

        if token_type:
            if token_type == "symbol" and token_val == " ":
                token_val, token_type = "", ""
                continue
            tokens.append({"val": token_val, "typ": token_type})
            token_val, token_type = "", ""
    tokens.insert(0, {"val": "start", "typ": "meta"})
    tokens.append({"val": "end", "typ": "meta"})
    return tokens
