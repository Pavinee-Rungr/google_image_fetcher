import hashlib


def random_string(string, length=7):
    return hashlib.md5(string).hexdigest()[:length]


def generate_image_naming(keyword, file_type=None, file_size=None, site=None, length=13, readable=True):
    concat_str = keyword
    if file_type is not None:
        concat_str = concat_str + '_' + file_type
    if file_size is not None:
        concat_str = concat_str + '_' + file_size
    if site is not None:
        concat_str = concat_str + '_' + site

    if readable:
        return concat_str
    else:
        return str(random_string(concat_str.encode('utf-8')), length)
