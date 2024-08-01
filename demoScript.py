# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 18:30:56 2024

@author: Simon
"""

# demoScript.py
import numpy as np
import matplotlib.pyplot as plt

# Generate data for a sine wave
x = np.linspace(0, 80 * np.pi, 100)
y = np.sin(x)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Sine Wave', color='blue', linewidth=2)

# Add labels and title
plt.title('Sine Wave Plot', fontsize=16)
plt.xlabel('x values (radians)', fontsize=14)
plt.ylabel('sin(x)', fontsize=14)
plt.legend()
plt.grid(True)

# Save the plot
plt.savefig('sine_wave_plot.png')

# Show the plot
plt.show()
