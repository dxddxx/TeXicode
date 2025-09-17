from lexer import lexer
from parser import parse
from renderer import render


def render_tex_rows(tex: str, debug: bool) -> list:
    try:
        lexered = lexer(tex, debug)
    except ValueError as e:
        return [f"TeXicode: lexerizing error: {e}"]
    try:
        parsed = parse(lexered, debug)
    except ValueError as e:
        return [f"TeXicode: parsing error: {e}"]
    try:
        rendered = render(parsed, debug)
    except ValueError as e:
        return [f"TeXicode: rendering error: {e}"]
    return rendered


def join_rows(rendered_rows: list, color: bool) -> str:
    tag_end = ""
    tag_start = ""
    if color:
        tag_end = "\x1b[0m"
        tag_start = "\x1b[38;5;232m\x1b[48;5;255m"
    joined = f"{tag_end}\n{tag_start}".join(rendered_rows)
    joined = tag_start + joined + tag_end
    return joined


def render_tex(tex: str, debug: bool, color: bool, context: str):
    tex_rows = render_tex_rows(tex, debug)
    single_line = len(tex_rows) == 1
    if context == "md_inline":
        tex_art = join_rows(tex_rows, False)
    else:
        tex_art = join_rows(tex_rows, color)
    if context == "md_inline" and single_line:
        if color:
            return f"`{tex_art}`"
        return tex_art
    elif context == "md_block" or (context == "md_inline" and not single_line):
        return f"\n```\n{tex_art}\n```\n"
    elif context == "raw":
        return tex_art
