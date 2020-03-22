from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

class Instagram():
    def __init__(self, user, pw, path_to_csv):
        self.user = user
        self.pw = pw
        self.path_to_csv = path_to_csv
        self.driver = webdriver.Chrome()

    #Connect to Instagram
    def _login(self):
        self.driver.implicitly_wait(10)
        site = 'http://instagram.com/accounts/login'
        
        self.driver.get(site)

        username = self.driver.find_element_by_name('username')
        password = self.driver.find_element_by_name('password')
        #Input Username and Password
        username.send_keys(self.user)
        password.send_keys(self.pw)
        password.submit()

    def _follow(self, fol=True):
        with open(self.path_to_csv) as insta:
            array = insta.readlines()
        array = [x.strip() for x in array]
        l = list(filter(len, array))
        for name in l:
            if (name[0] == '@'):
                name = name[1:]
            self.driver.get('https://www.instagram.com/' + name)
            if fol:
                t = "Follow"
            else:
                t = "Following"

            try:
                button = self.driver.find_element_by_xpath("//*[text()='{0}']".format(t))
                button.click()
                if not fol:
                    button = self.driver.find_element_by_xpath("//*[text()='{0}']".format('Unfollow'))
                    button.click()
                if fol:
                    print ('Followed ' + name)
                else:
                    print ("Unfollowed " + name) 

            except Exception as e:
                if fol:
                    print ('Already Following ' + name)
                else:
                    try:
                        button = self.driver.find_element_by_xpath("//*[text()='{0}']".format("Requested"))
                        button.click()
                        button = self.driver.find_element_by_xpath("//*[text()='{0}']".format('Unfollow'))
                        button.click()
                    except Exception as e:
                        pass
                    print ("Already not following " + name)
            

        print ('List successfully completed')
        time.sleep(5)
        # self.driver.close()
