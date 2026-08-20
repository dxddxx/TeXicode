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


def read_command(tex: str, i: int) -> tuple:
    """Read the control sequence starting at tex[i] == "\\".

    Returns (word, next_index), where next_index points just past the
    command. Control words are runs of characters sharing a non-symbol
    char type; any other character right after the backslash forms a
    single-character command (e.g. "\\{", "\\ ", "\\\\").
    """
    if i + 1 >= len(tex):
        raise ValueError("Unexpected character \\")
    start = i + 1
    end = start
    while (
        end + 1 < len(tex)
        and get_char_type(tex[end]) == get_char_type(tex[end + 1])
        and get_char_type(tex[end]) != "symb"
    ):
        end += 1
    return tex[start:end + 1], end + 1


def read_env_name(tex: str, i: int, word: str) -> tuple:
    """Read the {name} argument of \\begin or \\end starting after the word.

    Skips spaces between the command and the brace, then returns
    (name, next_index), where next_index points just past the closing
    brace. Any name is accepted; the parser decides whether the
    environment is known.
    """
    while i < len(tex) and tex[i] == " ":
        i += 1
    if i >= len(tex) or tex[i] != "{":
        raise ValueError(f"Expected {{ after \\{word}")
    start = i + 1
    while i < len(tex) and tex[i] != "}":
        i += 1
    if i >= len(tex):
        raise ValueError(f"Unclosed {{ after \\{word}")
    return tex[start:i], i + 1


def append_token(tokens: list, token: tuple, last_index: int,
                 debug: bool) -> None:
    tokens.append(token)
    if debug:
        print(last_index, token)


def wrap_display_math(tokens: list) -> list:
    """Add the root start/end markers around the token stream."""
    if not tokens:
        return tokens
    tokens.insert(0, ("meta", "start"))
    tokens.append(("meta", "end"))
    return tokens


def lexer(tex: str, debug: bool) -> list:
    tex = tex.replace('\n', ' ').replace('\r', ' ')
    if debug:
        print("Lexerizing")
        print(tex)
    tokens = []
    i = 0
    while i < len(tex):
        char = tex[i]
        if char == "\\":
            word, i = read_command(tex, i)
            if word in ("begin", "end"):
                name, i = read_env_name(tex, i, word)
                token_type = "env_bgin" if word == "begin" else "env_end"
                append_token(tokens, (token_type, name), i - 1, debug)
            else:
                append_token(tokens, ("cmnd", word), i - 1, debug)
        elif char == "$":
            if i + 1 < len(tex) and tex[i + 1] == "$":
                append_token(tokens, ("symb", "$$"), i + 1, debug)
                i += 2
            else:
                append_token(tokens, ("symb", "$"), i, debug)
                i += 1
        elif char == " ":
            if tokens and tokens[-1] != ("symb", " "):
                append_token(tokens, ("symb", " "), i, debug)
            i += 1
        else:
            append_token(tokens, (get_char_type(char), char), i, debug)
            i += 1
    tokens = wrap_display_math(tokens)
    if debug:
        for i in range(len(tokens)):
            print(i, tokens[i])
    return tokens
