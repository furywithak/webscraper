from selenium import webdriver
import time
#
# def get_driver(url):
#     switcher = {
#         "Chrome": chrome(),
#         "Edge": edge(),
#         "Firefox": firefox(),
#         "Safari": safari()
#     }
#     return switcher.get(url, "nothing")
#
# def chrome():
#     driver = webdriver.Chrome()
#     return driver
#
# def edge():
#     driver = webdriver.Edge()
#     return driver
#
# def firefox():
#     driver = webdriver.Firefox()
#     return driver
#
# def safari():
#     driver = webdriver.Safari()
#     return driver

def scroll_comments(driver):
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, "
                              "document.body.scrollHeight);")
        time.sleep(10)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

