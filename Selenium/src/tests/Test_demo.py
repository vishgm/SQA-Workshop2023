# Necessary import (Selenium, time modules)
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Options for keeping the Chrome window open (Prevent default close)
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Set up the Selenium driver for Chrome
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the bookstore website
driver.get("https://www.google.com/")

# Find the search bar element and enter a search query
search_bar = driver.find_element("name","q")
search_bar.send_keys("Vidyalankar School of information Technology")

# Pause for 0.2 seconds
time.sleep(0.2)
#perform Google search with Keys.ENTER
search_bar.send_keys(Keys.ENTER)

# Find the first Link and Click on it
result = driver.find_element(By.XPATH, '(//h3)[1]/../../a').click()
# result.click()


time.sleep(5)
# Find the first Link and Click on it

result = driver.find_element(By.LINK_TEXT, 'About Us').click()
result.click()

# Close the driver
# driver.quit()
