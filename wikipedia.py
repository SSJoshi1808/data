from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# 1. Open Wikipedia
driver.get("https://en.wikipedia.org/wiki/Main_Page")
driver.maximize_window()
time.sleep(2)

# 2. Print Page Title
print("Page Title:", driver.title)

# 3. Print Main Heading
main_heading = driver.find_element(By.ID, "mp-welcome")
print("Main Heading:", main_heading.text)

# 4. Print Wikipedia Logo SRC
logo = driver.find_element(By.CSS_SELECTOR, "img.mw-logo-icon")
print("Wikipedia Logo SRC:", logo.get_attribute("src"))

# 5. Print ALL Cookies
print("\n===== ALL Cookies BEFORE deleting =====")
cookies = driver.get_cookies()
for cookie in cookies:
    print(cookie)

# 6. Print ONE cookie (for example: 'GeoIP' or first cookie)
print("\n===== Printing ONE Cookie =====")
one_cookie = driver.get_cookie(cookies[0]["name"])   # Access first cookie name dynamically
print(one_cookie)

#  If you want by specific name:
#  print(driver.get_cookie("GeoIP"))

# 7. Delete ALL Cookies
driver.delete_all_cookies()
print("\n All cookies deleted!")

# 8. Verify
print("\n===== Cookies AFTER deleting =====")
print(driver.get_cookies())   # Should be empty list []

time.sleep(2)
driver.quit()
