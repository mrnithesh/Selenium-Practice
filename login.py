from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")

uname = driver.find_element(By.NAME,"username")
pwd = driver.find_element(By.NAME,"password")

uname.send_keys("tomsmith")
time.sleep(2)
pwd.send_keys("SuperSecretPassword!")
time.sleep(2)
submit = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/form/button")
submit.click()

time.sleep(5)
driver.quit()