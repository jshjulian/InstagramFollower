from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
#Find my password
user= "USERNAME"
pw = "PASSWORD"
#Find List of Instagram Names
dir = r'directory of list of names'
with open(dir) as insta:
    array = insta.readlines()
array = [x.strip() for x in array]
list = list(filter(len, array))
#Connect to Instagram
site = 'http://instagram.com/accounts/login'
driver = webdriver.Chrome()
driver.get(site)

username = driver.find_element_by_name('username')
password = driver.find_element_by_name('password')
#Input Username and Password
username.send_keys(user)
password.send_keys(pw)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/span/button').click()

for name in list:
    if (name[0] == '@'):
        name = name[1:]
    driver.get('https://www.instagram.com/' + name)
    try:
        button = driver.find_element_by_xpath("//button[@class='_qv64e _gexxb _r9b8f _njrw0']")
        print (button.text)
        if button.text == 'Follow':
            button.click()
            print ('Followed ' + name)
        else:
            print ('Already Following ' + name)
    except NoSuchElementException:
            print ('Already Following ' + name)

print ('List successfully completed')
time.sleep(5)
driver.close()
