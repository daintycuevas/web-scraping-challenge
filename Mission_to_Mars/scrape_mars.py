
from splinter import Browser
from bs4 import BeautifulSoup 
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

def scrape():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    
    time.sleep(1)

    # Scrape news page into bsoup
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    slides = soup.find_all('div', class_='list_text')

    news_title=[]
    news_p=[]

    for item in slides:
        title = item.find('div', class_='content_title')
        news_title.append(title)
        para = item.find('div', class_='article_teaser_body')
        news_p.append(para)


    # Get featured image url
 

    # Get Mars facts table
    url = 'https://space-facts.com/mars/'

    table = pd.read_html(url)
    table

    df = table[0]
    df

    mars_table = df.to_html('facts_table.html')


    ### Mars Hemispheres ###

    all_title = []
    all_img_url = []

    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    title = soup.find('h2', class_='title').text
    all_title.append(title)

    img_path = soup.find('img', class_='wide-image').get('src')
    img_url = 'https://astrogeology.usgs.gov' + img_path
    all_img_url.append(img_url)


    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    title = soup.find('h2', class_='title').text
    all_title.append(title)

    img_path = soup.find('img', class_='wide-image').get('src')
    img_url = 'https://astrogeology.usgs.gov' + img_path
    all_img_url.append(img_url)


    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    title = soup.find('h2', class_='title').text
    all_title.append(title)

    img_path = soup.find('img', class_='wide-image').get('src')
    img_url = 'https://astrogeology.usgs.gov' + img_path
    all_img_url.append(img_url)


    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    title = soup.find('h2', class_='title').text
    all_title.append(title)

    img_path = soup.find('img', class_='wide-image').get('src')
    img_url = 'https://astrogeology.usgs.gov' + img_path
    all_img_url.append(img_url)

    for title, paragraph, img_title, img_url in zip(news_title, news_p, all_title, all_img_url):
    
        results = {
                'title': title,
                'paragraph': paragraph,
                'image_title': img_title,
                'image_url': img_url
                }
        return results
    


if __name__=="__main__":
    print(scrape())





