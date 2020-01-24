from selenium import webdriver
from time import sleep


class InstaBot:
    def __init__(self,username,password):
        self.driver = webdriver.Chrome('/Users/abalendra/Downloads/chromedriver')
        self.driver.get('https://instagram.com')
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[2]/p/a").click()
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(password)
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        print("Logged in")
        sleep(2)
    def follow (self, account_name):
        self.driver.get(f'https://instagram.com/{account_name}')
        sleep(2)
        follow_button = self.driver.find_element_by_css_selector('button')
        if(follow_button.text !='Following'):
            follow_button.click()
            print(f'You are know following {account_name}')
            sleep(2)
        else:
            print(f"Your already following {account_name}")

















acc = InstaBot('instagram_username','instagram_password')
acc.follow('username_of_account_you_want_to_follow')