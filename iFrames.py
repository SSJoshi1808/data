from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# Step 1: Launch Chrome browser
driver = webdriver.Chrome()
# Step 2: Open the webpage containing an iFrame
driver.get("https://the-internet.herokuapp.com/iframe")
# Step 3: Switch to the iFrame by ID
driver.switch_to.frame("mce_0_ifr")
print("Switched to iframe")
# Step 4: Locate the editable body and clear using Ctrl + A + Delete
iframe_body = driver.find_element(By.TAG_NAME, "body")
iframe_body.send_keys(Keys.CONTROL + "a")  # Select all text
iframe_body.send_keys(Keys.DELETE)          # Delete selected text
iframe_body.send_keys("India")              # Type new text
print("Typed 'India' inside the iFrame")
# Step 5: Switch back to the main document
driver.switch_to.default_content()
print("Switched back to main document")
# Step 6: Verify with the main page header
main_header = driver.find_element(By.TAG_NAME, "h3")
print("Main Document Header:", main_header.text)
# Step 7: Close browser
time.sleep(100)
driver.quit()
