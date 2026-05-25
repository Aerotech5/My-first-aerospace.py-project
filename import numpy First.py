import numpy as np
import matplotlib.pyplot as plt

# Create x values
x = np.linspace(0, 10, 500)

# Create sine wave
y = np.sin(x)

# plot the wave
plt.plot(x,y)

# Labels and title 
plt.title("sine wave")
plt.xlabel("Time")
plt.ylabel("Amplitude")

# Show graph
plt.show()