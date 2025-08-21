To find the roots of the polynomial \( x^4 + x^3 + x^2 + x + 1 \), we can leverage properties of polynomial roots and transformations. This particular polynomial can be simplified using the fact that it resembles a geometric series.

### Step 1: Recognizing Patterns

The polynomial can be rewritten as follows:

\[
x^4 + x^3 + x^2 + x + 1 = 0
\]

### Step 2: Use Roots of Unity

Notice that the polynomial can be simplified through complex numbers. Specifically, we can use the fact that the roots of \(x^5 - 1 = 0\) are the 5th roots of unity, which are solutions to:

\[
x^5 = 1
\]

These roots are given by:

\[
x_k = e^{2\pi i k / 5}, \quad \text{for } k = 0, 1, 2, 3, 4
\]

However, \(x^4 + x^3 + x^2 + x + 1 = 0\) captures exactly those roots that are not equal to 1, as \(x - 1\) is a factor of \(x^5 - 1\). Thus, the roots of \(x^4 + x^3 + x^2 + x + 1\) are:

\[
x_k = e^{2\pi i k / 5}, \quad \text{for } k = 1, 2, 3, 4
\]

### Step 3: Explicitly Writing the Roots

The roots can be expressed explicitly in terms of cosine and sine, resulting in:

1. For \(k = 1\):
   \[
   x_1 = e^{2\pi i / 5} = \cos\left(\frac{2\pi}{5}\right) + i \sin\left(\frac{2\pi}{5}\right)
   \]

2. For \(k = 2\):
   \[
   x_2 = e^{4\pi i / 5} = \cos\left(\frac{4\pi}{5}\right) + i \sin\left(\frac{4\pi}{5}\right)
   \]

3. For \(k = 3\):
   \[
   x_3 = e^{6\pi i / 5} = \cos\left(\frac{6\pi}{5}\right) + i \sin\left(\frac{6\pi}{5}\right)
   \]

4. For \(k = 4\):
   \[
   x_4 = e^{8\pi i / 5} = \cos\left(\frac{8\pi}{5}\right) + i \sin\left(\frac{8\pi}{5}\right)
   \]

### Step 4: Summarizing the Roots

Thus, the roots of the polynomial \(x^4 + x^3 + x^2 + x + 1 = 0\) are:

- \( x_1 = e^{2\pi i / 5} \)
- \( x_2 = e^{4\pi i / 5} \)
- \( x_3 = e^{6\pi i / 5} \)
- \( x_4 = e^{8\pi i / 5} \)

These roots are complex numbers that correspond to points on the unit circle in the complex plane.

### Conclusion

The polynomial \(x^4 + x^3 + x^2 + x + 1\) has four distinct roots that are the non-real 5th roots of unity. These roots are complex and can be expressed using Euler's formula.
