def clip(value, lower, upper):
    return lower if value < lower else upper if value > upper else value

def lerp(a, b, ratio):
    r = clip(ratio, 0, 1)
    return a + (b-a)*r