# TeXicode, a cli script that renders TeX math into Unicode
# Author: Darcy Zhang
# Project url: https://github.com/dxddxx/TeXicode

import sys
import argparse
import re
from pipeline import render_tex


def process_markdown(content, debug, color, options):

    # Regex to find LaTeX blocks: $$...$$ or $...$ or \[...\] or \(...\)
    latex_regex = r'\$\$.*?\$\$|\$.*?\$|\\\[.*?\\\]|\\\(.*?\\\)|\\begin\{.*?\}.*?\\end\{.*?\}'

    def replace_latex(match):
        tex_block = match.group(0)
        clean_tex_block = tex_block.strip('$')
        context = "md_inline"
        if tex_block.startswith('$$') or tex_block.startswith(r'\[') \
                or tex_block.startswith(r'\begin'):
            context = "md_block"
        return render_tex(clean_tex_block, debug, color, context, options)

    new_content = re.sub(latex_regex, replace_latex, content, flags=re.DOTALL)
    print(new_content)


def main():
    help_description = \
            "TeXicode - render TeX strings or process markdown math\
             (https://github.com/dxddxx/TeXicode)"

    input_parser = argparse.ArgumentParser(description=help_description)
    input_parser.add_argument('-d', '--debug',
                              action='store_true',
                              help='enable debug')
    input_parser.add_argument('-f', '--file',
                              help='input Markdown file')
    input_parser.add_argument('-c', '--color',
                              action='store_true',
                              help='enable color')
    input_parser.add_argument('latex_string',
                              nargs='?',
                              help='raw TeX string (if not using -f)')
    input_parser.add_argument('-n', '--normal-font',
                              action='store_true',
                              help='use normal font instead of serif')
    args = input_parser.parse_args()
    debug = args.debug
    color = args.color
    options = {}
    options["fonts"] = "normal" if args.normal_font else "serif"

    if args.file:
        with open(args.file, 'r') as file:
            content = file.read()
        process_markdown(content, debug, color, options)
    elif args.latex_string:
        tex_art = render_tex(args.latex_string, debug, color, "raw", options)
        print(tex_art)
    else:
        print("Error: no input. provide TeX string or -f <markdown_file>")
        sys.exit(1)


if __name__ == "__main__":
    main()
