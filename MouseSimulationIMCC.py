from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# Step 1: Launch Chrome browser
driver = webdriver.Chrome()
driver.set_page_load_timeout(20)
driver.maximize_window()
# Step 2: Open IMCC official website
driver.get("https://imcc.mespune.in/")
# Step 3: Wait until the 'Prominent Recruiters' section is visible
wait = WebDriverWait(driver, 15)
actions = ActionChains(driver)

header = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "//h2[contains(normalize-space(.), 'Prominent Recruiters')]")
    )
)
# Step 4: Locate all recruiter logos (images) below the header
logos = wait.until(
    EC.presence_of_all_elements_located(
        (By.XPATH, "//h2[contains(normalize-space(.), 'Prominent Recruiters')]/following::img")
    )
)
# Step 5: Print the total number of logos found
print("Total logos found:", len(logos))
# Step 6: If 3 or more logos exist, drag the 3rd logo left by 100 pixels
if len(logos) >= 3:
    third_logo = wait.until(EC.visibility_of(logos[2]))  # index 2 = 3rd logo
    time.sleep(2)
    actions.click_and_hold(third_logo).move_by_offset(-100, 0).release().perform()
    # Alternatively:
    # actions.drag_and_drop_by_offset(third_logo, -100, 0).perform()
    print("Dragged 3rd logo 100px to the left.")
    time.sleep(2)
else:
    print("Less than 3 logos found.")
# Step 7: Close browser
driver.quit()
