---
title: Electromagnetism
author: Damian Chorążkiewicz
marp: true
theme: uncover
class: invert
math: mathjax
style: |
  section {
    font-size: 2em;  
  }
  .columns {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
  }
---

![bg brightness:.5](https://upload.wikimedia.org/wikipedia/commons/4/46/Plasma_globe_60th.jpg)

<!--_color: #FF6-->
# <!--fit--> :zap: Electromagnetism :zap:

by Damian Chorążkiewicz 

---
<!--_color: #FF6-->

# <!--fit-->  Electrostatics



---
## Couluomb's Law

<div class="columns">
<div>

## Math

$$
F = k \frac{q_1 q_2}{r^2}
$$

</div>
<div>

## Python

```python
def coulomb_force(q1, q2, r):
    k = 8.9875e9
    return k * q1 * q2 / r**2
```

</div>
</div>

![bg right:30%](https://upload.wikimedia.org/wikipedia/commons/4/42/Coulomb.jpg)

---

## Composite Forces

If we have more than one charge, we can calculate the total force acting on a charge $q$ by summing the forces from each charge.

$$
\vec{F} = \sum_i \vec{F}_i= \sum_i k \frac{{\bf\color{yellow}q}\ q_i}{r_i^2} \hat{r_i} = {\bf\color{yellow}q} \left( \sum_i k \frac{q_i}{r_i^2} \hat{r_i} \right)
$$


---

## Electric Field

$$
\vec{E}=\sum_i k \frac{q_i}{r_i^2} \hat{r_i}
$$

![vertical 50% invert:86% bg right:60%](https://upload.wikimedia.org/wikipedia/commons/e/ed/VFPt_charges_plus_minus_thumb.svg)
![50% invert:86% bg right:60%](https://upload.wikimedia.org/wikipedia/commons/e/eb/VFPt_capacitor-square-plate.svg)

---
#### Python implementation

```python
import numpy as np

def electric_field(pos: list[float], charges: list[list[float]]) -> np.ndarray:
    """
    Calculate the electric field at a given position due to a list of point charges.

    Args:
    pos (list[float]): The [x, y, z] position at which to calculate the electric field.
    charges (list[list[float]]): A list of charges, where each charge is defined as
                                 [x, y, z, q] for position (x, y, z) and charge q.

    Returns:
    np.ndarray: The resulting electric field vector [Ex, Ey, Ez] in Newtons per Coulomb.

    Note:
    - The position coordinates and charge should be in meters and Coulombs, respectively.
    - The function uses the Coulomb constant k = 8.9875e9 N m²/C².
    """
    k = 8.9875e9  # Coulomb's constant in N m²/C²
    E = np.zeros(3)  # Electric field vector initialized to zero
    for q in charges:
        r_vec = np.array(pos) - np.array(q[:3])
        r = np.linalg.norm(r_vec)
        E += (k * q[3] / r**3) * r_vec 

    return E

```

---
## Definition of flux

For any vector field $\vec{F}$, the flux $\Phi$ through a surface $S$ is defined as:

$$
\Phi = \int_S \vec{F} \cdot d\vec{A} \sim \sum \vec{F}_i \cdot \vec{A}_i
$$


![bg 100% right:40%](https://upload.wikimedia.org/wikipedia/commons/b/bd/Surface_integral_-_definition.svg)


---
## Gauss's Law

$$
\oint_S \vec{E} \cdot d\vec{A} = \frac{Q_{\text{enc}}}{\varepsilon_0}
$$


![vertical 60% invert:86% bg right:50%](https://upload.wikimedia.org/wikipedia/commons/3/32/Electric-flux-surface-example.svg)
![60% invert:86% bg right:50%](https://upload.wikimedia.org/wikipedia/commons/c/c8/Electric-flux-no-charge-inside.svg)


---
## Electic potential

The electric potential $V$ at a point in space is defined as the work done per unit charge in bringing a positive test charge from infinity to that point.

$$
V = -\int_{\infty}^{r} \vec{E} \cdot d\vec{r}
$$

so

$$
\vec{E} = -\nabla V
$$

In the case of point charge we have

$$
V = \frac{kq}{r}
$$

![bg 100% right:40%](https://upload.wikimedia.org/wikipedia/commons/6/68/VFPt_metal_balls_largesmall_potential%2Bcontour.svg)

---
##### Python implementation

```python
import numpy as np

def electric_potential(pos: list[float], charges: list[list[float]]) -> float:
    """
    Calculate the electric potential at a given position due to a list of point charges.

    Args:
    pos (list[float]): The [x, y, z] position at which to calculate the electric potential.
    charges (list[list[float]]): A list of charges, where each charge is defined as
                                 [x, y, z, q] for position (x, y, z) and charge q.

    Returns:
    float: The resulting electric potential in volts.

    Note:
    - The position coordinates and charge should be in meters and Coulombs, respectively.
    - The function uses the Coulomb constant k = 8.9875e9 N m²/C².
    """
    k = 8.9875e9  # Coulomb's constant in N m²/C²
    V = 0  # Electric potential initialized to zero
    for q in charges:
        r_vec = np.array(pos) - np.array(q[:3])
        r = np.linalg.norm(r_vec)
        V += k * q[3] / r

    return V

```

---
## Force acting on </br>electric dipole

$$
\vec{\tau} = \vec{p}\times\vec{E}
$$

where $\vec{p}$ is the electric dipole moment

$$
\vec{p} = q \vec{d}
$$

where $d$ is the distance between the charges.

Enegry of the dipole in an electric field

$$
U = -\vec{p}\cdot\vec{E}
$$

![bg invert 100% right:40%](https://upload.wikimedia.org/wikipedia/commons/b/b6/Electric_dipole_torque_uniform_field.svg)


---
## Capacitors


![bg 100% right:40%](https://upload.wikimedia.org/wikipedia/commons/6/68/VFPt_metal_balls_largesmall_potential%2Bcontour.svg)

$$
C = \frac{Q}{V}
$$


where $Q$ is the charge stored on the capacitor and $V$ is the potential difference between the conductors.

</br>

#### Energy stored in a capacitor

$$
U = \frac{1}{2} C V^2 = \frac{1}{2} \frac{Q^2}{C}
$$

---
### Examples

<div class="columns">
<div>

- Parallel plate capacitor
</br>
$$
C = \varepsilon_0 \frac{A}{d}
$$
</br>

- Spherical capacitor
</br>

$$
C = 4\pi \varepsilon_0 \frac{r_1 r_2}{r_2 - r_1}
$$

</br>
</div>
<div>

- Cylindrical capacitor

</br>

$$
C = 2\pi \varepsilon_0 \frac{L}{\ln(r_2/r_1)}
$$
</br>

- other
</br>

[www->Capacitance](https://en.wikipedia.org/wiki/Capacitance)

</div>
</div>

---
## Dielectrics

Dielectrics are insulating materials that can be polarized by an electric field. The presence of dielectrics in a capacitor increases its capacitance.

$$
C = \kappa \varepsilon_0 \frac{A}{d}
$$

where $\kappa$ is the relative permittivity of the dielectric material.

![bg invert 100% right:40%](https://upload.wikimedia.org/wikipedia/commons/c/cd/Capacitor_schematic_with_dielectric.svg)


---
## Connecting capacitors

<div class="columns">
<div>

### Series

$$
\frac{1}{C_{\text{eq}}} = \frac{1}{C_1} + \frac{1}{C_2} + \ldots
$$

![invert ](https://upload.wikimedia.org/wikipedia/commons/7/75/Capacitors_in_series.svg)

for two capacitors

$$
C_{\text{eq}} = \frac{C_1 C_2}{C_1 + C_2}
$$


</div>
<div>

### Parallel

$$
C_{\text{eq}} = C_1 + C_2 + \ldots
$$

![invert ](https://upload.wikimedia.org/wikipedia/commons/f/fa/Capacitors_in_parallel.svg)

</div>


---
<!--_color: #FF6-->
# <!--fit--> Electric current

---

![bg](https://upload.wikimedia.org/wikipedia/commons/1/13/Lightning_over_Oradea_Romania_3.jpg)
![bg ](https://upload.wikimedia.org/wikipedia/commons/c/c0/Cage_de_Faraday.jpg)
![bg ](https://upload.wikimedia.org/wikipedia/commons/2/20/London_MMB_%C2%BB1E6_Lightning.jpg)


---
## Electric current

$$
I = \frac{dQ}{dt}
$$

where $I$ is the current, $Q$ is the charge, and $t$ is the time.
</br>

![alt text](https://upload.wikimedia.org/wikipedia/commons/0/0c/Direzione_convenzionale_della_corrente_elettrica.svg)

---
## Ohm's Law

$$
V = I R
$$

</br>

where $V$ is the voltage, $I$ is the current, and $R$ is the resistance.

![bg right:33%](https://upload.wikimedia.org/wikipedia/commons/a/a6/Georg-simon-ohm_1.jpg)

--- 
## Electromotive force

$$
\mathcal{E} = I R + V
$$

where $\mathcal{E}$ is the electromotive force, $I$ is the current, and $R$ is the resistance.

![bg 96% invert:90% right:50%](https://upload.wikimedia.org/wikipedia/commons/6/6d/Galvanic_cell_with_no_cation_flow.svg)

---
## Kirchhoff's Laws

![bg 90% vertical invert right:33%](https://upload.wikimedia.org/wikipedia/commons/4/46/KCL_-_Kirchhoff%27s_circuit_laws.svg)
![bg 90% invert right:33%](https://upload.wikimedia.org/wikipedia/commons/4/40/Kirchhoff_voltage_law.svg)

1) Kirchhoff's current law (KCL) states that the sum of currents entering a node is equal to the sum of currents leaving the node.

$$
\sum I_{\text{in}} = \sum I_{\text{out}}
$$

2) Kirchhoff's voltage law (KVL) states that the sum of voltages around any closed loop in a circuit is zero.

$$
\sum V_{\text{loop}} = 0
$$

---
![bg invert 90% right:50%](https://upload.wikimedia.org/wikipedia/commons/7/77/Kirshhoff-example.svg)

$$
\begin{aligned}
i_1-i_2-i_3 &= 0 \\
\mathcal{E}_1 - i_1 R_1 - i_2 R_2 &= 0 \\
-\mathcal{E}_1-\mathcal{E}_2{\color{red}{+i_2R_2}}-i_3R_3 &= 0
\end{aligned}
$$


---
## Resistors

<dev class="columns">
<div>

### Series

$$
R_{\text{eq}} = R_1 + R_2 + \ldots
$$

![invert](https://upload.wikimedia.org/wikipedia/commons/1/11/Resistors_in_series.svg)

</div>
<div>

### Parallel

$$
\frac{1}{R_{\text{eq}}} = \frac{1}{R_1} + \frac{1}{R_2} + \ldots
$$

![invert](https://upload.wikimedia.org/wikipedia/commons/0/09/Resistors_in_parallel.svg)

for two resistors

$$
R_{\text{eq}} = \frac{R_1 R_2}{R_1 + R_2}
$$

---
<!--_color: #FF6-->
# <!--fit--> Magnetostatics

---
![bg 70%](https://upload.wikimedia.org/wikipedia/commons/a/a2/Magnetic_field_of_horseshoe_magnet.png)
![bg 95%](https://upload.wikimedia.org/wikipedia/commons/5/57/Magnet0873.png)
![bg 90%](https://upload.wikimedia.org/wikipedia/commons/4/42/Magnetic_field_around_solenoid.jpg)


 
---
## Gauss's law for magnetism


$$
\oint_S \vec{B} \cdot d\vec{A} = 0
$$

where $\vec{B}$ is the magnetic field and $d\vec{A}$ is the area vector.

![bg right:33%](https://upload.wikimedia.org/wikipedia/commons/9/9b/Carl_Friedrich_Gauss.jpg)

---
## Biot-Savart Law
</br>

$$
d\vec{B} = \frac{\mu_0}{4\pi} \frac{I d\vec{l} \times \hat{r}}{r^2}
$$
</br>
</br>

![width:150px](https://upload.wikimedia.org/wikipedia/commons/8/8d/Jean_baptiste_biot.jpg) ![width:150px](https://upload.wikimedia.org/wikipedia/commons/d/d4/Interior_of_Institut_de_France%2C_Paris_6th_013.jpg)

![bg 90% invert right:39%](https://upload.wikimedia.org/wikipedia/commons/4/4f/Biot_Savart.svg)



---
### Examples

<div class="columns">
<div>

- Infinite wire
</br>

$$
B = \frac{\mu_0 I}{2\pi r}
$$

- Circular loop
</br>

$$
B = \frac{\mu_0 I R^2}{2(R^2 + x^2)^{3/2}}
$$

- Solenoid
</br>

$$
B = \mu_0 n I
$$

</div>
<div>



<iframe width="560" height="315" src="https://www.youtube.com/embed/V-M07N4a6-Y?si=gpd26DMXHD-eeOi9&amp;start=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

</div>

---
## Lorentz Force

$$
\vec{F} = q(\vec{E} + \vec{v} \times \vec{B})
$$

- $\vec{F}$ is the force
- $q$ is the charge
- $\vec{E}$ is the electric field 
- $\vec{v}$ is the velocity
- $\vec{B}$ is the magnetic field.

![bg 90% right:50%](https://upload.wikimedia.org/wikipedia/commons/a/a9/Cyclotron_motion.jpg)


---
## Force on a current-carrying wire

$$
\vec{F} = I \vec{l} \times \vec{B}
$$

where $I$ is the current, $\vec{l}$ is the length of the wire, and $\vec{B}$ is the magnetic field.

![bg 90% right:50%](https://upload.wikimedia.org/wikipedia/commons/6/6a/Regla_mano_derecha_Laplace.svg)

---
## Ampère's force law

$$
F = \frac{\mu_0 I_1 I_2 l}{2\pi r}
$$

where $I_1$ and $I_2$ are the currents, $l$ is the length of the wires, and $r$ is the distance between the wires.

![bg invert:80% 90% right:50%](https://upload.wikimedia.org/wikipedia/commons/b/bc/MagneticWireAttraction.svg)

---
## Magmetic dipole moment

$$
\vec{m} = I \vec{A}
$$

where $I$ is the current and $\vec{A}$ is the area vector.

![bg invert 90% right:33%](https://upload.wikimedia.org/wikipedia/commons/4/4c/Magnetic_moment.svg)

---
## Torque on a </br>magnetic dipole

$$
\vec{\tau} = \vec{m} \times \vec{B}
$$

where $\vec{m}$ is the magnetic dipole moment and $\vec{B}$ is the magnetic field.

#### Energy 

$$  
U = -\vec{m} \cdot \vec{B}
$$

![bg invert:90% 90% right:60%](https://upload.wikimedia.org/wikipedia/commons/f/f8/Torque-current-loop.svg)



---
## Electric motor

An electric motor is a device that converts electrical energy into mechanical energy.

<div style="text-align:center;">
  <iframe width="560" height="315" src="https://www.youtube.com/embed/CWulQ1ZSE3c?si=AJy7UHRvorf5xGdI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/hZxD1hwntqY?si=d_3yL9C8pcGolB0r" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>



---
<!--_color: #FF6-->
# <!--fit--> Electromagnetic Induction

---

<div class="columns">
<div>
<iframe width="560" height="315" src="https://www.youtube.com/embed/txmKr69jGBk?si=0WP3oQclEQKVgTfT&amp;start=63" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/sENgdSF8ppA?si=fKQh9iwT3D0f7dI9&amp;start=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>
<div>
<iframe width="560" height="315" src="https://www.youtube.com/embed/hajIIGHPeuU?si=a33RMR950b27uJzv&amp;start=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/npls3sQP7xk?si=nCyy7wt8vuW0ApDd&amp;start=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

</div>
</div>

---
## Lentz's Law

The direction of the induced current is such that it opposes the change in magnetic flux that produced it.

![height:500px invert ](https://upload.wikimedia.org/wikipedia/commons/e/e4/Lenz_law_demonstration.png)



---
## Faraday's Law

$$
\mathcal{E} = -\frac{d\Phi}{dt}
$$

where $\mathcal{E}$ is the electromotive force and $\Phi$ is the magnetic flux.

</br>

![width:300px](https://upload.wikimedia.org/wikipedia/commons/7/72/Electromagnetic_induction_-_solenoid_to_loop_-_animation.gif)

![bg right:33%](https://upload.wikimedia.org/wikipedia/commons/7/7e/Michael_Faraday_sitting_crop.jpg)


---
## Inductance


$$
d\vec{B}_1 = \frac{\mu_0}{4\pi} \frac{I_1 d\vec{l}_1 \times \hat{r}}{r^2}
$$

......

$$
\Phi_2 = \int_S \vec{B}_1 \cdot d\vec{A}_2
$$

......

$$
\Phi_2 = M_{21} I_1
$$

......

$$
\mathcal{E}_2 = -\frac{d\Phi_2}{dt} = -M_{21} \frac{dI_1}{dt}
$$

![bg 90% invert:90% right:50%](https://peppyhare.github.io/r/img/griffiths/7.30.png)


---
## Self-inductance

Self-inductance is the property of a coil that causes an electromotive force to be induced in the coil itself when the current through the coil changes.

$$
\mathcal{E} = -L \frac{dI}{dt}
$$

where $L$ is the self-inductance of the coil.

![bg invert 80% right:33%](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Copper_coil_with_six_turns.png/640px-Copper_coil_with_six_turns.png)


---
## RL circuit

</br>

$$
\mathcal{E} - L \frac{dI}{dt} - IR=0
$$

</br>

where $L$ is the self-inductance of the coil, 

$I$ is the current, and $R$ is the resistance.

</br>

$$
I(t) = \frac{\mathcal{E}}{R} \left(1 - e^{-\frac{R}{L}t}\right)
$$


---
## Transformer

$$
\frac{V_p}{V_s} = \frac{I_s}{I_p} = \frac{N_s}{N_p}
$$

where $V_1$ and $V_2$ are the voltages and $N_1$ and $N_2$ are the number of turns in the primary and secondary coils, respectively ([www](https://en.wikipedia.org/wiki/Transformer)).

![bg invert 99% right:50%](https://upload.wikimedia.org/wikipedia/commons/6/64/Transformer3d_col3.svg)



---
### Maxwell's Equations
![bg right:33%](https://upload.wikimedia.org/wikipedia/en/4/42/Db_James_Clerk_Maxwell_in_his_40s_-2-7.jpg)

$$
\begin{aligned}
\nabla \cdot \mathbf{E} &= \frac{\rho}{\varepsilon_0}  \quad (\text{Gauss's Law}) \\
\nabla \cdot \mathbf{B} &= 0  \quad (\text{without name}) \\
\nabla \times \mathbf{E} &= -\frac{\partial \mathbf{B}}{\partial t}  \quad (\text{Faraday's Law}) \\
\nabla \times \mathbf{B} &= \mu_0 \mathbf{J} + \mu_0 \varepsilon_0 \frac{\partial \mathbf{E}}{\partial t}  \quad (\text{Ampère-Maxwell Law})
\end{aligned}
$$

---

## Maxwell's Equations: Differential and Integral Forms



$$
\begin{align}
\nabla \cdot \mathbf{E} = \frac{\rho}{\varepsilon_0} 
&\quad\longleftrightarrow\quad
\oint_S \mathbf{E} \cdot d\mathbf{A} = \frac{1}{\varepsilon_0} \int_V \rho \, dV \\
\nabla \cdot \mathbf{B} = 0
&\quad\longleftrightarrow\quad
\oint_S \mathbf{B} \cdot d\mathbf{A} = 0 \\
\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}
&\quad\longleftrightarrow\quad
\oint_C \mathbf{E} \cdot d\mathbf{l} = -\frac{d}{dt} \int_S \mathbf{B} \cdot d\mathbf{A} \\
\nabla \times \mathbf{B} = \mu_0 \mathbf{J} + \mu_0 \varepsilon_0 \frac{\partial \mathbf{E}}{\partial t}
&\quad\longleftrightarrow\quad
\oint_C \mathbf{B} \cdot d\mathbf{l} = \mu_0 \int_S \mathbf{J} \cdot d\mathbf{A} + \mu_0 \varepsilon_0 \frac{d}{dt} \int_S \mathbf{E} \cdot d\mathbf{A}
\end{align}
$$


---
## Vector calculus

[Vector calculus identities](https://en.wikipedia.org/wiki/Vector_calculus_identities)
[Divergence theorem](https://en.wikipedia.org/wiki/Divergence_theorem)
[Stokes' theorem](https://en.wikipedia.org/wiki/Stokes%27_theorem)


![bg vertical invert right:33%](https://upload.wikimedia.org/wikipedia/commons/f/f5/Vector_Field_on_a_Sphere.png)


</br>
</br>

$$
\iiint_V \nabla \cdot \mathbf{F} \, dV = \iint_S \mathbf{F} \cdot d\mathbf{A}
$$

</br>
</br>

$$
\oint_C \mathbf{F} \cdot d\mathbf{l} = \iint_S (\nabla \times \mathbf{F}) \cdot d\mathbf{A}
$$

![bg invert](https://upload.wikimedia.org/wikipedia/commons/4/4c/Stokes%27_Theorem.svg)


---
<!--_color: #FF6-->
# <!--fit--> Electromagnetic Waves

---
## Electromagnetic waves

If we combine Maxwell's equations, we get the wave equation for electromagnetic waves.

$$
\nabla^2 \mathbf{E} = \mu_0 \varepsilon_0 \frac{\partial^2 \mathbf{E}}{\partial t^2}
$$

$$
\nabla^2 \mathbf{B} = \mu_0 \varepsilon_0 \frac{\partial^2 \mathbf{B}}{\partial t^2}
$$

![bg invert 90% right:50%](https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/EM-Wave.gif/640px-EM-Wave.gif)



---

<div class="columns">
<div>

### [Interference](https://en.wikipedia.org/wiki/Interference_(wave_propagation))
<img src="https://upload.wikimedia.org/wikipedia/commons/2/2c/Two_sources_interference.gif" width="200" height="200" alt="Interference of two waves">


### [Diffraction](https://en.wikipedia.org/wiki/Diffraction)
<img src="https://upload.wikimedia.org/wikipedia/commons/4/42/Laser_Interference.JPG" width="200" height="200" alt="Laser Interference">




</div>
<div>

### [Reflection](https://en.wikipedia.org/wiki/Reflection_(physics))
<img src="https://upload.wikimedia.org/wikipedia/commons/e/e3/F%C3%A9nyvisszaver%C5%91d%C3%A9s.jpg" width="250" height="200" alt="Reflection angles">


### [Dispersion](https://en.wikipedia.org/wiki/Dispersion_(optics))
<img src="https://upload.wikimedia.org/wikipedia/commons/f/f5/Light_dispersion_conceptual_waves.gif" width="300" height="200" alt="Prism dispersion">




</div>
</div>


---

![bg 90%](https://upload.wikimedia.org/wikipedia/commons/1/14/EM_spectrum_updated.svg)


---
## Snell's law

$$
n_1 \sin(\theta_1) = n_2 \sin(\theta_2)
$$

where $n_1$ and $n_2$ are the refractive indices of the two media, and $\theta_1$ and $\theta_2$ are the angles of incidence and refraction, respectively.

![bg invert:80% 90% right:33%](https://upload.wikimedia.org/wikipedia/commons/3/3f/Snells_law2.svg)


---
## 
![bg 80%](https://upload.wikimedia.org/wikipedia/commons/7/70/Rainbow1.svg) 
![bg 80%](https://upload.wikimedia.org/wikipedia/commons/5/5c/Double-alaskan-rainbow.jpg)


---
## Radiation

<iframe width="560" height="250" src="https://www.youtube.com/embed/wUpOlqbHcjI?si=QlgWZUhUBGRUmpq7" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

<iframe width="560" height="250" src="https://www.youtube.com/embed/FWCN_uI5ygY?si=NItzEyUbnEBMkOQu" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

![bg vertical 70% invert right](https://upload.wikimedia.org/wikipedia/commons/a/a6/Dipole_xmting_antenna_animation_4_408x318x150ms.gif) 
![bg 70% invert](https://upload.wikimedia.org/wikipedia/commons/d/da/Felder_um_Dipol.jpg)


---

<iframe width="560" height="315" src="https://www.youtube.com/embed/LmvfphxyRuo?si=27h5lu87PLA__4-k" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---


# Links

- [Coulomb's Law](https://en.wikipedia.org/wiki/Coulomb%27s_law)
- [Maxwell's Equations](https://en.wikipedia.org/wiki/Maxwell%27s_equations)
- [Gauss's Law](https://en.wikipedia.org/wiki/Gauss%27s_law)
- [Ampère's Law](https://en.wikipedia.org/wiki/Amp%C3%A8re%27s_circuital_law)
- [Faraday's Law](https://en.wikipedia.org/wiki/Faraday%27s_law_of_induction)
- [Biot-Savart Law](https://en.wikipedia.org/wiki/Biot%E2%80%93Savart_law)
- [Lorentz Force](https://en.wikipedia.org/wiki/Lorentz_force)
- [Ohm's Law](https://en.wikipedia.org/wiki/Ohm%27s_law)
- [Electromagnetic Waves](https://en.wikipedia.org/wiki/Electromagnetic_radiation)

---
## Literature

- Griffiths, David J. (1999). Introduction to Electrodynamics (3rd ed.). Prentice Hall. ISBN 0-13-805326-X.
- Purcell, Edward M. (2013). Electricity and Magnetism (3rd ed.). Cambridge University Press. ISBN 978-1-107-01402-2.
- Jackson, John David (1999). Classical Electrodynamics (3rd ed.). Wiley. ISBN 0-471-30932-X.
- wikipedia.org

## Comments

All the images used in this presentation are from Wikimedia Commons and are licensed under the Creative Commons Attribution-Share Alike 3.0 Unported license.

---
