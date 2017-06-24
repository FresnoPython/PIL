from PIL import Image as i


def write_rgb_image(colors, bounds, background_color=(0, 0, 0), should_save=False, filename='image.png'):
    '''
    write_rgb_image(
        colors, List of {x,y,color} where color is a (red, green, blue) tuple
        bounds, (width, height) tuple
        background_color, (red, green, blue) tuple to determine base color. Defaults to (0, 0, 0)
    )
    '''

    image = i.new('RGB', bounds, background_color)
    pixels = image.load()

    for location in colors:
        pixels[location['x'], location['y']] = location['color']

    if should_save:
        image.save(filename)
    else:
        image.show(title=filename)
