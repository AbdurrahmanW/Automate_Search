from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.google.com/")
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[2]/div[2]/input").send_keys("Elephant" + Keys.ENTER)
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[7]/div/div[4]/div/div[1]/div/div[1]/div/div[2]/a").click()
time.sleep(5)
driver.close()
print ("SUCCESS find image of Elephant")