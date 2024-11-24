# Import necessary libraries
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Sample text data
text = (
    "Python is a programming language for data analysis and visualization. "
    "Python is used for machine learning, web development, and more. "
    "Python libraries such as NumPy, Pandas, and Matplotlib are essential for data scientists."
)

# Create a WordCloud object
wordcloud = WordCloud(
    width=800,        # Width of the word cloud image
    height=400,       # Height of the word cloud image
    background_color='white',  # Background color of the word cloud
    colormap='viridis',        # Color scheme for words
    contour_color='black',     # Outline color
    contour_width=1            # Thickness of the outline
).generate(text)

# Display the word cloud using matplotlib
plt.figure(figsize=(10, 5))  # Set the figure size
plt.imshow(wordcloud, interpolation='bilinear')  # Display the word cloud
plt.axis('off')  # Hide axes for a cleaner look
plt.title("Word Cloud Example", fontsize=16)  # Add a title
plt.show()  # Show the plot
