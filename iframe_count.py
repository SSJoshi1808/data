# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# driver = webdriver.Chrome()
# driver.get("https://www.google.com")
# time.sleep(3)   # wait for page load
#
# iframes = driver.find_elements(By.TAG_NAME, "iframe")
# print("Total iframes:", len(iframes))




from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.google.com")   # Change URL

time.sleep(3)  # Allow page to load

google_iframes = []

for frame in driver.find_elements(By.TAG_NAME, "iframe"):
    src = frame.get_attribute("src")
    if src and "google.com" in src:
        google_iframes.append(frame)

print("Google.com iframes:", len(google_iframes))

# Optional: print their URLs
for g in google_iframes:
    print(g.get_attribute("src"))

driver.quit()



# google_iframes = []
#
# for frame in driver.find_elements(By.TAG_NAME, "iframe"):
#     src = frame.get_attribute("src")
#     if src and "google" in src:
#         google_iframes.append(frame)
#
# print("Google-related iframes:", len(google_iframes))
