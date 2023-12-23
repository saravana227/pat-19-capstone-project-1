from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OrangeHRMActions:
    def __init__(self):
        self.url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    def login(self):
        self.driver.get(self.url)
        sleep(4)
        self.driver.find_element(by=By.XPATH, value='//form/div[1]/div/div[2]/input[@name="username"]').send_keys("Admin")
        self.driver.find_element(by=By.XPATH, value='//form/div[2]/div/div[2]/input').send_keys("admin123")
        self.driver.find_element(by=By.XPATH, value='//form/div[3]/button').click()

    def navigate_to_pim_module(self):
        sleep(5)
        pim_module = self.driver.find_element(by=By.XPATH, value='/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span')
        pim_module.click()

    def delete_employee(self):
        sleep(5)
        self.driver.find_element(by=By.XPATH, value='/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[9]/div/button[1]/i').click()
    
    def click_delete(self):
        sleep(5)
        self.driver.find_element(by=By.XPATH, value='/html/body/div/div[3]/div/div/div/div[3]/button[2]').click()

    def close_browser(self):
        sleep(5)
        self.driver.quit()

SK = OrangeHRMActions()

SK.login()

SK.navigate_to_pim_module()

SK.delete_employee()

SK.click_delete()

SK.close_browser()
