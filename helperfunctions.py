import xlsxwriter
import time
from selenium.webdriver.common.keys import Keys
import os

def scroll_down(driver):
    SCROLL_PAUSE = 10
    time.sleep(SCROLL_PAUSE*3)

    for i in range(0, 100):
        driver.find_element_by_tag_name('html').send_keys(Keys.END)
        time.sleep(SCROLL_PAUSE)

def create_youtube_excel_live(url, video_name, author_name, views, date, full_authorlist, full_commentlist):
    workbook = xlsxwriter.Workbook('youtube_live_' + author_name + '.xlsx')
    bold = workbook.add_format({'bold': True})

    worksheet = workbook.add_worksheet()
    worksheet.write('A1', 'Youtube Link', bold)
    worksheet.write('C1', url)
    worksheet.write('A2', 'Video Name', bold)
    worksheet.write('C2', video_name)
    worksheet.write('A3', 'Video Owner', bold)
    worksheet.write('C3', author_name)
    worksheet.write('A4', 'Number of Views', bold)
    worksheet.write('C4', views)
    worksheet.write('A5', 'Date Posted', bold)
    worksheet.write('C5', date)

    worksheet.set_column('A:C', 20)
    worksheet.set_column('C:C', 400)
    worksheet.write('A8', 'Author Names', bold)
    worksheet.write('B8', 'Comment Length', bold)
    worksheet.write('C8', 'Comments', bold)

    for i in range(0, len(full_commentlist)):
        worksheet.write('A' + str(9 + i), full_authorlist[i])
        worksheet.write('B' + str(9 + i), len(full_commentlist[i]))
        worksheet.write('C' + str(9 + i), full_commentlist[i])

    workbook.close()

def create_youtube_excel(url, video_name, video_owner, views, date, authors, comments):
    workbook = xlsxwriter.Workbook('youtube_' + video_name + '.xlsx')
    bold = workbook.add_format({'bold': True})

    worksheet = workbook.add_worksheet()
    worksheet.write('A1', 'Youtube Link', bold)
    worksheet.write('C1', url)
    worksheet.write('A2', 'Video Name', bold)
    worksheet.write('C2', video_name)
    worksheet.write('A3', 'Video Owner', bold)
    worksheet.write('C3', video_owner)
    worksheet.write('A4', 'Number of Views', bold)
    worksheet.write('C4', views)
    worksheet.write('A5', 'Date Posted', bold)
    worksheet.write('C5', date)

    worksheet.set_column('A:C', 20)
    worksheet.set_column('C:C', 400)
    worksheet.write('A8', 'Author Names', bold)
    worksheet.write('B8', 'Comment Length', bold)
    worksheet.write('C8', 'Comments', bold)

    for i in range(0, len(comments)):
        worksheet.write('A' + str(9 + i), authors[i])
        worksheet.write('B' + str(9 + i), len(comments[i]))
        worksheet.write('C' + str(9 + i), comments[i])

    workbook.close()

