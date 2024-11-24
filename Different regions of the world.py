# Importing the necessary libraries
import folium
from folium import Choropleth

# Step 1: Creating a base map centered on Dhule, Maharashtra, India
maharashtra_map = folium.Map(location=[20.9042, 74.7749], zoom_start=8, tiles='Stamen Terrain')

# Step 2: Adding markers to the map for nearby cities
folium.Marker([20.9042, 74.7749], popup="Dhule").add_to(maharashtra_map)
folium.Marker([20.5500, 74.5333], popup="Malegaon").add_to(maharashtra_map)
folium.Marker([21.0067, 75.5626], popup="Jalgaon").add_to(maharashtra_map)
folium.Marker([19.9975, 73.7898], popup="Nasik").add_to(maharashtra_map)
folium.Marker([19.8762, 75.3433], popup="Aurangabad").add_to(maharashtra_map)

# Step 3: Adding a Choropleth Map for District Populations
# Hypothetical district population data
district_population = {
    'Dhule': 2050863,
    'Malegaon': 4710065,
    'Jalgaon': 4224442,
    'Nasik': 6109052,
    'Aurangabad': 3701282
}

# Converting the population data into GeoJSON format for Choropleth (simple representation)
geojson_data = {
    "type": "FeatureCollection",
    "features": [
        {"type": "Feature", "properties": {"name": "Dhule"}, "geometry": {"type": "Point", "coordinates": [74.7749, 20.9042]}},
        {"type": "Feature", "properties": {"name": "Malegaon"}, "geometry": {"type": "Point", "coordinates": [74.5333, 20.5500]}},
        {"type": "Feature", "properties": {"name": "Jalgaon"}, "geometry": {"type": "Point", "coordinates": [75.5626, 21.0067]}},
        {"type": "Feature", "properties": {"name": "Nasik"}, "geometry": {"type": "Point", "coordinates": [73.7898, 19.9975]}},
        {"type": "Feature", "properties": {"name": "Aurangabad"}, "geometry": {"type": "Point", "coordinates": [75.3433, 19.8762]}}
    ]
}

# Adding a Choropleth Layer
Choropleth(
    geo_data=geojson_data,
    name="choropleth",
    data=district_population,
    columns=["District", "Population"],
    key_on="feature.properties.name",
    fill_color="YlGn",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Population by District"
).add_to(maharashtra_map)

# Step 4: Adding layer control
folium.LayerControl().add_to(maharashtra_map)

# Step 5: Display the map
maharashtra_map.save("maharashtra_map_with_choropleth.html")

# View in notebook or interactive environments
maharashtra_map
