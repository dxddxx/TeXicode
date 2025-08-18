from lexer import lexer
from parser import parse
from renderer import render


test = r"F_n = \frac{1}{\sqrt5} \left[ \left( \frac{1+\sqrt5}2 \right) ^n - \left( \frac{1-\sqrt5}2 \right) ^n \right]"
test = r"\frac{-b\pm\sqrt{b^2-4ac}}{2a}\pm"
# test = r"\sqrt[2ab]x^2"
# test = r"\sum^4+\int\limits_3^4-\lim_{3+3^2}^4"
print(test)
lexered = lexer(test)
for token in lexered:
    print(token)
parsed = parse(lexered)
for i in range(len(parsed)):
    print(i, parsed[i])
rendered = render(parsed)
for i in range(len(rendered)):
    print(i, rendered[i])
"""
0 ('opn_root', ('meta', 'start'), [1, 18], [])
1 ('cmd_frac', ('cmnd', 'frac'), [2, 15], [])
2 ('opn_brac', ('symb', '{'), [3, 4, 5, 6], [])
3 ('txt_leaf', ('symb', '-'), [], [])
4 ('txt_leaf', ('alph', 'b'), [], [])
5 ('cmd_leaf', ('cmnd', 'pm'), [], [])
6 ('cmd_sqrt', ('cmnd', 'sqrt'), [7], [])
7 ('opn_brac', ('symb', '{'), [8, 11, 12, 13, 14], [])
8 ('txt_leaf', ('alph', 'b'), [], [9])
9 ('sup_scrpt', ('symb', '^'), [10], [])
10 ('txt_leaf', ('numb', '2'), [], [])
11 ('txt_leaf', ('symb', '-'), [], [])
12 ('txt_leaf', ('numb', '4'), [], [])
13 ('txt_leaf', ('alph', 'a'), [], [])
14 ('txt_leaf', ('alph', 'c'), [], [])
15 ('opn_brac', ('symb', '{'), [16, 17], [])
16 ('txt_leaf', ('numb', '2'), [], [])
17 ('txt_leaf', ('alph', 'a'), [], [])
18 ('cmd_leaf', ('cmnd', 'pm'), [], [])
"""
