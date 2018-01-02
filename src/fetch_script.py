from fetcher import fetch_image

if __name__ == '__main__':
    with open("keyword_list.txt") as f:
        keywords = [x.strip() for x in f.readlines()]

    for keyword in keywords:
        fetch_image(keyword)
