from fractions import Fraction

# -------------------------
# Independent Events
# -------------------------
P_heads = Fraction(1, 2)
P_six = Fraction(1, 6)

P_independent = P_heads * P_six

# -------------------------
# Dependent Events
# -------------------------
P_first_red = Fraction(5, 10)
P_second_red = Fraction(4, 9)

P_dependent = P_first_red * P_second_red

# -------------------------
# Results
# -------------------------
print("Independent Event Probability (Heads AND 6):", P_independent)
print("Dependent Event Probability (Both Red):", P_dependent)
