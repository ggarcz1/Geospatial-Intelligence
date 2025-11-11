import requests

class Triangulate:

    def find_center_coordinates(self, coord1: list, coord2: list, coord3: list) -> list:
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


    def get_city_coordinates(self, city: str, api_key: str) -> list:
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


