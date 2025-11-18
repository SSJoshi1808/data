from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the driver
driver = webdriver.Chrome()

try:
    # Navigate to Heroku drag-and-drop demo
    driver.get("http://the-internet.herokuapp.com/drag_and_drop")
    
    # Wait for page to load
    wait = WebDriverWait(driver, 10)
    
    # Find element A (draggable)
    # element_a = wait.until(
    #     EC.presence_of_element_located((By.ID, "column-a"))
    # )/
    element_a=driver.find_element(By.ID, "column-a")  
    # Find element B (drop target)
    element_b = driver.find_element(By.ID, "column-b")
    
    # Create ActionChains instance
    actions = ActionChains(driver)
    
    # Drag A and drop it on B
    actions.drag_and_drop(element_a, element_b).perform()
    
    # Wait for animation to complete
    time.sleep(2)
    
    print("Successfully dragged Column A to Column B!")
    
    # # Optional: Verify the swap happened by checking header text
    # column_a_header = driver.find_element(By.CSS_SELECTOR, "#column-a header").text
    # print(f"Column A now contains: {column_a_header}")
    
except Exception as e:
    print(f"Error occurred: {e}")
    
finally:
    # Close the browser
    driver.quit()