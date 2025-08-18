import sys
import argparse
from lexer import lexer
from parser import parse
from renderer import render


def render_tex(tex, debug):
    if debug:
        print(tex)
    try:
        lexered = lexer(tex)
    except ValueError as e:
        print("lexerizing error:", e)
        return
    if debug:
        for token in lexered:
            print(token)
    try:
        parsed = parse(lexered)
    except ValueError as e:
        print("parsing error:", e)
        return
    if debug:
        for i in range(len(parsed)):
            print(i, parsed[i])
    try:
        rendered = render(parsed)
    except ValueError as e:
        print("rendering error:", e)
        return
    for i in range(len(rendered)):
        print(rendered[i])


def main():
    input_parser = argparse.ArgumentParser(description='My Python Program')
    input_parser.add_argument('input_tex', help='TeX input as str')
    input_parser.add_argument('debug', nargs='?', default=None, help='debug or no')
    args = input_parser.parse_args()
    tex = args.input_tex
    debug = args.debug
    render_tex(tex, debug)


if __name__ == "__main__":
    sys.exit(main())
