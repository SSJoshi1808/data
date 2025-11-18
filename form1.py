from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import  Select
import time

driver = webdriver.Chrome()
wait= WebDriverWait(driver,10)
driver.maximize_window()
driver.get("https://formy-project.herokuapp.com/form")
fname=wait.until(
    ec.presence_of_element_located((
        By.ID,"first-name"
    ))
)
sname= wait.until(
    ec.presence_of_element_located((
        By.ID,"last-name"
    ))
)
job_title= wait.until(
    ec.presence_of_element_located((
        By.ID,"job-title"
    ))
)

radio = wait.until(
    ec.presence_of_element_located((
        By.ID,"radio-button-2"
    ))
)
gender = wait.until((
    ec.presence_of_element_located((
        By.ID,"checkbox-2"
    ))
))

dropdown= Select(driver.find_element(By.ID,"select-menu"))
dropdown.select_by_visible_text("2-4")

btn = wait.until((
    ec.element_to_be_clickable((
        By.XPATH,"//a[normalize-space()='Submit']"
    ))
))
fname.send_keys("aaa")
sname.send_keys("bbb")
job_title.send_keys("Software developer")
radio.click()
gender.click()
btn.click()
time.sleep(2)
driver.close()
