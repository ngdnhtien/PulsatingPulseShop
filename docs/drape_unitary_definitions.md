# DRAPE closed-form definitions

*`defs.txt` of the qutrit-error project (late 2025): the matrices used in `misc/original_notebooks/qutrit_error_2026/simulation.ipynb` to write the DRAPE sequence $(U_-U_+)^{2n+1}$ in closed form. The file was written as a prompt to a computer-algebra assistant; kept verbatim.*

I want you to do some matrix multiplication for me. First, let me give you the definitions

1. Let $A$ and $B$ be
\begin{align}
A = \cos(\epsilon/2)-\sin(\epsilon/2),\\
B = \cos(\epsilon/2)+\sin(\epsilon/2).\end{align}

2. Let the $U_+$ and $U_-$ unitaries be
\begin{align}
U_+(\epsilon,\delta) = 1/\sqrt{2}\begin{pmatrix}
A & -iBe^{i\delta} \\
-iBe^{i\delta} & Ae^{i2\delta}
\end{pmatrix},\\
U_-(\epsilon,\delta) = 1/\sqrt{2}\begin{pmatrix}
A & +iBe^{i\delta} \\
+iBe^{i\delta} & Ae^{i2\delta}
\end{pmatrix}
\end{align}

3. The product of $U_{-}U_{+}$ is, noting that $AB=\cos\epsilon$ and $A^2+B^2=2$,
\begin{align}
U_{-}U_{+} = \frac{1}{2}\begin{pmatrix}
A^2+B^2 e^{i2\delta} & i \cos\epsilon e^{i\delta} (e^{i2\delta} -1) \\ i\cos\epsilon e^{i\delta}(1-e^{i2\delta}) & B^2e^{i2\delta}+A^2e^{i4\delta} \end{pmatrix}.
\end{align}

4. This product, $U_{-}U_{+}$ when exponentiated to $2n+1$,
\begin{align}
(U_{-}U_{+})^{2n+1} = e^{ik2\delta}
\begin{pmatrix}
\frac{S_k}{2}[(1-\sin\epsilon)e^{-i2\delta}+(1+\sin\epsilon)]-S_{k-1} & -S_k\cos\epsilon\sin\delta \\
S_k\cos\epsilon\sin\delta & \frac{S_{k}}{2}[(1+\sin\epsilon)+(1-\sin\epsilon)e^{i2\delta}]-S_{k-1}
\end{pmatrix},\\
k = 2n+1,\\
S_{k}=\frac{\sin(k\theta)}{\sin\theta},\\
S_{k-1}=\frac{\sin((k-1)\theta)}{\sin\theta},\\
\cos\theta = \frac{1}{2}[(1+\sin\epsilon)+(1-\sin\epsilon)\cos 2\delta]
\end{align}

5. There's a unitary called Y'_{\pi/2}. It is defined by 
\begin{align}
Y'_{\pi/2}= 1/\sqrt{2} \begin{pmatrix}
A & -B e^{i\delta} \\ +B e^{i\delta} & A e^{i 2\delta}
\end{pmatrix}
\end{align}

5. We start with the initial state $|\psi_0\rangle$
\begin{align}
|\psi_0\rangle &= U_{+}(-i|0\rangle),\\
&=\frac{1}{\sqrt{2}}\begin{pmatrix}
-i A \\ -Be^{i\delta}
\end{pmatrix}
\end{align}

Load these definitions into your memory and say "Ready" when you are ready to compute