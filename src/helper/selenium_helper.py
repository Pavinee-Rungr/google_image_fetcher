import time


GOOGLE_URL = 'https://www.google.com'
GOOGLE_IMAGE_SEARCH_URL = 'http://www.google.com/images?q={}'
GOOGLE_IMAGE_ADVANCE_SEARCH_URL = 'https://www.google.co.th/advanced_image_search'
ACTION_DELAY = 1


class FILE_TYPE:
    JPEG = 'jpg'


class FILE_SIZE:
    MEDIUM = 'medium'


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


def google_image_advance_search(browser, keyword, file_type=None, file_size=None, action_delay=1):
    browser.get(GOOGLE_IMAGE_ADVANCE_SEARCH_URL)

    search_field = browser.find_element_by_xpath("//input[@id='_dKg']")
    search_field.send_keys(keyword)

    if file_size is not None:
        click_element(browser, "//div[@id='imgsz_button']")
        if file_size is FILE_SIZE.MEDIUM:
            click_element(browser, "//div[contains(text(),'Medium')]")

    if file_type is not None:
        click_element(browser, "//div[@id='as_filetype_button']")
        if file_type is FILE_TYPE.JPEG:
            click_element(browser, "//div[contains(text(),'JPG files')]")

    click_element(browser, "//input[@type='submit']")



def google_image_search(browser, keyword, action_delay=1):
    browser.get(GOOGLE_IMAGE_SEARCH_URL.format(keyword))
    # tools button
    click_element(browser, "//a[@id='hdtb-tls']", action_delay)
    # size button
    click_element(browser, "//div[@class='hdtb-mn-hd']", action_delay)
    # size medium button
    click_element(browser, "//li[@id='isz_m']", action_delay)
