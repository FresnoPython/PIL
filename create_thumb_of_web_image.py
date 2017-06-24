from utility.fetch_image import fetch_random_image


def create_thumbnail(image, thumbnail_size=(100, 100)):
    image_copy = image.copy()

    image_copy.thumbnail(thumbnail_size)
    image_copy.show()

    return image_copy


image_size = (500, 500)
image = fetch_random_image(image_size)

image.show()

create_thumbnail(image)
