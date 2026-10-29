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
