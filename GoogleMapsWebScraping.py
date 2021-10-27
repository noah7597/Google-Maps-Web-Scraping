from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv

def get_url(search_term):
    template = 'https://www.google.com/maps/search/{}/data=!3m1!4b1'
    search_term = search_term.replace(' ', "+")
    return template.format(search_term)

def extract_data(item):
    #atag = item.div.a
    #atag = 'https://zillow.com' + atag.get('href')    
    try:
        place = item.find('h1',{'class':'section-hero-header-title-title GLOBAL__gm2-headline-5'}).text
    except AttributeError:
        return
     
    try:
        rating = item.find('span',{'class':'section-star-display'}).text
    except:
        rating = ''
    
    try:
        reviews = item.find('span',{'class':'reviews-tap-area reviews-tap-area-enabled'}).text
    except:
        reviews = ''
    
    try:    
        price = item.find('span',{'jsan':'0.aria-label'}).text
    except:
        price = ''
    
    try:
        style = item.find('button',{'jsan':'7.widget-pane-link,0.jsaction'}).text
    except:
        style = ''
    
    try:
        description = item.find('div',{'class':'section-editorial-quote'}).text
    except:
        description = ''
        
    try:
        location = item.find('div',{'class':'ugiz4pqJLAG__primary-text gm2-body-2'}).text
    except:
        location = ''
        
    try:
        place_link = item.find('div',{'class':'ugiz4pqJLAG__text ugiz4pqJLAG__underline_on_hover'}).text.strip()
    except:
        place_link = ''
        
    try:
        phone = item.find('button',{'data-tooltip':'Copy phone number'}).text.strip()
    except:
        phone = ''
        
    try:
        times = item.find_all('tr',{'class':'lo7U087hsMA__row-row'})
        times_mon = times[0].text.strip()
        times_tues = times[1].text.strip()
        times_wed = times[2].text.strip()
        times_thur = times[3].text.strip()
        times_fri = times[4].text.strip()
        times_sat = times[5].text.strip()
        times_sun = times[6].text.strip()
    except:
        times = ''
        times_mon = ''
        times_tues = ''
        times_wed = ''
        times_thur = ''
        times_fri = ''
        times_sat = ''
        times_sun = ''
    
    data = (place, rating, reviews, price, style, description, location, phone, place_link)
        
    return data


def main(search_term):
    driver = webdriver.Chrome(executable_path ="/Applications/chromedriver89")
    time.sleep(2)
    driver.get('https://www.google.com/maps/')
    
    records = set([])
    
    time.sleep(2)
    driver.get(get_url(search_term))
    
    for page in range(1):
        url = driver.current_url
        time.sleep(2)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        results = soup.find_all('a',{'class':'section-result'})
        time.sleep(2)
        #len(results) - 18
        for item in range(1, 101):
            
            xpath = '//*[@id="pane"]/div/div[1]/div/div/div[4]/div[1]/a[' + str(item) + ']'
            time.sleep(2)
            link = driver.find_element_by_xpath(xpath)
            link.click()
            time.sleep(2)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            time.sleep(2)
            
            record = extract_data(soup)
    
            if record:
                records.add(record)
                    
            time.sleep(3)
            driver.back()
            time.sleep(10)
        
        nextPage = driver.find_element_by_xpath('//*[@id="n7lv7yjyC35__section-pagination-button-next"]')
        time.sleep(2)
        nextPage.click()
        time.sleep(3)
    
    driver.close()
    
    records = list(records)
    with open('/Users/noahhallberg/Desktop/WebScraping/Google Maps WebScraping/google_maps.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Place', 'Rating', 'Reviews', 'Price', 'Style', 'Description','Location','Phone','Website'])
        writer.writerows(records)
