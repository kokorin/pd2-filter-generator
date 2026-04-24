# ruff: noqa: PIE796
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


class SetItem(Enum):
    """PD2 set item categories."""

    CIVERBS_WARD = _Metadata(
        set=Set.CIVERBS_VESTMENTS,
        lvl=13,
        lvl_req=9,
    )
    CIVERBS_ICON = _Metadata(
        set=Set.CIVERBS_VESTMENTS,
        lvl=13,
        lvl_req=9,
    )
    CIVERBS_CUDGEL = _Metadata(
        set=Set.CIVERBS_VESTMENTS,
        lvl=13,
        lvl_req=9,
    )
    HSARUS_IRON_HEEL = _Metadata(
        set=Set.HSARUS_DEFENSE,
        lvl=4,
        lvl_req=3,
    )
    HSARUS_IRON_FIST = _Metadata(
        set=Set.HSARUS_DEFENSE,
        lvl=4,
        lvl_req=3,
    )
    HSARUS_IRON_STAY = _Metadata(
        set=Set.HSARUS_DEFENSE,
        lvl=4,
        lvl_req=3,
    )
    CLEGLAWS_TOOTH = _Metadata(
        set=Set.CLEGLAWS_BRACE,
        lvl=6,
        lvl_req=4,
    )
    CLEGLAWS_CLAW = _Metadata(
        set=Set.CLEGLAWS_BRACE,
        lvl=6,
        lvl_req=4,
    )
    CLEGLAWS_PINCERS = _Metadata(
        set=Set.CLEGLAWS_BRACE,
        lvl=6,
        lvl_req=4,
    )
    IRATHAS_COLLAR = _Metadata(
        set=Set.IRATHAS_FINERY,
        lvl=21,
        lvl_req=15,
    )
    IRATHAS_CUFF = _Metadata(
        set=Set.IRATHAS_FINERY,
        lvl=21,
        lvl_req=15,
    )
    IRATHAS_COIL = _Metadata(
        set=Set.IRATHAS_FINERY,
        lvl=21,
        lvl_req=15,
    )
    IRATHAS_CORD = _Metadata(
        set=Set.IRATHAS_FINERY,
        lvl=21,
        lvl_req=15,
    )
    ISENHARTS_LIGHTBRAND = _Metadata(
        set=Set.ISENHARTS_ARMORY,
        lvl=11,
        lvl_req=8,
    )
    ISENHARTS_PARRY = _Metadata(
        set=Set.ISENHARTS_ARMORY,
        lvl=11,
        lvl_req=8,
    )
    ISENHARTS_CASE = _Metadata(
        set=Set.ISENHARTS_ARMORY,
        lvl=11,
        lvl_req=8,
    )
    ISENHARTS_HORNS = _Metadata(
        set=Set.ISENHARTS_ARMORY,
        lvl=11,
        lvl_req=8,
    )
    VIDALAS_BARB = _Metadata(
        set=Set.VIDALAS_RIG,
        lvl=19,
        lvl_req=14,
    )
    VIDALAS_FETLOCK = _Metadata(
        set=Set.VIDALAS_RIG,
        lvl=19,
        lvl_req=14,
    )
    VIDALAS_AMBUSH = _Metadata(
        set=Set.VIDALAS_RIG,
        lvl=19,
        lvl_req=14,
    )
    VIDALAS_SNARE = _Metadata(
        set=Set.VIDALAS_RIG,
        lvl=19,
        lvl_req=14,
    )
    MILABREGAS_ORB = _Metadata(
        set=Set.MILABREGAS_REGALIA,
        lvl=23,
        lvl_req=17,
    )
    MILABREGAS_ROD = _Metadata(
        set=Set.MILABREGAS_REGALIA,
        lvl=23,
        lvl_req=17,
    )
    MILABREGAS_DIADEM = _Metadata(
        set=Set.MILABREGAS_REGALIA,
        lvl=23,
        lvl_req=17,
    )
    MILABREGAS_ROBE = _Metadata(
        set=Set.MILABREGAS_REGALIA,
        lvl=23,
        lvl_req=17,
    )
    CATHANS_RULE = _Metadata(
        set=Set.CATHANS_TRAPS,
        lvl=15,
        lvl_req=11,
    )
    CATHANS_MESH = _Metadata(
        set=Set.CATHANS_TRAPS,
        lvl=15,
        lvl_req=11,
    )
    CATHANS_VISAGE = _Metadata(
        set=Set.CATHANS_TRAPS,
        lvl=15,
        lvl_req=11,
    )
    CATHANS_SIGIL = _Metadata(
        set=Set.CATHANS_TRAPS,
        lvl=15,
        lvl_req=11,
    )
    CATHANS_SEAL = _Metadata(
        set=Set.CATHANS_TRAPS,
        lvl=15,
        lvl_req=11,
    )
    TANCREDS_CROWBILL = _Metadata(
        set=Set.TANCREDS_BATTLEGEAR,
        lvl=27,
        lvl_req=20,
    )
    TANCREDS_SPINE = _Metadata(
        set=Set.TANCREDS_BATTLEGEAR,
        lvl=27,
        lvl_req=20,
    )
    TANCREDS_HOBNAILS = _Metadata(
        set=Set.TANCREDS_BATTLEGEAR,
        lvl=27,
        lvl_req=20,
    )
    TANCREDS_WEIRD = _Metadata(
        set=Set.TANCREDS_BATTLEGEAR,
        lvl=27,
        lvl_req=20,
    )
    TANCREDS_SKULL = _Metadata(
        set=Set.TANCREDS_BATTLEGEAR,
        lvl=27,
        lvl_req=20,
    )
    SIGONS_GAGE = _Metadata(
        set=Set.SIGONS_COMPLETE_STEEL,
        lvl=9,
        lvl_req=6,
    )
    SIGONS_VISOR = _Metadata(
        set=Set.SIGONS_COMPLETE_STEEL,
        lvl=9,
        lvl_req=6,
    )
    SIGONS_SHELTER = _Metadata(
        set=Set.SIGONS_COMPLETE_STEEL,
        lvl=9,
        lvl_req=6,
    )
    SIGONS_SABOT = _Metadata(
        set=Set.SIGONS_COMPLETE_STEEL,
        lvl=9,
        lvl_req=6,
    )
    SIGONS_WRAP = _Metadata(
        set=Set.SIGONS_COMPLETE_STEEL,
        lvl=9,
        lvl_req=6,
    )
    SIGONS_GUARD = _Metadata(
        set=Set.SIGONS_COMPLETE_STEEL,
        lvl=9,
        lvl_req=6,
    )
    INFERNAL_CRANIUM = _Metadata(
        set=Set.INFERNAL_TOOLS,
        lvl=7,
        lvl_req=5,
    )
    INFERNAL_SPIRE = _Metadata(
        set=Set.INFERNAL_TOOLS,
        lvl=7,
        lvl_req=5,
    )
    INFERNAL_SIGN = _Metadata(
        set=Set.INFERNAL_TOOLS,
        lvl=7,
        lvl_req=5,
    )
    BERSERKERS_HEADGEAR = _Metadata(
        set=Set.BERSERKERS_ARSENAL,
        lvl=5,
        lvl_req=3,
    )
    BERSERKERS_HAUBERK = _Metadata(
        set=Set.BERSERKERS_ARSENAL,
        lvl=5,
        lvl_req=3,
    )
    BERSERKERS_HATCHET = _Metadata(
        set=Set.BERSERKERS_ARSENAL,
        lvl=5,
        lvl_req=3,
    )
    DEATHS_HAND = _Metadata(
        set=Set.DEATHS_DISGUISE,
        lvl=8,
        lvl_req=6,
    )
    DEATHS_GUARD = _Metadata(
        set=Set.DEATHS_DISGUISE,
        lvl=8,
        lvl_req=6,
    )
    DEATHS_TOUCH = _Metadata(
        set=Set.DEATHS_DISGUISE,
        lvl=8,
        lvl_req=6,
    )
    ANGELIC_SICKLE = _Metadata(
        set=Set.ANGELIC_RAIMENT,
        lvl=17,
        lvl_req=12,
    )
    ANGELIC_MANTLE = _Metadata(
        set=Set.ANGELIC_RAIMENT,
        lvl=17,
        lvl_req=12,
    )
    ANGELIC_HALO = _Metadata(
        set=Set.ANGELIC_RAIMENT,
        lvl=17,
        lvl_req=12,
    )
    ANGELIC_WINGS = _Metadata(
        set=Set.ANGELIC_RAIMENT,
        lvl=17,
        lvl_req=12,
    )
    ARCTIC_HORN = _Metadata(
        set=Set.ARCTIC_GEAR,
        lvl=3,
        lvl_req=2,
    )
    ARCTIC_FURS = _Metadata(
        set=Set.ARCTIC_GEAR,
        lvl=3,
        lvl_req=2,
    )
    ARCTIC_BINDING = _Metadata(
        set=Set.ARCTIC_GEAR,
        lvl=3,
        lvl_req=2,
    )
    ARCTIC_MITTS = _Metadata(
        set=Set.ARCTIC_GEAR,
        lvl=3,
        lvl_req=2,
    )
    ARCANNAS_SIGN = _Metadata(
        set=Set.ARCANNAS_TRICKS,
        lvl=20,
        lvl_req=15,
    )
    ARCANNAS_DEATHWAND = _Metadata(
        set=Set.ARCANNAS_TRICKS,
        lvl=20,
        lvl_req=15,
    )
    ARCANNAS_HEAD = _Metadata(
        set=Set.ARCANNAS_TRICKS,
        lvl=20,
        lvl_req=15,
    )
    ARCANNAS_FLESH = _Metadata(
        set=Set.ARCANNAS_TRICKS,
        lvl=20,
        lvl_req=15,
    )
    NATALYAS_TOTEM = _Metadata(
        set=Set.NATALYAS_ODIUM,
        lvl=22,
        lvl_req=59,
    )
    NATALYAS_MARK = _Metadata(
        set=Set.NATALYAS_ODIUM,
        lvl=22,
        lvl_req=79,
    )
    NATALYAS_SHADOW = _Metadata(
        set=Set.NATALYAS_ODIUM,
        lvl=22,
        lvl_req=73,
    )
    NATALYAS_SOUL = _Metadata(
        set=Set.NATALYAS_ODIUM,
        lvl=22,
        lvl_req=25,
    )
    ALDURS_STONY_GAZE = _Metadata(
        set=Set.ALDURS_WATCHTOWER,
        lvl=29,
        lvl_req=36,
    )
    ALDURS_DECEPTION = _Metadata(
        set=Set.ALDURS_WATCHTOWER,
        lvl=29,
        lvl_req=76,
    )
    ALDURS_RHYTHM = _Metadata(
        set=Set.ALDURS_WATCHTOWER,
        lvl=29,
        lvl_req=42,
    )
    ALDURS_ADVANCE = _Metadata(
        set=Set.ALDURS_WATCHTOWER,
        lvl=29,
        lvl_req=45,
    )
    IMMORTAL_KINGS_WILL = _Metadata(
        set=Set.IMMORTAL_KING,
        lvl=37,
        lvl_req=47,
    )
    IMMORTAL_KINGS_SOUL_CAGE = _Metadata(
        set=Set.IMMORTAL_KING,
        lvl=37,
        lvl_req=76,
    )
    IMMORTAL_KINGS_DETAIL = _Metadata(
        set=Set.IMMORTAL_KING,
        lvl=37,
        lvl_req=29,
    )
    IMMORTAL_KINGS_FORGE = _Metadata(
        set=Set.IMMORTAL_KING,
        lvl=37,
        lvl_req=30,
    )
    IMMORTAL_KINGS_PILLAR = _Metadata(
        set=Set.IMMORTAL_KING,
        lvl=37,
        lvl_req=31,
    )
    IMMORTAL_KINGS_STONE_CRUSHER = _Metadata(
        set=Set.IMMORTAL_KING,
        lvl=37,
        lvl_req=76,
    )
    TAL_RASHAS_FINE_SPUN_CLOTH = _Metadata(
        set=Set.TAL_RASHAS_WRAPPINGS,
        lvl=26,
        lvl_req=53,
    )
    TAL_RASHAS_ADJUDICATION = _Metadata(
        set=Set.TAL_RASHAS_WRAPPINGS,
        lvl=26,
        lvl_req=67,
    )
    TAL_RASHAS_LIDLESS_EYE = _Metadata(
        set=Set.TAL_RASHAS_WRAPPINGS,
        lvl=26,
        lvl_req=65,
    )
    TAL_RASHAS_GUARDIANSHIP = _Metadata(
        set=Set.TAL_RASHAS_WRAPPINGS,
        lvl=26,
        lvl_req=71,
    )
    TAL_RASHAS_HORADRIC_CREST = _Metadata(
        set=Set.TAL_RASHAS_WRAPPINGS,
        lvl=26,
        lvl_req=66,
    )
    GRISWOLDS_VALOR = _Metadata(
        set=Set.GRISWOLDS_LEGACY,
        lvl=44,
        lvl_req=69,
    )
    GRISWOLDS_HEART = _Metadata(
        set=Set.GRISWOLDS_LEGACY,
        lvl=44,
        lvl_req=45,
    )
    GRISWOLDS_REDEMPTION = _Metadata(
        set=Set.GRISWOLDS_LEGACY,
        lvl=44,
        lvl_req=53,
    )
    GRISWOLDS_HONOR = _Metadata(
        set=Set.GRISWOLDS_LEGACY,
        lvl=44,
        lvl_req=68,
    )
    TRANG_OULS_GUISE = _Metadata(
        set=Set.TRANG_OULS_AVATAR,
        lvl=32,
        lvl_req=65,
    )
    TRANG_OULS_SCALES = _Metadata(
        set=Set.TRANG_OULS_AVATAR,
        lvl=32,
        lvl_req=49,
    )
    TRANG_OULS_WING = _Metadata(
        set=Set.TRANG_OULS_AVATAR,
        lvl=32,
        lvl_req=54,
    )
    TRANG_OULS_CLAWS = _Metadata(
        set=Set.TRANG_OULS_AVATAR,
        lvl=32,
        lvl_req=45,
    )
    TRANG_OULS_GIRTH = _Metadata(
        set=Set.TRANG_OULS_AVATAR,
        lvl=32,
        lvl_req=47,
    )
    MAVINAS_TRUE_SIGHT = _Metadata(
        set=Set.MAVINAS_BATTLE_HYMN,
        lvl=21,
        lvl_req=59,
    )
    MAVINAS_EMBRACE = _Metadata(
        set=Set.MAVINAS_BATTLE_HYMN,
        lvl=21,
        lvl_req=70,
    )
    MAVINAS_ICY_CLUTCH = _Metadata(
        set=Set.MAVINAS_BATTLE_HYMN,
        lvl=21,
        lvl_req=32,
    )
    MAVINAS_TENET = _Metadata(
        set=Set.MAVINAS_BATTLE_HYMN,
        lvl=21,
        lvl_req=45,
    )
    MAVINAS_CASTER = _Metadata(
        set=Set.MAVINAS_BATTLE_HYMN,
        lvl=21,
        lvl_req=70,
    )
    TELLING_OF_BEADS = _Metadata(
        set=Set.THE_DISCIPLE,
        lvl=39,
        lvl_req=30,
    )
    LAYING_OF_HANDS = _Metadata(
        set=Set.THE_DISCIPLE,
        lvl=39,
        lvl_req=63,
    )
    RITE_OF_PASSAGE = _Metadata(
        set=Set.THE_DISCIPLE,
        lvl=39,
        lvl_req=29,
    )
    DARK_ADHERENT = _Metadata(
        set=Set.THE_DISCIPLE,
        lvl=39,
        lvl_req=43,
    )
    CREDENDUM = _Metadata(
        set=Set.THE_DISCIPLE,
        lvl=39,
        lvl_req=65,
    )
    DANGOONS_TEACHING = _Metadata(
        set=Set.HEAVENS_BRETHREN,
        lvl=55,
        lvl_req=68,
    )
    TAEBAEKS_GLORY = _Metadata(
        set=Set.HEAVENS_BRETHREN,
        lvl=55,
        lvl_req=81,
    )
    HAEMOSUS_ADAMANT = _Metadata(
        set=Set.HEAVENS_BRETHREN,
        lvl=55,
        lvl_req=44,
    )
    ONDALS_ALMIGHTY = _Metadata(
        set=Set.HEAVENS_BRETHREN,
        lvl=55,
        lvl_req=69,
    )
    GUILLAUMES_FACE = _Metadata(
        set=Set.ORPHANS_CALL,
        lvl=41,
        lvl_req=34,
    )
    WILHELMS_PRIDE = _Metadata(
        set=Set.ORPHANS_CALL,
        lvl=41,
        lvl_req=42,
    )
    MAGNUS_SKIN = _Metadata(
        set=Set.ORPHANS_CALL,
        lvl=41,
        lvl_req=37,
    )
    WHITSTANS_GUARD = _Metadata(
        set=Set.ORPHANS_CALL,
        lvl=41,
        lvl_req=29,
    )
    HWANINS_SPLENDOR = _Metadata(
        set=Set.HWANINS_MAJESTY,
        lvl=28,
        lvl_req=45,
    )
    HWANINS_REFUGE = _Metadata(
        set=Set.HWANINS_MAJESTY,
        lvl=28,
        lvl_req=30,
    )
    HWANINS_BLESSING = _Metadata(
        set=Set.HWANINS_MAJESTY,
        lvl=28,
        lvl_req=35,
    )
    HWANINS_JUSTICE = _Metadata(
        set=Set.HWANINS_MAJESTY,
        lvl=28,
        lvl_req=28,
    )
    SAZABIS_COBALT_REDEEMER = _Metadata(
        set=Set.SAZABIS_GRAND_TRIBUTE,
        lvl=34,
        lvl_req=73,
    )
    SAZABIS_GHOST_LIBERATOR = _Metadata(
        set=Set.SAZABIS_GRAND_TRIBUTE,
        lvl=34,
        lvl_req=67,
    )
    SAZABIS_MENTAL_SHEATH = _Metadata(
        set=Set.SAZABIS_GRAND_TRIBUTE,
        lvl=34,
        lvl_req=43,
    )
    BUL_KATHOS_SACRED_CHARGE = _Metadata(
        set=Set.BUL_KATHOS_CHILDREN,
        lvl=50,
        lvl_req=61,
    )
    BUL_KATHOS_TRIBAL_GUARDIAN = _Metadata(
        set=Set.BUL_KATHOS_CHILDREN,
        lvl=50,
        lvl_req=54,
    )
    BUL_KATHOS_DEATH_BAND = _Metadata(
        set=Set.BUL_KATHOS_CHILDREN,
        lvl=50,
        lvl_req=69,
    )
    COW_KINGS_HORNS = _Metadata(
        set=Set.COW_KINGS_LEATHERS,
        lvl=20,
        lvl_req=25,
    )
    COW_KINGS_HIDE = _Metadata(
        set=Set.COW_KINGS_LEATHERS,
        lvl=20,
        lvl_req=18,
    )
    COW_KINGS_HOOVES = _Metadata(
        set=Set.COW_KINGS_LEATHERS,
        lvl=20,
        lvl_req=13,
    )
    NAJS_PUZZLER = _Metadata(
        set=Set.NAJS_ANCIENT_VESTIGE,
        lvl=43,
        lvl_req=78,
    )
    NAJS_LIGHT_PLATE = _Metadata(
        set=Set.NAJS_ANCIENT_VESTIGE,
        lvl=43,
        lvl_req=71,
    )
    NAJS_CIRCLET = _Metadata(
        set=Set.NAJS_ANCIENT_VESTIGE,
        lvl=43,
        lvl_req=28,
    )
    SANDERS_PARAGON = _Metadata(
        set=Set.SANDERS_FOLLY,
        lvl=20,
        lvl_req=25,
    )
    SANDERS_RIPRAP = _Metadata(
        set=Set.SANDERS_FOLLY,
        lvl=20,
        lvl_req=20,
    )
    SANDERS_TABOO = _Metadata(
        set=Set.SANDERS_FOLLY,
        lvl=20,
        lvl_req=28,
    )
    SANDERS_SUPERSTITION = _Metadata(
        set=Set.SANDERS_FOLLY,
        lvl=20,
        lvl_req=25,
    )

    @property
    def set(self) -> Set:
        return self.value.set

    @property
    def lvl(self) -> int:
        return self.value.lvl

    @property
    def lvl_req(self) -> int:
        return self.value.lvl_req
