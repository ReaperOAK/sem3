import matplotlib.pyplot as plt
import numpy as np

# Define the range for x
x = np.linspace(-10, 10, 400)

# Define the equations
y1 = x**2 - 4*x + 4
x2 = np.linspace(-10, 10, 400)
y2 = x2**2 / 4
y3 = x**2 - 4*x + 4
y4 = 4*x**2
x3 = np.linspace(0.1, 10, 400)
y5 = 40 / x3

# Create the plot
plt.figure(figsize=(10, 8))

# Plot the equations
plt.plot(x, y1, label='y = x^2 - 4x + 4')
plt.plot(x2, y2, label='x^2 = 4y')
plt.plot(x, y3, label='y = x^2 - 4x + 4')
plt.plot(x, y4, label='y = 4x^2')
plt.plot(x3, y5, label='xy = 40')

# Draw a straight line (example: y = 2x + 1)
y_line = 2 * x + 1
plt.plot(x, y_line, label='y = 2x + 1', linestyle='--')

# Add labels and legend
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graphs of Given Equations')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()