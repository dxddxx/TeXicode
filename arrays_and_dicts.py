# Lexerizing

special_char_token_type = {
    " " : "space",
    "\\": "backslash",
    "^" : "script",
    "_" : "script",
    "{" : "openbrac",
    "}" : "closebrac",
    "~" : "nonbreakingspace",
    }

symbols = """`!@#$%&*()+-=[]|;:'",.<>/?"""

combine_dict = {
    ("backslash", "backslash"): "linebreak",
    ("backslash", "space"    ): "forcedspace",
    ("backslash", "letter"   ): "command",
    ("backslash", "symbol"   ): "symbolcmd",
    ("backslash", "script"   ): "symbolcmd",
    ("backslash", "openbrac" ): "symbolcmd",
    ("backslash", "closebrac"): "symbolcmd",
    ("command"  , "letter"   ): "command",
    }

# Parsing
paired_token_types = {
    "Start" : "End",
    "openbrac" : "closebrac",
    }
paired_cmd_vals = {
    "left" : "right",
    }
single_arg_token_types = (
    "Start",
    "script",
    "openbrac",
    "left",
    )
single_arg_cmd_vals = (
    "sqrt",
    "left",
    "right",
    )
double_arg_cmd_vals = (
    "frac",
    )
atomic_token_types = (
    "backslash",
    "closebrac",
    "nonbreakingspace",
    "symbol",
    "linebreak",
    "forcedspace",
    "letter",
    "symbolcmd",
    )

#atomic_commands = (
#    )

# Rendering

bg_art = " "

self_replacement_token_types = (
    "letter",
    "number",
    "symbol",
    "symbolcmd",
    "forcedspace",
    )

# from ../inspirations/tex2utf.pl
self_replacement_commands = (
    '@',"_","$","{","}","#","&","arccos","arcsin","arctan","arg","cos",
    "cosh","cot","coth","csc","deg",
    #"det",
    "dim","exp",
    #"gcd",
    "hom",
    #"inf",
    "ker","lg","lim","liminf","limsup","ln","log",
    #"max","min",
    "mod",
    #"Pr",
    "sec","sin","sinh",
    #"sup",
    "tan","tanh", "%"
    )

# from utftex.md
single_line_commands_art = {
    "textit"   : " ", "oplus"    : "⊕", "otimes"   : "⊗", "ominus"   : "⊖",
    "leq"      : "≤", "equiv"    : "≡", "geq"      : "≥", "partial"  : "∂",
    "forall"   : "∀", "exists"   : "∃", "owns"     : "∋", "ni"       : "∌",
    "in"       : "∈", "notin"    : "∉", "qed"      : "∎", "pm"       : "±",
    "mp"       : "∓", "cong"     : "≅", "neq"      : "≠", "nmid"     : "∤",
    "subset"   : "⊂", "subseteq" : "⊆", "subseteq" : "⊇", "supset"   : "⊃",
    # "sqrt" : "radical",
    # "buildrel" : "buildrel",
    # "frac" : "fraction",
    # "LITERALnoLENGTH" : "literal_no_length",
    "alpha"   : "α", "Alpha"   : "Α", "beta"    : "β", "Beta"    : "Β", "gamma"   : "γ", "Gamma"   : "Γ",
    "delta"   : "δ", "Delta"   : "Δ", "epsilon" : "ε", "Epsilon" : "Ε", "zeta"    : "ζ", "Zeta"    : "Ζ",
    "eta"     : "η", "Eta"     : "Η", "theta"   : "θ", "Theta"   : "Θ", "iota"    : "ι", "Iota"    : "Ι",
    "phi"     : "φ", "Phi"     : "Φ", "kappa"   : "κ", "Kappa"   : "Κ", "lambda"  : "λ", "Lambda"  : "Λ", 
    "mu"      : "μ", "Mu"      : "Μ", "nu"      : "ν", "Nu"      : "Ν", "xi"      : "ξ", "Xi"      : "Ξ",
    "omicron" : "ο", "Omicron" : "Ο", "pi"      : "π", "Pi"      : "Π", "rho"     : "ρ", "Rho"     : "Ρ",
    "sigma"   : "σ", "Sigma"   : "Σ", "tau"     : "τ", "Tau"     : "Τ", "upsilon" : "υ", "Upsilon" : "Υ",
    "chi"     : "χ", "Chi"     : "Χ", "psi"     : "ψ", "Psi"     : "Ψ", "omega"   : "ω", "Omega"   : "Ω", 

    "~"     : " "  , ","     : " "  , "dots"  : "...",
    "ldots" : "...", "cdots" : "⋯"  , "colon" : ": " ,
    "mid"   : " | ",
    "smallsetminus" : " ⧵ ",
    "setminus"      : " ⧹ ",
    "backslash"     : "\\" ,
    "approx" : " ≅ "  , "simeq"  : " ≃ "  , "quad"   : "   "  , "qquad"  : "     ",
    #"Delta"  : "△"    , "Pi"     : "π"    , "alpha"  : "α"    , "to"     : " ──> ",
    #"from"   : " <── ", "wedge"  : "∧"    , "Lambda" : "∨"    , "lhd"    : " ⊲ "  ,
    "rhd"    : " ⊳ "  , "cdot"   : " · "  , "circ"   : " o "  , "bullet" : "•"    ,
    "infty"  : "∞"    , "ltimes" : "⋉"    , "rtimes" : " ⋊ "  , "times"  : " × "  ,
    "hookrightarrow"     : " ↪ "     , "hookleftarrow"      : " ↩ "     ,
    "longleftarrow"      : " <──── " , "longrightarrow"     : " ────> " ,
    "longleftrightarrow" : " <────> ",
    "rightarrow" : " ──> "      , "leftarrow"  : " <── "      ,
    "Rightarrow" : " ==> "      , "Leftarrow"  : " <== "      ,
    "mapsto"     : " ├──> "     , "longmapsto" : " ├────> "   ,
    "cap"        : " ∩ "        , "cup"        : " ∪ "        ,
    "section"    : "Section "   , "subsection" : "Subsection ",
    "|"          : "||"         , ';'          : " "          ,
    #'\noindent'  : "",
    }

frac_art = "─"

sqrt_art = {
    "top_bar"        : "─",
    "top_left_angle" : bg_art + "┌",
    "left_bar"       : bg_art + "│",
    "btm_left_angle" :         "🯓🯗",
    }

super_sub_script_art = {
    "0" : "⁰₀", "1" : "¹₁", "2" : "²₂", "3" : "³₃", "4" : "⁴₄", "5" : "⁵₅", "6" : "⁶₆", "7" : "⁷₇",
    "8" : "⁸₈", "9" : "⁹₉", "+" : "⁺₊", "-" : "⁻₋", "=" : "⁼₌", "!" : "ꜝ ", "(" : "⁽₍", ")" : "⁾₎",
    
    "A" : "ᴬ ", "a" : "ᵃₐ", "B" : "ᴮ𞁓", "b" : "ᵇ ", "C" : "ᶜ𞁞", "c" : "ᶜ𞁞", "D" : "ᴰ ", "d" : "ᵈ ",
    "E" : "ᴱ ", "e" : "ᵉₑ", "F" : "ᶠ ", "f" : "ᶠ ", "G" : "ᴳ ", "g" : "ᵍ ", "H" : "ᴴ ", "h" : "ʰₕ",
    "I" : "ᴵᶦ", "i" : "ⁱᵢ", "J" : "ᴶ ", "j" : "ʲⱼ", "K" : "ᴷ𞁚", "k" : "ᵏₖ", "L" : "ᴸ ", "l" : "ˡₗ",
    "M" : "ᴹ ", "m" : "ᵐₘ", "N" : "ᴺ ", "n" : "ⁿₙ", "O" : "ᴼ𞁜", "o" : "ᵒₒ", "P" : "ᴾ ", "p" : "ᵖₚ",
    "Q" : "ꟴ ", "q" : "𐞥 ", "R" : "ᴿ ", "r" : "ʳᵣ", "S" : "ˢₛ", "s" : "ˢₛ", "T" : "ᵀ ", "t" : "ᵗₜ",
    "U" : "ᵁ ", "u" : "ᵘᵤ", "V" : "ⱽᵥ", "v" : "ᵛᵥ", "W" : "ᵂ ", "w" : "ʷ ", "X" : "ˣₓ", "x" : "ˣₓ",
    "Y" : "𐞲ᵧ", "y" : "ʸᵧ", "Z" : "ᶻ ", "z" : "ᶻ ",
    
    "α" : "ᵅ ", "β" : "ᵝᵦ", "γ" : "ᵞᵧ", "δ" : "ᵟ ", "ε" : "ᵋ ", "θ" : "ᶿ ", "ι" : "ᶥ ",
    "ϕ" : "ᶲ ", "φ" : "ᵠᵩ", "χ" : "ᵡᵪ", "ρ" : "ᵨ ",
    }

left_right_art = {
    "(":{"left": {"top": "⎛",
                  "ctr": "⎜",
                  "fil": "⎜",
                  "btm": "⎝"},
         "right":{"top": "⎞",
                  "ctr": "⎟",
                  "fil": "⎟",
                  "btm": "⎠"}},
    "[":{"left": {"top": "⎡",
                  "ctr": "⎢",
                  "fil": "⎢",
                  "btm": "⎣"},
         "right":{"top": "⎤",
                  "ctr": "⎥",
                  "fil": "⎥",
                  "btm": "⎦"}},
    "{":{"left": {"top": "⎧",
                  "ctr": "⎨",
                  "fil": "⎪",
                  "btm": "⎩"},
         "right":{"top": "⎫",
                  "ctr": "⎬",
                  "fil": "⎪",
                  "btm": "⎭"}},
    "|":{"left": {"top": "⎟",
                  "ctr": "⎟",
                  "fil": "⎟",
                  "btm": "⎟"},
         "right":{"top": "⎜",
                  "ctr": "⎜",
                  "fil": "⎜",
                  "btm": "⎜"}},
    }
'''
⎷⎸⎹ ⏐
⎺⎻⎼⎽

⏐ 🭽⎺🭶
⎺ ⎸
  🭰

𜰰𜰱𜰲𜰳
𜰴𜰵𜰶𜰷
𜰸𜰹𜰺𜰻
𜰼𜰽𜰾𜰿

𜰰𜰱𜰲𜰳
𜰴𜰵𜰶𜰷
𜰸𜰹𜰺𜰻
𜰼𜰽𜰾𜰿

𜰰𜰱⎺⎺⎺𜰲𜰳
𜰴𜰵⎺⎺⎺𜰶𜰷
⎸⎸   ⎹⎹
⎸⎸   ⎹⎹
⎸⎸   ⎹⎹
𜰸𜰹⎽⎽⎽𜰺𜰻
𜰼𜰽⎽⎽⎽𜰾𜰿

𜰰𜰱⎺⎺⎺𜰲𜰳
𜰴𜰵⎺⎺⎺𜰶𜰷
𜰸𜰹⎽⎽⎽𜰺𜰻
𜰼𜰽⎽⎽⎽𜰾𜰿

𜰰𜰱𜰲𜰳
𜰴𜰵𜰶𜰷
⎸⎸⎹⎹
⎸⎸⎹⎹
⎸⎸⎹⎹
𜰸𜰹𜰺𜰻
𜰼𜰽𜰾𜰿
⎲-
 >
⎳_

🭻
🯟
🭶🭶
🭻🭻
🯟
🭶🭶
🭻🭻
🮥
🭶🭶
kk
'''
