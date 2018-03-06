from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from helperfunctions import *

SCROLL_PAUSE = 10

try:
    url = raw_input("Please enter a url: ")
    driver = webdriver.Firefox()
    driver.get(url)
    driver.implicitly_wait(30)

    video_name = WebDriverWait(driver,20).until(EC.presence_of_element_located
                                                   ((By.XPATH, """// *[ @ id = "container"] / h1""")))
    time.sleep(10)
    date = WebDriverWait(driver, 10).until(EC.presence_of_element_located
                                    ((By.XPATH, """//*[@id="upload-info"]""")))
    time.sleep(2)
    views = WebDriverWait(driver, 10).until(EC.presence_of_element_located
                                    ((By.XPATH, """//*[@id="count"]""")))
    time.sleep(2)
    author_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located
                                    ((By.XPATH, """ //*[@id="owner-name"]/a""")))
    time.sleep(10)

    for i in range(0, 100):
        driver.find_element_by_tag_name('html').send_keys(Keys.END)
        time.sleep(SCROLL_PAUSE)

    comment_div = driver.find_element_by_xpath("""// *[@id="contents"] """)
    comments = comment_div.find_elements_by_xpath("""//*[@id="content-text"] """)
    authors = driver.find_elements_by_xpath("""//*[@id="author-text"]""")
    comment_list = []
    author_list = []

    for comment in comments:
        comment_list.append(comment.text)

    for author in authors:
        author_list.append(author.text)

    create_youtube_excel(str(url), video_name.text, author_name.text, views.text, date.text, author_list, comment_list)
except TimeoutException:
    print("TimeoutException")
    driver.quit()
finally:
    driver.quit()





