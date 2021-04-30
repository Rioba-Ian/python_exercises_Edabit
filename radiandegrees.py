from math import pi

def radians_to_dgerees(rad):
    x = ((180/pi)*rad)
    return round(x,1)

radians_to_dgerees(1)