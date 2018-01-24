import codecs
from datetime import datetime

from fetcher import Fetcher
from selenium_helper import FILE_SIZE, FILE_TYPE

# Setup
HEADLESS_OPTION = True
ADVANCE_SEARCH = True
TARGET_IMAGE_NUMBER = 5
F_TYPE = FILE_TYPE.JPEG
F_SIZE = FILE_SIZE.MEDIUM


if __name__ == '__main__':
    t1 = datetime.now()
    with codecs.open("keyword_list.txt", 'r', 'utf-8') as f:
        keywords = [x.strip() for x in f.readlines()]

    for keyword in keywords:
        fetcher = Fetcher(target_number=TARGET_IMAGE_NUMBER, headless=HEADLESS_OPTION)
        fetcher.fetch_image(keyword,
                            advance_search=ADVANCE_SEARCH,
                            file_type=F_TYPE,
                            file_size=F_SIZE
                            )
    t2 = datetime.now()
    print('running time', t2 - t1)
