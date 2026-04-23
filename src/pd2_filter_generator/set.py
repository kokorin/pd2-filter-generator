"""
Generated Set enum from PD2 data.

DO NOT EDIT MANUALLY - regenerate with: hatch run ./scripts/generate.py generate
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


@dataclass(frozen=True)
class _Metadata:
    """Item type metadata."""

    level: int  # "level"


_METADATA: dict[str, _Metadata] = {
    "CIVERBS_VESTMENTS": _Metadata(
        level=13,
    ),
    "HSARUS_DEFENSE": _Metadata(
        level=4,
    ),
    "CLEGLAWS_BRACE": _Metadata(
        level=6,
    ),
    "IRATHAS_FINERY": _Metadata(
        level=21,
    ),
    "ISENHARTS_ARMORY": _Metadata(
        level=11,
    ),
    "VIDALAS_RIG": _Metadata(
        level=19,
    ),
    "MILABREGAS_REGALIA": _Metadata(
        level=23,
    ),
    "CATHANS_TRAPS": _Metadata(
        level=15,
    ),
    "TANCREDS_BATTLEGEAR": _Metadata(
        level=27,
    ),
    "SIGONS_COMPLETE_STEEL": _Metadata(
        level=9,
    ),
    "INFERNAL_TOOLS": _Metadata(
        level=7,
    ),
    "BERSERKERS_ARSENAL": _Metadata(
        level=5,
    ),
    "DEATHS_DISGUISE": _Metadata(
        level=8,
    ),
    "ANGELIC_RAIMENT": _Metadata(
        level=17,
    ),
    "ARCTIC_GEAR": _Metadata(
        level=3,
    ),
    "ARCANNAS_TRICKS": _Metadata(
        level=20,
    ),
    "NATALYAS_ODIUM": _Metadata(
        level=22,
    ),
    "ALDURS_WATCHTOWER": _Metadata(
        level=29,
    ),
    "IMMORTAL_KING": _Metadata(
        level=37,
    ),
    "TAL_RASHAS_WRAPPINGS": _Metadata(
        level=26,
    ),
    "GRISWOLDS_LEGACY": _Metadata(
        level=44,
    ),
    "TRANG_OULS_AVATAR": _Metadata(
        level=32,
    ),
    "MAVINAS_BATTLE_HYMN": _Metadata(
        level=21,
    ),
    "THE_DISCIPLE": _Metadata(
        level=39,
    ),
    "HEAVENS_BRETHREN": _Metadata(
        level=55,
    ),
    "ORPHANS_CALL": _Metadata(
        level=41,
    ),
    "HWANINS_MAJESTY": _Metadata(
        level=28,
    ),
    "SAZABIS_GRAND_TRIBUTE": _Metadata(
        level=34,
    ),
    "BUL_KATHOS_CHILDREN": _Metadata(
        level=50,
    ),
    "COW_KINGS_LEATHERS": _Metadata(
        level=20,
    ),
    "NAJS_ANCIENT_VESTIGE": _Metadata(
        level=43,
    ),
    "SANDERS_FOLLY": _Metadata(
        level=20,
    ),
}


class Set(Enum):
    """PD2 set categories."""

    CIVERBS_VESTMENTS = "Civerb's Vestments"
    HSARUS_DEFENSE = "Hsarus' Defense"
    CLEGLAWS_BRACE = "Cleglaw's Brace"
    IRATHAS_FINERY = "Iratha's Finery"
    ISENHARTS_ARMORY = "Isenhart's Armory"
    VIDALAS_RIG = "Vidala's Rig"
    MILABREGAS_REGALIA = "Milabrega's Regalia"
    CATHANS_TRAPS = "Cathan's Traps"
    TANCREDS_BATTLEGEAR = "Tancred's Battlegear"
    SIGONS_COMPLETE_STEEL = "Sigon's Complete Steel"
    INFERNAL_TOOLS = "Infernal Tools"
    BERSERKERS_ARSENAL = "Berserker's Arsenal"
    DEATHS_DISGUISE = "Death's Disguise"
    ANGELIC_RAIMENT = "Angelic Raiment"
    ARCTIC_GEAR = "Arctic Gear"
    ARCANNAS_TRICKS = "Arcanna's Tricks"
    NATALYAS_ODIUM = "Natalya's Odium"
    ALDURS_WATCHTOWER = "Aldur's Watchtower"
    IMMORTAL_KING = "Immortal King"
    TAL_RASHAS_WRAPPINGS = "Tal Rasha's Wrappings"
    GRISWOLDS_LEGACY = "Griswold's Legacy"
    TRANG_OULS_AVATAR = "Trang-Oul's Avatar"
    MAVINAS_BATTLE_HYMN = "M'avina's Battle Hymn"
    THE_DISCIPLE = "The Disciple"
    HEAVENS_BRETHREN = "Heaven's Brethren"
    ORPHANS_CALL = "Orphan's Call"
    HWANINS_MAJESTY = "Hwanin's Majesty"
    SAZABIS_GRAND_TRIBUTE = "Sazabi's Grand Tribute"
    BUL_KATHOS_CHILDREN = "Bul-Kathos' Children"
    COW_KINGS_LEATHERS = "Cow King's Leathers"
    NAJS_ANCIENT_VESTIGE = "Naj's Ancient Vestige"
    SANDERS_FOLLY = "Sander's Folly"

    @property
    def level(self) -> int:
        return _METADATA[self.name].level
