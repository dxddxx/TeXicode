# bg = "░"
bg = " "
# fraction = " – "
fraction = "╶─╴"
simple_symbols = """`!@#%*( )+-=[]|;:'",.<>/?"""

# Change values to lists
special_symbols = {
    "~": [[" "]],
    "&": [[""]],
    "\'": [["′"]],
}

# Alphabets stay as strings for indexing, but font mapping remains
alphabets = {
    "normal":     "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
    "serif_it":   "𝐴𝐵𝐶𝐷𝐸𝐹𝐺𝐻𝐼𝐽𝐾𝐿𝑀𝑁𝑂𝑃𝑄𝑅𝑆𝑇𝑈𝑉𝑊𝑋𝑌𝑍𝑎𝑏𝑐𝑑𝑒𝑓𝑔ℎ𝑖𝑗𝑘𝑙𝑚𝑛𝑜𝑝𝑞𝑟𝑠𝑡𝑢𝑣𝑤𝑥𝑦𝑧",
    "serif_bld":  "𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳",
    "serif_itbd": "𝑨𝑩𝑪𝑫𝑬𝑭𝑮𝑯𝑰𝑱𝑲𝑳𝑴𝑵𝑶𝑷𝑸𝑹𝑺𝑻𝑼𝑽𝑾𝑿𝒀𝒁𝒂𝒃𝒄𝒅𝒆𝒇𝒈𝒉𝒊𝒋𝒌𝒍𝒎𝒏𝒐𝒑𝒒𝒓𝒔𝒕𝒖𝒗𝒘𝒙𝒚𝒛",
    "sans":       "𝖠𝖡𝖢𝖣𝖤𝖥𝖦𝖧𝖨𝖩𝖪𝖫𝖬𝖭𝖮𝖯𝖰𝖱𝖲𝖳𝖴𝖵𝖶𝖷𝖸𝖹𝖺𝖻𝖼𝖽𝖾𝖿𝗀𝗁𝗂𝗃𝗄𝗅𝗆𝗇𝗈𝗉𝗊𝗋𝗌𝗍𝗎𝗏𝗐𝗑𝗒𝗓",
    "sans_it":    "𝘈𝘉𝘊𝘋𝘌𝘍𝘎𝘏𝘐𝘑𝘒𝘓𝘔𝘕𝘖𝘗𝘘𝘙𝘚𝘛𝘜𝘝𝘞𝘟𝘠𝘡𝘢𝘣𝘤𝘥𝘦𝘧𝘨𝘩𝘪𝘫𝘬𝘭𝘮𝘯𝘰𝘱𝘲𝘳𝘴𝘵𝘶𝘷𝘸𝘹𝘺𝘻",
    "sans_bld":   "𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇",
    "sans_itbd":  "𝘼𝘽𝘾𝘿𝙀𝙁𝙂𝙃𝙄𝙅𝙆𝙇𝙈𝙉𝙊𝙋𝙌𝙍𝙎𝙏𝙐𝙑𝙒𝙓𝙔𝙕𝙖𝙗𝙘𝙙𝙚𝙛𝙜𝙝𝙞𝙟𝙠𝙡𝙢𝙣𝙤𝙥𝙦𝙧𝙨𝙩𝙪𝙫𝙬𝙭𝙮𝙯",
    "mono":       "𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣",
    "cali_bld":   "𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃",
    "frak_bld":   "𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕿𝖀𝖁𝖂𝖃𝖄𝖅𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟",
    "double":     "𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫"
}

font_serif = {
    "mathrm":     alphabets["normal"],
    "operatorname":     alphabets["normal"],  # issue #7
    "mathbf":     alphabets["serif_bld"],
    "mathsf":     alphabets["sans"],
    "mathtt":     alphabets["mono"],
    "mathit":     alphabets["serif_it"],
    "mathnormal": alphabets["serif_it"],
    "mathcal":    alphabets["cali_bld"],
    "mathfrak":   alphabets["frak_bld"],
    "mathbb":     alphabets["double"],
    "mathscr":    alphabets["cali_bld"],
    "text":       alphabets["normal"]
}

font_normal = {
    "mathrm":     alphabets["normal"],
    "mathbf":     alphabets["serif_bld"],
    "mathsf":     alphabets["sans"],
    "mathtt":     alphabets["mono"],
    "mathit":     alphabets["serif_it"],
    "mathnormal": alphabets["normal"],
    "mathcal":    alphabets["cali_bld"],
    "mathfrak":   alphabets["frak_bld"],
    "mathbb":     alphabets["double"],
    "mathscr":    alphabets["cali_bld"],
    "text":       alphabets["normal"]
}

font = font_serif

# Convert to list-of-lists format
multi_line_leaf_commands = {
    # ordered like the Big Operators section of katex-supported.md
    "sum":  ([["┰", "─", "╴"],
              ["▐", "╸", " "],
              ["┸", "─", "╴"]], 1),
    "prod": ([["┰", "─", "┰"],
              ["┃", " ", "┃"],
              ["┸", " ", "┸"]], 1),
    "bigotimes": ([["╭", "─", "─", "─", "╮"],
                   # ["│", " ", "╳", " ", "│"],
                   ["│", " ", "×", " ", "│"],
                   ["╰", "─", "─", "─", "╯"]], 1),
    "bigvee": ([["╲", "╱"]], 0),
    "int":  ([["⌠"],
              ["│"],
              ["⌡"]], 1),
    "coprod": ([["┰", " ", "┰"],
                ["┃", " ", "┃"],
                ["┸", "─", "┸"]], 1),
    "bigoplus": ([["╭", "─", "─", "─", "╮"],
                  # ["│", "╶", "┼", "╴", "│"],
                  ["│", " ", "+", " ", "│"],
                  ["╰", "─", "─", "─", "╯"]], 1),
    "bigwedge": ([["╱", "╲"]], 0),
    "iint": ([["⌠", "⌠"],
              ["│", "│"],
              ["⌡", "⌡"]], 1),
    "intop":  ([["⌠"],
                ["│"],
                ["⌡"]], 1),
    "bigodot": ([["╭", "─", "─", "─", "╮"],
                 ["│", " ", "⋅", " ", "│"],
                 ["╰", "─", "─", "─", "╯"]], 1),
    # "bigcap": ([["╭", "─", "─", "─", "╮"],
    #             ["│", " ", " ", " ", "│"],
    #             ["╵", " ", " ", " ", "╵"]], 1),
    "bigcap": ([["╭", "─", "╮"],
                ["│", " ", "│"]], 1),
    "iiint": ([["⌠", "⌠", "⌠"],
               ["│", "│", "│"],
               ["⌡", "⌡", "⌡"]], 1),
    "smallint": ([["∫"]], 0),
    # "biguplus": ([["╷", " ", " ", " ", "╷"],
    #               # ["│", "╶", "┼", "╴", "│"],
    #               ["│", " ", "+", " ", "│"],
    #               ["╰", "─", "─", "─", "╯"]], 1),
    "biguplus": ([["│", "+", "│"],
                  ["╰", "─", "╯"]], 0),
    # "bigcup": ([["╷", " ", " ", " ", "╷"],
    #             ["│", " ", " ", " ", "│"],
    #             ["╰", "─", "─", "─", "╯"]], 1),
    "bigcup": ([["│", " ", "│"],
                ["╰", "─", "╯"]], 0),
    "oint": ([[" ", "⌠", " "],
              ["╶", "╪", "╴"],
              [" ", "⌡", " "]], 1),
    "oiint": ([[" ", "⌠", "⌠", " "],
               ["╶", "╪", "╪", "╴"],
               [" ", "⌡", "⌡", " "]], 1),
    "oiiint": ([[" ", "⌠", "⌠", "⌠", " "],
                ["╺", "╪", "╪", "╪", "╸"],
                [" ", "⌡", "⌡", "⌡", " "]], 1),
    "idotsint": ([["⌠", " ", "⌠"],
                  ["│", "⋯", "│"],
                  ["⌡", " ", "⌡"]], 1),  # not in the KaTeX checklist
}

# Keep square_root as strings, wrap when used
square_root = {
    "top_bar":   ["─"],
    "top_tail":  ["╴"],
    "top_angle": [" ", "┌"],
    "left_bar":  [" ", "│"],
    "btm_angle": ["╰", "┘"],
    # "top_bar": "─",
    # "top_tail": "╴",
    # "top_angle": " ┌",
    # "left_bar":  " │",
    # "btm_angle": "╺┪",
    # "top_bar": "─",
    # "top_tail": "╴",
    # "top_angle": " ┌",
    # "left_bar":  " │",
    # "btm_angle": "╲𜸙",
    # "top_bar": "─",
    # "top_tail": "╴",
    # "top_angle": " ┌",
    # "left_bar":  " │",
    # "btm_angle": "🯓🯗",
    # "top_bar": "─",
    # "top_tail": "╴",
    # "top_angle": " ┌",
    # "left_bar":  " │",
    # "btm_angle": "╲⎦", # ⌡
    # "top_bar": "▔",
    # "top_tail": "▔",
    # "top_angle": "▕▔",
    # "left_bar":  " ▏",
    # "btm_angle": "╲▏",
    # "top_bar": "─",
    # "top_tail": "╴",
    # "top_angle": "𜺯─",
    # "left_bar":  " ▏",
    # "btm_angle": "╲▏",
    # "top_bar": "─",
    # "top_tail": "╴",
    # "top_angle": " 🯐",
    # "left_bar":  " ▏",
    # "btm_angle": "╲▏",
}

# Change to list format for superscript/subscript pairs
# Combining characters used by accent commands
accents = {
    # Ordered like the Accents section in katex-supported.md.
    "tilde": "ã",  # U+0303 combining tilde
    "mathring": "å",  # U+030A combining ring above
    "widetilde": "a͠",  # U+0360 combining double tilde, 2 wide accent
    "overgroup": "a͡",  # U+0361 combining double inverted breve, 2 wide accent
    "utilde": "a̰",  # U+0330 combining tilde below
    "undergroup": "a͜",  # U+0330 combining tilde below
    "acute": "á",  # U+0301 combining acute accent
    "vec": "a⃗",  # U+20D7 combining right arrow above
    # "Overrightarrow": "a⃗",  # big accent; requires a separate row
    "bar": "ā",  # U+0304 combining macron
    "overleftarrow": "a⃖",  # U+20D6 combining left arrow above
    "overrightarrow": "a⃗",  # U+20D7 combining right arrow above
    "breve": "ă",  # U+0306 combining breve
    "underleftarrow": "a⃮",  # U+20EE combining left arrow below
    "underrightarrow": "a⃯",  # U+20EF combining right arrow below
    "check": "ǎ",  # U+030C combining caron
    "overleftharpoon": "a⃐",  # U+20D0 combining left harpoon above
    "overrightharpoon": "a⃑",  # U+20D1 combining right harpoon above
    "dot": "ȧ",  # U+0307 combining dot above
    "overleftrightarrow": "a⃡",  # U+20E1 combining left right arrow above
    # "overbrace": "a͡",  # big accent; requires a separate row
    "ddot": "ä",  # U+0308 combining diaeresis
    "underleftrightarrow": "a͍",  # U+034D combining left right arrow below
    # "underbrace": "a͜",  # big accent; requires a separate row
    "dddot": "a⃛",  # U+20DB combining three dots above
    "overline": "a̅",  # U+0305 combining overline
    "overbracket": "a⃩",  # U+20E9 combining wide bridge above
    "ddddot": "a⃜",  # U+20DC combining four dots above
    "underline": "a̲",  # U+0332 combining low line
    "underbracket": "a᷹",  # U+1DF9 combining wide inverted bridge below
    "grave": "à",  # U+0300 combining grave accent
    "underbar": "a̲",  # U+0332 combining low line
    # "overlinesegment": "a̅",  # big accent; requires a separate row
    "hat": "â",  # U+0302 combining circumflex accent
    "widecheck": "ǎ",  # U+030C combining caron
    # "underlinesegment": "a̲",  # big accent; requires a separate row
    "widehat": "â",  # U+0302 combining circumflex accent

    # Accent functions inside \text{...}, in Markdown order.
    "'": "á",  # U+0301 combining acute accent
    "~": "ã",  # U+0303 combining tilde
    ".": "ȧ",  # U+0307 combining dot above
    "H": "a̋",  # U+030B combining double acute accent
    "`": "à",  # U+0300 combining grave accent
    "=": "ā",  # U+0304 combining macron
    '"': "ä",  # U+0308 combining diaeresis
    "v": "ǎ",  # U+030C combining caron
    "^": "â",  # U+0302 combining circumflex accent
    "u": "ă",  # U+0306 combining breve
    "r": "å",  # U+030A combining ring above

    # Commands from the Annotation section of katex-supported.md.
    "cancel": "a̸",  # U+0338 combining long solidus overlay
    "bcancel": "a⃥",  # U+20E5 combining reverse solidus overlay
    "xcancel": "a̸⃥",  # long solidus and reverse solidus overlays
    "sout": "a̶",  # U+0336 combining long stroke overlay
    "angl": "a⃧",  # U+031A combining left angle above
}

# Stretchy accent rows.  Each entry stores the placement, the maximum width
# for its combining fallback, and the optional single-cell/left/fill/right
# art used when the accent needs its own row.
stretchy_accents = {
    # Ordered like the stretchy entries in the Accents section.
    "widetilde": {
        "placement": "top", "combining_width": 2,
        "left": "~", "fill": "~", "right": "~",
    },
    "overgroup": {
        "placement": "top", "combining_width": 2,
        "left": "╭", "fill": "─", "right": "╮",
    },
    "utilde": {
        "placement": "bottom", "combining_width": 1,
        "left": "~", "fill": "~", "right": "~",
    },
    "undergroup": {
        "placement": "bottom", "combining_width": 1,
        "left": "╰", "fill": "─", "right": "╯",
    },
    "Overrightarrow": {
        "placement": "top", "combining_width": 0,
        "single": "⇒", "left": "═", "fill": "═", "right": "⟹",
    },
    "overleftarrow": {
        "placement": "top", "combining_width": 1,
        "left": "←", "fill": "─", "right": "─",
    },
    "overrightarrow": {
        "placement": "top", "combining_width": 1,
        "left": "─", "fill": "─", "right": "→",
    },
    "underleftarrow": {
        "placement": "bottom", "combining_width": 1,
        "left": "←", "fill": "─", "right": "─",
    },
    "underrightarrow": {
        "placement": "bottom", "combining_width": 1,
        "left": "─", "fill": "─", "right": "→",
    },
    "overleftharpoon": {
        "placement": "top", "combining_width": 1,
        "left": "↼", "fill": "─", "right": "─",
    },
    "overrightharpoon": {
        "placement": "top", "combining_width": 1,
        "left": "╶", "fill": "─", "right": "⇀",
    },
    "overleftrightarrow": {
        "placement": "top", "combining_width": 1,
        "left": "←", "fill": "─", "right": "→",
    },
    "overbrace": {
        "placement": "top", "combining_width": 2,
        "single": "⏞", "left": "╭", "fill": "─", "center": "┴",
        "right": "╮",
    },
    "underleftrightarrow": {
        "placement": "bottom", "combining_width": 1,
        "left": "←", "fill": "─", "right": "→",
    },
    "underbrace": {
        "placement": "bottom", "combining_width": 2,
        "single": "⏟", "left": "╰", "fill": "─", "center": "┬",
        "right": "╯",
    },
    "overline": {
        "placement": "top", "combining_width": 1,
        "left": "─", "fill": "─", "right": "─",
    },
    "overbracket": {
        "placement": "top", "combining_width": 1,
        "left": "┌", "fill": "─", "right": "┐",
    },
    "underline": {
        "placement": "bottom", "combining_width": 1,
        "left": "─", "fill": "─", "right": "─",
    },
    "underbracket": {
        "placement": "bottom", "combining_width": 1,
        "left": "└", "fill": "─", "right": "┘",
    },
    "overlinesegment": {
        "placement": "top", "combining_width": 0,
        "single": "⟝", "left": "╾", "fill": "─", "right": "╼",
    },
    "widecheck": {
        "placement": "top", "combining_width": 1,
        "left": "╭", "fill": "─", "right": "╮",
    },
    "underlinesegment": {
        "placement": "bottom", "combining_width": 0,
        "single": "⟝", "left": "╾", "fill": "─", "right": "╼",
    },
    "widehat": {
        "placement": "top", "combining_width": 1,
        "left": "╰", "fill": "─", "right": "╯",
    },
}

unicode_scripts = {
    " ": [" ", " "], "0": ["⁰", "₀"], "1": ["¹", "₁"], "2": ["²", "₂"],
    "3": ["³", "₃"], "4": ["⁴", "₄"], "5": ["⁵", "₅"], "6": ["⁶", "₆"],
    "7": ["⁷", "₇"], "8": ["⁸", "₈"], "9": ["⁹", "₉"],
    "+": ["⁺", "₊"], "-": ["⁻", "₋"], "=": ["⁼", "₌"], "!": ["ꜝ", " "],
    "(": ["⁽", "₍"], ")": ["⁾", "₎"],
    #     "A": ["ᴬ", " "], "a": ["ᵃ", "ₐ"], "B": ["ᴮ", "𞁓"], "b": ["ᵇ", " "],
    #     "C": ["ꟲ", "𞁞"], "c": ["ᶜ", "𞁞"], "D": ["ᴰ", " "], "d": ["ᵈ", " "],
    #     "E": ["ᴱ", " "], "e": ["ᵉ", "ₑ"], "F": ["ᶠ", " "], "f": ["ᶠ", " "],
    #     "G": ["ᴳ", " "], "g": ["ᵍ", " "], "H": ["ᴴ", " "], "h": ["ʰ", "ₕ"],
    #     "I": ["ᴵ", "ᶦ"], "i": ["ⁱ", "ᵢ"], "J": ["ᴶ", " "], "j": ["ʲ", "ⱼ"],
    #     "K": ["ᴷ", "𞁚"], "k": ["ᵏ", "ₖ"], "L": ["ᴸ", " "], "l": ["ˡ", "ₗ"],
    #     "M": ["ᴹ", " "], "m": ["ᵐ", "ₘ"], "N": ["ᴺ", " "], "n": ["ⁿ", "ₙ"],
    #     "O": ["ᴼ", "𞁜"], "o": ["ᵒ", "ₒ"], "P": ["ᴾ", " "], "p": ["ᵖ", "ₚ"],
    "A": ["ᴬ", " "], "a": ["ᵃ", "ₐ"], "B": ["ᴮ", " "], "b": ["ᵇ", " "],
    "C": ["ꟲ", " "], "c": ["ᶜ", " "], "D": ["ᴰ", " "], "d": ["ᵈ", " "],
    "E": ["ᴱ", " "], "e": ["ᵉ", "ₑ"], "F": ["ᶠ", " "], "f": ["ᶠ", " "],
    "G": ["ᴳ", " "], "g": ["ᵍ", " "], "H": ["ᴴ", " "], "h": ["ʰ", "ₕ"],
    "I": ["ᴵ", "ᶦ"], "i": ["ⁱ", "ᵢ"], "J": ["ᴶ", " "], "j": ["ʲ", "ⱼ"],
    "K": ["ᴷ", " "], "k": ["ᵏ", "ₖ"], "L": ["ᴸ", " "], "l": ["ˡ", "ₗ"],
    "M": ["ᴹ", " "], "m": ["ᵐ", "ₘ"], "N": ["ᴺ", " "], "n": ["ⁿ", "ₙ"],
    "O": ["ᴼ", " "], "o": ["ᵒ", "ₒ"], "P": ["ᴾ", " "], "p": ["ᵖ", "ₚ"],

    "Q": ["ꟴ", " "], "q": ["𐞥", " "], "R": ["ᴿ", " "], "r": ["ʳ", "ᵣ"],
    "S": ["ˢ", "ₛ"], "s": ["ˢ", "ₛ"], "T": ["ᵀ", " "], "t": ["ᵗ", "ₜ"],
    "U": ["ᵁ", " "], "u": ["ᵘ", "ᵤ"], "V": ["ⱽ", "ᵥ"], "v": ["ᵛ", "ᵥ"],
    "W": ["ᵂ", " "], "w": ["ʷ", " "], "X": ["ˣ", "ₓ"], "x": ["ˣ", "ₓ"],
    "Y": ["𐞲", "ᵧ"], "y": ["ʸ", "ᵧ"], "Z": ["ᶻ", " "], "z": ["ᶻ", " "],
    "α": ["ᵅ", " "], "β": ["ᵝ", "ᵦ"], "γ": ["ᵞ", "ᵧ"], "δ": ["ᵟ", " "],
    "ε": ["ᵋ", " "], "θ": ["ᶿ", " "], "ι": ["ᶥ", " "], "ϕ": ["ᶲ", " "],
    "φ": ["ᵠ", "ᵩ"], "χ": ["ᵡ", "ᵪ"], "ρ": [" ", "ᵨ"],
    "/": ["ᐟ", " "], ".": ["·", " "], "∘": ["˚", " "], "′": ["′", " "],
}

# Keep delimiter as strings, wrap when used
delimiter = {
    "sgl": "(){}[]⌊⌋⌈⌉||‖‖",
    "top": "⎛⎞⎧⎫⎡⎤⎢⎥⎡⎤⎟⎜║║",
    "ctr": "⎜⎟⎨⎬⎢⎥⎢⎥⎢⎥⎟⎜║║",
    "fil": "⎜⎟⎪⎪⎢⎥⎢⎥⎢⎥⎟⎜║║",
    "btm": "⎝⎠⎩⎭⎣⎦⎣⎦⎢⎥⎟⎜║║",
}
