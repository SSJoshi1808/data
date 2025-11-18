from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# Step 1: Launch Chrome browser
driver = webdriver.Chrome()
# Step 2: Open the JavaScript alerts demo page
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# Step 3: Locate and click the "Click for JS Confirm" button
confirm_button = driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']")
confirm_button.click()
# Step 4: Switch focus to the alert
alert = driver.switch_to.alert
print("Alert text:", alert.text)
# Step 5: Accept the alert (Click "OK")
alert.accept()
# Alternative: use alert.dismiss() to click "Cancel"
# Step 6: Verify result message on the page
result = driver.find_element(By.ID, "result")
print("Page result after accepting alert:", result.text)
# Step 7: Wait a few seconds to see result, then close browser
time.sleep(3)
driver.quit()
