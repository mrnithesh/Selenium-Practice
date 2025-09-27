from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(5)
username = driver.find_element(By.NAME, "username")
username.send_keys("Admin")
time.sleep(2)
password = driver.find_element(By.NAME, "password")
password.send_keys("admin123")
time.sleep(2)
login_button = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")
login_button.click()

time.sleep(5)

driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a").click()
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button").click()
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/input").send_keys("Nick Fury")
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input").send_keys("Fury")
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input").send_keys("WakandaForever@123")
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input").send_keys("WakandaForever@123")
time.sleep(10)

driver.quit()