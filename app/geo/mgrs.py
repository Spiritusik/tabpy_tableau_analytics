from mgrs import MGRS

m = MGRS()

def mgrs_to_lat(_arg1):
    result = []

    for x in _arg1:
        try:
            if x is None:
                result.append(None)
                continue

            lat, lon = m.toLatLon(str(x).replace(" ", "").strip())
            result.append(lat)

        except:
            result.append(None)

    return result


def mgrs_to_lon(_arg1):
    result = []

    for x in _arg1:
        try:
            if x is None:
                result.append(None)
                continue

            lat, lon = m.toLatLon(str(x).replace(" ", "").strip())
            result.append(lon)

        except:
            result.append(None)

    return result