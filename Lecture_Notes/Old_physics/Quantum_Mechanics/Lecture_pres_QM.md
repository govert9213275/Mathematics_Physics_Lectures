---
title: Quantum Mechanics
author: Damian Chorążkiewicz
marp: true
theme: uncover
class: invert
math: mathjax
style: |
  section {
    font-size: 2em; /* Zmienia rozmiar czcionki na 1.5em */
  }
  .columns {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
  }
---

![bg brightness:.5](https://upload.wikimedia.org/wikipedia/commons/9/90/%C3%81tomo_de_Oro.gif)

<!--_color: #FF6-->
# <!--fit--> Quantum world

by Damian Chorążkiewicz 

---

# Lasciate ogne speranza, voi ch'intrate.

![bg right:50%](https://upload.wikimedia.org/wikipedia/commons/3/3e/Sandro_Botticelli_-_La_Carte_de_l%27Enfer.jpg)

---
## Planck's constant (1900)[ ...](https://en.wikipedia.org/wiki/Planck_constant)

![bg right:40%](https://upload.wikimedia.org/wikipedia/commons/d/df/Max_Planck_by_Hugo_Erfurth_1938cr.jpg)

$$
\Large E = {\color{yellow}h}\nu
$$

---
## Black body radiation (1901) [...](https://en.wikipedia.org/wiki/Black-body_radiation)

</br>

$$
u(\nu) = \frac{8\pi {\color{yellow}h}\nu^3}{c^3}\frac{1}{e^{\frac{{\color{yellow}h}\nu}{kT}}-1}
$$


![bg vertical 100% right:50%](https://upload.wikimedia.org/wikipedia/commons/2/21/Black_body_radiation.jpg)![bg 100%](https://upload.wikimedia.org/wikipedia/commons/1/1b/Planck1.svg)

---
## Photoelectric effect (1905) [...](https://en.wikipedia.org/wiki/Photoelectric_effect)
</br>

$$
K_{\text{max}} = {\color{yellow}h}\nu - W
$$

</br>

![bg 60% invert vertical right:50%](https://upload.wikimedia.org/wikipedia/commons/a/a6/Photoelectric_effect_in_a_solid_-_diagram.svg)![bg 80% invert](https://upload.wikimedia.org/wikipedia/commons/5/52/Photoelectric_effect_-_stopping_voltage_diagram_for_zinc_-_English.svg)




---
## Compton effect (1923) [...](https://en.wikipedia.org/wiki/Compton_scattering)

![bg invert 90% right:50%](https://upload.wikimedia.org/wikipedia/commons/e/e3/Compton-scattering.svg)

$$
\lambda' - \lambda = \frac{{\color{yellow}h}}{m_ec}(1-\cos\theta)
$$

---
## De Broglie wavelength (1924) [...](https://en.wikipedia.org/wiki/Matter_wave)

$$
E={\color{yellow}h}\nu=\frac{{\color{yellow}h}c}{\lambda}=pc
$$

so we can write

$$
\lambda = \frac{{\color{yellow}h}}{p} = \frac{{\color{yellow}h}}{mv}
$$

![bg vertical 100% right:50%](https://upload.wikimedia.org/wikipedia/commons/b/bf/Electron_buildup_movie_from_%22Controlled_double-slit_electron_diffraction%22_Roger_Bach_et_al_2013_New_J._Phys._15_033018.gif)![bg 100%](https://upload.wikimedia.org/wikipedia/commons/4/49/Roger_Bach_et_al_2013_New_J._Phys._15_033018_Nj458349f1.jpg)




---
## Rutherford scattering experiments (1911) [...](https://en.wikipedia.org/wiki/Geiger%E2%80%93Marsden_experiment)

![bg invert 90% right:60%](https://upload.wikimedia.org/wikipedia/commons/f/f9/Geiger-Marsden_experiment_expectation_and_result.svg)



---
## Bohr model  (1913) [...](https://en.wikipedia.org/wiki/Bohr_model)

$$
\begin{aligned}
n {\color{red}\lambda} &= 2\pi r \quad \text{standing wave!}\\
{\color{red}\lambda} &= \frac{{\color{yellow}h}}{mv} \quad \text{de Broglie!}\\
\end{aligned}
$$

so

$$
n{\color{red}\frac{{\color{yellow}h}}{mv}} = 2\pi r
$$

and (wow! :open_mouth:)

$$
l=mvr = n\frac{{\color{yellow}h}}{2\pi} \
$$  

**Quantization of angular momentum!**

![bg invert 100% right:30%](https://upload.wikimedia.org/wikipedia/commons/a/a7/Atom_deBrogie.jpg)


---
## Bohr model [...](https://en.wikipedia.org/wiki/Bohr_model)

Energy levels

$$
E_n = -\frac{Z^2e^2}{2a_0n^2}
$$

where

$$
a_0 = \frac{4\pi\epsilon_0{\color{yellow}\hbar^2}}{m_e e^2}
$$

![bg invert 100% right:50%](https://upload.wikimedia.org/wikipedia/commons/3/31/Bohr_atom_animation.gif)

---
## Rydberg formula (1888) [...](https://en.wikipedia.org/wiki/Rydberg_formula)

$$
\frac{1}{\lambda} = R\left(\frac{1}{n_1^2}-\frac{1}{n_2^2}\right)
$$

where

$$
R = \frac{m_e e^4}{8\epsilon_0^2{\color{yellow}h}^3c}
$$

![bg vertical invert 70% right:50%](https://upload.wikimedia.org/wikipedia/commons/9/93/Bohr_atom_model.svg)

---

![bg invert 90%](https://upload.wikimedia.org/wikipedia/commons/9/9a/Spectral_lines_of_the_hydrogen_atom.svg)![bg invert 100%](https://upload.wikimedia.org/wikipedia/commons/4/41/Hydrogen_spectrum.svg)


---


![bg vertical 100%](https://upload.wikimedia.org/wikipedia/commons/f/fb/Emission_spectrum-H_labeled.svg)

![bg 100%](https://upload.wikimedia.org/wikipedia/commons/2/2e/Helium_spectrum_visible.png)

![bg 100%](https://upload.wikimedia.org/wikipedia/commons/e/ec/Calcium_spectrum_visible.png)

---

![bg 90%](https://webbtelescope.org/files/live/sites/webb/files/home/resource-gallery/articles/_images/Spectroscopy/Article3/STScI-J-article-Spectroscopy-Part3-DifferentSpectra-f-1600x872.jpg?t=tn2400  )


---
## Laser (1960) [...](https://en.wikipedia.org/wiki/Laser)

 


![bg vertical invert 100% right:50%](https://upload.wikimedia.org/wikipedia/commons/0/09/Stimulated_Emission.svg)
![bg invert 90% right:50%](https://upload.wikimedia.org/wikipedia/commons/8/85/Helium_neon_laser_spectrum.svg)

---
## Schrödinger equation (1926) [...](https://en.wikipedia.org/wiki/Schr%C3%B6dinger_equation)

$$
\hat{H}\psi = E\psi
$$

where

$$
\hat{H} = -\frac{{\color{yellow}\hbar^2}}{2m}\nabla^2 + V
$$

![bg vertical invert 100% right:50%](https://upload.wikimedia.org/wikipedia/commons/e/e0/StationaryStatesAnimation.gif)


---
## Particle in a box 

$$
\psi(x) = [A\sin(kx) + B\cos(kx)]e^{-iEt/{\color{yellow}\hbar}} 
$$

</br>

**Energy levels**

</br>

$$
E_n = \frac{n^2\pi^2{\color{yellow}\hbar^2}}{2mL^2}
$$

![bg vertical invert 60% right:50%](https://upload.wikimedia.org/wikipedia/commons/1/13/Infinite_potential_well-en.svg)![bg invert 60%](https://upload.wikimedia.org/wikipedia/commons/8/8f/InfiniteSquareWellAnimation.gif)


---
## Quantum harmonic oscillator

</br>

$$
\hat{H} = -\frac{{\color{yellow}\hbar^2}}{2m}\nabla^2 + \frac{1}{2}m\omega^2x^2
$$

$$
E_n = \left(n+\frac{1}{2}\right){\color{yellow}\hbar}\omega
$$

</br>

![invert](https://upload.wikimedia.org/wikipedia/commons/c/c0/QHO-coherentstate3-animation-color.gif)

![bg vertical invert 40% right:50%](https://upload.wikimedia.org/wikipedia/commons/9/90/QuantumHarmonicOscillatorAnimation.gif)![bg invert 80%](https://upload.wikimedia.org/wikipedia/commons/3/35/Aufenthaltswahrscheinlichkeit_harmonischer_Oszillator.png)


---
## Quantum tunneling[ ...](https://en.wikipedia.org/wiki/Quantum_tunnelling)




![bg vertical invert 85% right:50%](https://upload.wikimedia.org/wikipedia/commons/4/48/E14-V20-B1.gif)![bg invert 90%](https://upload.wikimedia.org/wikipedia/commons/3/3f/Quantum_Tunnelling_animation.gif)


---
## STM

[Gallery](https://en.wikipedia.org/wiki/Scanning_tunneling_microscope#Gallery_of_STM_images)[, IMB](https://www.youtube.com/watch?v=oSCX78-8-q0&ab_channel=IBM)

![bg invert 100% right:50%](https://upload.wikimedia.org/wikipedia/commons/0/0f/Scanning_Tunneling_Microscope_schematic.svg)![](https://upload.wikimedia.org/wikipedia/commons/e/ec/Atomic_resolution_Au100.JPG)



---
## Real hydrogen atom! [ ...](https://en.wikipedia.org/wiki/Hydrogen_atom)

<iframe width="560" height="315" src="https://www.youtube.com/embed/W2Xb2GFK2yc?si=oVj1467opRobHgKq" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

![bg 90% right:50%](https://upload.wikimedia.org/wikipedia/commons/e/e7/Hydrogen_Density_Plots.png)


---
## Atomic bonding [ ...](https://en.wikipedia.org/wiki/Chemical_bond)

<style>
  .bg-invert-90 {
    filter: invert(90%);
  }
  .bg-invert-40 {
    filter: invert(40%);
  }
  .bg-invert-99 {
    filter: invert(99%);
  }
</style>

<table>
  <tr>
    <th>Ionic Bonding</th>
    <th>Covalent Bonding</th>
  </tr>
  <tr>
    <td>
      <img src="https://upload.wikimedia.org/wikipedia/commons/a/a8/NaF.gif" alt="Ionic Bonding" class="bg-invert-90" style="max-width: 100%;">
    </td>
    <td>
      <img src="https://upload.wikimedia.org/wikipedia/commons/1/19/Covalent_bond_hydrogen.svg" alt="Covalent Bonding" class="bg-invert-40" style="max-width: 100%;">
    </td>
  </tr>
  <tr>
    <th>Metallic Bonding</th>
    <th>Hydrogen Bonding</th>
  </tr>
  <tr>
    <td>
      <img src="https://upload.wikimedia.org/wikipedia/commons/3/3c/Metallic_Bonding_Example.svg" alt="Metallic Bonding" class="bg-invert-90" style="width: 300px;">
    </td>
    <td>
      <img src="https://upload.wikimedia.org/wikipedia/commons/c/c6/3D_model_hydrogen_bonds_in_water.svg" alt="Hydrogen Bonding" class="bg-invert-99" style="width: 250px;">
    </td>
  </tr>
</table>

---
## Shrödinger's cat (1935) [...](https://en.wikipedia.org/wiki/Schr%C3%B6dinger%27s_cat)

$$
\psi = \frac{1}{\sqrt{2}}\left(\psi_{\text{alive}} + \psi_{\text{dead}}\right)
$$

probabilities

$$
P_{\text{alive}} = \left|\psi_{\text{alive}}\right|^2
$$

$$
P_{\text{dead}} = \left|\psi_{\text{dead}}\right|^2
$$


![bg invert 100% right:50%](https://upload.wikimedia.org/wikipedia/commons/9/91/Schrodingers_cat.svg)


---
## Heisenberg uncertainty principle


$$
\Delta x\ \Delta p \geq \frac{{\color{yellow}\hbar}}{2}
$$

$$
\Delta E\ \Delta t \geq \frac{{\color{yellow}\hbar}}{2}
$$

![bg invert 70% right:50%](https://upload.wikimedia.org/wikipedia/commons/b/bc/Heisenberg_gamma_ray_microscope.svg)


---
## Dirac equation

$$
(i\gamma^\mu\partial_\mu - m)\psi = 0
$$
![bg invert:85% 100% right:50%](https://upload.wikimedia.org/wikipedia/commons/7/7d/Hydrogen_fine_structure.svg)


---
## QED

$$
\mathcal{L} = \bar{\psi}(i\gamma^\mu\partial_\mu - m)\psi - \frac{1}{4}F^{\mu\nu}F_{\mu\nu}
$$

![bg invert:85% 100% right:50%](https://upload.wikimedia.org/wikipedia/commons/0/0a/ElectronPositronAnnihilation.svg)


---
## Virtual particles...

<div class="columns">
  <div>
  <iframe width="560" height="315" src="https://www.youtube.com/embed/ztFovwCaOik?si=pv7Ai8v6ZbX0Cbku" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
  </div>
  <div>
<iframe width="560" height="315" src="https://www.youtube.com/embed/X-FEU4mQWtE?si=TSIdi7tnBOKdmWlz" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
  </div>


---
## Casimir effect

$$
F = \frac{\pi^2{\color{yellow}\hbar} c}{240d^4}
$$

where $d$ is the distance between the plates

![bg invert 90% right:50%](https://upload.wikimedia.org/wikipedia/commons/4/44/Casimir_plates.svg)

---
<!--_color: #FF6-->
## <!--fit--> Standard Model

---

![bg 70%](https://upload.wikimedia.org/wikipedia/commons/b/ba/Standard_Model_of_Elementary_Particles_and_Gravity.svg)


---

![bg](https://upload.wikimedia.org/wikipedia/commons/9/92/Quark_structure_proton.svg)![bg](https://upload.wikimedia.org/wikipedia/commons/8/81/Quark_structure_neutron.svg)


---
## Alpha decay [ ...](https://en.wikipedia.org/wiki/Alpha_decay)

![bg 90% invert:90% right:50%](https://upload.wikimedia.org/wikipedia/commons/7/79/Alpha_Decay.svg)

$$
^{238}_{92}U \rightarrow ^{234}_{90}Th + ^4_2He^{+2}
$$

</br>

$$
^{232}_{90}Th \rightarrow ^{228}_{88}Ra + ^4_2He^{+2}
$$

</br>


in general

</br>


$$
^{A}_{Z}X \rightarrow ^{A-4}_{Z-2}Y + ^4_2He^{+2}
$$


---
## Beta decay [ ...](https://en.wikipedia.org/wiki/Beta_decay)

![bg 90% invert:90% right:50%](https://upload.wikimedia.org/wikipedia/commons/a/aa/Beta-minus_Decay.svg)

![invert 150%](https://upload.wikimedia.org/wikipedia/commons/8/89/Beta_Negative_Decay.svg)


---
## Gamma decay [ ...](https://en.wikipedia.org/wiki/Gamma_decay)

![bg 90% invert:90% right:50%](https://upload.wikimedia.org/wikipedia/commons/c/c2/Gamma_Decay.svg)


---
## Nucler fission [ ...](https://en.wikipedia.org/wiki/Nuclear_fission)

![](https://upload.wikimedia.org/wikipedia/commons/9/95/TrinityDetonation1945GIF.gif)

![bg invert 70% right:50%](https://upload.wikimedia.org/wikipedia/commons/1/15/Nuclear_fission.svg)


---

![bg invert 80%](https://admin.energyencyclopedia.com/data/web/img-nuclear-energy/the-nuclear-power-industry/fission-chain-reaction/fission-chain-reaction.svg)


---
## Termo-nuclear fusion [ ...](https://en.wikipedia.org/wiki/Nuclear_fusion)

![bg invert 70% right:70%](https://upload.wikimedia.org/wikipedia/commons/8/85/Fusion_in_the_Sun.svg)![bg invert 90%](https://upload.wikimedia.org/wikipedia/commons/2/21/CNO_Cycle.svg)

---
## Links


<div>
    <ul>
      <li><a href="https://en.wikipedia.org/wiki/Introduction_to_quantum_mechanics">
      Introduction to quantum mechanics</a></li>
      <li><a href="https://www.youtube.com/watch?v=7vc-Uvp3vwg">YouTube</a></li>
    </ul>
</div>