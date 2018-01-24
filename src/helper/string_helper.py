import hashlib


def random_string(string, length=7):
    return hashlib.md5(string).hexdigest()[:length]
