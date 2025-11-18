from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# Step 1: Launch Chrome browser
driver = webdriver.Chrome()
# Step 2: Open Facebook signup page
driver.get("https://www.facebook.com/")
# Step 3: Wait until 'Create new account' button is clickable, then click
wait = WebDriverWait(driver, 10)
create_account_button = wait.until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Create new account"))
)
create_account_button.click()
# Step 4: Wait for registration form to appear
registration_form = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//form[@id='reg']"))
)
# Step 5: Locate all input fields
first_name = wait.until(EC.presence_of_element_located((By.NAME, "firstname")))
last_name = wait.until(EC.presence_of_element_located((By.NAME, "lastname")))
mobile_number = wait.until(EC.presence_of_element_located((By.NAME, "reg_email__")))
password = wait.until(EC.presence_of_element_located((By.NAME, "reg_passwd__")))
# Step 6: Fill in the registration details
first_name.send_keys("YourName")
last_name.send_keys("YourSurname")
mobile_number.send_keys("1234567890")
password.send_keys("SecurePassword123")
# Step 7: Select date of birth
day = wait.until(EC.presence_of_element_located((By.ID, "day")))
month = wait.until(EC.presence_of_element_located((By.ID, "month")))
year = wait.until(EC.presence_of_element_located((By.ID, "year")))
day.send_keys("6")
month.send_keys("Sep")
year.send_keys("1990")
# Step 8: Select gender
gender_male = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@value='2']")))
gender_male.click()
# Step 9: Click Sign Up button
sign_up_button = wait.until(EC.element_to_be_clickable((By.NAME, "websubmit")))
sign_up_button.click()
# Step 10: Handle confirmation/error message (optional - Facebook will block automation)
try:
    confirmation_message_wait = WebDriverWait(driver, 20)
    confirmation_message = confirmation_message_wait.until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'confirm') or contains(text(),'code')]"))
    )
    print("Confirmation or security message appeared.")
except:
    print("No confirmation detected (Facebook blocked automation).")
# Step 11: Pause and close browser
time.sleep(5)
driver.quit()
