import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import sys


def print_same_line(text):
    sys.stdout.write('\r')
    sys.stdout.flush()
    sys.stdout.write(text)
    sys.stdout.flush()


class InstaThot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome('./chromedriver')

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get('http://www.instagram.com/')
        time.sleep(5)
        login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        login_button.click()
        time.sleep(2)
        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        passworword_elem = driver.find_element_by_xpath("//input[@name='password']")
        passworword_elem.clear()
        passworword_elem.send_keys(self.password)
        passworword_elem.send_keys(Keys.RETURN)
        time.sleep(2)

    def like_photo(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(5 + random.randint(2, 4))

        # gathering photos
        pic_hrefs = []
        for i in range(1, 7):
            try:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(5 + random.randint(2, 4))
                # get tags
                hrefs_in_view = driver.find_elements_by_tag_name('a')
                # finding relevant hrefs
                hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view
                                 if '.com/p/' in elem.get_attribute('href')]
                # building list of unique photos
                [pic_hrefs.append(href) for href in hrefs_in_view if href not in pic_hrefs]
                # print("Check: pic href length " + str(len(pic_hrefs)))
            except Exception:
                continue

        # Liking photos
        unique_photos = len(pic_hrefs)
        for pic_href in pic_hrefs:
            driver.get(pic_href)
            time.sleep(5 + random.randint(2, 4))
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                time.sleep(5 + random.randint(2, 4))
                like_button = lambda: driver.find_element_by_xpath('//span[@aria-label="Like"]').click()
                like_button().click()
                for second in reversed(range(0, random.randint(18, 28))):
                    print_same_line(
                        "#" + hashtag + ': unique photos left: ' + str(unique_photos) + " | Sleeping " + str(second))
                    time.sleep(5 + random.randint(2, 4))
            except Exception as e:
                time.sleep(5)
            unique_photos -= 1

if __name__ == "__main__":

    username = "USERNAME"
    password = "PASSWORD"

    caitlinjillybelleIG = InstaThot("caitlinjillybelle", "Coffeeandgold28")
    caitlinjillybelleIG.login()

    hashtags = ['amazing', 'beautiful', 'adventure', 'photography', 'nofilter',
                'instaart', 'artsy', 'l4l', 'newzealand', 'artist', 'fun', 'happy',
                'art', 'nzart', 'me', 'art', 'botanical', 'oilpaint', 'cinema',
                'love', 'instaart', 'instagood', 'followme', 'watercolour', 'illustration', 'family',
                'aotearoa', 'botanicalillustration', 'beauty', 'artstudio', 'pretty', 'vintage', 'nz', 'nature']

    while True:
        try:
            # Choose a random tag from the list of tags
            tag = random.choice(hashtags)
            caitlinjillybelleIG.like_photo(tag)
        except Exception:
            caitlinjillybelleIG.closeBrowser()
            time.sleep(60)
            caitlinjillybelleIG = InstaThot("caitlinjillybelle", "Coffeeandgold28")
            caitlinjillybelleIG.login()

# testing webdriver
# browser = webdriver.Chrome('./chromedriver')
# browser.get('http://www.instagram.com/')
# browser.quit()