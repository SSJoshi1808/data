from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://www.google.com")

multi_search_txtbox = driver.find_element(By.XPATH, "//textarea")

multi_search_txtbox.send_keys("IMCC")
multi_search_txtbox.send_keys(Keys.ENTER)   

