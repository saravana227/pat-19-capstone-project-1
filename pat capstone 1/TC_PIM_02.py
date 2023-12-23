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

    def edit_existing_employee(self):
        sleep(5)
        self.driver.find_element(by=By.XPATH, value='/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[4]/div/div[9]/div/button[2]/i').click()

    def edit(self):
        sleep(5)
        self.driver.find_element(by=By.XPATH, value='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input').send_keys('antony')
        self.driver.find_element(by=By.XPATH, value='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/input').send_keys('arnold')

    def click_save(self):
        sleep(5)
        self.driver.find_element(by=By.XPATH, value='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[2]/button').click()

    def close_browser(self):
        sleep(5)
        self.driver.quit()

SK = OrangeHRMActions()

SK.login()

SK.navigate_to_pim_module()

SK.edit_existing_employee()

SK.edit()

SK.click_save()

SK.close_browser()