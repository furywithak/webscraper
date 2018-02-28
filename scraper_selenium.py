from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import string
from helperfunctions import *
import time



try:
    driver = webdriver.Firefox()
    url = raw_input("Please enter a url: ")

    # Create a popup url
    popup_url = string.replace(url, "watch", "live_chat")
    popup_url = popup_url.strip(" ") + "&is_popout=1"

    driver.get(url)
    driver.implicitly_wait(30)
    # Number of people watching the video currently
    viewers = WebDriverWait(driver, 10).\
        until(EC.presence_of_element_located((By.ID, "count")))
    print(viewers.text)

    # Name of the video
    name_of_video = WebDriverWait(driver,20).until(EC.presence_of_element_located
                                                   ((By.XPATH, """// *[ @ id = "container"] / h1""")))
    print(name_of_video.text)

    #Time of video
    time_of_video = WebDriverWait(driver, 10).until(EC.presence_of_element_located
                                                    ((By.XPATH, """ //*[@id="upload-info"]/span""")))
    print (time_of_video.text)

    #load comments
    driver.implicitly_wait(10)
    author_name = WebDriverWait(driver, 20).until(EC.presence_of_element_located
                                    ((By.XPATH, """ //*[@id="owner-name"]/a""")))
    print(author_name.text)

    driver.get(popup_url)
    driver.implicitly_wait(30)
    SCROLL_PAUSE = 10

    full_authorlist = []
    full_commentlist = []

    input = raw_input("Enter STOP to stop: ")
    while input != "STOP":
        comment_div = driver.find_element_by_xpath("""// *[ @ id = "message"] """)
        comments = comment_div.find_elements_by_xpath("""// *[ @ id = "message"] """)
        authors = comment_div.find_elements_by_xpath("""//*[@id="author-name"]""")
        for comment in comments:
            if comment not in full_commentlist:
                full_commentlist.append(comment)
                print(comment.text)
        for author in authors:
            if author not in full_authorlist:
                full_authorlist.append(author)
                print (author.text)
        driver.find_element_by_tag_name('html').send_keys(Keys.END)
        time.sleep(SCROLL_PAUSE)
        input = raw_input("Enter STOP to stop: ")

    create_youtubelive_excel(url, author_name, name_of_video, viewers, time_of_video, full_commentlist, full_authorlist)

except TimeoutException:
    print("TimeoutException")
    driver.quit()
finally:
    driver.quit()