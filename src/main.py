import sys
import argparse
import re
from lexer import lexer
from parser import parse
from renderer import render


def render_tex(tex: str, debug: bool) -> list:
    try:
        lexered = lexer(tex, debug)
    except ValueError as e:
        return [f"TexTR: lexerizing error: {e}"]
        return
    try:
        parsed = parse(lexered, debug)
    except ValueError as e:
        return [f"TexTR: parsing error: {e}"]
    try:
        rendered = render(parsed, debug)
    except ValueError as e:
        return [f"TexTR: rendering error: {e}"]
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


def process_markdown(content, debug, color):

    # Regex to find LaTeX blocks: $$...$$ or $...$ or \[...\] or \(...\)
    # latex_regex = r'(\$\$.*?\$\$|\\\[[\s\S]*?\\\]|\\\([^\)]*?\\\)|\$(.*?)\$|\((.*?)\))'
    # latex_regex = r'\$\$[\s\S]*?\$\$|\\\[[\s\S]*?\\\]|\\\([\s\S]*?\\\)|\$(?:(?!\$\$)[\s\S])*?\$'
    latex_regex = r'\$\$.*?\$\$|\$.*?\$|\\\[.*?\\\]|\\\(.*?\\\)'

    def replace_latex(match):
        tex_block = match.group(0)
        tex_rows = render_tex(tex_block, debug)
        is_multiline = len(tex_rows) > 1
        if is_multiline or \
                tex_block.startswith('$$') or \
                tex_block.startswith('\\['):
            tex_art = join_rows(tex_rows, color)
            return f"\n```\n{tex_art}\n```\n"
        else:
            tex_art = join_rows(tex_rows, False)
            return f"`{tex_art}`"

    new_content = re.sub(latex_regex, replace_latex, content, flags=re.DOTALL)
    print(new_content)


def main():
    input_parser = argparse.ArgumentParser(description='Process Markdown with LaTeX or raw LaTeX')
    input_parser.add_argument('-d', '--debug', action='store_true', help='Enable debug output')
    input_parser.add_argument('-f', '--file', help='Input Markdown file to process')
    input_parser.add_argument('-c', '--color', action='store_true', help='Enable colored output')
    input_parser.add_argument('latex_string', nargs='?', help='Raw LaTeX string (if not using -f)')
    args = input_parser.parse_args()
    debug = args.debug
    color = args.color

    if args.file:
        with open(args.file, 'r') as file:
            content = file.read()
        process_markdown(content, debug, color)
    elif args.latex_string:
        tex_rows = render_tex(args.latex_string, debug)
        tex_art = join_rows(tex_rows, color)
        print(tex_art)
    else:
        print("Error: No input provided. Use -f for file or provide raw LaTeX.")
        sys.exit(1)


if __name__ == "__main__":
    main()
