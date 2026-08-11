# TeXicode, a cli script that renders TeX math into Unicode
# Author: Darcy Zhang
# Project url: https://github.com/dxddxx/TeXicode

import sys
import argparse
import re
from .pipeline import render_tex


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
    input_parser.add_argument('-m', '--markdown',
                              action='store_true',
                              help='treat input as Markdown: find and replace math blocks')
    input_parser.add_argument('-f', '--file',
                              action='store_true',
                              help='treat input filename')
    input_parser.add_argument('-c', '--color',
                              action='store_true',
                              help='enable color (black on white)')
    input_parser.add_argument('latex_string',
                              nargs='?',
                              help='input text string, or filename when using -f')
    input_parser.add_argument('-n', '--normal-font',
                              action='store_true',
                              help='use normal font instead of serif')
    args = input_parser.parse_args()
    debug = args.debug
    color = args.color
    options = {}
    options["fonts"] = "normal" if args.normal_font else "serif"

    content = None
    if args.file:
        if not args.latex_string:
            input_parser.error("-f/--file requires a filename")
        try:
            with open(args.latex_string, "r", encoding="utf-8") as input_file:
                content = input_file.read()
        except OSError as error:
            input_parser.error(f"could not read {args.latex_string!r}: {error}")
    elif args.latex_string:
        content = args.latex_string
    else:
        try:
            stdin_has_data = not sys.stdin.isatty()
        except Exception:
            stdin_has_data = False
        if stdin_has_data:
            content = sys.stdin.read()
        else:
            input_parser.error(
                "no input; provide a TeX string, use -f with a filename, "
                "or pipe data into txc"
            )

    if args.markdown:
        process_markdown(content, debug, color, options)
    else:
        tex_art = render_tex(content, debug, color, "raw", options)
        print(tex_art)


if __name__ == "__main__":
    main()
