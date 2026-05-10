from mgrs import MGRS

def print_hi(name):
    m = MGRS()

    lat, lon = m.toLatLon("37U DQ 06488 39238".replace(" ", ""))

    print(f'Hi, {name}. Координаты: {lat}')


if __name__ == '__main__':
    print_hi('PyCharm')