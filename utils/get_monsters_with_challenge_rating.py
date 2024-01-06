from dataclasses import dataclass
import json
import os
import tarfile
import textwrap
import re

f_ = os.path.abspath("./dnd_ref/monster_data.tar.gz")

# Untar the data files.
with tarfile.open(f_, "r") as tar:
    tar.extractall(path="./dnd_ref")
with open("./dnd_ref/5e-SRD-Monsters.json", "r", encoding="utf-8") as f:
    data_5e = json.load(f)
with open("./dnd_ref/Custom-Monsters.json", "r", encoding="utf-8") as f:
    data_custom = json.load(f)

data = data_5e + data_custom

if __name__ == "__main__":
    # Inclusive.
    CHALLENGE_RATING_LOWER_BOUND = 0
    CHALLENGE_RATING_UPPER_BOUND = 1

    monster_list = [
        (row["name"], row["challenge_rating"])
        for row in data
        if (
            (row["challenge_rating"] >= CHALLENGE_RATING_LOWER_BOUND)
            and (row["challenge_rating"] <= CHALLENGE_RATING_UPPER_BOUND)
        )
    ]
    monster_list.sort(key=lambda row: row[1])

    for item in monster_list:
        print(f"{item[0]}: {item[1]}")
