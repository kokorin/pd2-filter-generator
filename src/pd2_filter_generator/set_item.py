"""
Generated SetItem enum from PD2 data.

DO NOT EDIT MANUALLY - regenerate with: hatch run ./scripts/generate.py generate
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from pd2_filter_generator.set import Set


@dataclass(frozen=True)
class _Metadata:
    """Item type metadata."""

    set: Set  # "set"
    lvl: int  # "lvl"
    lvl_req: int  # "lvl req"


_METADATA: dict[str, _Metadata] = {
    "CIVERBS_WARD": _Metadata(
        set=Set("Civerb's Vestments"),
        lvl=13,
        lvl_req=9,
    ),
    "CIVERBS_ICON": _Metadata(
        set=Set("Civerb's Vestments"),
        lvl=13,
        lvl_req=9,
    ),
    "CIVERBS_CUDGEL": _Metadata(
        set=Set("Civerb's Vestments"),
        lvl=13,
        lvl_req=9,
    ),
    "HSARUS_IRON_HEEL": _Metadata(
        set=Set("Hsarus' Defense"),
        lvl=4,
        lvl_req=3,
    ),
    "HSARUS_IRON_FIST": _Metadata(
        set=Set("Hsarus' Defense"),
        lvl=4,
        lvl_req=3,
    ),
    "HSARUS_IRON_STAY": _Metadata(
        set=Set("Hsarus' Defense"),
        lvl=4,
        lvl_req=3,
    ),
    "CLEGLAWS_TOOTH": _Metadata(
        set=Set("Cleglaw's Brace"),
        lvl=6,
        lvl_req=4,
    ),
    "CLEGLAWS_CLAW": _Metadata(
        set=Set("Cleglaw's Brace"),
        lvl=6,
        lvl_req=4,
    ),
    "CLEGLAWS_PINCERS": _Metadata(
        set=Set("Cleglaw's Brace"),
        lvl=6,
        lvl_req=4,
    ),
    "IRATHAS_COLLAR": _Metadata(
        set=Set("Iratha's Finery"),
        lvl=21,
        lvl_req=15,
    ),
    "IRATHAS_CUFF": _Metadata(
        set=Set("Iratha's Finery"),
        lvl=21,
        lvl_req=15,
    ),
    "IRATHAS_COIL": _Metadata(
        set=Set("Iratha's Finery"),
        lvl=21,
        lvl_req=15,
    ),
    "IRATHAS_CORD": _Metadata(
        set=Set("Iratha's Finery"),
        lvl=21,
        lvl_req=15,
    ),
    "ISENHARTS_LIGHTBRAND": _Metadata(
        set=Set("Isenhart's Armory"),
        lvl=11,
        lvl_req=8,
    ),
    "ISENHARTS_PARRY": _Metadata(
        set=Set("Isenhart's Armory"),
        lvl=11,
        lvl_req=8,
    ),
    "ISENHARTS_CASE": _Metadata(
        set=Set("Isenhart's Armory"),
        lvl=11,
        lvl_req=8,
    ),
    "ISENHARTS_HORNS": _Metadata(
        set=Set("Isenhart's Armory"),
        lvl=11,
        lvl_req=8,
    ),
    "VIDALAS_BARB": _Metadata(
        set=Set("Vidala's Rig"),
        lvl=19,
        lvl_req=14,
    ),
    "VIDALAS_FETLOCK": _Metadata(
        set=Set("Vidala's Rig"),
        lvl=19,
        lvl_req=14,
    ),
    "VIDALAS_AMBUSH": _Metadata(
        set=Set("Vidala's Rig"),
        lvl=19,
        lvl_req=14,
    ),
    "VIDALAS_SNARE": _Metadata(
        set=Set("Vidala's Rig"),
        lvl=19,
        lvl_req=14,
    ),
    "MILABREGAS_ORB": _Metadata(
        set=Set("Milabrega's Regalia"),
        lvl=23,
        lvl_req=17,
    ),
    "MILABREGAS_ROD": _Metadata(
        set=Set("Milabrega's Regalia"),
        lvl=23,
        lvl_req=17,
    ),
    "MILABREGAS_DIADEM": _Metadata(
        set=Set("Milabrega's Regalia"),
        lvl=23,
        lvl_req=17,
    ),
    "MILABREGAS_ROBE": _Metadata(
        set=Set("Milabrega's Regalia"),
        lvl=23,
        lvl_req=17,
    ),
    "CATHANS_RULE": _Metadata(
        set=Set("Cathan's Traps"),
        lvl=15,
        lvl_req=11,
    ),
    "CATHANS_MESH": _Metadata(
        set=Set("Cathan's Traps"),
        lvl=15,
        lvl_req=11,
    ),
    "CATHANS_VISAGE": _Metadata(
        set=Set("Cathan's Traps"),
        lvl=15,
        lvl_req=11,
    ),
    "CATHANS_SIGIL": _Metadata(
        set=Set("Cathan's Traps"),
        lvl=15,
        lvl_req=11,
    ),
    "CATHANS_SEAL": _Metadata(
        set=Set("Cathan's Traps"),
        lvl=15,
        lvl_req=11,
    ),
    "TANCREDS_CROWBILL": _Metadata(
        set=Set("Tancred's Battlegear"),
        lvl=27,
        lvl_req=20,
    ),
    "TANCREDS_SPINE": _Metadata(
        set=Set("Tancred's Battlegear"),
        lvl=27,
        lvl_req=20,
    ),
    "TANCREDS_HOBNAILS": _Metadata(
        set=Set("Tancred's Battlegear"),
        lvl=27,
        lvl_req=20,
    ),
    "TANCREDS_WEIRD": _Metadata(
        set=Set("Tancred's Battlegear"),
        lvl=27,
        lvl_req=20,
    ),
    "TANCREDS_SKULL": _Metadata(
        set=Set("Tancred's Battlegear"),
        lvl=27,
        lvl_req=20,
    ),
    "SIGONS_GAGE": _Metadata(
        set=Set("Sigon's Complete Steel"),
        lvl=9,
        lvl_req=6,
    ),
    "SIGONS_VISOR": _Metadata(
        set=Set("Sigon's Complete Steel"),
        lvl=9,
        lvl_req=6,
    ),
    "SIGONS_SHELTER": _Metadata(
        set=Set("Sigon's Complete Steel"),
        lvl=9,
        lvl_req=6,
    ),
    "SIGONS_SABOT": _Metadata(
        set=Set("Sigon's Complete Steel"),
        lvl=9,
        lvl_req=6,
    ),
    "SIGONS_WRAP": _Metadata(
        set=Set("Sigon's Complete Steel"),
        lvl=9,
        lvl_req=6,
    ),
    "SIGONS_GUARD": _Metadata(
        set=Set("Sigon's Complete Steel"),
        lvl=9,
        lvl_req=6,
    ),
    "INFERNAL_CRANIUM": _Metadata(
        set=Set("Infernal Tools"),
        lvl=7,
        lvl_req=5,
    ),
    "INFERNAL_SPIRE": _Metadata(
        set=Set("Infernal Tools"),
        lvl=7,
        lvl_req=5,
    ),
    "INFERNAL_SIGN": _Metadata(
        set=Set("Infernal Tools"),
        lvl=7,
        lvl_req=5,
    ),
    "BERSERKERS_HEADGEAR": _Metadata(
        set=Set("Berserker's Arsenal"),
        lvl=5,
        lvl_req=3,
    ),
    "BERSERKERS_HAUBERK": _Metadata(
        set=Set("Berserker's Arsenal"),
        lvl=5,
        lvl_req=3,
    ),
    "BERSERKERS_HATCHET": _Metadata(
        set=Set("Berserker's Arsenal"),
        lvl=5,
        lvl_req=3,
    ),
    "DEATHS_HAND": _Metadata(
        set=Set("Death's Disguise"),
        lvl=8,
        lvl_req=6,
    ),
    "DEATHS_GUARD": _Metadata(
        set=Set("Death's Disguise"),
        lvl=8,
        lvl_req=6,
    ),
    "DEATHS_TOUCH": _Metadata(
        set=Set("Death's Disguise"),
        lvl=8,
        lvl_req=6,
    ),
    "ANGELIC_SICKLE": _Metadata(
        set=Set("Angelic Raiment"),
        lvl=17,
        lvl_req=12,
    ),
    "ANGELIC_MANTLE": _Metadata(
        set=Set("Angelic Raiment"),
        lvl=17,
        lvl_req=12,
    ),
    "ANGELIC_HALO": _Metadata(
        set=Set("Angelic Raiment"),
        lvl=17,
        lvl_req=12,
    ),
    "ANGELIC_WINGS": _Metadata(
        set=Set("Angelic Raiment"),
        lvl=17,
        lvl_req=12,
    ),
    "ARCTIC_HORN": _Metadata(
        set=Set("Arctic Gear"),
        lvl=3,
        lvl_req=2,
    ),
    "ARCTIC_FURS": _Metadata(
        set=Set("Arctic Gear"),
        lvl=3,
        lvl_req=2,
    ),
    "ARCTIC_BINDING": _Metadata(
        set=Set("Arctic Gear"),
        lvl=3,
        lvl_req=2,
    ),
    "ARCTIC_MITTS": _Metadata(
        set=Set("Arctic Gear"),
        lvl=3,
        lvl_req=2,
    ),
    "ARCANNAS_SIGN": _Metadata(
        set=Set("Arcanna's Tricks"),
        lvl=20,
        lvl_req=15,
    ),
    "ARCANNAS_DEATHWAND": _Metadata(
        set=Set("Arcanna's Tricks"),
        lvl=20,
        lvl_req=15,
    ),
    "ARCANNAS_HEAD": _Metadata(
        set=Set("Arcanna's Tricks"),
        lvl=20,
        lvl_req=15,
    ),
    "ARCANNAS_FLESH": _Metadata(
        set=Set("Arcanna's Tricks"),
        lvl=20,
        lvl_req=15,
    ),
    "NATALYAS_TOTEM": _Metadata(
        set=Set("Natalya's Odium"),
        lvl=22,
        lvl_req=59,
    ),
    "NATALYAS_MARK": _Metadata(
        set=Set("Natalya's Odium"),
        lvl=22,
        lvl_req=79,
    ),
    "NATALYAS_SHADOW": _Metadata(
        set=Set("Natalya's Odium"),
        lvl=22,
        lvl_req=73,
    ),
    "NATALYAS_SOUL": _Metadata(
        set=Set("Natalya's Odium"),
        lvl=22,
        lvl_req=25,
    ),
    "ALDURS_STONY_GAZE": _Metadata(
        set=Set("Aldur's Watchtower"),
        lvl=29,
        lvl_req=36,
    ),
    "ALDURS_DECEPTION": _Metadata(
        set=Set("Aldur's Watchtower"),
        lvl=29,
        lvl_req=76,
    ),
    "ALDURS_RHYTHM": _Metadata(
        set=Set("Aldur's Watchtower"),
        lvl=29,
        lvl_req=42,
    ),
    "ALDURS_ADVANCE": _Metadata(
        set=Set("Aldur's Watchtower"),
        lvl=29,
        lvl_req=45,
    ),
    "IMMORTAL_KINGS_WILL": _Metadata(
        set=Set("Immortal King"),
        lvl=37,
        lvl_req=47,
    ),
    "IMMORTAL_KINGS_SOUL_CAGE": _Metadata(
        set=Set("Immortal King"),
        lvl=37,
        lvl_req=76,
    ),
    "IMMORTAL_KINGS_DETAIL": _Metadata(
        set=Set("Immortal King"),
        lvl=37,
        lvl_req=29,
    ),
    "IMMORTAL_KINGS_FORGE": _Metadata(
        set=Set("Immortal King"),
        lvl=37,
        lvl_req=30,
    ),
    "IMMORTAL_KINGS_PILLAR": _Metadata(
        set=Set("Immortal King"),
        lvl=37,
        lvl_req=31,
    ),
    "IMMORTAL_KINGS_STONE_CRUSHER": _Metadata(
        set=Set("Immortal King"),
        lvl=37,
        lvl_req=76,
    ),
    "TAL_RASHAS_FINE_SPUN_CLOTH": _Metadata(
        set=Set("Tal Rasha's Wrappings"),
        lvl=26,
        lvl_req=53,
    ),
    "TAL_RASHAS_ADJUDICATION": _Metadata(
        set=Set("Tal Rasha's Wrappings"),
        lvl=26,
        lvl_req=67,
    ),
    "TAL_RASHAS_LIDLESS_EYE": _Metadata(
        set=Set("Tal Rasha's Wrappings"),
        lvl=26,
        lvl_req=65,
    ),
    "TAL_RASHAS_GUARDIANSHIP": _Metadata(
        set=Set("Tal Rasha's Wrappings"),
        lvl=26,
        lvl_req=71,
    ),
    "TAL_RASHAS_HORADRIC_CREST": _Metadata(
        set=Set("Tal Rasha's Wrappings"),
        lvl=26,
        lvl_req=66,
    ),
    "GRISWOLDS_VALOR": _Metadata(
        set=Set("Griswold's Legacy"),
        lvl=44,
        lvl_req=69,
    ),
    "GRISWOLDS_HEART": _Metadata(
        set=Set("Griswold's Legacy"),
        lvl=44,
        lvl_req=45,
    ),
    "GRISWOLDS_REDEMPTION": _Metadata(
        set=Set("Griswold's Legacy"),
        lvl=44,
        lvl_req=53,
    ),
    "GRISWOLDS_HONOR": _Metadata(
        set=Set("Griswold's Legacy"),
        lvl=44,
        lvl_req=68,
    ),
    "TRANG_OULS_GUISE": _Metadata(
        set=Set("Trang-Oul's Avatar"),
        lvl=32,
        lvl_req=65,
    ),
    "TRANG_OULS_SCALES": _Metadata(
        set=Set("Trang-Oul's Avatar"),
        lvl=32,
        lvl_req=49,
    ),
    "TRANG_OULS_WING": _Metadata(
        set=Set("Trang-Oul's Avatar"),
        lvl=32,
        lvl_req=54,
    ),
    "TRANG_OULS_CLAWS": _Metadata(
        set=Set("Trang-Oul's Avatar"),
        lvl=32,
        lvl_req=45,
    ),
    "TRANG_OULS_GIRTH": _Metadata(
        set=Set("Trang-Oul's Avatar"),
        lvl=32,
        lvl_req=47,
    ),
    "MAVINAS_TRUE_SIGHT": _Metadata(
        set=Set("M'avina's Battle Hymn"),
        lvl=21,
        lvl_req=59,
    ),
    "MAVINAS_EMBRACE": _Metadata(
        set=Set("M'avina's Battle Hymn"),
        lvl=21,
        lvl_req=70,
    ),
    "MAVINAS_ICY_CLUTCH": _Metadata(
        set=Set("M'avina's Battle Hymn"),
        lvl=21,
        lvl_req=32,
    ),
    "MAVINAS_TENET": _Metadata(
        set=Set("M'avina's Battle Hymn"),
        lvl=21,
        lvl_req=45,
    ),
    "MAVINAS_CASTER": _Metadata(
        set=Set("M'avina's Battle Hymn"),
        lvl=21,
        lvl_req=70,
    ),
    "TELLING_OF_BEADS": _Metadata(
        set=Set("The Disciple"),
        lvl=39,
        lvl_req=30,
    ),
    "LAYING_OF_HANDS": _Metadata(
        set=Set("The Disciple"),
        lvl=39,
        lvl_req=63,
    ),
    "RITE_OF_PASSAGE": _Metadata(
        set=Set("The Disciple"),
        lvl=39,
        lvl_req=29,
    ),
    "DARK_ADHERENT": _Metadata(
        set=Set("The Disciple"),
        lvl=39,
        lvl_req=43,
    ),
    "CREDENDUM": _Metadata(
        set=Set("The Disciple"),
        lvl=39,
        lvl_req=65,
    ),
    "DANGOONS_TEACHING": _Metadata(
        set=Set("Heaven's Brethren"),
        lvl=55,
        lvl_req=68,
    ),
    "TAEBAEKS_GLORY": _Metadata(
        set=Set("Heaven's Brethren"),
        lvl=55,
        lvl_req=81,
    ),
    "HAEMOSUS_ADAMANT": _Metadata(
        set=Set("Heaven's Brethren"),
        lvl=55,
        lvl_req=44,
    ),
    "ONDALS_ALMIGHTY": _Metadata(
        set=Set("Heaven's Brethren"),
        lvl=55,
        lvl_req=69,
    ),
    "GUILLAUMES_FACE": _Metadata(
        set=Set("Orphan's Call"),
        lvl=41,
        lvl_req=34,
    ),
    "WILHELMS_PRIDE": _Metadata(
        set=Set("Orphan's Call"),
        lvl=41,
        lvl_req=42,
    ),
    "MAGNUS_SKIN": _Metadata(
        set=Set("Orphan's Call"),
        lvl=41,
        lvl_req=37,
    ),
    "WHITSTANS_GUARD": _Metadata(
        set=Set("Orphan's Call"),
        lvl=41,
        lvl_req=29,
    ),
    "HWANINS_SPLENDOR": _Metadata(
        set=Set("Hwanin's Majesty"),
        lvl=28,
        lvl_req=45,
    ),
    "HWANINS_REFUGE": _Metadata(
        set=Set("Hwanin's Majesty"),
        lvl=28,
        lvl_req=30,
    ),
    "HWANINS_BLESSING": _Metadata(
        set=Set("Hwanin's Majesty"),
        lvl=28,
        lvl_req=35,
    ),
    "HWANINS_JUSTICE": _Metadata(
        set=Set("Hwanin's Majesty"),
        lvl=28,
        lvl_req=28,
    ),
    "SAZABIS_COBALT_REDEEMER": _Metadata(
        set=Set("Sazabi's Grand Tribute"),
        lvl=34,
        lvl_req=73,
    ),
    "SAZABIS_GHOST_LIBERATOR": _Metadata(
        set=Set("Sazabi's Grand Tribute"),
        lvl=34,
        lvl_req=67,
    ),
    "SAZABIS_MENTAL_SHEATH": _Metadata(
        set=Set("Sazabi's Grand Tribute"),
        lvl=34,
        lvl_req=43,
    ),
    "BUL_KATHOS_SACRED_CHARGE": _Metadata(
        set=Set("Bul-Kathos' Children"),
        lvl=50,
        lvl_req=61,
    ),
    "BUL_KATHOS_TRIBAL_GUARDIAN": _Metadata(
        set=Set("Bul-Kathos' Children"),
        lvl=50,
        lvl_req=54,
    ),
    "BUL_KATHOS_DEATH_BAND": _Metadata(
        set=Set("Bul-Kathos' Children"),
        lvl=50,
        lvl_req=69,
    ),
    "COW_KINGS_HORNS": _Metadata(
        set=Set("Cow King's Leathers"),
        lvl=20,
        lvl_req=25,
    ),
    "COW_KINGS_HIDE": _Metadata(
        set=Set("Cow King's Leathers"),
        lvl=20,
        lvl_req=18,
    ),
    "COW_KINGS_HOOVES": _Metadata(
        set=Set("Cow King's Leathers"),
        lvl=20,
        lvl_req=13,
    ),
    "NAJS_PUZZLER": _Metadata(
        set=Set("Naj's Ancient Vestige"),
        lvl=43,
        lvl_req=78,
    ),
    "NAJS_LIGHT_PLATE": _Metadata(
        set=Set("Naj's Ancient Vestige"),
        lvl=43,
        lvl_req=71,
    ),
    "NAJS_CIRCLET": _Metadata(
        set=Set("Naj's Ancient Vestige"),
        lvl=43,
        lvl_req=28,
    ),
    "SANDERS_PARAGON": _Metadata(
        set=Set("Sander's Folly"),
        lvl=20,
        lvl_req=25,
    ),
    "SANDERS_RIPRAP": _Metadata(
        set=Set("Sander's Folly"),
        lvl=20,
        lvl_req=20,
    ),
    "SANDERS_TABOO": _Metadata(
        set=Set("Sander's Folly"),
        lvl=20,
        lvl_req=28,
    ),
    "SANDERS_SUPERSTITION": _Metadata(
        set=Set("Sander's Folly"),
        lvl=20,
        lvl_req=25,
    ),
}


class SetItem(Enum):
    """PD2 set item categories."""

    CIVERBS_WARD = "Civerb's Ward"
    CIVERBS_ICON = "Civerb's Icon"
    CIVERBS_CUDGEL = "Civerb's Cudgel"
    HSARUS_IRON_HEEL = "Hsarus' Iron Heel"
    HSARUS_IRON_FIST = "Hsarus' Iron Fist"
    HSARUS_IRON_STAY = "Hsarus' Iron Stay"
    CLEGLAWS_TOOTH = "Cleglaw's Tooth"
    CLEGLAWS_CLAW = "Cleglaw's Claw"
    CLEGLAWS_PINCERS = "Cleglaw's Pincers"
    IRATHAS_COLLAR = "Iratha's Collar"
    IRATHAS_CUFF = "Iratha's Cuff"
    IRATHAS_COIL = "Iratha's Coil"
    IRATHAS_CORD = "Iratha's Cord"
    ISENHARTS_LIGHTBRAND = "Isenhart's Lightbrand"
    ISENHARTS_PARRY = "Isenhart's Parry"
    ISENHARTS_CASE = "Isenhart's Case"
    ISENHARTS_HORNS = "Isenhart's Horns"
    VIDALAS_BARB = "Vidala's Barb"
    VIDALAS_FETLOCK = "Vidala's Fetlock"
    VIDALAS_AMBUSH = "Vidala's Ambush"
    VIDALAS_SNARE = "Vidala's Snare"
    MILABREGAS_ORB = "Milabrega's Orb"
    MILABREGAS_ROD = "Milabrega's Rod"
    MILABREGAS_DIADEM = "Milabrega's Diadem"
    MILABREGAS_ROBE = "Milabrega's Robe"
    CATHANS_RULE = "Cathan's Rule"
    CATHANS_MESH = "Cathan's Mesh"
    CATHANS_VISAGE = "Cathan's Visage"
    CATHANS_SIGIL = "Cathan's Sigil"
    CATHANS_SEAL = "Cathan's Seal"
    TANCREDS_CROWBILL = "Tancred's Crowbill"
    TANCREDS_SPINE = "Tancred's Spine"
    TANCREDS_HOBNAILS = "Tancred's Hobnails"
    TANCREDS_WEIRD = "Tancred's Weird"
    TANCREDS_SKULL = "Tancred's Skull"
    SIGONS_GAGE = "Sigon's Gage"
    SIGONS_VISOR = "Sigon's Visor"
    SIGONS_SHELTER = "Sigon's Shelter"
    SIGONS_SABOT = "Sigon's Sabot"
    SIGONS_WRAP = "Sigon's Wrap"
    SIGONS_GUARD = "Sigon's Guard"
    INFERNAL_CRANIUM = "Infernal Cranium"
    INFERNAL_SPIRE = "Infernal Spire"
    INFERNAL_SIGN = "Infernal Sign"
    BERSERKERS_HEADGEAR = "Berserker's Headgear"
    BERSERKERS_HAUBERK = "Berserker's Hauberk"
    BERSERKERS_HATCHET = "Berserker's Hatchet"
    DEATHS_HAND = "Death's Hand"
    DEATHS_GUARD = "Death's Guard"
    DEATHS_TOUCH = "Death's Touch"
    ANGELIC_SICKLE = "Angelic Sickle"
    ANGELIC_MANTLE = "Angelic Mantle"
    ANGELIC_HALO = "Angelic Halo"
    ANGELIC_WINGS = "Angelic Wings"
    ARCTIC_HORN = "Arctic Horn"
    ARCTIC_FURS = "Arctic Furs"
    ARCTIC_BINDING = "Arctic Binding"
    ARCTIC_MITTS = "Arctic Mitts"
    ARCANNAS_SIGN = "Arcanna's Sign"
    ARCANNAS_DEATHWAND = "Arcanna's Deathwand"
    ARCANNAS_HEAD = "Arcanna's Head"
    ARCANNAS_FLESH = "Arcanna's Flesh"
    NATALYAS_TOTEM = "Natalya's Totem"
    NATALYAS_MARK = "Natalya's Mark"
    NATALYAS_SHADOW = "Natalya's Shadow"
    NATALYAS_SOUL = "Natalya's Soul"
    ALDURS_STONY_GAZE = "Aldur's Stony Gaze"
    ALDURS_DECEPTION = "Aldur's Deception"
    ALDURS_RHYTHM = "Aldur's Rhythm"
    ALDURS_ADVANCE = "Aldur's Advance"
    IMMORTAL_KINGS_WILL = "Immortal King's Will"
    IMMORTAL_KINGS_SOUL_CAGE = "Immortal King's Soul Cage"
    IMMORTAL_KINGS_DETAIL = "Immortal King's Detail"
    IMMORTAL_KINGS_FORGE = "Immortal King's Forge"
    IMMORTAL_KINGS_PILLAR = "Immortal King's Pillar"
    IMMORTAL_KINGS_STONE_CRUSHER = "Immortal King's Stone Crusher"
    TAL_RASHAS_FINE_SPUN_CLOTH = "Tal Rasha's Fine-Spun Cloth"
    TAL_RASHAS_ADJUDICATION = "Tal Rasha's Adjudication"
    TAL_RASHAS_LIDLESS_EYE = "Tal Rasha's Lidless Eye"
    TAL_RASHAS_GUARDIANSHIP = "Tal Rasha's Guardianship"
    TAL_RASHAS_HORADRIC_CREST = "Tal Rasha's Horadric Crest"
    GRISWOLDS_VALOR = "Griswold's Valor"
    GRISWOLDS_HEART = "Griswold's Heart"
    GRISWOLDS_REDEMPTION = "Griswold's Redemption"
    GRISWOLDS_HONOR = "Griswold's Honor"
    TRANG_OULS_GUISE = "Trang-Oul's Guise"
    TRANG_OULS_SCALES = "Trang-Oul's Scales"
    TRANG_OULS_WING = "Trang-Oul's Wing"
    TRANG_OULS_CLAWS = "Trang-Oul's Claws"
    TRANG_OULS_GIRTH = "Trang-Oul's Girth"
    MAVINAS_TRUE_SIGHT = "M'avina's True Sight"
    MAVINAS_EMBRACE = "M'avina's Embrace"
    MAVINAS_ICY_CLUTCH = "M'avina's Icy Clutch"
    MAVINAS_TENET = "M'avina's Tenet"
    MAVINAS_CASTER = "M'avina's Caster"
    TELLING_OF_BEADS = "Telling of Beads"
    LAYING_OF_HANDS = "Laying of Hands"
    RITE_OF_PASSAGE = "Rite of Passage"
    DARK_ADHERENT = "Dark Adherent"
    CREDENDUM = "Credendum"
    DANGOONS_TEACHING = "Dangoon's Teaching"
    TAEBAEKS_GLORY = "Taebaek's Glory"
    HAEMOSUS_ADAMANT = "Haemosu's Adamant"
    ONDALS_ALMIGHTY = "Ondal's Almighty"
    GUILLAUMES_FACE = "Guillaume's Face"
    WILHELMS_PRIDE = "Wilhelm's Pride"
    MAGNUS_SKIN = "Magnus' Skin"
    WHITSTANS_GUARD = "Whitstan's Guard"
    HWANINS_SPLENDOR = "Hwanin's Splendor"
    HWANINS_REFUGE = "Hwanin's Refuge"
    HWANINS_BLESSING = "Hwanin's Blessing"
    HWANINS_JUSTICE = "Hwanin's Justice"
    SAZABIS_COBALT_REDEEMER = "Sazabi's Cobalt Redeemer"
    SAZABIS_GHOST_LIBERATOR = "Sazabi's Ghost Liberator"
    SAZABIS_MENTAL_SHEATH = "Sazabi's Mental Sheath"
    BUL_KATHOS_SACRED_CHARGE = "Bul-Kathos' Sacred Charge"
    BUL_KATHOS_TRIBAL_GUARDIAN = "Bul-Kathos' Tribal Guardian"
    BUL_KATHOS_DEATH_BAND = "Bul-Kathos' Death Band"
    COW_KINGS_HORNS = "Cow King's Horns"
    COW_KINGS_HIDE = "Cow King's Hide"
    COW_KINGS_HOOVES = "Cow King's Hooves"
    NAJS_PUZZLER = "Naj's Puzzler"
    NAJS_LIGHT_PLATE = "Naj's Light Plate"
    NAJS_CIRCLET = "Naj's Circlet"
    SANDERS_PARAGON = "Sander's Paragon"
    SANDERS_RIPRAP = "Sander's Riprap"
    SANDERS_TABOO = "Sander's Taboo"
    SANDERS_SUPERSTITION = "Sander's Superstition"

    @property
    def set(self) -> Set:
        return _METADATA[self.name].set

    @property
    def lvl(self) -> int:
        return _METADATA[self.name].lvl

    @property
    def lvl_req(self) -> int:
        return _METADATA[self.name].lvl_req
