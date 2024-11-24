# Importing the folium library
import folium

# Step 1: Create a base map centered on a specific location
# Here, the location is set to Ratnagiri (16.9902, 73.3120) with an initial zoom level of 12
my_map = folium.Map(location=[16.9902, 73.3120], zoom_start=12)

# Step 2: Add custom markers with popups
# Adding a marker for Ratnagiri
folium.Marker([16.9902, 73.3120], popup='Ratnagiri').add_to(my_map)
# Adding a marker for Dhule
folium.Marker([20.9042, 74.7749], popup='Dhule').add_to(my_map)

# Step 3: Draw a polyline connecting Ratnagiri and Dhule
# The line_opacity argument sets the transparency of the line
folium.PolyLine(locations=[(16.9902, 73.3120), (20.9042, 74.7749)],
                color='blue', line_opacity=0.5).add_to(my_map)

# Step 4: Save the map as an HTML file
my_map.save("map.html")

# Step 5: Display the map (useful in Jupyter Notebooks or compatible environments)
my_map
