from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# Step 1: Launch browser
driver = webdriver.Chrome()
# Step 2: Open Google
driver.get("https://www.google.com/")
# Step 3: Find the search box
search_txtbox = driver.find_element(By.XPATH, "//textarea[@name='q']")
# Step 4: Type 'imcc'
search_txtbox.send_keys('imcc')
# Step 5: Wait for dropdown suggestions to appear
time.sleep(2)
# Step 6: Find all dropdown items containing 'imcc'
imcc_dropdown = driver.find_elements(By.XPATH, "//span[contains(normalize-space(), 'imcc')]")
# Step 7: Print the results in the console
print("Number of dropdown suggestions found:", len(imcc_dropdown))
for i, item in enumerate(imcc_dropdown):
    print(f"{i+1}. {item.text}")
# Step 8: Close the browser
driver.close()
