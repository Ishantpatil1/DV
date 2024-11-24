# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Area Plot
# Create data
x = range(1, 6)
y = [1, 4, 6, 8, 4]

# Create the area plot
plt.fill_between(x, y, color="red", alpha=0.7)  # Adding alpha for slight transparency
plt.title("Area Plot Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)  # Optional: Adds a grid for better readability
plt.show()

# Histogram
# Generate random data for the histogram
data = np.random.randn(1000)  # 1000 data points sampled from a normal distribution

# Plotting a basic histogram
plt.hist(data, bins=30, color='blue', edgecolor='black', alpha=0.7)
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Basic Histogram')
plt.grid(True)  # Optional: Adds a grid for better readability
plt.show()
