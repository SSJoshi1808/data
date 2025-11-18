from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Launch Chrome
driver = webdriver.Chrome()

# Open Google
driver.get("https://www.google.com")

# Apply implicit wait
driver.implicitly_wait(10)

# Try to find a wrong element (this locator does NOT exist)
search_box = driver.find_element(By.NAME, "wrong")  # <-- Invalid locator
search_box.send_keys("Pune")

# Explicit wait for the same wrong element
wait = WebDriverWait(driver, 15)
search_box_explicit = wait.until(
    EC.presence_of_element_located((By.NAME, "wrong"))
)
search_box_explicit.send_keys("Maharashtra")

# Fluent wait (polling wait) for the same wrong element
polling_wait = WebDriverWait(
    driver, 20, poll_frequency=3, ignored_exceptions=[Exception]
)
search_box_polling = polling_wait.until(
    EC.visibility_of_element_located((By.NAME, "wrong"))
)
search_box_polling.send_keys("India")

driver.quit()
