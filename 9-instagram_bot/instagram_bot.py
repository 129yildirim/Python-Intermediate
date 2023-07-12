from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from instagram_info import username, password


class Instagram:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
    def log_in(self, url):
        self.browser.get(url)
        time.sleep(2)
        self.browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(self.username)
        self.browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(self.password)
        time.sleep(2)
        self.browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').click()
        time.sleep(10)
    def getFollowers(self):
        #profile page
        profile_url = f'https://www.instagram.com/{self.username}/'
        self.browser.get(profile_url)
        time.sleep(5)
        #getting the followers section
        tabs = self.browser.find_elements(By.CSS_SELECTOR, 'ul.x78zum5.x1q0g3np.xieb3on li a')
        for tab in tabs:
            text = tab.text
            if text.__contains__('followers'):
                followers_button = tab
                break
        followers_button.click()
        time.sleep(5)

        #current followers
        followers = self.browser.find_elements(By.CSS_SELECTOR, 'div._aano .xt0psk2 a[role=link]')
        count = len(followers)
        print(f'count:{count}')
        #pressing the TAB key 2 times to get to the scrollable section
        action = webdriver.ActionChains(self.browser)
        action.key_down(Keys.TAB).key_up(Keys.TAB).perform()
        time.sleep(1)
        action.key_down(Keys.TAB).key_up(Keys.TAB).perform()
        time.sleep(1)
        #scroll down(press END key) until you can see all of the followers
        while(True):
            action.key_down(Keys.END).key_up(Keys.END).perform()
            time.sleep(3)
            newCount = len(self.browser.find_elements(By.CSS_SELECTOR, 'div._aano .xt0psk2 a[role=link]'))
            if count != newCount:
                count = newCount
                print(f'count again:{count}')
                time.sleep(1)
            else:
                followers = self.browser.find_elements(By.CSS_SELECTOR, 'div._aano .xt0psk2 a[role=link]')
                break

        print(f'final count: {len(followers)}')
        print('Followers:')
        for follower in followers:
            print(follower.get_property('href'))

instagram = Instagram(username, password)
instagram.log_in('https://www.instagram.com/')
instagram.getFollowers()
        
