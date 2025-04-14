# Derivation of Faraday's Law from Lorentz Force

## Lorentz Force

The Lorentz force $\mathbf{F}$ acting on a charged particle moving with velocity $\mathbf{v}$ in a magnetic field $\mathbf{B}$ is given by:

$$
\mathbf{F} = q(\mathbf{v} \times \mathbf{B})
$$

where $q$ is the charge of the particle.

## Force on a Wire

Consider a straight wire of length $L$ moving with velocity $\mathbf{v}$ perpendicular to a constant magnetic field $\mathbf{B}$.

The force acting on the wire due to the magnetic field is the sum of the forces on all the charged particles within the wire. Integrating over the length of the wire, we have:

$$
\mathbf{F} = \int (\mathbf{v} \times \mathbf{B}) \, dq
$$

## Charge Density and Current

The charge density $q$ along the wire is related to the current $I$ flowing through it. For a wire of cross-sectional area $A$, we have:

$$
q = \rho A L
$$

where $\rho$ is the charge density.

Since $I = \frac{\Delta q}{\Delta t}$, we can express $dq$ in terms of $dI$:

$$
dq = \rho A \, dx = \rho A v \, dt = I \, dt
$$

Substituting $dq$ in terms of $I$, we get:

$$
\mathbf{F} = \int (\mathbf{v} \times \mathbf{B}) \, I \, dt
$$

## Faraday's Law

Using the definition of electromotive force (emf) as the work done per unit charge in moving a test charge around a closed path, we have:

$$
\mathcal{E} = \oint \mathbf{E} \cdot d\mathbf{l}
$$

For a straight wire moving in a magnetic field, the induced emf $\mathcal{E}$ is equal to the force per unit charge times the length of the wire:

$$
\mathcal{E} = \int \mathbf{F} \cdot d\mathbf{l}
$$

Using the expression for force $\mathbf{F}$ derived earlier, we obtain:

$$
\mathcal{E} = \int (\mathbf{v} \times \mathbf{B}) \cdot d\mathbf{l}
$$

By the vector identity $\mathbf{A} \cdot (\mathbf{B} \times \mathbf{C}) = \mathbf{B} \cdot (\mathbf{C} \times \mathbf{A})$, we can rewrite this as:

$$
\mathcal{E} = \int (\mathbf{B} \times d\mathbf{l}) \cdot \mathbf{v}
$$

Recognizing that $\mathbf{B} \times d\mathbf{l}$ is the infinitesimal area vector $d\mathbf{A}$ swept out by the wire as it moves, and that $\mathbf{v} \cdot d\mathbf{A} = dA \frac{dx}{dt} = dA v$, we finally obtain Faraday's law:

$$
\mathcal{E} = -\frac{d\Phi}{dt}
$$

where $\Phi$ is the magnetic flux through the loop formed by the wire.

