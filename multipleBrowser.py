from selenium import webdriver
from selenium.webdriver.common.by import By 
import time
driver = webdriver.Chrome() 
driver.get("https://www.google.com")
driver.switch_to.new_window("window") 
driver.get("https://www.facebook.com")
driver.switch_to.new_window("tab") 
driver.get("https://www.youtube.com") 
time.sleep(10)
driver.close() 
