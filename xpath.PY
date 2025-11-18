from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Step 1: Create Chrome driver instance
driver = webdriver.Chrome()
# Step 2: Open Google
driver.get("https://www.google.com/")

driver.maximizewindow()
# Step 3: Locate search box using XPath
search_txtbox = driver.find_element(By.XPATH, "//textarea[@name='q']")
# Step 4: Type 'imcc'
search_txtbox.send_keys('imcc')
# Step 5: Wait for dropdown suggestions to appear
time.sleep(2)
# Step 6: Locate the first suggestion that contains 'imcc'
imcc_dropdown = driver.find_element(By.XPATH, "(//span[contains(normalize-space(), 'imcc')])[1]")
# Step 7: Click the suggestion
imcc_dropdown.click()
# Optional: Wait to view the result
time.sleep(100)
# Step 8: Close browser
driver.quit()

