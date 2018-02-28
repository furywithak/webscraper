# Webscrapers

First, ensure that both selenium and XlsxWriter are both installed.
pip install selenium
pip install XlsxWriter

The scraper_youtubecomments scrapes youtube comments from a youtube video. It scrapes the video name, video author, 
and the date posted. The scrapers also scraps all the comments and the author names. But, it does not scrap comments
that are nested in the reply. It then outputs the information into an excel file.

The scraper_youtubelive scrapes youtube live comments. It scrapes the video name, video author, 
and the date posted. The scraper also scrapes the name and the author. It then outputs the information into an excel file.
