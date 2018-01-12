from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

import os
import time
import sys
import threading
import traceback

total = 0
delay = 1 # second
img_search_url = 'http://www.google.com/images?q={}'
timeout_delay = 10
chrome_options = Options()
chrome_options.add_argument('--headless')

def scroll(browser, delay=delay):
    show_more_btn = browser.find_elements_by_xpath("//input[@value='Show more results']")
    if len(show_more_btn) > 0:
        try:
            show_more_btn[0].click()
        except:
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    else:
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(delay)


def click_element(browser, xpath, delay=None):
    element = browser.find_element_by_xpath(xpath)
    element.click()
    if delay is not None:
        time.sleep(delay)


def download_image(keyword, idx, gtag):
    try:
        c = Chrome(chrome_options=chrome_options)
        c.set_page_load_timeout(timeout_delay)
        url = gtag.get_attribute('href')
        c.get(url)
        image_tag = c.find_element_by_xpath("//img[@class='irc_mi']")
        img_url = image_tag.get_attribute('src')
        os.system('wget {} -O "../images/{}/{}"'.format(img_url, keyword, str(idx)))
        c.close()
        return total + 1
    except:
        print("Unexpected error:", sys.exc_info()[0])
        traceback.print_exc()
        c.close()
        return total


def fetch_image(keyword, total_image=10):
    browser = Chrome(chrome_options=chrome_options)
    browser.set_page_load_timeout(timeout_delay)
    browser.get('http://www.google.com')
    click_element(browser, "//div[@id='_eEe']/a")

    browser.get(img_search_url.format(keyword))

    click_element(browser, "//a[@id='hdtb-tls']", delay) # tools button
    click_element(browser, "//div[@class='hdtb-mn-hd']", delay) # size button
    click_element(browser, "//li[@id='isz_m']", delay) # size medium button

    total_img = 0
    while True:
        google_img_tag = browser.find_elements_by_xpath("//div[@id='rg_s']/div/a")
        if total_img == len(google_img_tag):
            break
        else:
            total_img = len(google_img_tag)
        if total_img < total_image:
            scroll(browser)

    total = 0

    if not os.path.exists('../images/{}'.format(keyword)):
        os.makedirs('../images/{}'.format(keyword))

    for idx, gtag in enumerate(google_img_tag):
        t = threading.Thread(target=download_image, args=(keyword, idx, gtag))
        t.start()
        t.join(timeout_delay)
        if total >= total_image:
            break

    browser.close()


if __name__ == '__main__':
    keyword = 'laptop'
    fetch_image(keyword, total_image=500)
