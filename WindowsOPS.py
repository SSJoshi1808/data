from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Step 1: Launch Chrome browser
driver = webdriver.Chrome()
# Step 2: Open Facebook
driver.get("https://www.facebook.com")
# Step 3: Create WebDriverWait instance
wait = WebDriverWait(driver, 10)
# Step 4: Get the handle of the current (original) window
original_window = driver.current_window_handle
print("Original Window Handle:", original_window)
print("Type of original_window:", type(original_window))
# Step 5: Open a new browser window
driver.switch_to.new_window('window')
wait.until(EC.number_of_windows_to_be(2))
# Step 6: Open another new tab with Google using JavaScript
driver.execute_script("window.open('http://www.google.com/');")
wait.until(EC.number_of_windows_to_be(3))
# Step 7: Get all window handles
all_windows = driver.window_handles
print("All Window Handles:", all_windows)
print("Type of all_windows:", type(all_windows))
# Step 8: Switch to any window other than the original
for window in all_windows:
    if window != original_window:
        driver.switch_to.window(window)
        print("Switched to new window:", window)
        break
# Step 9: Close all windows
driver.quit()
