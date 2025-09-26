from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")
search_box = driver.find_element(By.NAME,"q")

search_box.send_keys("Nithesh codes"+ Keys.RETURN)
time.sleep(3)
print(f"Page title after search: {driver.title}")

driver.quit()