# Inline LaTeX

This is an inline latex equation $e \approx 2.718281828$ wrapped with dollar signs. This is an inline latex equation \(e^{i\theta} = \cos\theta + i\sin\theta\) wrapped with backslash parenthesis. This is also an inline latex equation $e\ =\ \lim_{n\to\infty}~\left(1+\frac1n\right)^n$, but too tall to be rendered inline.

# LaTeX Blocks

This is a latex block
<!-- some spaces are added in for padding and aesthetics... -->
\begin{align*}
\ \sin(x) ~&=~ \Im(e^{ix})
~&=~ \frac{e^{ix} - e^{-ix}}{2i}
^\
\\
~&=~ \sum_{n=0}^\infty
\left[
(-1)^n\frac{x^{2n+1}}{(2n+1)!}
\right]
~&=~ x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} +\ \cdots
\\
~&=~ x\prod_{n=1}^{\infty}
\left(1 - \frac{x^2}{n^2\pi^2} \right)
~&=~ x
\left(1 - \frac{x^2}{ \pi^2} \right)
\left(1 - \frac{x^2}{4\pi^2} \right)
\left(1 - \frac{x^2}{9\pi^2} \right) \cdots
\
\end{align*}
