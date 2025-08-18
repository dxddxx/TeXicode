from lexer import lexer
from parser import parse
from renderer import render


def render_tex(tex):
    # print(tex)
    try:
        lexered = lexer(tex)
    except ValueError as e:
        print("lexerizing error:", e)
        return
    # for token in lexered:
    #     print(token)
    try:
        parsed = parse(lexered)
    except ValueError as e:
        print("parsing error:", e)
        return
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
    tex = input()
    render_tex(tex)


if __name__ == "__main__":
    main()
