
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON_SCRIPT="$SCRIPT_DIR/src/main.py"

echo 'test1'
python3 "$PYTHON_SCRIPT" '
\hat{u}_m &= \frac{1}{4}\sum_{j=0}^{3}u_j\omega_m^{-j}\\
    &= \frac{1}{4}\sum_{j=0}^{3}(i^m)^{-j}
'
echo 'test2'
python3 "$PYTHON_SCRIPT" '
 f_{\lfloor zy\rfloor}(t=k) = \mathrm{min} \left\{ x\in \mathbb{N} \mid \sum_{\substack{u_i\geq 0; \\ u_0+u_1+u_2+u_3=k; \\ u_1+2u_2+3u_3\geq x}}\frac{k!}{u_0!u_1!u_2!u_3!} \geq (1-z)\cdot 4^k \right\}\\
'
echo 'test3'
python3 "$PYTHON_SCRIPT" '
\mathrm{E}[f(t=k)]&= \mathrm{E}\left[U_1+2U_2+3U_3\right]\\
    &= \mathrm{E}\left[U_1\right]+2\mathrm{E}\left[2U_2\right] +3\mathrm{E}\left[U_3\right] \\
    &= 0.25\cdot k+0.25\cdot 2k+0.25\cdot 3k \\
    &= 1.5 k
'
echo 'test4'
python3 "$PYTHON_SCRIPT" '
 \mathrm{P}(U_0=u_0,U_1=u_1,U_2=u_2,U_3=u_3) &= \frac{k!}{u_0!u_1!u_2!u_3!}\cdot p_0^{u0}p_1^{u1}p_2^{u2}p_3^{u3}\\
    &= \frac{k!}{u_0!u_1!u_2!u_3!} \cdot (0.25)^{u_0+u_1+u_2+u_3}\\
    &= \frac{k!}{u_0!u_1!u_2!u_3!}\cdot0.25^k
'
echo 'test5'
python3 "$PYTHON_SCRIPT" '
f_{\left\lfloor zy \right\rfloor}(t=k)&=\mathrm{min} \left\{ x\in \mathbb{N} \, \middle| \, \, \sum_{j=0}^{x}\binom{k}{j} \geq (1-z) \cdot  2^k \right\}
'
echo 'test6'
python3 "$PYTHON_SCRIPT" '
\[
\mathcal{Z}(\alpha,\beta) \;=\; 
\sum_{n=1}^{\infty} \;
\prod_{m=1}^{n}
\left[
\int_{0}^{\infty} 
e^{-\alpha x_m^2}\,
x_m^{\frac{m}{2}}\,
J_{\nu}\!\big(\beta x_m\big)\,
dx_m
\right]
\cdot
\det\!\Bigg(
\delta_{ij} +
\frac{\Gamma(i+j+\tfrac{1}{2})}{\zeta(i+j+2)}
\Bigg)_{i,j=1}^{n}
\;\;+\;
\int_{\mathbb{R}^d}
\exp\!\Bigg(
- \tfrac{1}{2} \sum_{i,j=1}^d
A_{ij} x_i x_j
+ i \sum_{k=1}^d b_k x_k
\Bigg) d^dx
\]
'
echo 'test7'
python3 "$PYTHON_SCRIPT" '
\[
\mathscr{M}(\alpha,\beta,\gamma,\delta) \;=\;
\sqrt{
    \frac{
        \displaystyle
        \sum_{n=1}^{\infty}
        \left(
            \prod_{m=1}^{n}
            \frac{
                \Bigg(
                    \int_{0}^{\infty}
                    \sqrt[
                        4
                    ]{
                        \frac{e^{-\alpha x^2}}
                        {1 +
                            \dfrac{
                                \sin^2(\beta x)
                            }{
                                \sqrt{m^2+n^2+1}
                            }
                        }
                    }
                    \; {}_{2}F_{1}\!\left(\tfrac{1}{2}, \tfrac{m}{n};\; m+n;\; e^{-x^2}\right)
                    dx
                \Bigg)^{\!\!\!m}
            }
            {
                \Big(
                1+\dfrac{1}{\sqrt{1+\dfrac{1}{\sqrt{1+\cdots+\tfrac{1}{m+n}}}}}
                \Big)^n
            }
        \right)
    }
    {
        \displaystyle
        \prod_{k=1}^{\infty}
        \left(
            1 +
            \frac{
                \exp\!\Big(
                    -\sqrt{\tfrac{\pi}{k}}\,e^{-\gamma/k}
                \Big)
            }
            {
                k^{\,
                    \sqrt{
                        1+\frac{\gamma}{k}+
                        \sqrt{1+\frac{\delta}{k}}
                    }
                }
            }
        \right)
    }
}
\]

\[
\qquad + \exp\!\Bigg(
    -\frac{
        \displaystyle
        \int_{\mathbb{R}}
        \bigg(
            \frac{
                \sin\!\big(\sqrt{1+i t^2}\,\big)
            }
            {
                1+\sum_{j=1}^{\infty}
                \dfrac{(-1)^j}{j!\,\,(t^2+j^2)}
            }
        \bigg)^{\!\!2}
        dt
    }
    {
        \sqrt{
            1+\tfrac{1}{1+\tfrac{1}{1+\tfrac{1}{1+\cdots}}}
        }
    }
\Bigg)
\]
'
