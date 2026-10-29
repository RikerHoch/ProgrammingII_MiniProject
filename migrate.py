import csv
import json
import logging
from datetime import datetime, timezone

# ---------------------------------------------------------------
# Settings
# ---------------------------------------------------------------

csv_file = "legacy_inventory.csv"
json_file = "legacy_equipment.json"
output_file = "inventory"
date_formats = ["%Y-%m-%d", "%d/%m/%Y"]
units = {"g": "g", "kg": "kg", "ml": "mL", "l": "L"}
ID_keys = ["ID", "item_id", "equipment_id"]
maintenance_keys = ["last_maintenance", "last_maintenance_date"]

status_values = {
    "online": "online",
    "offline": "offline",
    True: "online",
    False: "offline",
}

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger("migrate")

# ---------------------------------------------------------------
# Phase I: Read the two outdated files.
# ---------------------------------------------------------------


def read_csv(path):
    with open(path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)


def read_json(path):
    with open(path, "r", encoding="utf=8") as file:
        return json.load(file)

# ---------------------------------------------------------------
# Phase II: Small helper functions, one for each cleaning rule.
# ---------------------------------------------------------------


def clean_text(value):
    if value is None:
        return None
    value = str(value).strip()
    if value == "":
        return None
    return value


def fix_name(name):
    name = clean_text(name)
    if name is None:
        return None
    return name.title()


def fix_date(value):
    value = clean_text(value)
    if value is None:
        return None
    for date_format in date_formats:
        try:
            parsed = datetime.strptime(value, date_format).replace(
                tzinfo=timezone.utc)
            return parsed.strftime("%Y-%m-%d")
        except ValueError:
            pass
        logger.warning("Could not read the date %r, saved as null", value)
        return None


def split_quantity(value):
    value = clean_text(value)
    if value is None:
        return None

    number_part = ""
    position = 0
    while position < len(value) and (value[position].isdigit()
                                     or value[position] == "."):
        number_part += value[position]
        position += 1
    unit_part = value[position:].strip().lower()

    try:
        number = float(number_part)
    except ValueError:
        logger.warning("Could not read the quantity %r, saved as null",
                       value)
        return None

    if number.is_integer():
        number = int(number)

    unit = units.get(unit_part, unit_part)
    return {"value": number, "unit": unit}


def make_slug(name):
    slug = ""
    for character in name.lower():
        if character.isalnum():
            slug += character
        elif not slug.endswith("-"):
            slug += "-"
    return slug.strip("-")


def fix_status(value):
    if isinstance(value, str):
        value = value.strip().lower()
    if value in status_values:
        return status_values[value]
    logger.warning("Unknown status %r, saved as null", value)
    return None


def get_first_key(record, keys):
    for key in keys:
        if key in record:
            return record[key]
        return None
