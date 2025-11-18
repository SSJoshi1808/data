from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
# Step 1: Launch Chrome browser
driver = webdriver.Chrome()
# Step 2: Open the webpage
driver.get("https://demoqa.com/select-menu")
# Step 3: Locate the multi-select dropdown element
multi_select_element = driver.find_element(By.ID, "cars")
multi_select = Select(multi_select_element)  # Standard multi-select
# Step 4: Select "Volvo" by visible text
multi_select.select_by_visible_text("Volvo")
time.sleep(2)
# Step 5: Deselect "Volvo" by visible text
multi_select.deselect_by_visible_text("Volvo")
time.sleep(2)
# Step 6: Select "Saab" (index = 1)
multi_select.select_by_index(1)
time.sleep(1)
# Step 7: Select "Audi" (value = 'audi')
multi_select.select_by_value("audi")
time.sleep(1)
# Step 8: Print all selected options
print("Currently selected options:")
all_selected_opt_list = multi_select.all_selected_options
for opt in all_selected_opt_list:
    print(opt.text)
# Step 9: Deselect options
multi_select.deselect_by_index(0)   # Deselect Volvo (if selected)
multi_select.deselect_by_value("audi")
multi_select.deselect_all()         # Clear all selections
# Step 10: Wait and close
time.sleep(5)
driver.quit()
