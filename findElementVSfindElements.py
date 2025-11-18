from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.com/")

single_webele = driver.find_element(By.XPATH, "//textarea")
multi_webele = driver.find_elements(By.XPATH, "//textarea")

print(type(single_webele))
print(type(multi_webele))

driver.quit()
