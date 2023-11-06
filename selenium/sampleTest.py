from selenium import webdriver
import time
from selenium.webdriver.common.by import By

print("Test Execution Started")
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Remote( command_executor='http://localhost:4444', options=options)
print("Test Execution Started 2nd time")
driver.get("https://www.google.com/")
time.sleep(5)
driver.get("https://www.bing.com/")
time.sleep(5)
driver.close()
driver.quit()
print("Test Execution Successfully Completed!")