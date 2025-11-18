import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
# Step 1: Launch Chrome browser
driver = webdriver.Chrome()
# Step 2: Open the webpage
driver.get("https://the-internet.herokuapp.com/dropdown")
# Step 3: Locate dropdown element by ID
mydropdown = driver.find_element(By.ID, "dropdown")
# Step 4: Create Select object
dropdown = Select(mydropdown)
# Step 5: Select Option 1 using visible text
dropdown.select_by_visible_text("Option 1")
time.sleep(5)
# Step 6: Print selected option
selected_option = dropdown.first_selected_option
print(f"Selected option: {selected_option.text}")
# Step 7: Select Option 2 using value
dropdown.select_by_value("2")
time.sleep(5)
# Step 8: Select Option 1 again using index (index starts from 0)
dropdown.select_by_index(1)
time.sleep(5)
# Step 9: Deselect options (only works for multi-select dropdowns)
# Note: The dropdown on this page is NOT multi-select, so these will raise an error
try:
    dropdown.deselect_by_visible_text("Option 1")
    dropdown.deselect_all()
except Exception as e:
    print("Deselect operations not supported for single-select dropdowns.")
# Step 10: Close browser
driver.quit()
