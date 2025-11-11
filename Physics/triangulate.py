import requests

def find_center_coordinates(coord1: list, coord2: list, coord3: list) -> list:
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    lat3, lon3 = coord3

    avg_lat = (lat1 + lat2 + lat3) / 3
    avg_lon = (lon1 + lon2 + lon3) / 3

    # Format with 6 decimal places and degree symbol
    # formatted_lat = f"{avg_lat:.6f}°"
    # formatted_lon = f"{avg_lon:.6f}°"

    # return [[avg_lat, avg_lon],[formatted_lat, formatted_lon]]
    return [avg_lat, avg_lon]


def get_city_coordinates(city: str, api_key: str) -> list:
    geocoding_api_url = 'https://maps.googleapis.com/maps/api/geocode/json'

    # API request parameters
    params = {
        'address': city,
        'key': api_key  # Replace
    }

    response = requests.get(url=geocoding_api_url, params=params)
    data = response.json()

    # Parse the response to extract coordinates
    if data['status'] == 'OK' and len(data['results']) > 0:
        location = data['results'][0]['geometry']['location']
        lat = location['lat']
        lng = location['lng']
        return lat, lng
    else:
        print('Error occurred while geocoding.')
        return None


## Example usage to get a city's coordinates
# city_name = 'New York'
# coordinates = get_city_coordinates(city_name)

# if coordinates:
#     print(f'Coordinates of {city_name}: Latitude={coordinates[0]}, Longitude={coordinates[1]}')

# Example coordinates
coordinate1 = (41.8781, -87.6298)  # Chicago
coordinate2 = (34.0522, -118.2437)  # Los Angeles
coordinate3 = (40.7128, -74.0060)  # New York

# Find the center coordinates
center_coordinates = find_center_coordinates(coordinate1, coordinate2, coordinate3)

# Print the center coordinates
print(f'Center coordinates: {center_coordinates[0]:.6f}, {center_coordinates[1]:.6f}')