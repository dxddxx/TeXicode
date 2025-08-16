from lexer import lexer
from parser import parse


test = r"F_n = \frac{1}{\sqrt5} \left[ \left( \frac{1+\sqrt5}2 \right) ^n - \left( \frac{1-\sqrt5}2 \right) ^n \right]"
test = r"\frac{-b\pm\sqrt{b^2-4ac}}{2a}\pm"
test = r"\sqrt[2ab]x^2"
test = r"\sum^4+\int\limits_3^4-\lim_{3+3^2}^4"
test = r"{a}b"
print(test)
lexered = lexer(test)
print(lexered)
for token in lexered:
    print(token)
parsed = parse(lexered)
for i in range(len(parsed)):
    print(i, parsed[i])
