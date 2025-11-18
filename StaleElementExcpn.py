import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.get("https://www.google.com")
wait = WebDriverWait(driver, 10)
search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))
search_box.send_keys("IMCC")
search_box.send_keys(Keys.ENTER)
wait.until(EC.title_contains("IMCC"))
driver.get("https://www.facebook.com")
try:
    search_box.clear()  # This will raise StaleElementReferenceException
    search_box.send_keys("This will not be typed")
except Exception as e:
    print("Exception occurred:", type(e).__name__)
    print("Reason: Tried to use an element from the old page (stale reference).")
time.sleep(3)
driver.quit()
