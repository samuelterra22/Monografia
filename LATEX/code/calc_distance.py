@jit
def calc_distance(x1, y1, x2, y2):
    return sqrt(pow((x1 - x2), 2.0) + pow((y1 - y2), 2.0)) * precisao
