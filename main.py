from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("http://localhost/")

input_element_username = driver.find_element(By.ID,"username")
input_element_password = driver.find_element(By.ID,"password")
input_element_username.send_keys("supervisor")
input_element_password.send_keys("1" + Keys.ENTER)


WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="main-menu"]/li[4]/a')
    )
).click()


time.sleep(10)

driver.quit()

