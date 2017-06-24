from utility.fetch_image import fetch_random_image
import PIL.ImageFilter as filters


def apply_filters(image, *filters_to_apply):
    '''
    Arguments:
        image, PIL.Image
        *filters_to_apply, list of PIL.ImageFilter
    '''
    image_copy = image.copy()

    for image_filter in filters_to_apply:
        image_copy = image_copy.filter(image_filter)

    image_copy.show()

    return image


image_size = (500, 500)
image = fetch_random_image(image_size)

image.show()

# Use `help(filters)` or `pydoc PIL.ImageFilter` to find available filters.
apply_filters(image, filters.DETAIL, filters.CONTOUR)
