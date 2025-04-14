# Derivation of Equivalent Resistance using Ohm's Law

### Equivalent Resistance in Series Connection:

In a series connection, the same current flows through each resistor successively. According to Ohm's law, the voltage $V$ across two points is equivalent to the product of the current $I$ flowing through those points and the resistance $R$ between them, i.e., $V = IR$.

In a series connection, however, the current is the same through each resistor. So, the voltage across the entire circuit is the sum of the voltages across individual resistors. Let's denote the resistances as $R_1, R_2, R_3, \ldots$, and the current as $I$.

From Ohm's law:
$$ V_{\text{total}} = IR_{\text{total}} $$

Substituting this equation for each resistor, we get:
$$ V_{\text{total}} = IR_1 + IR_2 + IR_3 + \ldots $$

Since the current is identical for each resistor, we can factor it out:
$$ V_{\text{total}} = I(R_1 + R_2 + R_3 + \ldots) $$

Ultimately, we obtain the formula for equivalent resistance:
$$ R_{\text{eq}} = R_1 + R_2 + R_3 + \ldots $$

### Equivalent Resistance in Parallel Connection:

In a parallel connection, the voltage is the same across each resistor because they are connected to the same points. According to Ohm's law, the current flowing through each resistor is inversely proportional to its resistance.

Let's denote the resistances as $R_1, R_2, R_3, \ldots$, and the voltage as $V$. From Ohm's law:
$$ I_1 = \frac{V}{R_1}, \, I_2 = \frac{V}{R_2}, \, I_3 = \frac{V}{R_3}, \ldots $$

Summing the currents leaving the voltage source, we get the total current $I$:
$$ I = I_1 + I_2 + I_3 + \ldots $$

Substituting the expressions for currents:
$$ I = V(\frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3} + \ldots) $$

We can factor out $V$ from the parentheses:
$$ I = V(\frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3} + \ldots) $$

Now, using Ohm's law, we find the equivalent resistance:
$$ R_{\text{eq}} = \frac{V}{I} = \frac{1}{\frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3} + \ldots} $$
