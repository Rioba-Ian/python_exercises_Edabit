from math import pi

# we want to get the volume in 1L
# which is also equal to 1 kg
def volume(r,h):
    volume = pi * h * (r**2)
    volume = volume * 0.001
    return round(volume,2)


print(volume(4, 10))
