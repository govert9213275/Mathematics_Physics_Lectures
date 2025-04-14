# Derivation of Equivalent Capacitance using Capacitors

### Equivalent Capacitance in Series Connection:

In a series connection of capacitors, the same charge flows through each capacitor in succession. According to the capacitor equation $Q = CV$, where $Q$ is the charge, $C$ is the capacitance, and $V$ is the voltage across the capacitor, the voltage across the entire series connection is the sum of the voltages across individual capacitors. Let's denote the capacitances as $C_1, C_2, C_3, \ldots$, and the voltage as $V$.

From the capacitor equation:
$$ Q_{\text{total}} = CV_{\text{total}} $$

Substituting this equation for each capacitor, we get:
$$ Q_{\text{total}} = CV_1 + CV_2 + CV_3 + \ldots $$

Since the charge is identical for each capacitor, we can factor it out:
$$ Q_{\text{total}} = C(V_1 + V_2 + V_3 + \ldots) $$

Ultimately, we obtain the formula for equivalent capacitance:
$$ C_{\text{eq}} = \frac{1}{\frac{1}{C_1} + \frac{1}{C_2} + \frac{1}{C_3} + \ldots} $$

### Equivalent Capacitance in Parallel Connection:

In a parallel connection of capacitors, the same voltage is applied across each capacitor because they are connected to the same points. According to the capacitor equation $Q = CV$, the charge stored in each capacitor is directly proportional to its capacitance.

Let's denote the capacitances as $C_1, C_2, C_3, \ldots$, and the voltage as $V$. From the capacitor equation:
$$ Q_1 = CV_1, \, Q_2 = CV_2, \, Q_3 = CV_3, \ldots $$

Summing the charges leaving the voltage source, we get the total charge $Q$:
$$ Q = Q_1 + Q_2 + Q_3 + \ldots $$

Substituting the expressions for charges:
$$ Q = C(V_1 + V_2 + V_3 + \ldots) $$

We can factor out $C$ from the parentheses:
$$ Q = C(V_1 + V_2 + V_3 + \ldots) $$

Now, using the capacitor equation, we find the equivalent capacitance:
$$ C_{\text{eq}} = \frac{Q}{V} = C_1 + C_2 + C_3 + \ldots $$
