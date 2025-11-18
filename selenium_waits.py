from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time


def implicit_wait_demo(driver):
    print("\n--- Implicit Wait Demo ---")
    # This sets a global implicit wait for all find_element calls
    driver.implicitly_wait(10)
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
    print("Opened dynamic loading (1). Clicking Start (implicit)...")
    driver.find_element(By.CSS_SELECTOR, "#start button").click()

    try:
        # implicit wait will make find_element block up to 10s until element exists
        elem = driver.find_element(By.CSS_SELECTOR, "#finish h4")
        print("Element text (implicit):", elem.text)
    except NoSuchElementException:
        print("Element not found using implicit wait")


def explicit_wait_demo(driver):
    print("\n--- Explicit Wait Demo ---")
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
    driver.find_element(By.CSS_SELECTOR, "#start button").click()
    try:
        # Explicit wait: wait until the element becomes visible (up to 15s)
        wait = WebDriverWait(driver, 15)
        elem = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish h4")))
        print("Element text (explicit):", elem.text)
    except TimeoutException:
        print("Timed out waiting for element (explicit)")


def fluent_wait_demo(driver):
    print("\n--- Fluent Wait Demo ---")
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    driver.find_element(By.CSS_SELECTOR, "#start button").click()

    # WebDriverWait supports polling frequency and ignored_exceptions -> fluent behavior
    wait = WebDriverWait(driver, timeout=20, poll_frequency=0.5, ignored_exceptions=[NoSuchElementException])
    try:
        elem = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish h4")))
        print("Element text (fluent):", elem.text)
    except TimeoutException:
        print("Timed out waiting for element (fluent)")


def main():
    # Create Chrome driver (ensure chromedriver is on PATH or adjust executable_path)
    driver = webdriver.Chrome()
    try:
        implicit_wait_demo(driver)
        time.sleep(2)
        explicit_wait_demo(driver)
        time.sleep(2)
        fluent_wait_demo(driver)

    except Exception as e:
        print("An unexpected error occurred:", type(e).__name__, str(e))

    finally:
        print("\nDemos finished — closing browser in 5 seconds...")
        time.sleep(5)
        driver.quit()


if __name__ == "__main__":
    main()
