
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Check_box:
    def __init__(self):
        self.driver = None

    def box(self,url):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.driver.maximize_window()
        check_input = self.driver.find_element(By.XPATH,'//*[@id="__next"]/div/main/div/section[2]/div/ul/li[9]/a')
        check_input.click()
        single_input = self.driver.find_element(By.XPATH,'//*[@id="__next"]/div/main/div/section/div/div/div[1]/label/input')
        single_input.click()

        checked_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div/main/div/section/div/div/div[1]/p'))
        )

        assert checked_message.text == "Checked!"

        disable_input = self.driver.find_element(By.XPATH,'//*[@id="__next"]/div/main/div/section/div/div/div[2]/div/label[1]/input')
        disable_input.click()
        disable_input2 =self.driver.find_element(By.XPATH,'//*[@id="__next"]/div/main/div/section/div/div/div[2]/div/label[2]/input')
        disable_input2.click()


check_box = Check_box()
driver = webdriver.Chrome()
url = "https://www.testmuai.com/selenium-playground/"
check_box.box(url)