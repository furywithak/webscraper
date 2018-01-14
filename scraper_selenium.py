from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
import string
import urlparse
import time
from helper_functions import scroll_comments

url = raw_input("Please enter a url: ")

# Create a popup url
popup_url = string.replace(url, "watch", "live_chat")
popup_url = popup_url.strip(" ") + "&is_popout=1"
print (popup_url)
# driver = raw_input("Please enter a browser: ")

driver = webdriver.Firefox()
driver.get(popup_url)
driver.implicitly_wait(30)
try:
    # Number of people watching the video currently
    # element = WebDriverWait(driver, 10).\
    #     until(EC.presence_of_element_located((By.ID, "count")))
    # print(element.text)
    #
    # # Name of the video
    # name_of_video = WebDriverWait(driver,20).until(EC.presence_of_element_located
    #                                                ((By.XPATH, """// *[ @ id = "container"] / h1""")))
    # print(name_of_video.text)
    #
    # # Time of video
    # time_of_video = WebDriverWait(driver, 10).until(EC.presence_of_element_located
    #                                                 ((By.XPATH, """ //*[@id="upload-info"]/span""")))
    # print (time_of_video.text)
    #
    # #load comments
    #
    # driver.implicitly_wait(10)
    # author_name = WebDriverWait(driver, 20).until(EC.presence_of_element_located
    #                                 ((By.XPATH, """ //*[@id="owner-name"]/a""")))
    #
    # print(author_name.text)


    #scroll = driver.find_elements_by_xpath("""//*[@id="item-scroller"]""")

    # element = WebDriverWait(driver, 10).until(EC.presence_of_element_located
    #                                           ((By.XPATH, """//*[@id="item-scroller"]""")))
    # webdriver.ActionChains(driver).move_to_element(element).double_click(element).perform()

    # author = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
    #
    #                                                 """//*[@id="author-name"]""")))
    # comments = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
    #                                                                            """// *[ @ id = "message"] """)))
    # print(comments.text)
    while True:
        comment_div = driver.find_element_by_xpath("""// *[ @ id = "message"] """)
        comments = comment_div.find_elements_by_xpath("""// *[ @ id = "message"] """)
        for comment in comments:
            print(comment.text)
        scroll_comments(driver)


except TimeoutException:
    print("TimeoutException")
    driver.quit()
finally:
    driver.quit()

# #driver.close()
