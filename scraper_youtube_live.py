from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import string
from helperfunctions import *
import time

try:
    start_time = time.time()
    url = raw_input("Please enter a url: ")
    num = raw_input("Please enter number of minutes you would like the program to run: ")
    driver = webdriver.Firefox()

    # Create a popup url
    popup_url = string.replace(url, "watch", "live_chat")
    popup_url = popup_url.strip(" ") + "&is_popout=1"

    driver.get(url)
    window_youtube = driver.window_handles[0]
    driver.implicitly_wait(30)

    tmp_video_name = WebDriverWait(driver,20).until(EC.presence_of_element_located
                                                   ((By.XPATH, """// *[ @ id = "container"] / h1""")))
    video_name = tmp_video_name.text
    time.sleep(10)
    tmp_date = WebDriverWait(driver, 10).until(EC.presence_of_element_located
                                    ((By.XPATH, """//*[@id="upload-info"]""")))
    date = tmp_date.text

    time.sleep(2)
    tmp_views = WebDriverWait(driver, 10).until(EC.presence_of_element_located
                                    ((By.XPATH, """//*[@id="count"]""")))
    views = tmp_views.text
    time.sleep(2)
    tmpauthor_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located
                                    ((By.XPATH, """ //*[@id="owner-name"]/a""")))
    author_name = tmpauthor_name.text
    time.sleep(10)

    #second tab
    driver.execute_script("window.open('about:blank', 'tab2');")
    driver.switch_to.window("tab2")

    driver.get(popup_url)
    driver.implicitly_wait(30)
    SCROLL_PAUSE = 10

    full_authorlist = []
    full_commentlist = []

    time_out = time.time() + 60*int(num)
    # comment_div = driver.find_element_by_xpath("""// *[ @ id = "message"] """)

    while True:
        comment_div = driver.find_element_by_xpath("""// *[ @ id = "message"] """)
        comments = comment_div.find_elements_by_xpath("""// *[ @ id = "message"] """)
        authors = comment_div.find_elements_by_xpath("""//*[@id="author-name"]""")

        for comment in comments:
            full_commentlist.append(comment.text)
        for author in authors:
            full_authorlist.append(author.text)

        driver.find_element_by_tag_name('html').send_keys(Keys.END)
        time.sleep(SCROLL_PAUSE/2)

        if (time.time() > time_out):
            break

    create_youtube_excel_live(str(url), video_name, author_name, views, date, full_authorlist, full_commentlist)

except TimeoutException:
    print("TimeoutException")
    driver.quit()
finally:
    driver.quit()
