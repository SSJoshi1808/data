from selenium import webdriver
from selenium.webdriver.common.by import By 
import time 
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/checkboxes")
checkbox1 = driver.find_element(By.XPATH, "(//form[@id='checkboxes'])[1]") 
checkbox2 = driver.find_element(By.XPATH, "(//input[@type='checkbox'])[2]")
checkbox1.click() 
time.sleep(5) 
checkbox1.click() 
time.sleep(5) 
checkbox2.click() 
time.sleep(5) 
checkbox2.click() 
time.sleep(5)
time.sleep(5)
if not checkbox1.is_selected(): 
 checkbox1.click()
time.sleep(5)
if checkbox1.is_selected(): 
 checkbox1.click()
 time.sleep(5)
 # Click checkbox1 to Select only if its is NOT selected
 # Click checkbox1 to Unselect only if its selected
