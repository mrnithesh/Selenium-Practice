from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.amazon.in")
time.sleep(5)
signin = driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div[3]/div/div[2]/a")
signin.click()
time.sleep(2)
uname = driver.find_element(By.NAME,"email")
uname.send_keys("phone/email")
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/div/div/div/span/form/span/span/input").click()
time.sleep(5)

driver.find_element(By.NAME,"password").send_keys("passwordhere")
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[2]/div/form/div/div[2]/span/span/input").click()
time.sleep(5)

search = driver.find_element(By.NAME,"field-keywords")
search.send_keys("macbook air m4")
search.send_keys(Keys.RETURN)
time.sleep(5)

driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/span/div/div/div/div[2]/div/div/div[1]/a").click()
time.sleep(5)

driver.switch_to.window(driver.window_handles[1])
time.sleep(10)

driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[5]/div[1]/div[4]/div/div[1]/div/div[1]/div/div/div[2]/div/div[2]/div/form/div/div/div[40]/div[1]/span/span/span/input").click()
time.sleep(10)

driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[5]/div[1]/div[10]/div/div[2]/div[2]/div/div[1]/div[3]/a").click()
time.sleep(5)


driver.find_element(By.XPATH,"/html/body/div[2]/header/div[1]/div[1]/div[3]/div/a[2]").click()
time.sleep(10)
driver.quit()