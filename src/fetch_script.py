import codecs
from datetime import datetime
import os
from yaml import load

from fetcher import Fetcher
from helper.selenium_helper import FILE_SIZE, FILE_TYPE

# Setup
HEADLESS_OPTION = True
ADVANCE_SEARCH = True
TARGET_IMAGE_NUMBER = 500
F_TYPE = FILE_TYPE.JPEG
F_SIZE = FILE_SIZE.MEDIUM


# Default Value
DEFAULT_TOTAL_TARGET = 500
DEFAULT_FILE_TYPE = FILE_TYPE.JPEG


if __name__ == '__main__':
    t1 = datetime.now()
    with codecs.open("config.yaml", "r", "utf-8") as config_file:
        fetch_config = load(config_file)

    for cat, keyword_groups in fetch_config.items():
        cat_dir = os.path.join("../images", str(cat))
        if not os.path.exists(cat_dir):
            os.makedirs(cat_dir)

        for keyword_group in keyword_groups:
            keywords = keyword_group.get('keywords') or []
            target_number = keyword_group.get('target_number') or DEFAULT_TOTAL_TARGET
            sites = keyword_group.get('sites')
            file_type = keyword_group.get('file_type') or DEFAULT_FILE_TYPE
            for keyword in keywords:
                keyword_dir = os.path.join(cat_dir, str(keyword))
                print(keyword_dir)
                if sites is None:
                    fetcher = Fetcher(target_number=target_number, headless=HEADLESS_OPTION)
                    fetcher.fetch_image(keyword, keyword_dir,
                                        advance_search=ADVANCE_SEARCH,
                                        file_type=file_type,
                                        file_size=F_SIZE
                                        )
                else:
                    for site in sites:
                        fetcher = Fetcher(target_number=target_number, headless=HEADLESS_OPTION)
                        fetcher.fetch_image(keyword, keyword_dir,
                                            advance_search=ADVANCE_SEARCH,
                                            file_type=file_type,
                                            file_size=F_SIZE,
                                            site=site
                                            )
    t2 = datetime.now()
    print('running time', t2 - t1)
