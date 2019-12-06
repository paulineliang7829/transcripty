"""
Example file
------------

This file demonstrates how to create a simulation for N individuals
who start as college freshman. It then plots the 10/20/.../80/90
quantiles of credits after two years
"""
import matplotlib.pyplot as plt
import numpy as np
import transcripty as t


# Create the model and simulate
hpm = t.HeterogeneousProbabilityModel(0.35, 0.6778, 1.0556, 0.1, 6, 12, 3, 125)
a_i, gpa_i, credits = hpm.simulate(25000)

# Cumulative sum of credits to get total credits after year
# t and then find relevant quantiles
cumsum_credits = np.cumsum(credits, axis=1)
deciles = np.linspace(0.1, 0.9, 9)
y2_credit_deciles = np.quantile(cumsum_credits[:, 1], deciles)

fig, ax = plt.subplots()

ax.bar(deciles, y2_credit_deciles, width=0.05)




