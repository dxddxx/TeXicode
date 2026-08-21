# Supported Functions (KaTeX)

## Accents

- [ ] `a'`
- [ ] `\tilde{a}`
- [ ] `\mathring{g}`
- [ ] `a''`
- [ ] `\widetilde{ac}`
- [ ] `\overgroup{AB}`
- [ ] `a^{\prime}`
- [ ] `\utilde{AB}`
- [ ] `\undergroup{AB}`
- [ ] `\acute{a}`
- [ ] `\vec{F}`
- [ ] `\Overrightarrow{AB}`
- [ ] `\bar{y}`
- [ ] `\overleftarrow{AB}`
- [ ] `\overrightarrow{AB}`
- [ ] `\breve{a}`
- [ ] `\underleftarrow{AB}`
- [ ] `\underrightarrow{AB}`
- [ ] `\check{a}`
- [ ] `\overleftharpoon{ac}`
- [ ] `\overrightharpoon{ac}`
- [ ] `\dot{a}`
- [ ] `\overleftrightarrow{AB}`
- [ ] `\overbrace{AB}`
- [ ] `\ddot{a}`
- [ ] `\underleftrightarrow{AB}`
- [ ] `\underbrace{AB}`
- [ ] `\dddot{a}`
- [ ] `\overline{AB}`
- [ ] `\overbracket{AB}`
- [ ] `\ddddot{a}`
- [ ] `\underline{AB}`
- [ ] `\underbracket{AB}`
- [ ] `\grave{a}`
- [ ] `\underbar{X}`
- [ ] `\overlinesegment{AB}`
- [ ] `\hat{\theta}`
- [ ] `\widecheck{ac}`
- [ ] `\underlinesegment{AB}`
- [ ] `\widehat{ac}`

#### Accent functions inside \text{…}

- [ ] `\'{a}`
- [ ] `\~{a}`
- [ ] `\.{a}`
- [ ] `\H{a}`
- [ ] ``\`{a}``
- [ ] `\={a}`
- [ ] `\"{a}`
- [ ] `\v{a}`
- [ ] `\^{a}`
- [ ] `\u{a}`
- [ ] `\r{a}`

## Delimiters

- [ ] `( )`
- [x] `\lparen`
- [x] `\rparen`
- [ ] `⌈ ⌉`
- [x] `\lceil`
- [x] `\rceil`
- [x] `\uparrow` → ↑
- [ ] `[ ]`
- [x] `\lbrack`
- [x] `\rbrack`
- [ ] `⌊ ⌋`
- [x] `\lfloor`
- [x] `\rfloor`
- [x] `\downarrow` → ↓
- [x] `\{ \}`
- [x] `\lbrace`
- [x] `\rbrace`
- [ ] `⎰⎱`
- [x] `\lmoustache`
- [x] `\rmoustache`
- [x] `\updownarrow` → ↕
- [ ] `⟨ ⟩`
- [x] `\langle`
- [x] `\rangle`
- [ ] `⟮ ⟯`
- [x] `\lgroup`
- [x] `\rgroup`
- [x] `\Uparrow` → ⇑
- [ ] `|` → ∣
- [x] `\vert` → ∣
- [ ] `┌ ┐`
- [x] `\ulcorner`
- [x] `\urcorner`
- [x] `\Downarrow` → ⇓
- [x] `\|` → ∥
- [x] `\Vert` → ∥
- [ ] `└ ┘`
- [x] `\llcorner`
- [x] `\lrcorner`
- [x] `\Updownarrow` → ⇕
- [x] `\lvert`
- [x] `\rvert`
- [x] `\lVert`
- [x] `\rVert`
- [ ] `\left.`
- [ ] `\right.`
- [x] `\backslash` → \
- [x] `\lang`
- [x] `\rang`
- [x] `\lt \gt`
- [ ] `⟦ ⟧`
- [x] `\llbracket`
- [x] `\rrbracket`
- [ ] `/` → /
- [x] `\lBrace \rBrace`

#### Delimiter Sizing

- [ ] `\left(\LARGE{AB}\right)`
- [ ] `( \big( \Big( \bigg( \Bigg(`
- [ ] `\left`
- [ ] `\big`
- [ ] `\bigl`
- [ ] `\bigm`
- [ ] `\bigr`
- [ ] `\middle`
- [ ] `\Big`
- [ ] `\Bigl`
- [ ] `\Bigm`
- [ ] `\Bigr`
- [ ] `\right`
- [ ] `\bigg`
- [ ] `\biggl`
- [ ] `\biggm`
- [ ] `\biggr`
- [ ] `\Bigg`
- [ ] `\Biggl`
- [ ] `\Biggm`
- [ ] `\Biggr`

## Environments

- [ ] `\begin{matrix} a & b \\ c & d \end{matrix}`
- [ ] `\begin{array}{cc} a & b \\ c & d \end{array}`
- [ ] `\begin{pmatrix} a & b \\ c & d \end{pmatrix}`
- [ ] `\begin{bmatrix} a & b \\ c & d \end{bmatrix}`
- [ ] `\begin{vmatrix} a & b \\ c & d \end{vmatrix}`
- [ ] `\begin{Vmatrix} a & b \\ c & d \end{Vmatrix}`
- [ ] `\begin{Bmatrix} a & b \\ c & d \end{Bmatrix}`
- [ ] `\def\arraystretch{1.5} \begin{array}{c:c:c} a & b & c \\ \hline d & e & f \\ \hdashline g & h & i \end{array}`
- [ ] `x = \begin{cases} a &\text{if } b \\ c &\text{if } d \end{cases}`
- [ ] `\begin{rcases} a &\text{if } b \\ c &\text{if } d \end{rcases}⇒…`
- [ ] `\begin{smallmatrix} a & b \\ c & d \end{smallmatrix}`
- [ ] `\sum_{ \begin{subarray}{l} i\in\Lambda\\ 0<j<n \end{subarray}}`
- [ ] `$$…$$`
- [ ] `\begin{equation} \begin{split} a &=b+c\\ &=e+f \end{split} \end{equation}`
- [ ] `\begin{align} a&=b+c \\ d+e&=f \end{align}`
- [ ] `\begin{gather} a=b \\ e=b+c \end{gather}`
- [ ] `\begin{alignat}{2} 10&x+&3&y=2\\ 3&x+&13&y=4 \end{alignat}`
- [ ] `\begin{CD} A @>a>> B \\ @VbVV @AAcA \\ C @= D \end{CD}`

#### Other KaTeX Environments

- [ ] `darray`
- [ ] `dcases`
- [ ] `drcases`
- [ ] `displaystyle`
- [ ] `matrix*`
- [ ] `pmatrix*`
- [ ] `bmatrix*`
- [ ] `Bmatrix*`
- [ ] `vmatrix*`
- [ ] `Vmatrix*`
- [ ] `\begin{matrix*}[r]`
- [ ] `equation*`
- [ ] `gather*`
- [ ] `align*`
- [ ] `alignat*`
- [ ] `\nonumber`
- [ ] `\notag`
- [ ] `gathered`
- [ ] `aligned`
- [ ] `alignedat`
- [ ] `\\`
- [ ] `\cr`
- [ ] `\\[distance]`
- [ ] `\cr[distance]`
- [ ] `{array}`
- [ ] `:`
- [ ] `\cline`
- [ ] `\multicolumn`
- [ ] `\tag`
- [ ] `align`
- [ ] `alignat`
- [ ] `gather`

## HTML

- [ ] `\href{https://katex.org/}{\KaTeX}`
- [ ] `\url{https://katex.org/}`
- [ ] `\includegraphics[height=0.8em, totalheight=0.9em, width=0.9em, alt=KA logo]{https://katex.org/img/khan-academy.png}`
- [ ] `\htmlId{bar}{x}`
- [ ] `\htmlClass{foo}{x}`
- [ ] `\htmlStyle{color: red;}{x}`
- [ ] `\htmlData{foo=a, bar=b}{x}`
- [ ] `\includegraphics`
- [ ] `\html`

## Letters and Unicode


#### Greek Letters

- [x] `\Alpha` → A
- [x] `\Beta` → B
- [x] `\Gamma` → Γ
- [x] `\Delta` → Δ
- [x] `\Epsilon` → E
- [x] `\Zeta` → Z
- [x] `\Eta` → H
- [x] `\Theta` → Θ
- [x] `\Iota` → I
- [x] `\Kappa` → K
- [x] `\Lambda` → Λ
- [x] `\Mu` → M
- [x] `\Nu` → N
- [x] `\Xi` → Ξ
- [x] `\Omicron` → O
- [x] `\Pi` → Π
- [x] `\Rho` → P
- [x] `\Sigma` → Σ
- [x] `\Tau` → T
- [x] `\Upsilon` → Υ
- [x] `\Phi` → Φ
- [x] `\Chi` → X
- [x] `\Psi` → Ψ
- [x] `\Omega` → Ω
- [x] `\varGamma` → Γ
- [x] `\varDelta` → Δ
- [x] `\varTheta` → Θ
- [x] `\varLambda` → Λ
- [x] `\varXi` → Ξ
- [x] `\varPi` → Π
- [x] `\varSigma` → Σ
- [x] `\varUpsilon` → Υ
- [x] `\varPhi` → Φ
- [x] `\varPsi` → Ψ
- [x] `\varOmega` → Ω
- [x] `\alpha` → α
- [x] `\beta` → β
- [x] `\gamma` → γ
- [x] `\delta` → δ
- [x] `\epsilon` → ϵ
- [x] `\zeta` → ζ
- [x] `\eta` → η
- [x] `\theta` → θ
- [x] `\iota` → ι
- [x] `\kappa` → κ
- [x] `\lambda` → λ
- [x] `\mu` → μ
- [x] `\nu` → ν
- [x] `\xi` → ξ
- [x] `\omicron` → ο
- [x] `\pi` → π
- [x] `\rho` → ρ
- [x] `\sigma` → σ
- [x] `\tau` → τ
- [x] `\upsilon` → υ
- [x] `\phi` → ϕ
- [x] `\chi` → χ
- [x] `\psi` → ψ
- [x] `\omega` → ω
- [x] `\varepsilon` → ε
- [x] `\varkappa` → ϰ
- [x] `\vartheta` → ϑ
- [x] `\thetasym` → ϑ
- [x] `\varpi` → ϖ
- [x] `\varrho` → ϱ
- [x] `\varsigma` → ς
- [x] `\varphi` → φ
- [x] `\digamma` → ϝ

#### Other Letters

- [x] `\imath` → ı
- [x] `\nabla` → ∇
- [x] `\Im` → ℑ
- [x] `\Reals` → R
- [x] `\text{\OE}`
- [x] `\jmath` → ȷ
- [x] `\partial` → ∂
- [x] `\image` → ℑ
- [x] `\wp` → ℘
- [x] `\text{\o}`
- [x] `\aleph` → ℵ
- [x] `\Game` → ⅁
- [x] `\Bbbk` → k
- [x] `\weierp` → ℘
- [x] `\text{\O}`
- [x] `\alef` → ℵ
- [x] `\Finv` → Ⅎ
- [x] `\N` → N
- [x] `\Z` → Z
- [x] `\text{\ss}`
- [x] `\alefsym` → ℵ
- [x] `\cnums` → C
- [x] `\natnums` → N
- [x] `\text{\aa}`
- [x] `\text{\i}`
- [x] `\beth` → ℶ
- [x] `\Complex` → C
- [x] `\R` → R
- [x] `\text{\AA}`
- [x] `\text{\j}`
- [x] `\gimel` → ℷ
- [x] `\ell` → ℓ
- [x] `\Re` → ℜ
- [x] `\text{\ae}`
- [x] `\daleth` → ℸ
- [x] `\hbar` → ℏ
- [x] `\real` → ℜ
- [x] `\text{\AE}`
- [x] `\eth` → ð
- [x] `\hslash` → ℏ
- [x] `\reals` → R
- [x] `\text{\oe}`
- [ ] `A²⁺³`
- [ ] `A^{2+3}`

#### Unicode Mathematical Alphanumeric Symbols


#### Unicode

- [ ] `.latin_fallback`
- [ ] `.cyrillic_fallback`
- [ ] `.brahmic_fallback`
- [ ] `.georgian_fallback`
- [ ] `.cjk_fallback`
- [ ] `.hangul_fallback`
- [ ] `strict: false`
- [ ] `strict: "warn"`
- [ ] `\char`
- [ ] `\char"263a`

## Layout


### Annotation

- [ ] `\cancel{5}`
- [ ] `\overbrace{a+b+c}^{\text{note}}`
- [ ] `\bcancel{5}`
- [ ] `\underbrace{a+b+c}_{\text{note}}`
- [ ] `\xcancel{ABC}`
- [ ] `\not =`
- [ ] `\text{\sout{abc}}`
- [ ] `\boxed{\pi=\frac c d}`
- [ ] `$a_{\angl n}`
- [ ] `a_\angln`
- [ ] `\overbracket{a+b+c}^{\text{note}}`
- [ ] `\underbracket{a+b+c}_{\text{note}}`
- [ ] `\phase{-78^\circ}`
- [ ] `\tag{hi} x+y^{2x}`
- [ ] `\tag*{hi} x+y^{2x}`

### Line Breaks

- [ ] `\nobreak`
- [ ] `{F=ma}`
- [ ] `\allowbreak`
- [ ] `\newline`
- [ ] `strict: true`

### Vertical Layout

- [ ] `x_n`
- [ ] `\stackrel{!}{=}`
- [ ] `a \atop b`
- [ ] `e^x`
- [ ] `\overset{!}{=}`
- [ ] `a\raisebox{0.25em}{$b$}c`
- [ ] `_u^o`
- [ ] `\underset{!}{=}`
- [ ] `a+\left(\vcenter{\hbox{$\frac{\frac a b}c$}}\right)`
- [ ] `\sum_{\substack{0<i<m\\0<j<n}}`
- [ ] `\raisebox`
- [ ] `\hbox`
- [ ] `$…$`
- [ ] `\vcenter`
- [ ] `strict`

### Overlap and Spacing

- [ ] `{=}\mathllap{/\,}`
- [ ] `\left(x^{\smash{2}}\right)`
- [ ] `\mathrlap{\,/}{=}`
- [ ] `\sqrt{\smash[b]{y}}`
- [ ] `\sum_{\mathclap{1\le i\le j\le n}} x_{ij}`
- [ ] `\llap`
- [ ] `\rlap`
- [ ] `\clap`

#### Spacing

- [x] `\,`
- [ ] `\kern{distance}`
- [x] `\thinspace`
- [ ] `\mkern{distance}`
- [x] `\>`
- [ ] `\mskip{distance}`
- [x] `\:`
- [ ] `\hskip{distance}`
- [x] `\medspace`
- [ ] `\hspace{distance}`
- [x] `\;`
- [ ] `\hspace*{distance}`
- [x] `\thickspace`
- [ ] `\phantom{content}`
- [x] `\enspace`
- [ ] `\hphantom{content}`
- [x] `\quad`
- [ ] `\vphantom{content}`
- [x] `\qquad`
- [ ] `\!`
- [x] `~`
- [ ] `\negthinspace`
- [x] `\<space>`
- [ ] `\negmedspace`
- [x] `\nobreakspace`
- [ ] `\negthickspace`
- [x] `\space`
- [ ] `\mathstrut`
- [ ] `\vphantom{(}`

#### Notes:

- [ ] `distance`
- [ ] `\kern`
- [ ] `\mkern`
- [ ] `\mskip`
- [ ] `\hspace`
- [ ] `\kern1em`
- [ ] `mu`

## Logic and Set Theory

- [x] `\forall` → ∀
- [x] `\complement` → ∁
- [x] `\therefore` → ∴
- [x] `\emptyset` → ∅
- [x] `\exists` → ∃
- [x] `\subset` → ⊂
- [x] `\because` → ∵
- [x] `\empty` → ∅
- [x] `\exist` → ∃
- [x] `\supset` → ⊃
- [x] `\mapsto` → ↦
- [x] `\varnothing` → ∅
- [x] `\nexists` → ∄
- [x] `\mid` → ∣
- [x] `\to` → →
- [x] `\implies`
- [x] `\in` → ∈
- [x] `\land` → ∧
- [x] `\gets` → ←
- [x] `\impliedby`
- [x] `\isin` → ∈
- [x] `\lor` → ∨
- [x] `\leftrightarrow` → ↔
- [x] `\iff`
- [x] `\notin` → ∉
- [x] `\ni` → ∋
- [x] `\notni` → ∌
- [x] `\neg`
- [x] `\lnot`
- [ ] `\Set{ x | x<\frac 1 2 }`
- [ ] `\set{x|x<5}`

## Macros

- [ ] `\def\foo{x^2} \foo + \foo`
- [ ] `\gdef\foo#1{#1^2} \foo{y} + \foo{y}`
- [ ] `\edef\macroname#1#2…{definition to be expanded}`
- [ ] `\xdef\macroname#1#2…{definition to be expanded}`
- [ ] `\let\foo=\bar`
- [ ] `\futurelet\foo\bar x`
- [ ] `\global\def\macroname#1#2…{definition}`
- [ ] `\newcommand\macroname[numargs]{definition}`
- [ ] `\renewcommand\macroname[numargs]{definition}`
- [ ] `\providecommand\macroname[numargs]{definition}`
- [ ] `\gdef`
- [ ] `\xdef`
- [ ] `\global\def`
- [ ] `\global\edef`
- [ ] `\global\let`
- [ ] `\global\futurelet`
- [ ] `\par`
- [ ] `\long`
- [ ] `\mathchoice`
- [ ] `\TextOrMath`
- [ ] `\@ifstar`
- [ ] `\@ifnextchar`
- [ ] `\@firstoftwo`
- [ ] `\@secondoftwo`
- [ ] `\relax`
- [ ] `\expandafter`
- [ ] `\noexpand`
- [ ] `\makeatletter`

## Operators


### Big Operators

- [x] `\sum` → ∑
- [x] `\prod` → ∏
- [ ] `\bigotimes` → ⨂
- [ ] `\bigvee` → ⋁
- [x] `\int` → ∫
- [ ] `\coprod` → ∐
- [ ] `\bigoplus` → ⨁
- [ ] `\bigwedge` → ⋀
- [x] `\iint` → ∬
- [ ] `\intop` → ∫
- [ ] `\bigodot` → ⨀
- [ ] `\bigcap` → ⋂
- [x] `\iiint` → ∭
- [ ] `\smallint` → ∫
- [ ] `\biguplus` → ⨄
- [ ] `\bigcup` → ⋃
- [x] `\oint` → ∮
- [x] `\oiint` → ∯
- [x] `\oiiint` → ∰
- [ ] `\bigsqcup` → ⨆

### Binary Operators

- [ ] `+` → +
- [x] `\cdot` → ⋅
- [x] `\gtrdot` → ⋗
- [ ] `x \pmod a`
- [ ] `-` → −
- [x] `\cdotp` → ⋅
- [x] `\intercal` → ⊺
- [ ] `x \pod a`
- [x] `\centerdot` → ⋅
- [x] `\rhd` → ⊳
- [ ] `*` → ∗
- [x] `\circ` → ∘
- [x] `\leftthreetimes` → ⋋
- [x] `\rightthreetimes` → ⋌
- [x] `\amalg` → ⨿
- [x] `\circledast` → ⊛
- [x] `\ldotp` → .
- [x] `\rtimes` → ⋊
- [x] `\And` → &
- [x] `\circledcirc` → ⊚
- [x] `\setminus` → ∖
- [x] `\ast` → ∗
- [x] `\circleddash` → ⊝
- [x] `\lessdot` → ⋖
- [x] `\smallsetminus` → ∖
- [x] `\barwedge` → ⊼
- [x] `\Cup` → ⋓
- [x] `\lhd` → ⊲
- [x] `\sqcap` → ⊓
- [x] `\bigcirc` → ◯
- [x] `\cup` → ∪
- [x] `\ltimes` → ⋉
- [x] `\sqcup` → ⊔
- [x] `\bmod`
- [x] `\curlyvee` → ⋎
- [ ] `x\mod a`
- [x] `\times` → ×
- [x] `\boxdot` → ⊡
- [x] `\curlywedge` → ⋏
- [x] `\mp` → ∓
- [x] `\unlhd` → ⊴
- [x] `\boxminus` → ⊟
- [x] `\div` → ÷
- [x] `\odot` → ⊙
- [x] `\unrhd` → ⊵
- [x] `\boxplus` → ⊞
- [x] `\divideontimes` → ⋇
- [x] `\ominus` → ⊖
- [x] `\uplus` → ⊎
- [x] `\boxtimes` → ⊠
- [x] `\dotplus` → ∔
- [x] `\oplus` → ⊕
- [x] `\vee` → ∨
- [x] `\bullet` → ∙
- [x] `\doublebarwedge` → ⩞
- [x] `\otimes` → ⊗
- [x] `\veebar` → ⊻
- [x] `\Cap` → ⋒
- [x] `\doublecap` → ⋒
- [x] `\oslash` → ⊘
- [x] `\wedge` → ∧
- [x] `\cap` → ∩
- [x] `\doublecup` → ⋓
- [x] `\pm`
- [x] `\plusmn`
- [x] `\wr` → ≀

### Fractions and Binomials

- [ ] `\frac{a}{b}`
- [ ] `\tfrac{a}{b}`
- [ ] `\genfrac ( ] {2pt}{1}a{a+1}`
- [ ] `{a \over b}`
- [ ] `\dfrac{a}{b}`
- [ ] `{a \above{2pt} b+1}`
- [ ] `a/b`
- [ ] `\cfrac{a}{1 + \cfrac{1}{b}}`
- [ ] `\binom{n}{k}`
- [ ] `\dbinom{n}{k}`
- [ ] `{n\brace k}`
- [ ] `{n \choose k}`
- [ ] `\tbinom{n}{k}`
- [ ] `{n\brack k}`

### Math Operators

- [x] `\arcsin`
- [x] `\cosec`
- [x] `\deg`
- [x] `\sec`
- [x] `\arccos`
- [x] `\cosh`
- [x] `\dim`
- [x] `\sin`
- [x] `\arctan`
- [x] `\cot`
- [x] `\exp`
- [x] `\sinh`
- [x] `\arctg`
- [x] `\cotg`
- [x] `\hom`
- [x] `\sh`
- [x] `\arcctg`
- [x] `\coth`
- [x] `\ker`
- [x] `\tan`
- [x] `\arg`
- [x] `\csc`
- [x] `\lg`
- [x] `\tanh`
- [x] `\ch`
- [x] `\ctg`
- [x] `\ln`
- [x] `\tg`
- [x] `\cos`
- [x] `\cth`
- [x] `\log`
- [x] `\th`
- [ ] `\operatorname{f}`
- [x] `\argmax`
- [x] `\injlim`
- [x] `\min`
- [ ] `\varinjlim`
- [x] `\argmin`
- [x] `\lim`
- [x] `\plim`
- [ ] `\varliminf`
- [x] `\det`
- [x] `\liminf`
- [x] `\Pr`
- [ ] `\varlimsup`
- [x] `\gcd`
- [x] `\limsup`
- [x] `\projlim`
- [ ] `\varprojlim`
- [x] `\inf`
- [x] `\max`
- [x] `\sup`
- [ ] `\operatorname*{f}`
- [ ] `\operatornamewithlimits{f}`
- [ ] `\limits`

### \sqrt

- [ ] `\sqrt{x}`
- [ ] `\sqrt[3]{x}`

## Relations

- [ ] `=` → =
- [x] `\doteqdot` → ≑
- [x] `\lessapprox` → ⪅
- [x] `\smile` → ⌣
- [ ] `<` → <
- [x] `\eqcirc` → ≖
- [x] `\lesseqgtr` → ⋚
- [x] `\sqsubset` → ⊏
- [ ] `>` → >
- [x] `\eqcolon`
- [x] `\minuscolon`
- [x] `\lesseqqgtr` → ⪋
- [x] `\sqsubseteq` → ⊑
- [x] `\Eqcolon`
- [x] `\minuscoloncolon`
- [x] `\lessgtr` → ≶
- [x] `\sqsupset` → ⊐
- [x] `\approx` → ≈
- [x] `\eqqcolon`
- [x] `\equalscolon`
- [x] `\lesssim` → ≲
- [x] `\sqsupseteq` → ⊒
- [x] `\approxcolon`
- [x] `\Eqqcolon`
- [x] `\equalscoloncolon`
- [x] `\ll` → ≪
- [x] `\Subset` → ⋐
- [x] `\approxcoloncolon`
- [x] `\eqsim` → ≂
- [x] `\lll` → ⋘
- [x] `\sub`
- [x] `\approxeq` → ≊
- [x] `\eqslantgtr` → ⪖
- [x] `\llless` → ⋘
- [x] `\subseteq`
- [x] `\sube`
- [x] `\asymp` → ≍
- [x] `\eqslantless` → ⪕
- [x] `\lt` → <
- [x] `\subseteqq` → ⫅
- [x] `\backepsilon` → ∍
- [x] `\equiv` → ≡
- [x] `\succ` → ≻
- [x] `\backsim` → ∽
- [x] `\fallingdotseq` → ≒
- [x] `\models` → ⊨
- [x] `\succapprox` → ⪸
- [x] `\backsimeq` → ⋍
- [x] `\frown` → ⌢
- [x] `\multimap` → ⊸
- [x] `\succcurlyeq` → ≽
- [x] `\between` → ≬
- [x] `\ge` → ≥
- [x] `\origof` → ⊶
- [x] `\succeq` → ⪰
- [x] `\bowtie` → ⋈
- [x] `\geq` → ≥
- [x] `\owns` → ∋
- [x] `\succsim` → ≿
- [x] `\bumpeq` → ≏
- [x] `\geqq` → ≧
- [x] `\parallel` → ∥
- [x] `\Supset` → ⋑
- [x] `\Bumpeq` → ≎
- [x] `\geqslant` → ⩾
- [x] `\perp` → ⊥
- [x] `\circeq` → ≗
- [x] `\gg` → ≫
- [x] `\pitchfork` → ⋔
- [x] `\supseteq`
- [x] `\supe`
- [x] `\colonapprox`
- [x] `\ggg` → ⋙
- [x] `\prec` → ≺
- [x] `\supseteqq` → ⫆
- [x] `\Colonapprox`
- [x] `\coloncolonapprox`
- [x] `\gggtr` → ⋙
- [x] `\precapprox` → ⪷
- [x] `\thickapprox` → ≈
- [x] `\coloneq`
- [x] `\colonminus`
- [x] `\gt` → >
- [x] `\preccurlyeq` → ≼
- [x] `\thicksim` → ∼
- [x] `\Coloneq`
- [x] `\coloncolonminus`
- [x] `\gtrapprox` → ⪆
- [x] `\preceq` → ⪯
- [x] `\trianglelefteq` → ⊴
- [x] `\coloneqq`
- [x] `\colonequals`
- [x] `\gtreqless` → ⋛
- [x] `\precsim` → ≾
- [x] `\triangleq` → ≜
- [x] `\Coloneqq`
- [x] `\coloncolonequals`
- [x] `\gtreqqless` → ⪌
- [x] `\propto` → ∝
- [x] `\trianglerighteq` → ⊵
- [x] `\colonsim`
- [x] `\gtrless` → ≷
- [x] `\risingdotseq` → ≓
- [x] `\varpropto` → ∝
- [x] `\Colonsim`
- [x] `\coloncolonsim`
- [x] `\gtrsim` → ≳
- [x] `\shortmid` → ∣
- [x] `\vartriangle` → △
- [x] `\cong` → ≅
- [x] `\imageof` → ⊷
- [x] `\shortparallel` → ∥
- [x] `\vartriangleleft` → ⊲
- [x] `\curlyeqprec` → ⋞
- [x] `\sim` → ∼
- [x] `\vartriangleright` → ⊳
- [x] `\curlyeqsucc` → ⋟
- [x] `\Join` → ⋈
- [x] `\simcolon`
- [x] `\vcentcolon`
- [x] `\ratio`
- [x] `\dashv` → ⊣
- [x] `\le` → ≤
- [x] `\simcoloncolon`
- [x] `\vdash` → ⊢
- [x] `\dblcolon`
- [x] `\coloncolon`
- [x] `\leq` → ≤
- [x] `\simeq` → ≃
- [x] `\vDash` → ⊨
- [x] `\doteq` → ≐
- [x] `\leqq` → ≦
- [x] `\smallfrown` → ⌢
- [x] `\Vdash` → ⊩
- [x] `\Doteq` → ≑
- [x] `\leqslant` → ⩽
- [x] `\smallsmile` → ⌣
- [x] `\Vvdash` → ⊪
- [ ] `≔ ≕ ⩴`

### Negated Relations

- [x] `\gnapprox` → ⪊
- [x] `\ngeqslant` → ≱
- [x] `\nsubseteq` → ⊈
- [x] `\precneqq` → ⪵
- [x] `\gneq` → ⪈
- [x] `\ngtr` → ≯
- [x] `\nsubseteqq` → ⊈
- [x] `\precnsim` → ⋨
- [x] `\gneqq` → ≩
- [x] `\nleq` → ≰
- [x] `\nsucc` → ⊁
- [x] `\subsetneq` → ⊊
- [x] `\gnsim` → ⋧
- [x] `\nleqq` → ≰
- [x] `\nsucceq` → ⋡
- [x] `\subsetneqq` → ⫋
- [x] `\gvertneqq` → ≩
- [x] `\nleqslant` → ≰
- [x] `\nsupseteq` → ⊉
- [x] `\succnapprox` → ⪺
- [x] `\lnapprox` → ⪉
- [x] `\nless` → ≮
- [x] `\nsupseteqq` → ⊉
- [x] `\succneqq` → ⪶
- [x] `\lneq` → ⪇
- [x] `\nmid` → ∤
- [x] `\ntriangleleft` → ⋪
- [x] `\succnsim` → ⋩
- [x] `\lneqq` → ≨
- [x] `\ntrianglelefteq` → ⋬
- [x] `\supsetneq` → ⊋
- [x] `\lnsim` → ⋦
- [x] `\ntriangleright` → ⋫
- [x] `\supsetneqq` → ⫌
- [x] `\lvertneqq` → ≨
- [x] `\nparallel` → ∦
- [x] `\ntrianglerighteq` → ⋭
- [x] `\varsubsetneq` → ⊊
- [x] `\ncong` → ≆
- [x] `\nprec` → ⊀
- [x] `\nvdash` → ⊬
- [x] `\varsubsetneqq` → ⫋
- [x] `\ne` → ≠
- [x] `\npreceq` → ⋠
- [x] `\nvDash` → ⊭
- [x] `\varsupsetneq` → ⊋
- [x] `\neq` → ≠
- [x] `\nshortmid` → ∤
- [x] `\nVDash` → ⊯
- [x] `\varsupsetneqq` → ⫌
- [x] `\ngeq` → ≱
- [x] `\nshortparallel` → ∦
- [x] `\nVdash` → ⊮
- [x] `\ngeqq` → ≱
- [x] `\nsim` → ≁
- [x] `\precnapprox` → ⪹

### Arrows

- [x] `\circlearrowleft` → ↺
- [x] `\leftharpoonup` → ↼
- [x] `\rArr` → ⇒
- [x] `\circlearrowright` → ↻
- [x] `\leftleftarrows` → ⇇
- [x] `\rarr` → →
- [x] `\curvearrowleft` → ↶
- [x] `\restriction` → ↾
- [x] `\curvearrowright` → ↷
- [x] `\Leftrightarrow` → ⇔
- [x] `\rightarrow` → →
- [x] `\Darr` → ⇓
- [x] `\leftrightarrows` → ⇆
- [x] `\Rightarrow` → ⇒
- [x] `\dArr` → ⇓
- [x] `\leftrightharpoons` → ⇋
- [x] `\rightarrowtail` → ↣
- [x] `\darr` → ↓
- [x] `\leftrightsquigarrow` → ↭
- [x] `\rightharpoondown` → ⇁
- [x] `\dashleftarrow` → ⇠
- [x] `\Lleftarrow` → ⇚
- [x] `\rightharpoonup` → ⇀
- [x] `\dashrightarrow` → ⇢
- [x] `\longleftarrow` → ⟵
- [x] `\rightleftarrows` → ⇄
- [x] `\Longleftarrow` → ⟸
- [x] `\rightleftharpoons` → ⇌
- [x] `\longleftrightarrow` → ⟷
- [x] `\rightrightarrows` → ⇉
- [x] `\downdownarrows` → ⇊
- [x] `\Longleftrightarrow` → ⟺
- [x] `\rightsquigarrow` → ⇝
- [x] `\downharpoonleft` → ⇃
- [x] `\longmapsto` → ⟼
- [x] `\Rrightarrow` → ⇛
- [x] `\downharpoonright` → ⇂
- [x] `\longrightarrow` → ⟶
- [x] `\Rsh` → ↱
- [x] `\Longrightarrow` → ⟹
- [x] `\searrow` → ↘
- [x] `\Harr` → ⇔
- [x] `\looparrowleft` → ↫
- [x] `\swarrow` → ↙
- [x] `\hArr` → ⇔
- [x] `\looparrowright` → ↬
- [x] `\harr` → ↔
- [x] `\Lrarr` → ⇔
- [x] `\twoheadleftarrow` → ↞
- [x] `\hookleftarrow` → ↩
- [x] `\lrArr` → ⇔
- [x] `\twoheadrightarrow` → ↠
- [x] `\hookrightarrow` → ↪
- [x] `\lrarr` → ↔
- [x] `\Uarr` → ⇑
- [x] `\Lsh` → ↰
- [x] `\uArr` → ⇑
- [x] `\uarr` → ↑
- [x] `\nearrow` → ↗
- [x] `\Larr` → ⇐
- [x] `\nleftarrow` → ↚
- [x] `\lArr` → ⇐
- [x] `\nLeftarrow` → ⇍
- [x] `\larr` → ←
- [x] `\nleftrightarrow` → ↮
- [x] `\leadsto` → ⇝
- [x] `\nLeftrightarrow` → ⇎
- [x] `\upharpoonleft` → ↿
- [x] `\leftarrow` → ←
- [x] `\nrightarrow` → ↛
- [x] `\upharpoonright` → ↾
- [x] `\Leftarrow` → ⇐
- [x] `\nRightarrow` → ⇏
- [x] `\upuparrows` → ⇈
- [x] `\leftarrowtail` → ↢
- [x] `\nwarrow` → ↖
- [x] `\leftharpoondown` → ↽
- [x] `\Rarr` → ⇒

#### Extensible Arrows

- [ ] `\xleftarrow{abc}`
- [ ] `\xrightarrow[under]{over}`
- [ ] `\xLeftarrow{abc}`
- [ ] `\xRightarrow{abc}`
- [ ] `\xleftrightarrow{abc}`
- [ ] `\xLeftrightarrow{abc}`
- [ ] `\xhookleftarrow{abc}`
- [ ] `\xhookrightarrow{abc}`
- [ ] `\xtwoheadleftarrow{abc}`
- [ ] `\xtwoheadrightarrow{abc}`
- [ ] `\xleftharpoonup{abc}`
- [ ] `\xrightharpoonup{abc}`
- [ ] `\xleftharpoondown{abc}`
- [ ] `\xrightharpoondown{abc}`
- [ ] `\xleftrightharpoons{abc}`
- [ ] `\xrightleftharpoons{abc}`
- [ ] `\xtofrom{abc}`
- [ ] `\xmapsto{abc}`
- [ ] `\xlongequal{abc}`

## Special Notation


#### Bra-ket Notation

- [ ] `\bra{\phi}`
- [ ] `\ket{\psi}`
- [ ] `\braket{\phi|\psi}`
- [ ] `\Bra{\phi}`
- [ ] `\Ket{\psi}`
- [ ] `\Braket{ ϕ | \frac{∂^2}{∂ t^2} | ψ }`

## Style, Color, Size, and Font


#### Class Assignment

- [ ] `\mathbin`
- [ ] `\mathclose`
- [ ] `\mathinner`
- [ ] `\mathop`
- [ ] `\mathopen`
- [ ] `\mathord`
- [ ] `\mathpunct`
- [ ] `\mathrel`

#### Color

- [ ] `\color{blue} F=ma`
- [ ] `\color`
- [ ] `\textcolor{blue}{F=ma}`
- [ ] `\textcolor{#228B22}{F=ma}`
- [ ] `\colorbox{aqua}{$F=ma$}`
- [ ] `\fcolorbox{red}{aqua}{$F=ma$}`
- [ ] `\colorbox`
- [ ] `\fcolorbox`
- [ ] `$`

#### Font

- [ ] `\mathrm{Ab0}`
- [ ] `\mathbf{Ab0}`
- [ ] `\mathsf{Ab0}`
- [ ] `\mathnormal{Ab0}`
- [ ] `\textbf{Ab0}`
- [ ] `\textsf{Ab0}`
- [ ] `\textrm{Ab0}`
- [ ] `\bf Ab0`
- [ ] `\sf Ab0`
- [ ] `\rm Ab0`
- [ ] `\bold{Ab0}`
- [ ] `\mathsfit{Ab0}`
- [ ] `\textnormal{Ab0}`
- [ ] `\boldsymbol{Ab0}`
- [ ] `\Bbb{AB}`
- [ ] `\text{Ab0}`
- [ ] `\bm{Ab0}`
- [ ] `\mathbb{AB}`
- [ ] `\textup{Ab0}`
- [ ] `\textmd{Ab0}`
- [ ] `\frak{Ab0}`
- [ ] `\mathit{Ab0}`
- [ ] `\mathtt{Ab0}`
- [ ] `\mathfrak{Ab0}`
- [ ] `\textit{Ab0}`
- [ ] `\texttt{Ab0}`
- [ ] `\mathcal{AB0}`
- [ ] `\it Ab0`
- [ ] `\tt Ab0`
- [ ] `\cal AB0`
- [ ] `\emph{Ab0}`
- [ ] `\mathscr{AB}`
- [ ] `\textXX`
- [ ] `\textsf{\textbf{H}}`
- [ ] `\mathsf{\mathbf{H}}`
- [ ] `\pmb`
- [ ] `\pmb{\mu}`

#### Size

- [ ] `\Huge AB`
- [ ] `\normalsize AB`
- [ ] `\huge AB`
- [ ] `\small AB`
- [ ] `\LARGE AB`
- [ ] `\footnotesize AB`
- [ ] `\Large AB`
- [ ] `\scriptsize AB`
- [ ] `\large AB`
- [ ] `\tiny AB`

#### Style

- [ ] `\displaystyle\sum_{i=1}^n`
- [ ] `\textstyle\sum_{i=1}^n`
- [ ] `\scriptstyle x` → x
- [ ] `\scriptscriptstyle x` → x
- [ ] `\lim\limits_x`
- [ ] `\lim\nolimits_x`
- [ ] `\verb!x^2!`
- [ ] `\text{…}`

## Symbols and Punctuation

- [ ] `% comment`
- [x] `\dots` → …
- [ ] `\KaTeX`
- [x] `\%` → %
- [x] `\cdots` → ⋯
- [x] `\LaTeX`
- [x] `\#` → #
- [x] `\ddots` → ⋱
- [x] `\TeX`
- [x] `\&` → &
- [x] `\ldots` → …
- [x] `\_` → _
- [x] `\vdots`
- [x] `\infty` → ∞
- [x] `\text{\textunderscore}`
- [x] `\dotsb` → ⋯
- [x] `\infin` → ∞
- [x] `\text{--}`
- [x] `\dotsc` → …
- [x] `\checkmark` → ✓
- [x] `\text{\textendash}`
- [x] `\dotsi`
- [x] `\dag` → †
- [x] `\text{---}`
- [x] `\dotsm` → ⋯
- [x] `\dagger` → †
- [x] `\text{\textemdash}`
- [x] `\dotso` → …
- [x] `\text{\textdagger}`
- [x] `\text{\textasciitilde}`
- [x] `\sdot` → ⋅
- [x] `\ddag` → ‡
- [x] `\text{\textasciicircum}`
- [x] `\mathellipsis` → …
- [x] `\ddagger` → ‡
- [ ] `` ` `` → ‘
- [x] `\text{\textellipsis}` → …
- [x] `\text{\textdaggerdbl}`
- [x] `\text{\textquoteleft}`
- [x] `\Box` → □
- [x] `\Dagger` → ‡
- [x] `\lq` → ‘
- [x] `\square` → □
- [x] `\angle` → ∠
- [x] `\text{\textquoteright}`
- [x] `\blacksquare` → ■
- [x] `\measuredangle` → ∡
- [x] `\rq`
- [x] `\triangle` → △
- [x] `\sphericalangle` → ∢
- [x] `\text{\textquotedblleft}`
- [x] `\triangledown` → ▽
- [x] `\top` → ⊤
- [ ] `"` → "
- [x] `\triangleleft` → ◃
- [x] `\bot` → ⊥
- [x] `\text{\textquotedblright}`
- [x] `\triangleright` → ▹
- [x] `\$` → $
- [x] `\colon`
- [x] `\bigtriangledown` → ▽
- [x] `\text{\textdollar}`
- [x] `\backprime` → ‵
- [x] `\bigtriangleup` → △
- [x] `\pounds` → £
- [x] `\prime` → ′
- [x] `\blacktriangle` → ▲
- [x] `\mathsterling` → £
- [x] `\text{\textless}`
- [x] `\blacktriangledown` → ▼
- [x] `\text{\textsterling}`
- [x] `\text{\textgreater}`
- [x] `\blacktriangleleft` → ◀
- [x] `\yen` → ¥
- [x] `\text{\textbar}`
- [x] `\blacktriangleright` → ▶
- [x] `\surd` → √
- [x] `\text{\textbardbl}`
- [x] `\diamond` → ⋄
- [x] `\degree` → °
- [x] `\text{\textbraceleft}`
- [x] `\Diamond` → ◊
- [x] `\text{\textdegree}`
- [x] `\text{\textbraceright}`
- [x] `\lozenge` → ◊
- [x] `\mho` → ℧
- [x] `\text{\textbackslash}`
- [x] `\blacklozenge` → ⧫
- [x] `\diagdown` → ╲
- [x] `\text{\P}`
- [x] `\P`
- [x] `\star` → ⋆
- [x] `\diagup` → ╱
- [x] `\text{\S}`
- [x] `\S`
- [x] `\bigstar` → ★
- [x] `\flat` → ♭
- [x] `\text{\sect}`
- [x] `\clubsuit` → ♣
- [x] `\natural` → ♮
- [x] `\copyright`
- [x] `\clubs` → ♣
- [x] `\sharp` → ♯
- [x] `\circledR` → ®
- [x] `\diamondsuit` → ♢
- [x] `\heartsuit` → ♡
- [x] `\text{\textregistered}`
- [x] `\diamonds` → ♢
- [x] `\hearts` → ♡
- [x] `\circledS` → Ⓢ
- [x] `\spadesuit` → ♠
- [x] `\spades` → ♠
- [ ] `\text{\textcircled a}`
- [x] `\maltese` → ✠
- [x] `\minuso` → ⦵

## Units

