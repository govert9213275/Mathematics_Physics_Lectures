# Derivation of Electromagnetic Waves from Maxwell's Equations

## Maxwell's Equations

The four Maxwell's equations in differential form are:

1. Gauss's Law for Electricity:

   $$
   \nabla \cdot \mathbf{E} = \frac{\rho}{\epsilon_0}
   $$

2. Gauss's Law for Magnetism:

   $$
   \nabla \cdot \mathbf{B} = 0
   $$

3. Faraday's Law of Induction:

   $$
   \nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}
   $$

4. Ampère's Law with Maxwell's Addition:

   $$
   \nabla \times \mathbf{B} = \mu_0 \mathbf{J} + \mu_0 \epsilon_0 \frac{\partial \mathbf{E}}{\partial t}
   $$

## Derivation

### Step 1: Eliminate Charges ($\rho$ and $\mathbf{J}$)

Assuming no free charges or currents ($\rho = 0$ and $\mathbf{J} = 0$), we simplify Maxwell's equations to:

1. Gauss's Law for Electricity:

   $$
   \nabla \cdot \mathbf{E} = 0
   $$

2. Gauss's Law for Magnetism:

   $$
   \nabla \cdot \mathbf{B} = 0
   $$

3. Faraday's Law of Induction:

   $$
   \nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}
   $$

4. Ampère's Law with Maxwell's Addition:

   $$
   \nabla \times \mathbf{B} = \mu_0 \epsilon_0 \frac{\partial \mathbf{E}}{\partial t}
   $$

### Step 2: Cross Derivatives

Take the curl of Faraday's Law and Ampère's Law:

$$
\nabla \times \nabla \times \mathbf{E} = \nabla \times \left( -\frac{\partial \mathbf{B}}{\partial t} \right)
$$

$$
\nabla \times \nabla \times \mathbf{B} = \nabla \times \left( \mu_0 \epsilon_0 \frac{\partial \mathbf{E}}{\partial t} \right)
$$

### Step 3: Vector Calculus Identities

Apply vector calculus identities:

$$
\nabla \times \nabla \times \mathbf{E} = \nabla (\nabla \cdot \mathbf{E}) - \nabla^2 \mathbf{E}
$$

$$
\nabla \times \nabla \times \mathbf{B} = \nabla (\nabla \cdot \mathbf{B}) - \nabla^2 \mathbf{B}
$$

### Step 4: Simplification

Since $\nabla \cdot \mathbf{E} = 0$ and $\nabla \cdot \mathbf{B} = 0$, the above equations simplify to:

$$
\nabla \times \nabla \times \mathbf{E} = -\nabla^2 \mathbf{E}
$$

$$
\nabla \times \nabla \times \mathbf{B} = -\nabla^2 \mathbf{B}
$$

### Step 5: Substitution

Substitute the simplified expressions back into Faraday's Law and Ampère's Law:

$$
-\nabla^2 \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}
$$

$$
-\nabla^2 \mathbf{B} = \mu_0 \epsilon_0 \frac{\partial \mathbf{E}}{\partial t}
$$

### Step 6: Wave Equation

Combine the two equations:

$$
\nabla^2 \mathbf{E} = \mu_0 \epsilon_0 \frac{\partial^2 \mathbf{E}}{\partial t^2}
$$

$$
\nabla^2 \mathbf{B} = \mu_0 \epsilon_0 \frac{\partial^2 \mathbf{B}}{\partial t^2}
$$

These are the wave equations for electric and magnetic fields, confirming the existence of electromagnetic waves.
