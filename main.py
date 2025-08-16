from lexer import *
from parser import *


test = r"F_n = \frac{1}{\sqrt5} \left[ \left( \frac{1+\sqrt5}2 \right) ^n - \left( \frac{1-\sqrt5}2 \right) ^n \right]"
# test = r"\frac{-b\pm\sqrt{b^2-4ac}}{2a}\pm"
print(test)
lexered = lexer(test)
print(lexered)
for token in lexered:
    print(token)
parsed = parse(lexered)
for i in range(len(parsed)):
    print(i, parsed[i])
