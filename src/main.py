import sys
import argparse
from lexer import lexer
from parser import parse
from renderer import render
import re


def render_tex(tex, debug):
    if debug:
        print(tex)
    try:
        lexered = lexer(tex, debug)
    except ValueError as e:
        print("TexTR lexerizing error:", e)
        return
    try:
        parsed = parse(lexered, debug)
    except ValueError as e:
        print("TexTR parsing error:", e)
        return
    try:
        rendered = render(parsed, debug)
    except ValueError as e:
        print("TexTR rendering error:", e)
        return
    rendered_art = "\n".join(rendered)
    return rendered_art


def process_markdown(input_file):
    with open(input_file, 'r') as file:
        content = file.read()

    # Regex to find LaTeX blocks: $...$ or $$...$$ or \[...\] or \[...\]
    latex_pattern = r'(\$\$.*?\$\$|\\\[[^\]]*?\\\]|\\\([^\)]*?\\\))'

    def replace_latex(match):
        latex_block = match.group(0)
        # Remove the $$ markers for rendering
        clean_latex = latex_block.strip('$')
        tex_art = render_tex(clean_latex, False)
        return f"\n```\n{tex_art}\n```\n"

    modified_content = re.sub(latex_pattern, replace_latex, content, flags=re.DOTALL)
    print(modified_content)


def main():
    input_parser = argparse.ArgumentParser(description='Process a Markdown file with LaTeX')
    input_parser.add_argument('input_file', help='Input Markdown file to process')
    input_parser.add_argument('--debug', action='store_true', help='Enable debug output')
    args = input_parser.parse_args()

    process_markdown(args.input_file)


if __name__ == "__main__":
    main()
