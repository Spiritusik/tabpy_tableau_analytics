import os
from dotenv import load_dotenv
from tabpy.tabpy_tools.client import Client

from app.geo import mgrs_to_lat, mgrs_to_lon
from app.text import normalize_geo_name, transliterate

load_dotenv()
TABPY_HOST = os.getenv("TABPY_HOST")

client = Client(TABPY_HOST)

client.deploy(
    "mgrs_to_lat",
    mgrs_to_lat,
    "Convert MGRS to latitude",
    override=True
)

client.deploy(
    "mgrs_to_lon",
    mgrs_to_lon,
    "Convert MGRS to longitude",
    override=True
)

client.deploy(
    "normalize_geo_name",
    normalize_geo_name,
    "Normalize geo name",
    override=True
)

client.deploy(
    "transliterate",
    transliterate,
    "Transliterate text",
    override=True
)

print("TabPy endpoints deployed successfully.")