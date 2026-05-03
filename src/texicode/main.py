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
    input_parser.add_argument('-f', '--file',
                              action='store_true',
                              help='treat input as Markdown: find math blocks and replace them (use piping or positional argument for input)')
    input_parser.add_argument('-c', '--color',
                              action='store_true',
                              help='enable color (black on white)')
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

    # Determine input source: prefer positional argument if provided; otherwise
    # read piped stdin when present. This avoids accidentally treating stdin as
    # having data in environments where isatty() can be unreliable.
    content = None
    if args.latex_string:
        content = args.latex_string
    else:
        try:
            stdin_has_data = not sys.stdin.isatty()
        except Exception:
            stdin_has_data = False
        if stdin_has_data:
            content = sys.stdin.read()
        else:
            print("Error: no input. provide TeX string as argument or pipe data into txc")
            sys.exit(1)

    if args.file:
        # treat input as markdown
        process_markdown(content, debug, color, options)
    else:
        tex_art = render_tex(content, debug, color, "raw", options)
        print(tex_art)


if __name__ == "__main__":
    main()
