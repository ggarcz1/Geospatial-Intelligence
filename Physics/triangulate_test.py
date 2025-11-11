from triangulate import Triangulate



t = Triangulate()

## Example usage to get a city's coordinates
# city_name = 'New York'
# coordinates = t.get_city_coordinates(city_name)

# if coordinates:
#     print(f'Coordinates of {city_name}: Latitude={coordinates[0]}, Longitude={coordinates[1]}')

# Example coordinates
coordinate1 = (41.8781, -87.6298)  # Chicago
coordinate2 = (34.0522, -118.2437)  # Los Angeles
coordinate3 = (40.7128, -74.0060)  # New York

# Find the center coordinates
center_coordinates = t.find_center_coordinates(coordinate1, coordinate2, coordinate3)

# Print the center coordinates
print(f'Center coordinates: {center_coordinates[0]:.6f}, {center_coordinates[1]:.6f}')