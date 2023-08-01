from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

EMAIL = "rajpurohitvijesh7401@gmail.com"
PASSWORD = "Alex7401"
chrome_driver_path = "F:\software\chrome drive\chromedriver"
ACCOUNT_ID = "alex.advent"


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.driver.get("https://www.instagram.com/")

    def login(self):
        # authentication login
        self.email_section = self.driver.find_element_by_name("username")
        self.email_section.send_keys(EMAIL)
        self.password_section = self.driver.find_element_by_name("password")
        self.password_section.send_keys(PASSWORD)
        self.password_section.send_keys(Keys.RETURN)

    def search(self):
        self.search = self.driver.find_element_by_class_name("XTCLo")
        self.search.send_keys(ACCOUNT_ID)
        self.search.send_keys(Keys.RETURN)
        sleep(1)
        self.select_user = self.driver.find_element_by_css_selector("._01UL2 a")
        self.select_user.click()
        sleep(2)
        self.follow_select = self.driver.find_elements_by_class_name("-nal3")
        self.follow_select[1].click()
        sleep(1)

    def follow(self):
        self.run = True
        modal = self.driver.find_element_by_class_name("isgrP")
        # modal = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')
        self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
        # self.scroll = self.driver.find_element_by_class_name("isgrP")
        # self.scroll.send_keys(Keys.END)
        while self.run:
            self.select_user = self.driver.find_elements_by_css_selector(".y3zKF")
            if len(self.select_user) == 0:
                print("in zero")
                modal = self.driver.find_element_by_class_name("isgrP")
                self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
                sleep(1)
            else:
                for i in self.select_user:
                    i.click()
                    sleep(1)
