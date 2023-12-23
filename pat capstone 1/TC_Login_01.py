from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException


class Guvi:
   def __init__(self):
       self.url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
       self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

   def login(self):
       try:
           self.driver.get(self.url)
           sleep(10)
           self.driver.find_element(by=By.XPATH, value='//form/div[1]/div/div[2]/input[@name="username"]').send_keys("Admin")
           self.driver.find_element(by=By.XPATH, value='//form/div[2]/div/div[2]/input').send_keys("admin123")
           self.driver.find_element(by=By.XPATH, value='//form/div[3]/button').click()
       except NoSuchElementException as selenium_error:
           print(selenium_error)
       finally:
           self.driver.close()


suman = Guvi()


suman.login()