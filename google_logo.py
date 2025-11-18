from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.google.com")
driver.maximize_window()

# WAIT until logo is visible
logo = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[name()='svg' and @aria-label='Google']"))
)

logo.screenshot("goog.png")

print("Logo Class:", logo.get_attribute("class"))
print("Logo Tag:", logo.tag_name)

driver.quit()
