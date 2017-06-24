from PIL import Image as i
from urllib2 import urlopen as get


def fetch_image_from_url(url):
    return i.open(get(url))


def fetch_random_image(size=(500, 500)):
    url = "https://unsplash.it/{0}/{1}/?random".format(size[0], size[1])

    return fetch_image_from_url(url)
