# TeXicode, a cli script that renders TeX math into Unicode
# Author: Darcy Zhang
# Project url: https://github.com/dxddxx/TeXicode

import sys
import argparse
import re
from pipeline import render_tex


def process_markdown(content, debug, color):

    # Regex to find LaTeX blocks: $$...$$ or $...$ or \[...\] or \(...\)
    latex_regex = r'\$\$.*?\$\$|\$.*?\$|\\\[.*?\\\]|\\\(.*?\\\)|\\begin\{.*?\}.*?\\end\{.*?\}'

    def replace_latex(match):
        tex_block = match.group(0)
        clean_tex_block = tex_block.strip('$')
        # tex_rows = render_tex(clean_tex_block, debug)
        # is_multiline = len(tex_rows) > 1
        # if tex_block.startswith('$$') or \
        #         tex_block.startswith(r'\[') or \
        #         tex_block.startswith(r'\begin'):
        #     tex_art = join_rows(tex_rows, color)
        #     return f"\n```\n{tex_art}\n```\n"
        # elif is_multiline:
        #     tex_art = join_rows(tex_rows, False)
        #     return f"\n```\n{tex_art}\n```\n"
        # # else if single line inline math
        # tex_art = join_rows(tex_rows, False)
        # if color:
        #     return f"`{tex_art}`"
        # else:
        #     return tex_art
        context = "md_inline"
        if tex_block.startswith('$$') or tex_block.startswith(r'\[') \
                or tex_block.startswith(r'\begin'):
            context = "md_block"
        return render_tex(clean_tex_block, debug, color, context)

    new_content = re.sub(latex_regex, replace_latex, content, flags=re.DOTALL)
    print(new_content)


def main():
    input_parser = argparse.ArgumentParser(description='render TeX string or process markdown math')
    input_parser.add_argument('-d', '--debug', action='store_true', help='enable debug')
    input_parser.add_argument('-f', '--file', help='input Markdown file')
    input_parser.add_argument('-c', '--color', action='store_true', help='enable color')
    input_parser.add_argument('latex_string', nargs='?', help='raw TeX string (if not using -f)')
    args = input_parser.parse_args()
    debug = args.debug
    color = args.color

    if args.file:
        with open(args.file, 'r') as file:
            content = file.read()
        process_markdown(content, debug, color)
    elif args.latex_string:
        # tex_rows = render_tex(args.latex_string, debug)
        # tex_art = join_rows(tex_rows, color)
        tex_art = render_tex(args.latex_string, debug, color, "raw")
        print(tex_art)
    else:
        print("Error: no input. provide TeX string or -f <markdown_file>")
        sys.exit(1)


if __name__ == "__main__":
    main()
