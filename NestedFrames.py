from selenium import webdriver
from selenium.webdriver.common.by import By
# Step 1: Launch Chrome browser
driver = webdriver.Chrome()
# Step 2: Open the webpage containing nested frames
driver.get("https://the-internet.herokuapp.com/nested_frames")
# Step 3: Switch to the top frame
driver.switch_to.frame("frame-top")
print("Switched to top frame")
# Step 4: Switch to the left frame (inside top frame)
driver.switch_to.frame("frame-left")
print("Switched to left frame")
# Step 5: Extract text from the left frame
left_frame = driver.find_element(By.TAG_NAME, "body")
print("Left Frame Text:", left_frame.text)
# Step 6: Switch back to the top frame (parent)
driver.switch_to.parent_frame()
print("Switched back to top frame")
# Step 7: Switch to the middle frame (inside top frame)
driver.switch_to.frame("frame-middle")
print("Switched to middle frame")
# Step 8: Extract text from the middle frame
middle_frame = driver.find_element(By.TAG_NAME, "body")
print("Middle Frame Text:", middle_frame.text)
# Step 9: Switch back to the top frame
driver.switch_to.parent_frame()
print("Switched back to top frame")
# Step 10: Switch to the main document
driver.switch_to.default_content()
# Step 11: Switch to the bottom frame
driver.switch_to.frame("frame-bottom")
print("Switched to bottom frame")
# Step 12: Extract text from the bottom frame
bottom_frame = driver.find_element(By.TAG_NAME, "body")
print("Bottom Frame Text:", bottom_frame.text)
# Step 13: Close browser
driver.quit()
