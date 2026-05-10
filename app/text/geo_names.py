import re
import geonamescache
from rapidfuzz import process
from transliterate import translit

gc = geonamescache.GeonamesCache()

cities = gc.get_cities()

GEO_MAP = {}

for city in cities.values():
    name = city.get("name")
    alternates = city.get("alternatenames", [])

    if name:
        GEO_MAP[name.lower()] = name

    for alt in alternates:
        if alt:
            GEO_MAP[alt.lower()] = name


def clean_text(value: str) -> str:
    return re.sub(r"\s+", " ", str(value).strip().lower())


def transliterate_value(value: str) -> str:
    try:
        return translit(value, reversed=True)
    except Exception:
        return value


def normalize_geo_name(value: str):
    if value is None:
        return None

    clean = clean_text(value)

    if not clean:
        return None

    match = process.extractOne(
        clean,
        GEO_MAP.keys(),
        score_cutoff=80
    )

    if match:
        matched_key, score, _ = match
        return GEO_MAP[matched_key]

    return transliterate_value(value)