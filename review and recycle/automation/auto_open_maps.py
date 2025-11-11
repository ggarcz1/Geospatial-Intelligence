import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import argparse

# source
# https://googlechromelabs.github.io/chrome-for-testing/

# python .\auto_open_maps.py -lat 38.89694433202297 -long -77.0366269543101 -zoom 13

# default set to 0
latitude = longitude = 0
lat_look = long_look = 0
# url = 'https://www.google.com/maps'
coordinates = '38.9878171700676, -76.92139776882883'
coordinates = coordinates.replace(' ', '').split(',')
latitude = coordinates[0]
longitude = coordinates[1]

# default set these to the same as the lat and long to search
lat_look = latitude
long_look = longitude

parser = argparse.ArgumentParser(description='map lat, long, zoom')
parser.add_argument('-lat', '--arg1', help='latituide')
parser.add_argument('-long', '--arg2', help='longituide')
parser.add_argument('-zoom', '--arg3', help='zoom')
parser.add_argument('-view', '--arg4', help='view')


args = parser.parse_args()
if args.arg1:
    latitude = args.arg1
else:
    latitude = latitude
    
if args.arg2:
    longitude = args.arg2
else:
    longitude = longitude

# double from 0 - 20
if args.arg3:
    zoom = args.arg3
else:
    zoom = 13

# s --> satellite
# n --> normal maps
# f --> find location
if args.arg4:
    view = args.arg4
else:
    view = 's'


if view == 'f':
    # finds your location
    url = f'https://www.google.com/maps/@None,None,1046m/data=!3m1!1e3?entry=ttu&g_ep=EgoyMDI0MTAyOS4wIKXMDSoASAFQAw%3D%3D'

elif view == 'n':
    # plain map
    url = f'https://www.google.com/maps/@{latitude},{longitude},{zoom}z?entry=ttu'

elif view == 's':
    # satellite
    url = f'https://www.google.com/maps/@{latitude},{longitude},1046m/data=!3m1!1e3?entry=ttu&g_ep=EgoyMDI0MTAyOS4wIKXMDSoASAFQAw%3D%3D'

file_name = 'selenium_tests.py'

# keep tab opened
chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(url=url)

# # this is how to do it with typing, 
# # find element named 'username'
# driver.find_element(By.NAME, 'username').send_keys(username)
# # pressing the submit button
# driver.find_element(By.CSS_SELECTOR, 'input[type=\'submit\' i]').click()
