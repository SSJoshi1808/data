from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains 
import time
driver = webdriver.Chrome() 
driver.get("https://imcc.mespune.in/")
program_menu = driver.find_element(By.XPATH, "//li[@id='menu-item-4383']")
actions = ActionChains(driver) 
actions.move_to_element(program_menu).perform()
time.sleep(5)
