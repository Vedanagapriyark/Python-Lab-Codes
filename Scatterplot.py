import matplotlib.pyplot as plt
import numpy as np

# Generate random data for demonstration
x = np.random.rand(50) * 10  # Random x values between 0 and 10
y = np.random.rand(50) * 10  # Random y values between 0 and 10

# Create a scatter plot
plt.scatter(x, y, color='blue', label='Data points')

# Add labels and title
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('Simple Scatter Plot')

# Display a legend
plt.legend()

# Show the plot
plt.show()
