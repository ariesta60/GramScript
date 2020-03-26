# VERSION 0.1.9.2

from art import *
import pandas as pd
import random
from random import randint
from time import sleep, strftime
import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import ui
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from tqdm import tqdm
from tqdm import tqdm_gui
import sys
sys.path.insert(0, './utils/')
import secret
import hashtags
import limits
import proxy
import config
import userlist
import warnings
import datetime







tprint("GramScript")
sleep(0.5)
print("Made with Selenium")
sleep(0.5)
print("Version 0.1.9.2")
print("Loading Scripts...")
time_start = datetime.datetime.now()
for i in tqdm(range(6)):
    sleep(0.05)
    pass

def proxy():
    global webdriver
    global stories_watched
    use_proxy = input("Do you want to use a proxy? [y/n]: ")

    if use_proxy == "y":
        use_proxy_config = input("Do you want to use the proxy config file? [y/n]: ")
        if use_proxy_config == "n":
            proxy_type = input("IP:PORT only? [y/n]: ")
            if proxy_type == "n":
                proxy_username = input("Enter your proxy username: ")
                proxy_password = input("Enter your proxy passowrd: ")
                proxy_host = input("Enter your proxy host (ip:port): ")
                from selenium.webdriver.firefox.options import Options
                from seleniumwire import webdriver
                #options = webdriver.ChromeOptions()

                options = {
                    'proxy': {
                        'http': 'http://{}:{}@{}'.format(proxy_username, proxy_password, proxy_host),
                        'https': 'https://{}:{}@{}'.format(proxy_username, proxy_password, proxy_host)
                        }
                }
                ##options.add_argument("--mute-audio")
                warnings.filterwarnings("ignore", category=DeprecationWarning) 
                profile = webdriver.FirefoxProfile()
                profile.set_preference("media.volume_scale", "0.0")
                if config.data_save_mode == "true":
                    profile.set_preference("permissions.default.image", 2)
                    print("Data Save mode - Active")
                else:
                    pass
                ##webdriver = webdriver.Chrome(seleniumwire_options=options, chrome_options=options, executable_path='./chromedriver')
                webdriver = webdriver.Firefox(seleniumwire_options=options, firefox_options=options, executable_path="./geckodriver", firefox_profile=profile)
                sleep(2)
                webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
                sleep(3)
            else:
                proxy_host = input("Enter your proxy IP:PORT: ")
                from selenium.webdriver.firefox.options import Options
                #options = webdriver.ChromeOptions()

                warnings.filterwarnings("ignore", category=DeprecationWarning) 
                options.add_argument('--proxy-server={}'.format(proxy_host))
                ##options.add_argument("--mute-audio")
                profile = webdriver.FirefoxProfile()
                profile.set_preference("media.volume_scale", "0.0")
                if config.data_save_mode == "true":
                    profile.set_preference("permissions.default.image", 2)
                    print("Data Save mode - Active")
                else:
                    pass
                ##webdriver = webdriver.Chrome(chrome_options=options, executable_path='./chromedriver')
                webdriver = webdriver.Firefox(firefox_options=options, executable_path="./geckodriver", firefox_profile=profile)
                sleep(2)
                webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
                sleep(3)
        else:
            proxy_type = input("IP:PORT only? [y/n]: ")
            if proxy_type == "n":
                from selenium.webdriver.firefox.options import Options
                from seleniumwire import webdriver
                #options = webdriver.ChromeOptions()

                options = {
                    'proxy': {
                        'http': 'http://{}:{}@{}'.format(proxy.proxy_username, proxy.proxy_password, proxy.proxy_host),
                        'https': 'https://{}:{}@{}'.format(proxy.proxy_username, proxy.proxy_password, proxy.proxy_host)
                        }
                }
                ##options.add_argument("--mute-audio")
                warnings.filterwarnings("ignore", category=DeprecationWarning) 
                profile = webdriver.FirefoxProfile()
                profile.set_preference("media.volume_scale", "0.0")
                if config.data_save_mode == "true":
                    profile.set_preference("permissions.default.image", 2)
                    print("Data Save mode - Active")
                else:
                    pass
                ##webdriver = webdriver.Chrome(seleniumwire_options=options, chrome_options=options, executable_path='./chromedriver')
                webdriver = webdriver.Firefox(seleniumwire_options=options, firefox_options=options, executable_path="./geckodriver", firefox_profile=profile)
                sleep(2)
                webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
                sleep(3)
            else:
                #options = webdriver.ChromeOptions()

                warnings.filterwarnings("ignore", category=DeprecationWarning) 
                options.add_argument('--proxy-server={}'.format(proxy.proxy_host))
                ##options.add_argument("--mute-audio")
                profile = webdriver.FirefoxProfile()
                profile.set_preference("media.volume_scale", "0.0")
                ##webdriver = webdriver.Chrome(chrome_options=options, executable_path='./chromedriver')
                webdriver = webdriver.Firefox(firefox_options=options, executable_path="./geckodriver", firefox_profile=profile)
                sleep(2)
                webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
                sleep(3)
    else:
        profile = webdriver.FirefoxProfile()
        profile.set_preference("media.volume_scale", "0.0")
        if config.data_save_mode == "true":
            profile.set_preference("permissions.default.image", 2)
            print("Data Save mode - Active")
        else:
            pass
        ##options = webdriver.ChromeOptions()
        ##options.add_argument("--mute-audio")
        ##webdriver = webdriver.Chrome(executable_path='./chromedriver')
        webdriver = webdriver.Firefox(executable_path="./geckodriver", firefox_profile=profile)
        sleep(2)
        webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        sleep(3)

def login():
    username = webdriver.find_element_by_name('username')
    username.send_keys(secret.username)
    password = webdriver.find_element_by_name('password')
    password.send_keys(secret.password)
    sleep(2)
    button_login = webdriver.find_element_by_xpath(
        '/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button')
    button_login.click()
    sleep(10)

    try:
        notnow = webdriver.find_element_by_css_selector(
            'button.aOOlW:nth-child(2)')
        notnow.click()  # comment these last 2 lines out, if you don't get a pop up asking about notifications
    except NoSuchElementException:
        pass


def story_from_followers():
    num = 0
    for user in userlist.users:
        sleep(2)
        webdriver.get('https://www.instagram.com/' +
                    userlist.users[num] + '/')
        sleep(5)
        print("Getting followers with Stories to watch from: {}".format(userlist.users[num]))
        num += 1
        sleep(1)
        followers_list__open = webdriver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a')
        followers_list__open.click()
        sleep(2)

        fBody  = webdriver.find_element_by_xpath("//div[@class='isgrP']")
        scroll = 0
        while scroll < limits.scroll_amount: # scroll 5 times
            webdriver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
            sleep(2)
            scroll += 1

        fList  = webdriver.find_elements_by_xpath("//div[@class='isgrP']//li")

        wbList = webdriver.find_elements_by_xpath("//div[@class='RR-M- h5uC0 SAvC5']")
        print("Users found with Story to watch: {}".format(len(wbList)))
        story_watching_done = 'false'
        stories_next_watch = "true"
        story_watching_counter = 0
        stories_bf_watched = 1

        try:
            for user_story in wbList:
                while story_watching_done == 'false':
                    stories_next_watch = "true"
                    wbList = webdriver.find_elements_by_xpath("//div[@class='RR-M- h5uC0 SAvC5']")
                    webdriver.execute_script("arguments[0].scrollIntoView();", wbList[story_watching_counter])
                    wbList[story_watching_counter].click()
                    while stories_next_watch == "true":
                        try:
                            sleep(randint(2, 3))
                            webdriver.implicitly_wait(2)
                            watch_all_stories_next = webdriver.find_element_by_css_selector(".ow3u_").click()
                            stories_bf_watched += 1
                            print("Stories watched from followers: {}".format(stories_bf_watched))
                        except (NoSuchElementException, StaleElementReferenceException) as e:
                            stories_next_watch = "false"

                    else:
                        try:
                            watch_all_stories_close_from_followers = webdriver.find_element_by_xpath("/html/body/div[1]/section/div/div/section/div[2]/button[3]/div")
                            watch_all_stories_close_from_followers.click()
                        except NoSuchElementException:
                            pass
                        wbList = webdriver.find_elements_by_xpath("//div[@class='RR-M- h5uC0 SAvC5']")
                        story_watching_counter += 1
                        sleep(1)
                else:
                    pass
        except IndexError as error:
            print("Index Error..")
            print("Moving to next user...")
            pass
    else:
        pass

def story_from_feed():
    stories_watched = -1
    total_stories_watched = 0

    webdriver.get('https://www.instagram.com/')



    sleep(2)
    try:
        watch_all_stories_btn = webdriver.find_element_by_xpath(
            "/html/body/div[1]/section/main/section/div[3]/div[2]/div[1]/a/div")
        watch_all_stories_btn.click()
        sleep(2)
    except NoSuchElementException:
        stories_watched =+ limits.max_stories
        stories_watched += 1

    while stories_watched <= limits.max_stories:
        try:
            watch_all_stories_next = webdriver.find_element_by_css_selector(".ow3u_")
            watch_all_stories_next.click()
            sleep(randint(2, 3))
            stories_watched += 1
            total_stories_watched += 1
            print("stories watched: {}".format(stories_watched))
        except NoSuchElementException:
            stories_watched += limits.max_stories
            stories_watched += 1
    else:
        try:
            watch_all_stories_close = webdriver.find_element_by_xpath("/html/body/div[1]/section/div/div/section/div[2]/button[3]/div/span")
            watch_all_stories_close.click()
        except NoSuchElementException:
            pass
        sleep(1)
def follow_suggestions():
    suggestions_counter = 1
    total_suggestion_followed = 0
    try:
        suggestions_all_btn = webdriver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[3]/div[1]/a")
        suggestions_all_btn.click()
        sleep(3)
        while suggestions_counter <= limits.max_follow_suggestion:
            suggestions_follow_btn = webdriver.find_element_by_css_selector("div.XfCBB:nth-child({0}) > div:nth-child(3) > button:nth-child(1)".format(suggestions_counter))
            suggestions_follow_btn.click()
            print("suggestions followed: {}".format(suggestions_counter))
            suggestions_counter += 1
            total_suggestion_followed += 1
            sleep(randint(5, 15))
        else:
            print("total number of users being followed: {}".format(suggestions_counter))
            pass
    except NoSuchElementException:
        pass
def like():
    tag = -1
    likes = 0
    total_likes = 0
    for hashtag in hashtags.hashtag_list:
        sleep(2)
        tag += 1
        webdriver.get('https://www.instagram.com/explore/tags/' +
                    hashtags.hashtag_list[tag] + '/')
        image_img=webdriver.find_element_by_xpath(
            '/html/body/div[1]/section/main/article/div[2]/div/div[1]/div[1]')
        sleep(1)
        image_img.click()
        sleep(1)
        
        
        while likes <= limits.max_likes:
            sleep(1)
            print("trying to like image...")
            sleep(1)
            try:
                image_like_svg=webdriver.find_element_by_css_selector(
                    '.fr66n > button:nth-child(1) > svg:nth-child(1)')
                image_like_label=image_like_svg.get_attribute("aria-label")
                if image_like_label == "Like":
                    image_like_svg.click()
                    likes += 1
                    total_likes += 1
                    print('liked images: {}'.format(likes))
                    sleep(randint(5, 15))  # random timer here
                    image_next=webdriver.find_element_by_xpath(
                        '/html/body/div[4]/div[1]/div/div/a[2]')
                    image_next.click()
                    sleep(randint(3, 4))  # random timer here
                else:
                    sleep(2)
                    print('image already liked by {}'.format(secret.username))
                    image_next=webdriver.find_element_by_xpath(
                        '/html/body/div[4]/div[1]/div/div/a[2]')
                    image_next.click()
                    sleep(2)  # random timer here
            except NoSuchElementException:
                try:
                    print('error loading image...')
                    sleep(2)
                    image_next=webdriver.find_element_by_xpath(
                            '/html/body/div[4]/div[1]/div/div/a[2]')
                    image_next.click()
                    sleep(2)  # random timer here
                except NoSuchElementException:
                    print('no more images...')
                    sleep(2)
                    likes += limits.max_likes

        else:
            likes = 0
            tag = -1
            print('finished like process')
            print('total liked images: {}'.format(likes))
            sleep(2)
            print('moving on to the next process...')
            image_close=webdriver.find_element_by_xpath(
                '/html/body/div[4]/div[3]/button')
            sleep(2)
            image_close.click()
            sleep(2)
        
def comment():
    tag = -1
    comments = 0
    total_comments = 0
    for hashtag in hashtags.hashtag_list:
        sleep(2)
        tag += 1
        webdriver.get('https://www.instagram.com/explore/tags/' +
                    hashtags.hashtag_list[tag] + '/')
        image_img=webdriver.find_element_by_xpath(
            '/html/body/div[1]/section/main/article/div[2]/div/div[1]/div[1]')
        sleep(1)
        image_img.click()
        sleep(1)

        while comments <= limits.max_comments:  
            all_comments = []
            comment_by_user = webdriver.find_elements_by_class_name('ZIAjV')
            
            for i in comment_by_user:
                all_comments.append(i.get_attribute('innerText'))
            try:
                comment_allowed = webdriver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/div[3]/div")
                if (comment_allowed.text == "Comments on this post have been limited."):
                    sleep(2)
                    image_next=webdriver.find_element_by_xpath(
                    '/html/body/div[4]/div[1]/div/div/a[2]')
                    image_next.click()
                    print("Media does not allow comments")
                    sleep(2)
            except NoSuchElementException:
                pass
            if any(x == secret.username for x in all_comments):
                sleep(2)
                image_next=webdriver.find_element_by_xpath(
                '/html/body/div[4]/div[1]/div/div/a[2]')
                image_next.click()
                sleep(2)
            else:
                print("no comment by {}".format(secret.username))
                sleep(2)
                comment_list=['nice one 👍🏼', 'great! 🚀', 'Amazing 😍', 'Looking great!', 'so cool!!! 😳', '🔥🔥🔥🔥', '😍😍😍', '🧬 Great Stuff!!']
                comment_item=random.choice(comment_list)

                sleep(randint(2, 5))  # random timer here

                comment_box=ui.WebDriverWait(webdriver, 10).until(EC.element_to_be_clickable(
                    (By.XPATH, "/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea")))
                sleep(1)
                webdriver.execute_script(
                    "arguments[0].scrollIntoView(true);", comment_box)

                (
                    ActionChains(webdriver)
                    .move_to_element(comment_box)
                    .click()
                    .send_keys(comment_item)
                    .perform()
                )

                sleep(2)

                send_comment=webdriver.find_element_by_xpath(
                    "/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/button")
                send_comment.click()
                comments += 1
                total_comments += 1
                print('images commented: {}'.format(comments))
                sleep(25)
                sleep(randint(5, 10))  # random timer here
                image_next=webdriver.find_element_by_xpath(
                '/html/body/div[4]/div[1]/div/div/a[2]')
                image_next.click()
                sleep(1)
        comments=0
    else:
        pass
def report():
    print("Script finished!")
    time_end = datetime.datetime.now()
    sleep(1)
    print ("Script Started at: {}".format(time_start.strftime("%Y-%m-%d %H:%M:%S")))
    sleep(1)
    print ("Script Ended at: {}".format(time_end.strftime("%Y-%m-%d %H:%M:%S")))
    sleep(1)
    print("Total Stories watched from {}'s followers: {}".format(limits.user_watch_followers_stories, stories_bf_watched))
    sleep(1)
    print("Total Stories watched from feed: {}".format(total_stories_watched))
    sleep(1)
    print("Total suggestions followed: {}".format(total_suggestion_followed))
    sleep(1)
    print("Total number of likes: {}".format(total_likes))
    sleep(1)
    print("Total number of comments: {}".format(total_comments))
    sleep(1)
    print("closing browser...")
    sleep(1)
    webdriver.close()
    
proxy()
login()
if config.story_from_users_followers == "true":
    story_from_followers()
else:
    pass
if config.story_from_feed == "true":
    story_from_feed()
else:
    pass
if config.follow_suggestions == "true":
    follow_suggestions()
else:
    pass
if config.like == "true":
    like()
else:
    pass
if config.comment == "true":
    comment()
else:
    pass
if config.report == "true":
    report()
else:
    pass