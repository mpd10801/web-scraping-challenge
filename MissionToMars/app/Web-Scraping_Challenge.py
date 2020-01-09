from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd

executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path)
url = 'https://mars.nasa.gov/news/'
browser.visit(url)

html = browser.html
soup = BeautifulSoup(html, 'html.parser')
slides = soup.select_one('ul.item_list li.slide')

slides.find("div", class_='content_title')

first_title = slides.find("div", class_='content_title').get_text()
first_title

news_p = slides.find('div', class_="article_teaser_body").get_text()
news_p



url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)
full_image = browser.find_by_id('full_image')
full_image.click()

browser.is_element_present_by_text('more info', wait_time=1)
more_info = browser.find_link_by_partial_text('more info')
more_info.click()

html = browser.html
img_soup = BeautifulSoup(html, 'html.parser')
img_partial_url = img_soup.select_one('figure.lede a img').get("src")
img_partial_url

featured_image_url = f'https://www.jpl.nasa.gov{img_url_rel}'
featured_image_url

url = 'https://twitter.com/marswxreport?lang=en'
browser.visit(url)

html = browser.html
weather_soup = BeautifulSoup(html, 'html.parser')

tweet = weather_soup.find('div', attrs={"class": "tweet", "data-name": "Mars Weather"})
mars_weather = tweet.find('p', 'tweet-text').get_text()
mars_weather

df = pd.read_html('https://space-facts.com/mars/')[0]
df.to_html()





url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)

hemi_images = []
hemi_list = browser.find_by_css("a.product-item h3")

for images in range(len(hemi_list)):
    hemisphere = {}
    browser.find_by_css("a.product-item h3")[images].click()
    sample = browser.find_link_by_text('Sample').first
    hemisphere['img_url'] = sample['href']
    hemisphere['title'] = browser.find_by_css("h2.title").text
    hemi_images.append(hemisphere)
    browser.back()

hemi_images



browser.quit()
