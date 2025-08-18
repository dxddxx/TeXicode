from lexer import lexer
from parser import parse
from renderer import render


test = r"F_n = \frac{1}{\sqrt5} \left[ \left( \frac{1+\sqrt5}2 \right) ^n - \left( \frac{1-\sqrt5}2 \right) ^n \right]"
test = r"E = mc^2 + \int_{a}^{b} \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(x-\mu)^2}{2\sigma^2}} \, dx + \sum_{n=1}^{\infty} \frac{(-1)^{n-1}}{n^2}"
test = r"\frac a \binom12"
# print(test)
lexered = lexer(test)
# for token in lexered:
#     print(token)
parsed = parse(lexered)
for i in range(len(parsed)):
    print(i, parsed[i])
rendered = render(parsed)
for i in range(len(rendered)):
    print(rendered[i])
