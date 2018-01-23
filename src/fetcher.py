import magic

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

import os
import sys
import threading
import traceback

from selenium_helper import *


class Fetcher:

    GOOGLE_IMAGE_SEARCH_URL = 'http://www.google.com/images?q{}'

    MAX_THREAD = 3
    MAX_TRY = 2
    TIMEOUT_DELAY = 10
    ACTION_DELAY = 1
    LOCK = threading.Lock()

    def __init__(self,
                 headless=True):
        self.chrome_options = Options()
        if headless:
            self.chrome_options.add_argument('--headless')
        self.counter = 0

    @staticmethod
    def set_max_thread(max_thread):
        Fetcher.MAX_THREAD = max_thread

    def counting(self, reverse=False):
        Fetcher.LOCK.acquire()
        if reverse:
            self.counter -= 1
        else:
            self.counter += 1
        Fetcher.LOCK.release()

    def reset_counter(self):
        Fetcher.LOCK.acquire()
        self.counter = 0
        Fetcher.LOCK.release()

    def download_image(self, keyword, idx, gtag):
        try:
            c = Chrome(chrome_options=self.chrome_options)
            c.set_page_load_timeout(Fetcher.TIMEOUT_DELAY)

            url = gtag.get_attribute('href')
            c.get(url)
            image_tag = c.find_element_by_xpath("//img[@class='irc_mi']")
            img_url = image_tag.get_attribute('src')
            output_img_path = "../images/{}/{}".format(keyword, str(idx))
            # '-nv'

            print('Downloading #', str(idx))
            command = 'wget -nv --tries={} --timeout={} "{}" -O "{}"'\
                .format(Fetcher.MAX_TRY,
                        Fetcher.TIMEOUT_DELAY,
                        img_url,
                        output_img_path)
            os.system(command)

            print(os.path.exists(output_img_path))
            if os.path.exists(output_img_path):
                file_type = magic.from_file(output_img_path)
                if file_type.split()[0] != 'JPEG':
                    os.remove(output_img_path)
                else:
                    os.rename(output_img_path, output_img_path + '.jpg')
                    self.counting()

            c.close()
        except:
            c.close()
            print("Unexpected error:", sys.exc_info()[0])
            traceback.print_exc()

    def fetch_image(self, keyword, total_fetch=None):
        if keyword is None:
            raise ValueError('keyword is required.')
        if total_fetch is None:
            raise ValueError('total_fetch is required.')

        # Setup Main browser
        main_browser = Chrome(chrome_options=self.chrome_options)
        set_google_to_english(main_browser)
        google_image_search(main_browser, keyword)

        google_image_number = 0
        while True:
            images_tag = main_browser.find_elements_by_xpath("//div[@id='rg_s']/div/a")
            if google_image_number == len(images_tag):
                break
            else:
                google_image_number = len(images_tag)
            if google_image_number < total_fetch:
                scroll(main_browser)

        self.counter = 0

        # create keyword dir if not exist
        if not os.path.exists('../images/{}'.format(keyword)):
            os.makedirs('../images/{}'.format(keyword))

        # fetching thread
        for idx, img_tag in enumerate(images_tag):
            t = threading.Thread(target=self.download_image, args=(keyword, idx, img_tag))
            while threading.active_count() > Fetcher.MAX_THREAD:
                time.sleep(1)
            t.start()
            print('Image #', idx, 'is added to queue.')
            if self.counter >= total_fetch:
                break
        self.reset_counter()
        main_browser.close()


if __name__ == '__main__':
    fetcher = Fetcher(headless=False)
    keyword = 'laptop'
    fetcher.fetch_image(keyword, total_fetch=5)
