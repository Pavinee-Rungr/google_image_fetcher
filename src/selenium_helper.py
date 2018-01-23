import time


GOOGLE_URL = 'https://www.google.com'
GOOGLE_IMAGE_SEARCH_URL = 'http://www.google.com/images?q={}'
ACTION_DELAY = 1


def click_element(browser, xpath, delay=ACTION_DELAY):
    element = browser.find_element_by_xpath(xpath)
    element.click()
    if delay is not None:
        time.sleep(delay)


def scroll(browser, delay=ACTION_DELAY):
    show_more_btn = browser.find_elements_by_xpath("//input[@value='Show more results']")
    if len(show_more_btn) > 0:
        try:
            show_more_btn[0].click()
        except:
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    else:
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(delay)


def set_google_to_english(browser):
    browser.get(GOOGLE_URL)
    click_element(browser, "//div[@id='_eEe']/a")


def google_image_search(browser, keyword, action_delay=1):
    (GOOGLE_IMAGE_SEARCH_URL.format(keyword))
    browser.get(GOOGLE_IMAGE_SEARCH_URL.format(keyword))
    # tools button
    click_element(browser, "//a[@id='hdtb-tls']", action_delay)
    # size button
    click_element(browser, "//div[@class='hdtb-mn-hd']", action_delay)
    # size medium button
    click_element(browser, "//li[@id='isz_m']", action_delay)
