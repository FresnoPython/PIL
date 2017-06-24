from utility.write_rgb_image import write_rgb_image as write_image
import colorsys as cs


def convert_rgb_percentage_to_255(rgb_percentage):
    rgb_255 = map(lambda percentage: int(255 * percentage), rgb_percentage)

    return tuple(rgb_255)


def select_color(x, y, bounds):
    hue = x / (bounds[0] * 1.0)
    saturation = y / (bounds[1] * 1.0)

    rgb_percentage = cs.hls_to_rgb(hue, 0.5, 1 - saturation)

    color = convert_rgb_percentage_to_255(rgb_percentage)

    return {
        'x': x,
        'y': y,
        'color': color,
    }


bounds = (500, 200)
colors = [
    select_color(x, y, bounds)
    for x in range(bounds[0])
    for y in range(bounds[1])
]

write_image(colors, bounds)
