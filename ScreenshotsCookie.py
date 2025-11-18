from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# Step 1: Launch Chrome browser
driver = webdriver.Chrome()
# Step 2: Open Google and maximize window
driver.get("https://www.google.com")
driver.maximize_window()
# Step 3: Locate the search text box and print its position and size (rect)
search_textbox = driver.find_element(By.NAME, "q")
print("Search box rect details:", search_textbox.rect)
# Step 4: Locate Google logo (SVG) and capture a screenshot of it
g_logo = driver.find_element(By.XPATH, "(//*[name()='svg'][@aria-label='Google'])[1]")
g_logo.screenshot("img_searchtextbox_logo.png")
print("Logo screenshot saved as img_searchtextbox_logo.png")
# Step 5: Capture full-screen screenshot
driver.save_screenshot("img_fullscreen.png")
print("Full page screenshot saved as img_fullscreen.png")
# Step 6: Print all cookies
print("\nAll Cookies:")
print(driver.get_cookies())
# Step 7: Retrieve specific cookies (may vary by system/browser)
print("\nCookie NID:", driver.get_cookie('NID'))
print("Cookie AEC:", driver.get_cookie('AEC'))
# Step 8: Get current window position
print("\nCurrent window position:", driver.get_window_position())
# Step 9: Resize and reposition the browser window
driver.set_window_rect(100, 200, 300, 400)
print("Window repositioned and resized.")
# Step 10: Wait and close browser
time.sleep(3)
driver.quit()
