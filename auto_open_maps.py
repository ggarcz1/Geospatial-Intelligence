import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# source
# https://chromedriver.storage.googleapis.com/index.html?path=113.0.5672.24/

# set variable, such as username and password to send to each element
url = 'https://www.google.com/maps'
file_name = 'selenium_tests.py'
# keep tab opened
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(url=url)


# username = 'admin'
# password = 'admin'
# # find element named "username"
# driver.find_element(By.NAME, "username").send_keys(username)
# # find element named "password"
# driver.find_element(By.NAME, "password").send_keys(password)

# wait 5 seconds to see it actually work
time.sleep(5)

# driver.find_element(By.CSS_SELECTOR, "input[type=\"submit\" i]").click()

# malicious event, credential access from a certian computer/IP address?

# what about captchas?

#  delete the file after login from a user


# brute force

# change the ip every X login attempts