from datetime import datetime

from fetcher import Fetcher
from selenium_helper import FILE_SIZE, FILE_TYPE

ADVANCE_SEARCH = True
TOTAL_KEYWORD = 500
F_TYPE = FILE_TYPE.JPEG
F_SIZE = FILE_SIZE.MEDIUM

if __name__ == '__main__':
    t1 = datetime.now()
    with open("keyword_list.txt") as f:
        keywords = [x.strip() for x in f.readlines()]

    for keyword in keywords:
        fetcher = Fetcher(headless=False)
        fetcher.fetch_image(keyword,
                            total_fetch=5,
                            advance_search=ADVANCE_SEARCH,
                            file_type=F_TYPE,
                            file_size=F_SIZE
        )
    t2 = datetime.now()
    print('running time', t2 - t1)
