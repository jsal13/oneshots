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


@dataclass
class Monster:
    name: str
    size: str
    ac: int
    enemy_type: str
    alignment: str
    hp: int
    speed_ft: int
    vulns: list[str]
    resists: list[str]
    languages: list[str]
    xp: int

    def to_html(self):
        return textwrap.dedent(
            f"""
        ## {self.name} {{#monster-{self.name.lower().replace(" ", "-")}}}
        
        ```{{=html}}
        <table class="table table-striped">
            <tbody>
                <tr>                    
                    <td><b>HP</b>: {self.hp}</td>
                    <td><b>AC</b>: {self.ac}</td>
                    <td><b>Speed</b>: {self.speed_ft} feet</td>
                </tr>
                <tr>
                    <td colspan="2"><b>Type</b>: {self.size} {self.enemy_type} ({self.alignment})</td>
                    <td><b>XP</b>: {self.xp}</td>
                </tr>
                <tr>
                    <td colspan="3"><b>Vulnerabilities</b>: {self.vulns}</td>
                </tr>
                <tr>
                    <td colspan="3"><b>Resists</b>: {self.resists}</td>
                </tr>
                <tr>
                    <td colspan="3"><b>Languages</b>: {self.languages}</td>
                </tr>
            </tbody>
        </table>
        ```
        """
        ).strip()


def _get_walk_speed(raw_speed_str: str) -> int:
    if raw_speed_str.get("walk") is None:
        return -1
    else:
        return int(raw_speed_str["walk"].split(" ")[0])


def _create_file_name(name: str) -> str:
    fname = re.sub(r"[^A-Za-z0-9 ]", "", name)
    return fname.lower().replace(" ", "_")


def _get_ac(ac_data: list[dict[str, any]]) -> int:
    return int(ac_data[0]["value"])  # TODO: Are there more than 1?


if __name__ == "__main__":
    OUTPUT_FOLDER = "bestiary"
    os.makedirs(name=OUTPUT_FOLDER, exist_ok=True)
    for d in data:
        monster_file_name = _create_file_name(d["name"])

        m = Monster(
            name=d["name"],
            size=d["size"],
            ac=d["armor_class"],
            enemy_type=d["type"].capitalize(),
            alignment=" ".join(i.capitalize() for i in d["alignment"].split(" ")),
            hp=d["hit_points"],
            speed_ft=_get_walk_speed(d["speed"]),
            vulns=", ".join(d["damage_vulnerabilities"]),
            resists=", ".join(d["damage_resistances"]),
            languages=d["languages"].capitalize(),
            xp=d["xp"],
        )
        with open(f"./{OUTPUT_FOLDER}/{monster_file_name}.qmd", "w+") as f:
            f.write(m.to_html())
