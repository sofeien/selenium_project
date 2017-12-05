from selenium import webdriver
from selenium.webdriver.common.by import By
import os

file_path = "file:///"+os.path.abspath("index.html")
driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get(file_path)
driver.find_element(By.CSS_SELECTOR,"#s > option:nth-child(3)").click()
