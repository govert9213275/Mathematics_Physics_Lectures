---
title: Basic Electric Circuits and Electronics
author: Damian Chorążkiewicz
marp: true
theme: uncover
class: invert
math: mathjax
style: |
  section {
    font-size: 1.5em;
  }
  .columns {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
  }
  img.rotate-90 {
    transform: rotate(90deg);
  }
  img.rotate-180 {
    transform: rotate(180deg);
  }
  img.rotate-270 {
    transform: rotate(270deg);
  }
---

![bg brightness:.3](https://upload.wikimedia.org/wikipedia/commons/7/7e/RUS-IC.JPG)

<!--_color: #FF6-->
# <!--fit--> Basic Electric Circuits and Electronics



---
## AC Generator

<table align="center">
  <tr>
    <td>
      <iframe height="200" width="500" src="https://www.youtube.com/embed/WhATjUHgzxQ?si=TWzAtNnOzgZTY90q" title="AC Generator Video 1" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
    </td>
    <td>
      <iframe height="200" width="500" src="https://www.youtube.com/embed/quABfe4Ev3s?si=Ln06DDtC3pHMQo6B" title="AC Generator Video 2" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
    </td>
  </br>
  </br>
  <tr>
    <td>
      <iframe width="500" height="200" src="https://www.youtube.com/embed/jpDRfaWYk3I?si=5SuGGFGz4iZhG_eu" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
    </td>
    <td>
      <iframe width="500" height="200" src="https://www.youtube.com/embed/IdPTuwKEfmA?si=bBXqKSmGF0cL4zTz" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
    </td>
  </tr>
</table>


---

<div class="columns">
<div>

# Resistor

### Ohm's Law

$$
V = I \cdot R
$$

### Power

$$
P = UI =I^2 \cdot R = \frac{V^2}{R}
$$

</div>
<div>

<iframe width="560" height="315" src="https://www.youtube.com/embed/DYcLFHgVCn0?si=XTaB-PDrjLXT6nW-" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

</div>
</div>


---

### Series Connection

![bg invert 100% right:40%](https://upload.wikimedia.org/wikipedia/commons/1/11/Resistors_in_series.svg)

$$
\begin{aligned}
V &= V_1 + V_2 + \ldots \\
&= I \cdot R_1 + I \cdot R_2 + \ldots \\
&= I \cdot (R_1 + R_2 + \ldots) \\
\end{aligned}
$$

so 

$$
R_{\text{series}} = R_1 + R_2 + \ldots
$$

and 

$$
V = I\ R_{\text{series}}
$$

---
 
### Parallel Connection

![bg invert 100% right:40%](https://upload.wikimedia.org/wikipedia/commons/0/09/Resistors_in_parallel.svg)

$$
\begin{aligned}
I &= I_1 + I_2 + \ldots \\
&= \frac{V}{R_1} + \frac{V}{R_2} + \ldots \\
&= V \left(\frac{1}{R_1} + \frac{1}{R_2} + \ldots\right) \\
\end{aligned}
$$

so

$$
\frac{1}{R_{\text{parallel}}} = \frac{1}{R_1} + \frac{1}{R_2} + \ldots
$$

and

$$
R_{\text{parallel}} = \left(\frac{1}{R_1} + \frac{1}{R_2} + \ldots\right)^{-1}
$$

then

$$
V = I\ R_{\text{parallel}}
$$


---
### Parallel Connection examples

#### Two resistors in parallel

$$
\frac{1}{R_{\text{parallel}}} = \frac{1}{\color{red}R_1} + \frac{1}{\color{yellow}R_2} \leftrightarrow R_{\text{parallel}} = \frac{\color{red}R_1 \cdot \color{yellow}R_2}{\color{red}R_1 + \color{yellow}R_2}
$$

#### Three resistors in parallel

$$
\frac{1}{R_{\text{parallel}}} = \frac{1}{\color{red}R_1} + \frac{1}{\color{yellow}R_2} + \frac{1}{\color{green}R_3} \leftrightarrow R_{\text{parallel}} = \frac{\color{red}R_1 \cdot \color{yellow}R_2 \cdot \color{green}R_3}{\color{red}R_1 \cdot \color{yellow}R_2 + \color{red}R_1 \cdot \color{green}R_3 + \color{yellow}R_2 \cdot \color{green}R_3}
$$

#### Four resistors in parallel

$$
\frac{1}{R_{\text{parallel}}} = \frac{1}{\color{red}R_1} + \frac{1}{\color{yellow}R_2} + \frac{1}{\color{green}R_3} + \frac{1}{\color{orange}R_4} \leftrightarrow R_{\text{parallel}} = \frac{\color{red}R_1 \cdot \color{yellow}R_2 \cdot \color{green}R_3 \cdot \color{orange}R_4}{\color{red}R_1 \cdot \color{yellow}R_2 \cdot \color{green}R_3 + \color{red}R_1 \cdot \color{yellow}R_2 \cdot \color{orange}R_4 + \color{red}R_1 \cdot \color{green}R_3 \cdot \color{orange}R_4 + \color{yellow}R_2 \cdot \color{green}R_3 \cdot \color{orange}R_4}
$$


---

<div class="columns">
<div>

# Capacitor

### Capacitance

$$
C = \frac{Q}{V}
$$

### Energy

$$
U = \frac{1}{2} \cdot C \cdot V^2
$$


</div>
<div>

<iframe width="560" height="315" src="https://www.youtube.com/embed/X4EUwTwZ110?si=JesR9kOKnmRsKjDu" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

</div>
</div>


---
## Series Connection

![bg invert 100% right:40%](https://upload.wikimedia.org/wikipedia/commons/7/75/Capacitors_in_series.svg)

$$
\begin{aligned}
V &= V_1 + V_2 + \ldots \\
&= \frac{Q}{C_1} + \frac{Q}{C_2} + \ldots \\
&= Q \left(\frac{1}{C_1} + \frac{1}{C_2} + \ldots\right) \\
\end{aligned}
$$

so

$$
\frac{1}{C_{\text{series}}} = \frac{1}{C_1} + \frac{1}{C_2} + \ldots
$$


---
## Parallel Connection

![bg invert 100% right:40%](https://upload.wikimedia.org/wikipedia/commons/f/fa/Capacitors_in_parallel.svg)

$$
\begin{aligned}
Q &= Q_1 + Q_2 + \ldots \\
&= C_1 \cdot V + C_2 \cdot V + \ldots \\
&= V \left(C_1 + C_2 + \ldots\right) \\
\end{aligned}
$$

so

$$
C_{\text{parallel}} = C_1 + C_2 + \ldots
$$


---
## Comparison of series and parallel connection

**PLEASE NOTE THAT THE CAPACITORS IN SERIES AND PARALLEL CONNECTIONS ARE NOT THE SAME AS RESISTORS IN SERIES AND PARALLEL CONNECTIONS.**

**THE FORMULAS FOR CAPACITORS ARE INVERSE TO THE FORMULAS FOR RESISTORS!!!**


---

<div class="columns">
<div>


# Inductor

### Inductance & Back EMF

$$
L = \frac{\Phi}{I}, \quad\&\quad \mathcal{E} = -L \cdot \frac{dI}{dt}
$$

### Series and Parallel Connection

$$
\frac{1}{L_{\text{parallel}}} = \frac{1}{L_1} + \frac{1}{L_2} + \ldots
$$

$$
L_{\text{series}} = L_1 + L_2 + \ldots
$$
</div>
<div>


<iframe width="560" height="315" src="https://www.youtube.com/embed/KSylo01n5FY?si=bpDonrcCwaa7zor5" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

</div>
</div>

---
# Kirchhoff's Laws

![bg 90% invert right](https://upload.wikimedia.org/wikipedia/commons/7/77/Kirshhoff-example.svg)

$$
\begin{aligned}
 {\color{yellow}I_1} -{\color{green}I_2} - {\color{red}I_3}&= 0\\&\\
{\color{orange}\mathcal{E}_1} -{\color{yellow}R_1 I_1} - {\color{green}R_2 I_2} &=0\\&\\
-{\color{orange}\mathcal{E}_1}+{\color{green}R_2 I_2} - {\color{red}R_3 I_3}  -{\color{pink}\mathcal{E}_2} &= 0
\end{aligned}
$$





---

<div class="columns">
<div>

# Diode

Diod is a semiconductor device that allows current to flow in one direction only.

</div>
<div>

<iframe width="560" height="315" src="https://www.youtube.com/embed/Fwj_d3uO5g8?si=VvDn7zN6Dzd3fvNa" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

</div>
</div>

---

<div class="columns">
<div>

# LED

Led is a semiconductor device that emits light when current flows through it.

</div>
<div>

<iframe width="560" height="315" src="https://www.youtube.com/embed/O8M2z2hIbag?si=yU14gy5eAlvUKY-V" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

</div>
</div>

---
# Transistor

<div class="columns">
<div>
A transistor is a semiconductor device used to amplify or switch electrical signals and power.

</div>
<div>

<iframe width="560" height="315" src="https://www.youtube.com/embed/J4oO7PT_nzQ?si=PsBSwl4zeH6TrG7Z" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

</div>
</div>

---

# MOSFET

<div class="columns">
<div>
A transistor is a semiconductor device used to amplify or switch electrical signals and power.

</div>
<div>

<iframe width="560" height="315" src="https://www.youtube.com/embed/AwRJsze_9m4?si=uCxWx5h2PVTbjd3U" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

</div>
</div>


---
<div class="columns">
<div>

## Solar panels

</div>
<div>

<iframe width="560" height="315" src="https://www.youtube.com/embed/Yxt72aDjFgY?si=gzKjYuodZCSd3khb" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

</div>
</div>

---
## RC Circuit

RC circuit is a circuit with a resistor and a capacitor connected in series.
By Kirchhoff's voltage law, the voltage across the resistor and the capacitor must be equal to the voltage source.

$$
\mathcal{E} = V_R + V_C
$$

which can be written as

$$
\mathcal{E} = IR + \frac{Q}{C}
$$

where $Q$ is the charge on the capacitor.

this equation can be rewritten as

$$
\frac{dQ}{dt} = I = C \frac{dV_C}{dt}
$$

the solution to this differential equation is

$$
V_C(t) = \mathcal{E} \left(1 - e^{-\frac{t}{RC}}\right)
$$

---
## RL Circuit

RL circuit is a circuit with a resistor and an inductor connected in series.

By Kirchhoff's voltage law, the voltage across the resistor and the inductor must be equal to the voltage source.

$$
\mathcal{E} = IR + L \frac{dI}{dt}
$$

which can be written as

$$
\frac{dI}{dt} = \frac{\mathcal{E}}{L} - \frac{R}{L}I
$$

the solution to this differential equation is

$$
I(t) = \frac{\mathcal{E}}{R} \left(1 - e^{-\frac{Rt}{L}}\right)
$$



---
## LC Circuit

LC circuit is a circuit with a capacitor and an inductor connected in series.

By Kirchhoff's voltage law, the voltage across the capacitor and the inductor must be equal to the voltage source.

$$
0 = \frac{Q}{C} + L \frac{dI}{dt}
$$

which can be written as

$$
\frac{d^2Q}{dt^2} = -\frac{Q}{LC}
$$

the solution to this differential equation is

$$
Q(t) = Q_0 \cos\left(\sqrt{\frac{1}{LC}}t\right)
$$



---
# RLC Circuit General Solution

The general solution to the RLC circuit is the sum of the solutions to the RC, RL, and LC circuits. Differential equations for the RLC circuit for Q looks like

$$
\frac{d^2Q}{dt^2} + \frac{R}{L} \frac{dQ}{dt} + \frac{1}{LC}Q = \mathcal{E} cos(\omega t)
$$

Characteristic equation for this differential equation is

$$
\lambda^2 + \frac{R}{L} \lambda + \frac{1}{LC} = 0
$$

so we have three cases for the solution of this equation:

1. Overdamped: $\frac{R^2}{4L^2} > \frac{1}{LC}$
2. Critically damped: $\frac{R^2}{4L^2} = \frac{1}{LC}$
3. Underdamped: $\frac{R^2}{4L^2} < \frac{1}{LC}$

---
## Overdamped RLC Circuit

For the overdamped case, the general solution is

$$
Q(t) = A_1 e^{r_1 t} + A_2 e^{r_2 t}
$$

where $r_1$ and $r_2$ are the roots of the characteristic equation.

$$
r_{1,2} = -\frac{R}{2L} \pm \sqrt{\left(\frac{R}{2L}\right)^2 - \frac{1}{LC}}
$$


---
## Critically Damped RLC Circuit

For the critically damped case, the general solution is

$$
Q(t) = (A_1 + A_2 t) e^{-\frac{R}{2L}t}
$$


---
## Underdamped RLC Circuit

For the underdamped case, the general solution is

$$
Q(t) = e^{-\frac{R}{2L}t} \left(A_1 \cos(\omega_1 t) + A_2 \sin(\omega_1 t)\right)
$$

where $\omega_1 = \sqrt{\frac{1}{LC} - \left(\frac{R}{2L}\right)^2}$

---