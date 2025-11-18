import time
from re import search

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.maximize_window()
search_element = driver.find_element(By.NAME, "q")
search_element.send_keys("imcc")
search_element.send_keys(Keys.ENTER)


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
print("\nAll cookies deleted!")

# 8. Verify
print("\n===== Cookies AFTER deleting =====")
print(driver.get_cookies())   # Should be empty list []

time.sleep(3)

driver.quit()
