from fetcher1 import fetch_image
from datetime import datetime

if __name__ == '__main__':
    t1 = datetime.now()
    with open("keyword_list.txt") as f:
        keywords = [x.strip() for x in f.readlines()]

    for keyword in keywords:
        fetch_image(keyword, total_image=500)
    t2 = datetime.now()
    print('running time', t2 - t1)
