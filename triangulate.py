import requests

# from chat gpt
def find_center_coordinates(coord1, coord2, coord3):
    # Latitude and longitude values of the coordinates
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    lat3, lon3 = coord3

    # Calculate the average latitude and longitude
    avg_lat = (lat1 + lat2 + lat3) / 3
    avg_lon = (lon1 + lon2 + lon3) / 3

    # Return the center coordinates
    return avg_lat, avg_lon

def get_city_coordinates(city):
    # Google Geocoding API endpoint
    geocoding_api_url = 'https://maps.googleapis.com/maps/api/geocode/json'

    # API request parameters
    params = {
        'address': city,
        'key': 'YOUR_API_KEY'  # Replace with your own Google Maps API key
    }

    # Send GET request to Geocoding API
    response = requests.get(geocoding_api_url, params=params)
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

# Example usage
city_name = 'New York'
coordinates = get_city_coordinates(city_name)

if coordinates:
    print(f'Coordinates of {city_name}: Latitude={coordinates[0]}, Longitude={coordinates[1]}')


# Example coordinates
coordinate1 = (41.8781, -87.6298)  # Chicago
coordinate2 = (34.0522, -118.2437)  # Los Angeles
coordinate3 = (40.7128, -74.0060)  # New York

# Find the center coordinates
center_coordinates = find_center_coordinates(coordinate1, coordinate2, coordinate3)

# Print the center coordinates
print("Center coordinates:", center_coordinates)