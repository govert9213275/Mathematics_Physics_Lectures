# Point charge

The electric field of a point charge is given by

$$
\mathbf{E} = \frac{1}{4\pi\epsilon_0} \frac{q}{r^2} \hat{\mathbf{r}}
$$

where $q$ is the charge, $r$ is the distance from the charge, and $\hat{\mathbf{r}}$ is the unit vector pointing from the charge to the point where the field is being calculated. The electric field is radially outward from a positive charge and radially inward toward a negative charge.

Our sufface is a sphere of radius $r$ centered on the charge. The electric field is perpendicular to the surface at every point, so the electric flux through the surface is constant and equal to the electric field at the surface times the area of the surface. The electric field is the same at every point on the surface, so the flux is

$$
\Phi = \mathbf{E} \cdot \mathbf{A} = E A = \frac{1}{4\pi\epsilon_0} \frac{q}{r^2} 4\pi r^2 = \frac{q}{\epsilon_0}
$$

To prove that result is independent on shape is little bit more complicated. 

# Infinite line of charge

Let's consider an infinite line of charge with charge density $\lambda$. Due to the symmetry of the problem, the electric field must be perpendicular to the line of charge and have the same magnitude at every point at the same distance from the line. Choose a cylindrical Gaussian surface of radius $r$ and length $L$ that is centered on the line of charge. The electric field is perpendicular to the surface at every point, so the electric flux through the surface is constant and equal to the electric field at the surface times the area of the surface. The electric field is the same at every point on the surface, so the flux is

$$
\Phi = \mathbf{E} \cdot \mathbf{A} = E 2\pi r L = \frac{\lambda L}{\epsilon_0}
$$

So the electric field is

$$
E = \frac{\lambda}{2\pi\epsilon_0 r}
$$

# Infinite plane of charge

Let's consider an infinite plane of charge with charge density $\sigma$. Due to the symmetry of the problem, the electric field must be perpendicular to the plane of charge and have the same magnitude at every point at the same distance from the plane. Choose a rectangular Gaussian surface of area $A$ that is parallel to the plane of charge. The electric field is perpendicular to the surface at every point, so the electric flux through the surface is constant and equal to the electric field at the surface times the area of the surface. The electric field is the same at every point on the surface, so the flux is

$$
\Phi = \mathbf{E} \cdot \mathbf{A} = E 2A = \frac{\sigma A}{\epsilon_0}
$$

So the electric field is

$$
E = \frac{\sigma}{2\epsilon_0}
$$

# Electric field between two plates

Just by superposition of the previous results, the electric field between two plates with charge densities $+\sigma$ and $-\sigma$. 
We will have the electric field between the plates as

$$
E = \frac{\sigma}{\epsilon_0}
$$


<figure style="text-align: center;">
    <img src="https://upload.wikimedia.org/wikipedia/commons/e/eb/VFPt_capacitor-square-plate.svg" alt="Electric Field" width="200" height="auto">
    <figcaption>Illustration of Electric Field between two plates of a capacitor.
     Source: Wikimedia Commons</figcaption>
</figure>


