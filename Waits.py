from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 1: Launch Chrome browser
driver = webdriver.Chrome()
# Step 2: Open Google
driver.get("https://www.google.com")
# Step 3: Implicit Wait
driver.implicitly_wait(10)  # waits up to 10 sec for elements to appear automatically
# Step 4: Find search box and type text
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Pune")
# Step 5: Explicit Wait (until element is present)
wait = WebDriverWait(driver, 15)
search_box_explicit = wait.until(
    EC.presence_of_element_located((By.NAME, "q"))
)
search_box_explicit.send_keys(" Maharashtra")
# Step 6: Fluent Wait (custom poll frequency)
polling_wait = WebDriverWait(
    driver, 20, poll_frequency=3, ignored_exceptions=[Exception]
)
search_box_polling = polling_wait.until(
    EC.visibility_of_element_located((By.NAME, "q"))
)
search_box_polling.send_keys(" India")
# Step 7: Close browser
driver.quit()
