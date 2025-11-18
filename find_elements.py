from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Create Chrome driver instance
driver = webdriver.Chrome()

# Open Google
driver.get("https://www.google.com/")

# Find all <textarea> elements
multi_search_txtbox = driver.find_elements(By.XPATH, "//textarea")

# Type 'imcc' into the first one and press Enter
multi_search_txtbox[0].send_keys('imcc')
multi_search_txtbox[0].send_keys(Keys.ENTER)

# Wait for results to load
time.sleep(100)

# Close the browser
driver.quit()
