from selenium import webdriver
from selenium.webdriver.common.by import By

class form_submit:
    def __init__(self):
        self.driver = None

    def ajax_form(self,driver):
        self.driver = driver
        self.driver.maximize_window()

    def ajax_submit(self,url):
        self.driver.get(url)
        title_click_input = self.driver.find_element(By.XPATH,'//*[@id="__next"]/div/main/div/section[2]/div/ul/li[1]/a')
        title_click_input.click()
        name_input = self.driver.find_element(By.ID,'title')
        name_input.send_keys("welcome to test")
        message_input = self.driver.find_element(By.ID,'description')
        message_input.send_keys("1st session start soon")
        submit_button = self.driver.find_element(By.ID,'btn-submit')
        submit_button.click()


driver = webdriver.Chrome()
form_submit = form_submit()
form_submit.ajax_form(driver)
url = "https://www.testmuai.com/selenium-playground/"
form_submit.ajax_submit(url)