
import json
import os
import random
from typing import Dict, List

# Load a mapping of countries to fruit lists based on real-world data.
FRUIT_FILE = os.path.join(os.path.dirname(__file__), "country_fruits.json")
with open(FRUIT_FILE, "r", encoding="utf-8") as f:
    COUNTRY_FRUITS: Dict[str, List[str]] = json.load(f)

# Country list is derived from the keys of the fruit mapping.
UN_COUNTRIES: List[str] = sorted(COUNTRY_FRUITS.keys())

COUNTRY_MAP: Dict[str, str] = {c.lower(): c for c in UN_COUNTRIES}

def ask_country() -> str:
    """Prompt the user for a country and return the validated name."""
    while True:
        country = input(
            "From which country should the fruits come from? (type 'list' to see available countries) "
        ).strip().lower()
        if country == "list":
            print(", ".join(sorted(UN_COUNTRIES)))
            continue
        if country in COUNTRY_MAP:
            return COUNTRY_MAP[country]
        print("Sorry, that country is not recognized. Please try again.")

def main() -> None:
    country = ask_country()
    print(f"Five random fruits from {country}:")
    for fruit in random.sample(COUNTRY_FRUITS[country], 5):
        print(fruit)

if __name__ == "__main__":
    main()

