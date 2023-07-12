from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

import github_userinfo

driver = webdriver.Chrome()

#---------1------------Simple Usage of selenium webdriver
"""
url = 'http://www.github.com/'
driver.get(url)
#print(driver.page_source)
time.sleep(2)
driver.maximize_window()
driver.save_screenshot("github.com-hompage.png")
url = "https://github.com/129yildirim"
driver.get(url)
print(driver.title)
time.sleep(2)
driver.close()
"""
#------------2----------Working with selectors
"""
url = 'http://www.github.com/'
driver.get(url)
time.sleep(1)
driver.maximize_window()
time.sleep(1)
#search_input = driver.find_element(By.NAME, "q")
search_input = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/header/div/div[2]/div/div/div[1]/div/div/form/label/input[1]")
search_input.send_keys('Python')
time.sleep(2)
search_input.send_keys(Keys.ENTER)
time.sleep(2)

result = driver.find_elements(By.CSS_SELECTOR, ".repo-list .d-flex a")
for element in result:
    print('element text: ', element.text)
"""


#Getting the followers on out github account
url = 'http://www.github.com/'
driver.get(url)#open github page
driver.maximize_window()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/header/div/div[2]/div/div/div[2]/a").click()#sign in button
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="login_field"]').send_keys(github_userinfo.username)#username
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(github_userinfo.password)#password
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="login"]/div[4]/form/div/input[13]').click()#log in into the account
time.sleep(1)

followers_url = 'https://github.com/' + github_userinfo.username + '?tab=followers'
driver.get(followers_url)#open followers page
time.sleep(2)
followers = driver.find_elements(By.CSS_SELECTOR, '#user-profile-frame span.f4.Link--primary')#find all the names of followers
for item in followers:
    print('Follower:', item.text)#print each follower's name
time.sleep(2)

driver.close()
