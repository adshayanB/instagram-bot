from selenium import webdriver
from time import sleep


class InstaBot:
    def __init__(self,username,password):
        self.driver = webdriver.Chrome('/Users/abalendra/Downloads/chromedriver')
        self.driver.get('https://instagram.com')
        sleep(4)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[2]/p/a").click()
        sleep(4)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(password)
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        print("Logged in")
        sleep(4)
    def follow (self, account_name):
        self.driver.get(f'https://instagram.com/{account_name}')
        sleep(4)
        follow_button = self.driver.find_element_by_css_selector('button')
        if(follow_button.text !='Following'):
            follow_button.click()
            print(f'You are now following {account_name}')
            sleep(4)
        else:
            print(f"You are already following {account_name}")
    def unfollow (self, account_name):
        self.driver.get(f'https://instagram.com/{account_name}')
        sleep(2)
        follow_button = self.driver.find_element_by_css_selector('button')
        if(follow_button.text =='Following'):
            follow_button.click()
            confirmButton = self.driver.find_element_by_xpath('//button[text() = "Unfollow"]')
            confirmButton.click()
            print(f'Sucessfully unfollowed {account_name}')
        else:
            print(f"You don't follow {account_name}")
        sleep(2)

    def close (self):
        self.driver.quit()




user = input("Enter your instagram account: ")
password = input("Enter your instagram password: ")
account_follow = input("Enter the account name you would like to follow: ")
account_unfollow = input("Enter the account you would like to unfollow: ")

acc = InstaBot(user,password)
acc.follow(account_follow)
acc.unfollow(account_unfollow)
acc.close()

