import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element(By.NAME, "email").send_keys("xyz@gmail.com")
driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys("12345")
driver.find_element(By.XPATH, "//input[@type ='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert").text
print(message)
assert "Success" in message

print(driver.current_url)
print(driver.title)

time.sleep(2)