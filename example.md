# Inline LaTeX

This is an inline latex equation $e \approx 2.718281828$ wrapped with dollar signs
This is an inline latex equation \(e^{i\theta} = \cos\theta + i\sin\theta\) wrapped with backslash parenthesis
This is also an inline latex equation $e\ =\ \lim_{n\to\infty}~\left(1+\frac1n\right)^n$, but too tall to be rendered inline.

# LaTeX Blocks

This is a latex block wrapped with double dollar signs

$$
\cos\theta ~=~ \Re(e^{i\theta})
~=~ \frac{e^{i\theta} + e^{-i\theta}}2 \\
\sin\theta ~=~ \Im(e^{i\theta})
~=~ \frac{e^{i\theta} - e^{-i\theta}}{2i}
$$

This is a latex block wrapped with backslash square brackets
<!-- actually its begin align now, will update screenshot later -->

\begin{align*}
|a+bi| ~&= \sqrt{a^2+b^2} \\
\arg(a+bi) ~&=~ \tan^{-1}\left( \frac b a \right)
\end{align*}

This is what products, sums, and exponents look like:

- without brackets

$$
\prod_{x=m}^n\ k^{f(x)}
~=~ k^{\sum_{x=m}^n f(x)}
$$

- with brackets

$$
\prod_{x=m}^n\ k^{f(x)}
~=~ k^\left[\sum_{x=m}^n f(x)\right]
$$

- or use the sigma symbol to save space:

$$
\prod_{x=m}^n\ k^{f(x)}
~=~ k^{\Sigma_{x=m}^n f(x)} \\
\prod_{x=m}^n\ k^{f(x)}
~=~ k^\left[\Sigma_{x=m}^n f(x)\right]
$$
