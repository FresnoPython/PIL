from utility.write_rgb_image import write_rgb_image as write_image


def select_color(x, y, bounds, color_signature):
    show_fg = color_signature['test'](x, y, bounds)

    return {
        'x': x,
        'y': y,
        'color': color_signature['fg'] if show_fg else color_signature['bg']
    }


def if_sum_of_digits_is_lt_20(x, y, bounds):
    def digitSum(x, y):
        return sum([int(i) for i in str(abs(x))]) + sum([int(i) for i in str(abs(y))])

    half_bounds = map(lambda v: v / 2, bounds)

    return digitSum(x - half_bounds[0], y - half_bounds[1]) < 20


def if_x_squared_mod_y(x, y, bounds):
    if not y:
        return False

    return x**2 % y == 0


def if_prime(x, y, bounds):
    def test_prime(value):
        if value <= 0:
            return False

        if value < 4:
            return True

        return all(value % case for case in range(2, int(value**0.5) + 1))

    # Hint: try out x%(y+1) and x*y
    return test_prime(x + y)

color_signature = {
    'test': if_prime,
    'fg': (255, 255, 255),
    'bg': (0, 0, 0),
}
bounds = (600, 600)
colors = [
    select_color(x, y, bounds, color_signature)
    for x in range(bounds[0])
    for y in range(bounds[1])
]

write_image(colors, bounds)
