import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# source
# https://chromedriver.storage.googleapis.com/index.html?path=113.0.5672.24/


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

# double from 0 - 20
zoom = 13
# url = f'https://www.google.com/maps/@{latituide},{longituide},{zoom}z?entry=ttu'
url = f'https://www.google.com/maps/place/0%C2%B000\'{latitude}%22N+0%C2%B000\'{longitude}%22E/@{lat_look},{long_look},{zoom}z?entry=ttu'
file_name = 'selenium_tests.py'

# keep tab opened
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(url=url)

# # this is how to do it with typing, 
# # find element named "username"
# driver.find_element(By.NAME, "username").send_keys(username)
# # pressing the submit button
# driver.find_element(By.CSS_SELECTOR, "input[type=\"submit\" i]").click()
