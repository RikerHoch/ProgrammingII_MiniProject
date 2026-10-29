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
