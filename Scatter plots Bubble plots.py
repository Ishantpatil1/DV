Scatter Plot Program
python
Copy code
# Import necessary libraries
import matplotlib.pyplot as plt

# Define the data
hours_studied = [1, 2, 3, 4, 5, 6, 7, 8]
test_scores = [50, 55, 60, 65, 70, 75, 80, 85]

# Create a scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(hours_studied, test_scores, color='skyblue', marker='D')

# Add title and labels
plt.title('Scatter Plot of Hours Studied vs. Test Score', fontsize=14)
plt.xlabel('Hours Studied', fontsize=12)
plt.ylabel('Test Score', fontsize=12)

# Show grid
plt.grid(True)

# Display the plot
plt.show()

Bubble Chart Program
python
Copy code
# Import necessary libraries
import matplotlib.pyplot as plt

# Define the data
hours_studied = [1, 2, 3, 4, 5, 6, 7, 8]
test_scores = [50, 55, 60, 65, 70, 75, 80, 85]
bubble_sizes = [100, 200, 300, 400, 500, 600, 700, 800]  # Size of bubbles

# Create a bubble chart
plt.figure(figsize=(8, 6))
plt.scatter(hours_studied, test_scores, s=bubble_sizes, alpha=0.7, color='blue', edgecolors='black')

# Add title and labels
plt.title('Bubble Chart of Hours Studied vs. Test Score', fontsize=14)
plt.xlabel('Hours Studied', fontsize=12)
plt.ylabel('Test Score', fontsize=12)

# Display the plot
plt.show()
