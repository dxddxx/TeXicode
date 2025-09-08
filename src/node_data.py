parent_dependent_type_dict = {
    ("cmd_sqrt",  ("symb", "[")):  "opn_degr",
    ("opn_degr",  ("symb", "]")):  "cls_degr",
    ("cmd_sbstk", ("symb", "{")):  "opn_stkln",
    ("opn_stkln", ("symb", "}")):  "cls_stkln",
    ("stk_lbrk",  ("symb", "}")):  "cls_stkln",
    ("opn_envn",  ("symb", "}")):  "cls_envn",
    ("cmd_bgin",  ("symb", "{")):  "opn_envn",
    ("cmd_end",   ("symb", "{")):  "opn_envn",
    ("opn_stkln", ("cmnd", "\\")): "stk_lbrk",
    ("stk_lbrk",  ("cmnd", "\\")): "stk_lbrk",
    ("opn_stkln", ("cmnd", "newline")): "stk_lbrk",
    ("stk_lbrk",  ("cmnd", "newline")): "stk_lbrk",
    ("opn_dllr",  ("symb", "$")):  "cls_dllr",
    ("opn_ddlr",  ("symb", "$$")): "cls_ddlr",
    ("cmd_lbrk",  ("symb", "$")):  "cls_dllr",
    ("cmd_lbrk",  ("symb", "$$")): "cls_ddlr",
}

type_dict = {
    ("meta",     "start"): "opn_root", ("meta",     "end"): "cls_root",
    ("meta", "startline"): "opn_line", ("meta", "endline"): "cls_line",
    ("symb",         "^"): "sup_scrpt", ("symb",      "_"): "sub_scrpt",
    ("symb", "$"): "opn_dllr",  ("symb",  "$$"): "opn_ddlr",
    ("cmnd", "["): "opn_brak",  ("cmnd",  "]"): "cls_brak",
    ("cmnd", "("): "opn_pren",  ("cmnd",  ")"): "cls_pren",
    ("symb", "{"): "opn_brac",  ("symb",  "}"): "cls_brac",

    ("cmnd",  "left"): "opn_dlim", ("cmnd", "right"): "cls_dlim",
    ("cmnd",  "bigl"): "big_dlim", ("cmnd",   "big"): "big_dlim",
    ("cmnd",  "bigr"): "big_dlim", ("cmnd",  "Bigl"): "big_dlim",
    ("cmnd",   "Big"): "big_dlim", ("cmnd",  "Bigr"): "big_dlim",
    ("cmnd", "biggl"): "big_dlim", ("cmnd",  "bigg"): "big_dlim",
    ("cmnd", "biggr"): "big_dlim", ("cmnd", "Biggl"): "big_dlim",
    ("cmnd",  "Bigg"): "big_dlim", ("cmnd", "Biggr"): "big_dlim",

    ("cmnd",  "sqrt"): "cmd_sqrt",

    ("cmnd",  "frac"): "cmd_frac", ("cmnd", "tfrac"): "cmd_frac",
    ("cmnd", "dfrac"): "cmd_frac", ("cmnd", "cfrac"): "cmd_frac",

    ("cmnd",   "sum"): "ctr_base", ("cmnd", "prod"): "ctr_base",
    ("cmnd",   "lim"): "ctr_base",

    ("cmnd", "binom"): "cmd_binom", ("cmnd", "dbinom"): "cmd_binom",

    ("cmnd",  "limits"): "cmd_lmts", ("cmnd",     "acute"): "cmd_acnt",
    ("cmnd",     "bar"): "cmd_acnt", ("cmnd",     "breve"): "cmd_acnt",
    ("cmnd",   "check"): "cmd_acnt", ("cmnd",      "ddot"): "cmd_acnt",
    ("cmnd",     "dot"): "cmd_acnt", ("cmnd",     "grave"): "cmd_acnt",
    ("cmnd",     "hat"): "cmd_acnt", ("cmnd",  "mathring"): "cmd_acnt",
    ("cmnd",   "tilde"): "cmd_acnt", ("cmnd",       "vec"): "cmd_acnt",
    ("cmnd", "widehat"): "cmd_acnt", ("cmnd", "widetilde"): "cmd_acnt",

    ("cmnd",  "mathrm"): "cmd_font", ("cmnd",     "mathbf"): "cmd_font",
    ("cmnd",  "mathsf"): "cmd_font", ("cmnd",     "mathtt"): "cmd_font",
    ("cmnd",  "mathit"): "cmd_font", ("cmnd", "mathnormal"): "cmd_font",
    ("cmnd", "mathcal"): "cmd_font", ("cmnd",   "mathfrak"): "cmd_font",
    ("cmnd",  "mathbb"): "cmd_font", ("cmnd",       "text"): "cmd_font",
    ("cmnd", "mathscr"): "cmd_font",

    ("cmnd", "substack"): "cmd_sbstk",
    ("cmnd",    "\\"): "cmd_lbrk", ("cmnd", "newline"): "cmd_lbrk",
    ("cmnd", "begin"): "cmd_bgin", ("cmnd",     "end"): "cmd_end",

    ("cmnd", "textstyle"): "cmd_styl",
    ("cmnd", "displaystyle"): "cmd_styl",
    ("cmnd", "scriptstyle"): "cmd_styl",
    ("cmnd", "scriptscriptstyle"): "cmd_styl",
}


# parent_node_info( ("only/only_not", popable_by["node_type"])
#                   (add_amount)
#                   (can_add_to_nodes_tree, "err if/if_not", under[])
#                   (can_be_children, can_break_parent, can_double_pop)
# ) can double pop is a bit of a hack for cls_stkln and cmd_end
type_info_dict = {
    "opn_root":  ((True,  ["cls_root"
                           ]), (1,), (True,  True, []), (False, False, False)),
    "opn_brac":  ((True,  ["cls_brac"
                           ]), (1,), (True,  True,  []), (True, False, False)),
    "opn_degr":  ((True,  ["cls_degr"
                           ]), (1,), (True,  False, ["cmd_sqrt"
                                                     ]), (True, False, False)),
    "opn_dlim":  ((True,  ["cls_dlim"
                           ]), (1,), (True,  True,  []), (True, False, False)),
    "cmd_sqrt":  ((False, ["opn_degr"
                           ]), (1,), (True,  True,  []), (True, False, False)),
    "cmd_frac":  ((False, []), (2,), (True,  True,  []), (True, False, False)),
    "cmd_binom": ((False, []), (2,), (True,  True,  []), (True, False, False)),
    "big_dlim":  ((False, []), (1,), (True,  True,  []), (True, False, False)),
    "sup_scrpt": ((False, []), (1,), (True,  True,  []), (True, False, False)),
    "sub_scrpt": ((False, []), (1,), (True,  True,  []), (True, False, False)),
    "top_scrpt": ((False, []), (1,), (True,  True,  []), (True, False, False)),
    "btm_scrpt": ((False, []), (1,), (True,  True,  []), (True, False, False)),
    "cls_dlim":  ((False, []), (1,), (True,  True,  []), (True, False, False)),
    "cmd_acnt":  ((False, []), (1,), (True,  True,  []), (True, False, False)),
    "cmd_font":  ((False, []), (1,), (True,  True,  []), (True, False, False)),
    "cmd_lmts":  ((True, []), (0,), (True,  True,  []), (True, False, False)),
    "ctr_base":  ((True, []), (0,), (True,  True,  []), (True, False, False)),
    "txt_leaf":  ((True, []), (0,), (True,  True,  []), (True, False, False)),
    "txt_info":  ((True, []), (0,), (True,  True,  []), (True, False, False)),
    "cmd_leaf":  ((True, []), (0,), (True,  True,  []), (True, False, False)),
    "cmd_styl":  ((True, []), (0,), (False, True,  []), (False, False, False)),
    "cls_root":  ((True, []), (0,), (False, False, ["opn_root"
                                                    ]), (False, False, False)),
    "cls_brac":  ((True, []), (0,), (False, False, ["opn_brac"
                                                    ]), (False, False, False)),
    "cls_degr":  ((True, []), (0,), (False, False, ["opn_degr"
                                                    ]), (False, False, False)),
    "cls_line":  ((True, []), (0,), (False, False, ["opn_line", "cmd_lbrk"
                                                    ]), (False, False, False)),
    "cls_brak":  ((True, []), (0,), (False, False, ["opn_brak", "cmd_lbrk"
                                                    ]), (False, False, False)),
    "cls_pren":  ((True, []), (0,), (False, False, ["opn_pren", "cmd_lbrk"
                                                    ]), (False, False, False)),
    "cls_dllr":  ((True, []), (0,), (False, False, ["opn_dllr", "cmd_lbrk"
                                                    ]), (False, False, False)),
    "cls_ddlr":  ((True, []), (0,), (False, False, ["opn_ddlr", "cmd_lbrk"
                                                    ]), (False, False, False)),
    "cmd_end":  ((False, []), (1,), (True,  False, ["cmd_bgin", "cmd_lbrk"
                                                    ]), (False, True,  False)),
    "cls_stkln": ((True, []), (0,), (False, False, ["opn_stkln", "stk_lbrk"
                                                    ]), (False, True,  True)),
    "cls_envn":  ((True, []), (0,), (False, False, ["opn_envn"
                                                    ]), (False, False, False)),
    "opn_line":  ((True, ["cls_line", "cmd_lbrk"
                          ]), (1,), (True,  False, ["opn_root"
                                                    ]), (True,  False, False)),
    "opn_brak":  ((True, ["cls_brak", "cmd_lbrk"
                          ]), (1,), (True,  False, ["opn_root"
                                                    ]), (True,  False, False)),
    "opn_pren":  ((True, ["cls_pren", "cmd_lbrk"
                          ]), (1,), (True,  False, ["opn_root"
                                                    ]), (True,  False, False)),
    "opn_dllr":  ((True, ["cls_dllr", "cmd_lbrk"
                          ]), (1,), (True,  False, ["opn_root"
                                                    ]), (True,  False, False)),
    "opn_ddlr":  ((True, ["cls_ddlr", "cmd_lbrk"
                          ]), (1,), (True,  False, ["opn_root"
                                                    ]), (True,  False, False)),
    "cmd_bgin":  ((True, ["cmd_end", "cmd_lbrk"
                          ]), (1,), (True,  False, ["opn_root"
                                                    ]), (True,  False, False)),
    "stk_lbrk":  ((True, ["cls_stkln", "stk_lbrk"
                          ]), (1,), (True,  False, ["opn_stkln", "stk_lbrk"
                                                    ]), (True,  True,  False)),
    "opn_stkln": ((True, ["cls_stkln", "stk_lbrk"
                          ]), (1,), (True,  False, ["cmd_sbstk"
                                                    ]), (True,  False, False)),
    "opn_envn":  ((True, ["cls_envn"
                          ]), (1,), (True,  False, ["cmd_bgin", "cmd_end"
                                                    ]), (True,  False, False)),
    "cmd_sbstk": ((True, ["cls_stkln"
                          ]), (1,), (True,  True,  ["opn_root"
                                                    ]), (True,  False, False)),
    "cmd_lbrk":  ((True, ["cmd_lbrk", "cls_line", "cls_brak", "cls_pren",
                          "cls_dllr", "cls_ddlr", "cmd_end"
                          ]), (1,), (True,  False, ["cmd_lbrk", "opn_line",
                                                    "opn_brak", "opn_pren",
                                                    "opn_dllr", "opn_ddlr",
                                                    "cmd_bgin"
                                                    ]), (True,  True,  False)),
}
