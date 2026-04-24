"""
Generated Weapon enum from PD2 data.

DO NOT EDIT MANUALLY - regenerate with: hatch run ./scripts/generate.py generate
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from pd2_filter_generator.expression import BoolMixin, BoolRef


@dataclass(frozen=True)
class _Metadata:
    """Item type metadata."""

    type: str  # "type"
    type2: str  # "type2"


_METADATA: dict[str, _Metadata] = {
    "HAND_AXE": _Metadata(
        type="axe",
        type2="",
    ),
    "AXE": _Metadata(
        type="axe",
        type2="",
    ),
    "DOUBLE_AXE": _Metadata(
        type="axe",
        type2="",
    ),
    "MILITARY_PICK": _Metadata(
        type="axe",
        type2="",
    ),
    "WAR_AXE": _Metadata(
        type="axe",
        type2="",
    ),
    "LARGE_AXE": _Metadata(
        type="axe",
        type2="2han",
    ),
    "BROAD_AXE": _Metadata(
        type="axe",
        type2="2han",
    ),
    "BATTLE_AXE": _Metadata(
        type="axe",
        type2="2han",
    ),
    "GREAT_AXE": _Metadata(
        type="axe",
        type2="2han",
    ),
    "GIANT_AXE": _Metadata(
        type="axe",
        type2="2han",
    ),
    "WAND": _Metadata(
        type="wand",
        type2="",
    ),
    "YEW_WAND": _Metadata(
        type="wand",
        type2="",
    ),
    "BONE_WAND": _Metadata(
        type="wand",
        type2="",
    ),
    "GRIM_WAND": _Metadata(
        type="wand",
        type2="",
    ),
    "CLUB": _Metadata(
        type="club",
        type2="",
    ),
    "SCEPTER": _Metadata(
        type="scep",
        type2="",
    ),
    "GRAND_SCEPTER": _Metadata(
        type="scep",
        type2="",
    ),
    "WAR_SCEPTER": _Metadata(
        type="scep",
        type2="",
    ),
    "SPIKED_CLUB": _Metadata(
        type="club",
        type2="",
    ),
    "MACE": _Metadata(
        type="mace",
        type2="",
    ),
    "MORNING_STAR": _Metadata(
        type="mace",
        type2="",
    ),
    "FLAIL": _Metadata(
        type="mace",
        type2="",
    ),
    "WAR_HAMMER": _Metadata(
        type="hamm",
        type2="",
    ),
    "MAUL": _Metadata(
        type="hamm",
        type2="2han",
    ),
    "GREAT_MAUL": _Metadata(
        type="hamm",
        type2="2han",
    ),
    "SHORT_SWORD": _Metadata(
        type="swor",
        type2="",
    ),
    "SCIMITAR": _Metadata(
        type="swor",
        type2="",
    ),
    "SABRE": _Metadata(
        type="swor",
        type2="",
    ),
    "FALCHION": _Metadata(
        type="swor",
        type2="",
    ),
    "CRYSTAL_SWORD": _Metadata(
        type="swor",
        type2="crys",
    ),
    "BROAD_SWORD": _Metadata(
        type="swor",
        type2="",
    ),
    "LONG_SWORD": _Metadata(
        type="swor",
        type2="",
    ),
    "WAR_SWORD": _Metadata(
        type="swor",
        type2="",
    ),
    "TWO_HANDED_SWORD": _Metadata(
        type="swor",
        type2="2hsw",
    ),
    "CLAYMORE": _Metadata(
        type="swor",
        type2="2hsw",
    ),
    "GIANT_SWORD": _Metadata(
        type="swor",
        type2="2hsw",
    ),
    "BASTARD_SWORD": _Metadata(
        type="swor",
        type2="2hsw",
    ),
    "FLAMBERGE": _Metadata(
        type="swor",
        type2="2hsw",
    ),
    "GREAT_SWORD": _Metadata(
        type="swor",
        type2="2hsw",
    ),
    "DAGGER": _Metadata(
        type="knif",
        type2="",
    ),
    "DIRK": _Metadata(
        type="knif",
        type2="",
    ),
    "KRIS": _Metadata(
        type="knif",
        type2="",
    ),
    "BLADE": _Metadata(
        type="knif",
        type2="",
    ),
    "THROWING_KNIFE": _Metadata(
        type="tkni",
        type2="",
    ),
    "THROWING_AXE": _Metadata(
        type="taxe",
        type2="",
    ),
    "BALANCED_KNIFE": _Metadata(
        type="tkni",
        type2="",
    ),
    "BALANCED_AXE": _Metadata(
        type="taxe",
        type2="",
    ),
    "JAVELIN": _Metadata(
        type="jave",
        type2="",
    ),
    "PILUM": _Metadata(
        type="jave",
        type2="",
    ),
    "SHORT_SPEAR": _Metadata(
        type="jave",
        type2="",
    ),
    "GLAIVE": _Metadata(
        type="jave",
        type2="",
    ),
    "THROWING_SPEAR": _Metadata(
        type="jave",
        type2="",
    ),
    "SPEAR": _Metadata(
        type="spea",
        type2="2han",
    ),
    "TRIDENT": _Metadata(
        type="spea",
        type2="2han",
    ),
    "BRANDISTOCK": _Metadata(
        type="spea",
        type2="2han",
    ),
    "SPETUM": _Metadata(
        type="spea",
        type2="2han",
    ),
    "PIKE": _Metadata(
        type="spea",
        type2="2han",
    ),
    "BARDICHE": _Metadata(
        type="pole",
        type2="2han",
    ),
    "VOULGE": _Metadata(
        type="pole",
        type2="2han",
    ),
    "SCYTHE": _Metadata(
        type="sc9",
        type2="2han",
    ),
    "POLEAXE": _Metadata(
        type="pole",
        type2="2han",
    ),
    "HALBERD": _Metadata(
        type="pole",
        type2="2han",
    ),
    "WAR_SCYTHE": _Metadata(
        type="sc9",
        type2="2han",
    ),
    "SHORT_STAFF": _Metadata(
        type="staf",
        type2="2han",
    ),
    "LONG_STAFF": _Metadata(
        type="staf",
        type2="2han",
    ),
    "GNARLED_STAFF": _Metadata(
        type="staf",
        type2="2han",
    ),
    "BATTLE_STAFF": _Metadata(
        type="staf",
        type2="2han",
    ),
    "WAR_STAFF": _Metadata(
        type="staf",
        type2="2han",
    ),
    "SHORT_BOW": _Metadata(
        type="bow",
        type2="",
    ),
    "HUNTERS_BOW": _Metadata(
        type="bow",
        type2="",
    ),
    "LONG_BOW": _Metadata(
        type="bow",
        type2="",
    ),
    "COMPOSITE_BOW": _Metadata(
        type="bow",
        type2="",
    ),
    "SHORT_BATTLE_BOW": _Metadata(
        type="bow",
        type2="",
    ),
    "LONG_BATTLE_BOW": _Metadata(
        type="bow",
        type2="",
    ),
    "SHORT_WAR_BOW": _Metadata(
        type="bow",
        type2="",
    ),
    "LONG_WAR_BOW": _Metadata(
        type="bow",
        type2="",
    ),
    "LIGHT_CROSSBOW": _Metadata(
        type="xbow",
        type2="",
    ),
    "CROSSBOW": _Metadata(
        type="xbow",
        type2="",
    ),
    "HEAVY_CROSSBOW": _Metadata(
        type="xbow",
        type2="",
    ),
    "REPEATING_CROSSBOW": _Metadata(
        type="xbow",
        type2="",
    ),
    "DECOY_GIDBINN": _Metadata(
        type="knif",
        type2="",
    ),
    "THE_GIDBINN": _Metadata(
        type="knif",
        type2="",
    ),
    "WIRTS_LEG": _Metadata(
        type="club",
        type2="",
    ),
    "HORADRIC_MALUS": _Metadata(
        type="hamm",
        type2="",
    ),
    "HELL_FORGE_HAMMER": _Metadata(
        type="hamm",
        type2="",
    ),
    "HORADRIC_STAFF": _Metadata(
        type="staf",
        type2="2han",
    ),
    "SHAFT_OF_THE_HORADRIC_STAFF": _Metadata(
        type="staf",
        type2="2han",
    ),
    "HATCHET": _Metadata(
        type="axe",
        type2="",
    ),
    "CLEAVER": _Metadata(
        type="axe",
        type2="",
    ),
    "TWIN_AXE": _Metadata(
        type="axe",
        type2="",
    ),
    "CROWBILL": _Metadata(
        type="axe",
        type2="",
    ),
    "NAGA": _Metadata(
        type="axe",
        type2="",
    ),
    "MILITARY_AXE": _Metadata(
        type="axe",
        type2="2han",
    ),
    "BEARDED_AXE": _Metadata(
        type="axe",
        type2="2han",
    ),
    "TABAR": _Metadata(
        type="axe",
        type2="2han",
    ),
    "GOTHIC_AXE": _Metadata(
        type="axe",
        type2="2han",
    ),
    "ANCIENT_AXE": _Metadata(
        type="axe",
        type2="2han",
    ),
    "BURNT_WAND": _Metadata(
        type="wand",
        type2="",
    ),
    "PETRIFIED_WAND": _Metadata(
        type="wand",
        type2="",
    ),
    "TOMB_WAND": _Metadata(
        type="wand",
        type2="",
    ),
    "GRAVE_WAND": _Metadata(
        type="wand",
        type2="",
    ),
    "CUDGEL": _Metadata(
        type="club",
        type2="",
    ),
    "RUNE_SCEPTER": _Metadata(
        type="scep",
        type2="",
    ),
    "HOLY_WATER_SPRINKLER": _Metadata(
        type="scep",
        type2="",
    ),
    "DIVINE_SCEPTER": _Metadata(
        type="scep",
        type2="",
    ),
    "BARBED_CLUB": _Metadata(
        type="club",
        type2="",
    ),
    "FLANGED_MACE": _Metadata(
        type="mace",
        type2="",
    ),
    "JAGGED_STAR": _Metadata(
        type="mace",
        type2="",
    ),
    "KNOUT": _Metadata(
        type="mace",
        type2="",
    ),
    "BATTLE_HAMMER": _Metadata(
        type="hamm",
        type2="",
    ),
    "WAR_CLUB": _Metadata(
        type="hamm",
        type2="2han",
    ),
    "MARTEL_DE_FER": _Metadata(
        type="hamm",
        type2="2han",
    ),
    "GLADIUS": _Metadata(
        type="swor",
        type2="",
    ),
    "CUTLASS": _Metadata(
        type="swor",
        type2="",
    ),
    "SHAMSHIR": _Metadata(
        type="swor",
        type2="",
    ),
    "TULWAR": _Metadata(
        type="swor",
        type2="",
    ),
    "DIMENSIONAL_BLADE": _Metadata(
        type="swor",
        type2="crys",
    ),
    "BATTLE_SWORD": _Metadata(
        type="swor",
        type2="",
    ),
    "RUNE_SWORD": _Metadata(
        type="swor",
        type2="",
    ),
    "ANCIENT_SWORD": _Metadata(
        type="swor",
        type2="",
    ),
    "ESPANDON": _Metadata(
        type="swor",
        type2="2hsw",
    ),
    "DACIAN_FALX": _Metadata(
        type="swor",
        type2="2hsw",
    ),
    "TUSK_SWORD": _Metadata(
        type="swor",
        type2="2hsw",
    ),
    "GOTHIC_SWORD": _Metadata(
        type="swor",
        type2="2hsw",
    ),
    "ZWEIHANDER": _Metadata(
        type="swor",
        type2="2hsw",
    ),
    "EXECUTIONER_SWORD": _Metadata(
        type="swor",
        type2="2hsw",
    ),
    "POIGNARD": _Metadata(
        type="knif",
        type2="",
    ),
    "RONDEL": _Metadata(
        type="knif",
        type2="",
    ),
    "CINQUEDEAS": _Metadata(
        type="knif",
        type2="",
    ),
    "STILETTO": _Metadata(
        type="knif",
        type2="",
    ),
    "BATTLE_DART": _Metadata(
        type="tkni",
        type2="",
    ),
    "FRANCISCA": _Metadata(
        type="taxe",
        type2="",
    ),
    "WAR_DART": _Metadata(
        type="tkni",
        type2="",
    ),
    "HURLBAT": _Metadata(
        type="taxe",
        type2="",
    ),
    "WAR_JAVELIN": _Metadata(
        type="jave",
        type2="",
    ),
    "GREAT_PILUM": _Metadata(
        type="jave",
        type2="",
    ),
    "SIMBILAN": _Metadata(
        type="jave",
        type2="",
    ),
    "SPICULUM": _Metadata(
        type="jave",
        type2="",
    ),
    "HARPOON": _Metadata(
        type="jave",
        type2="",
    ),
    "WAR_SPEAR": _Metadata(
        type="spea",
        type2="2han",
    ),
    "FUSCINA": _Metadata(
        type="spea",
        type2="2han",
    ),
    "WAR_FORK": _Metadata(
        type="spea",
        type2="2han",
    ),
    "YARI": _Metadata(
        type="spea",
        type2="2han",
    ),
    "LANCE": _Metadata(
        type="spea",
        type2="2han",
    ),
    "LOCHABER_AXE": _Metadata(
        type="pole",
        type2="2han",
    ),
    "BILL": _Metadata(
        type="pole",
        type2="2han",
    ),
    "BATTLE_SCYTHE": _Metadata(
        type="sc9",
        type2="2han",
    ),
    "PARTIZAN": _Metadata(
        type="pole",
        type2="2han",
    ),
    "BEC_DE_CORBIN": _Metadata(
        type="pole",
        type2="2han",
    ),
    "GRIM_SCYTHE": _Metadata(
        type="sc9",
        type2="2han",
    ),
    "JO_STAFF": _Metadata(
        type="staf",
        type2="2han",
    ),
    "QUARTERSTAFF": _Metadata(
        type="staf",
        type2="2han",
    ),
    "CEDAR_STAFF": _Metadata(
        type="staf",
        type2="2han",
    ),
    "GOTHIC_STAFF": _Metadata(
        type="staf",
        type2="2han",
    ),
    "RUNE_STAFF": _Metadata(
        type="staf",
        type2="2han",
    ),
    "EDGE_BOW": _Metadata(
        type="bow",
        type2="",
    ),
    "RAZOR_BOW": _Metadata(
        type="bow",
        type2="",
    ),
    "CEDAR_BOW": _Metadata(
        type="bow",
        type2="",
    ),
    "DOUBLE_BOW": _Metadata(
        type="bow",
        type2="",
    ),
    "SHORT_SIEGE_BOW": _Metadata(
        type="bow",
        type2="",
    ),
    "LARGE_SIEGE_BOW": _Metadata(
        type="bow",
        type2="",
    ),
    "RUNE_BOW": _Metadata(
        type="bow",
        type2="",
    ),
    "GOTHIC_BOW": _Metadata(
        type="bow",
        type2="",
    ),
    "ARBALEST": _Metadata(
        type="xbow",
        type2="",
    ),
    "SIEGE_CROSSBOW": _Metadata(
        type="xbow",
        type2="",
    ),
    "BALLISTA": _Metadata(
        type="xbow",
        type2="",
    ),
    "CHU_KO_NU": _Metadata(
        type="xbow",
        type2="",
    ),
    "KHALIMS_FLAIL": _Metadata(
        type="mace",
        type2="",
    ),
    "KHALIMS_WILL": _Metadata(
        type="mace",
        type2="",
    ),
    "KATAR": _Metadata(
        type="h2h",
        type2="",
    ),
    "WRIST_BLADE": _Metadata(
        type="h2h",
        type2="",
    ),
    "HATCHET_HANDS": _Metadata(
        type="h2h",
        type2="",
    ),
    "CESTUS": _Metadata(
        type="h2h",
        type2="",
    ),
    "CLAWS": _Metadata(
        type="h2h",
        type2="",
    ),
    "BLADE_TALONS": _Metadata(
        type="h2h",
        type2="",
    ),
    "SCISSORS_KATAR": _Metadata(
        type="h2h",
        type2="",
    ),
    "QUHAB": _Metadata(
        type="h2h",
        type2="",
    ),
    "WRIST_SPIKE": _Metadata(
        type="h2h",
        type2="",
    ),
    "FASCIA": _Metadata(
        type="h2h",
        type2="",
    ),
    "HAND_SCYTHE": _Metadata(
        type="h2h2",
        type2="",
    ),
    "GREATER_CLAWS": _Metadata(
        type="h2h2",
        type2="",
    ),
    "GREATER_TALONS": _Metadata(
        type="h2h2",
        type2="",
    ),
    "SCISSORS_QUHAB": _Metadata(
        type="h2h2",
        type2="",
    ),
    "SUWAYYAH": _Metadata(
        type="h2h2",
        type2="",
    ),
    "WRIST_SWORD": _Metadata(
        type="h2h2",
        type2="",
    ),
    "WAR_FIST": _Metadata(
        type="h2h2",
        type2="",
    ),
    "BATTLE_CESTUS": _Metadata(
        type="h2h2",
        type2="",
    ),
    "FERAL_CLAWS": _Metadata(
        type="h2h2",
        type2="",
    ),
    "RUNIC_TALONS": _Metadata(
        type="h2h2",
        type2="",
    ),
    "SCISSORS_SUWAYYAH": _Metadata(
        type="h2h2",
        type2="",
    ),
    "TOMAHAWK": _Metadata(
        type="axe",
        type2="",
    ),
    "SMALL_CRESCENT": _Metadata(
        type="axe",
        type2="",
    ),
    "ETTIN_AXE": _Metadata(
        type="axe",
        type2="",
    ),
    "WAR_SPIKE": _Metadata(
        type="axe",
        type2="",
    ),
    "BERSERKER_AXE": _Metadata(
        type="axe",
        type2="",
    ),
    "FERAL_AXE": _Metadata(
        type="axe",
        type2="2han",
    ),
    "SILVER_EDGED_AXE": _Metadata(
        type="axe",
        type2="2han",
    ),
    "DECAPITATOR": _Metadata(
        type="axe",
        type2="2han",
    ),
    "CHAMPION_AXE": _Metadata(
        type="axe",
        type2="2han",
    ),
    "GLORIOUS_AXE": _Metadata(
        type="axe",
        type2="2han",
    ),
    "POLISHED_WAND": _Metadata(
        type="wand",
        type2="",
    ),
    "GHOST_WAND": _Metadata(
        type="wand",
        type2="",
    ),
    "LICH_WAND": _Metadata(
        type="wand",
        type2="",
    ),
    "UNEARTHED_WAND": _Metadata(
        type="wand",
        type2="",
    ),
    "TRUNCHEON": _Metadata(
        type="club",
        type2="",
    ),
    "MIGHTY_SCEPTER": _Metadata(
        type="scep",
        type2="",
    ),
    "SERAPH_ROD": _Metadata(
        type="scep",
        type2="",
    ),
    "CADUCEUS": _Metadata(
        type="scep",
        type2="",
    ),
    "TYRANT_CLUB": _Metadata(
        type="club",
        type2="",
    ),
    "REINFORCED_MACE": _Metadata(
        type="mace",
        type2="",
    ),
    "DEVIL_STAR": _Metadata(
        type="mace",
        type2="",
    ),
    "SCOURGE": _Metadata(
        type="mace",
        type2="",
    ),
    "LEGENDARY_MALLET": _Metadata(
        type="hamm",
        type2="",
    ),
    "OGRE_MAUL": _Metadata(
        type="hamm",
        type2="2han",
    ),
    "THUNDER_MAUL": _Metadata(
        type="hamm",
        type2="2han",
    ),
    "FALCATA": _Metadata(
        type="swor",
        type2="",
    ),
    "ATAGHAN": _Metadata(
        type="swor",
        type2="",
    ),
    "ELEGANT_BLADE": _Metadata(
        type="swor",
        type2="",
    ),
    "HYDRA_EDGE": _Metadata(
        type="swor",
        type2="",
    ),
    "PHASE_BLADE": _Metadata(
        type="swor",
        type2="crys",
    ),
    "CONQUEST_SWORD": _Metadata(
        type="swor",
        type2="",
    ),
    "CRYPTIC_SWORD": _Metadata(
        type="swor",
        type2="",
    ),
    "MYTHICAL_SWORD": _Metadata(
        type="swor",
        type2="",
    ),
    "LEGEND_SWORD": _Metadata(
        type="swor",
        type2="2hsw",
    ),
    "HIGHLAND_BLADE": _Metadata(
        type="swor",
        type2="2hsw",
    ),
    "BALROG_BLADE": _Metadata(
        type="swor",
        type2="2hsw",
    ),
    "CHAMPION_SWORD": _Metadata(
        type="swor",
        type2="2hsw",
    ),
    "COLOSSUS_SWORD": _Metadata(
        type="swor",
        type2="2hsw",
    ),
    "COLOSSUS_BLADE": _Metadata(
        type="swor",
        type2="2hsw",
    ),
    "BONE_KNIFE": _Metadata(
        type="knif",
        type2="",
    ),
    "MITHRIL_POINT": _Metadata(
        type="knif",
        type2="",
    ),
    "FANGED_KNIFE": _Metadata(
        type="knif",
        type2="",
    ),
    "LEGEND_SPIKE": _Metadata(
        type="knif",
        type2="",
    ),
    "FLYING_KNIFE": _Metadata(
        type="tkni",
        type2="",
    ),
    "FLYING_AXE": _Metadata(
        type="taxe",
        type2="",
    ),
    "WINGED_KNIFE": _Metadata(
        type="tkni",
        type2="",
    ),
    "WINGED_AXE": _Metadata(
        type="taxe",
        type2="",
    ),
    "HYPERION_JAVELIN": _Metadata(
        type="jave",
        type2="",
    ),
    "STYGIAN_PILUM": _Metadata(
        type="jave",
        type2="",
    ),
    "BALROG_SPEAR": _Metadata(
        type="jave",
        type2="",
    ),
    "GHOST_GLAIVE": _Metadata(
        type="jave",
        type2="",
    ),
    "WINGED_HARPOON": _Metadata(
        type="jave",
        type2="",
    ),
    "HYPERION_SPEAR": _Metadata(
        type="spea",
        type2="2han",
    ),
    "STYGIAN_PIKE": _Metadata(
        type="spea",
        type2="2han",
    ),
    "MANCATCHER": _Metadata(
        type="spea",
        type2="2han",
    ),
    "GHOST_SPEAR": _Metadata(
        type="spea",
        type2="2han",
    ),
    "WAR_PIKE": _Metadata(
        type="spea",
        type2="2han",
    ),
    "OGRE_AXE": _Metadata(
        type="pole",
        type2="2han",
    ),
    "COLOSSUS_VOULGE": _Metadata(
        type="pole",
        type2="2han",
    ),
    "THRESHER": _Metadata(
        type="sc9",
        type2="2han",
    ),
    "CRYPTIC_AXE": _Metadata(
        type="pole",
        type2="2han",
    ),
    "GREAT_POLEAXE": _Metadata(
        type="pole",
        type2="2han",
    ),
    "GIANT_THRESHER": _Metadata(
        type="sc9",
        type2="2han",
    ),
    "WALKING_STICK": _Metadata(
        type="staf",
        type2="2han",
    ),
    "STALAGMITE": _Metadata(
        type="staf",
        type2="2han",
    ),
    "ELDER_STAFF": _Metadata(
        type="staf",
        type2="2han",
    ),
    "SHILLELAGH": _Metadata(
        type="staf",
        type2="2han",
    ),
    "ARCHON_STAFF": _Metadata(
        type="staf",
        type2="2han",
    ),
    "SPIDER_BOW": _Metadata(
        type="bow",
        type2="",
    ),
    "BLADE_BOW": _Metadata(
        type="bow",
        type2="",
    ),
    "SHADOW_BOW": _Metadata(
        type="bow",
        type2="",
    ),
    "GREAT_BOW": _Metadata(
        type="bow",
        type2="",
    ),
    "DIAMOND_BOW": _Metadata(
        type="bow",
        type2="",
    ),
    "CRUSADER_BOW": _Metadata(
        type="bow",
        type2="",
    ),
    "WARD_BOW": _Metadata(
        type="bow",
        type2="",
    ),
    "HYDRA_BOW": _Metadata(
        type="bow",
        type2="",
    ),
    "PELLET_BOW": _Metadata(
        type="xbow",
        type2="",
    ),
    "GORGON_CROSSBOW": _Metadata(
        type="xbow",
        type2="",
    ),
    "COLOSSUS_CROSSBOW": _Metadata(
        type="xbow",
        type2="",
    ),
    "DEMON_CROSSBOW": _Metadata(
        type="xbow",
        type2="",
    ),
    "EAGLE_ORB": _Metadata(
        type="orb",
        type2="",
    ),
    "SACRED_GLOBE": _Metadata(
        type="orb",
        type2="",
    ),
    "SMOKED_SPHERE": _Metadata(
        type="orb",
        type2="",
    ),
    "CLASPED_ORB": _Metadata(
        type="orb",
        type2="",
    ),
    "JAREDS_STONE": _Metadata(
        type="orb",
        type2="",
    ),
    "STAG_BOW": _Metadata(
        type="abow",
        type2="",
    ),
    "REFLEX_BOW": _Metadata(
        type="abow",
        type2="",
    ),
    "MAIDEN_SPEAR": _Metadata(
        type="aspe",
        type2="2han",
    ),
    "MAIDEN_PIKE": _Metadata(
        type="aspe",
        type2="2han",
    ),
    "MAIDEN_JAVELIN": _Metadata(
        type="ajav",
        type2="",
    ),
    "GLOWING_ORB": _Metadata(
        type="orb",
        type2="",
    ),
    "CRYSTALLINE_GLOBE": _Metadata(
        type="orb",
        type2="",
    ),
    "CLOUDY_SPHERE": _Metadata(
        type="orb",
        type2="",
    ),
    "SPARKLING_BALL": _Metadata(
        type="orb",
        type2="",
    ),
    "SWIRLING_CRYSTAL": _Metadata(
        type="orb",
        type2="",
    ),
    "ASHWOOD_BOW": _Metadata(
        type="abow",
        type2="",
    ),
    "CEREMONIAL_BOW": _Metadata(
        type="abow",
        type2="",
    ),
    "CEREMONIAL_SPEAR": _Metadata(
        type="aspe",
        type2="2han",
    ),
    "CEREMONIAL_PIKE": _Metadata(
        type="aspe",
        type2="2han",
    ),
    "CEREMONIAL_JAVELIN": _Metadata(
        type="ajav",
        type2="",
    ),
    "HEAVENLY_STONE": _Metadata(
        type="orb",
        type2="",
    ),
    "ELDRITCH_ORB": _Metadata(
        type="orb",
        type2="",
    ),
    "DEMON_HEART": _Metadata(
        type="orb",
        type2="",
    ),
    "VORTEX_ORB": _Metadata(
        type="orb",
        type2="",
    ),
    "DIMENSIONAL_SHARD": _Metadata(
        type="orb",
        type2="",
    ),
    "MATRIARCHAL_BOW": _Metadata(
        type="abow",
        type2="",
    ),
    "GRAND_MATRON_BOW": _Metadata(
        type="abow",
        type2="",
    ),
    "MATRIARCHAL_SPEAR": _Metadata(
        type="aspe",
        type2="2han",
    ),
    "MATRIARCHAL_PIKE": _Metadata(
        type="aspe",
        type2="2han",
    ),
    "MATRIARCHAL_JAVELIN": _Metadata(
        type="ajav",
        type2="",
    ),
    "FULMINATING_POTION": _Metadata(
        type="tpot",
        type2="",
    ),
    "EXPLODING_POTION": _Metadata(
        type="tpot",
        type2="",
    ),
    "OIL_POTION": _Metadata(
        type="tpot",
        type2="",
    ),
    "STRANGLING_POTION": _Metadata(
        type="tpot",
        type2="",
    ),
    "CHOKING_POTION": _Metadata(
        type="tpot",
        type2="",
    ),
    "RANCID_POTION": _Metadata(
        type="tpot",
        type2="",
    ),
    "CHILLING_POTION": _Metadata(
        type="tpot",
        type2="",
    ),
    "FROST_POTION": _Metadata(
        type="tpot",
        type2="",
    ),
    "FREEZING_POTION": _Metadata(
        type="tpot",
        type2="",
    ),
    "CHARGED_POTION": _Metadata(
        type="tpot",
        type2="",
    ),
    "STATIC_POTION": _Metadata(
        type="tpot",
        type2="",
    ),
    "SHOCK_POTION": _Metadata(
        type="tpot",
        type2="",
    ),
}


class Weapon(BoolMixin, Enum):
    """PD2 weapon categories."""

    HAND_AXE = "hax"  # Hand Axe
    AXE = "axe"  # Axe
    DOUBLE_AXE = "2ax"  # Double Axe
    MILITARY_PICK = "mpi"  # Military Pick
    WAR_AXE = "wax"  # War Axe
    LARGE_AXE = "lax"  # Large Axe
    BROAD_AXE = "bax"  # Broad Axe
    BATTLE_AXE = "btx"  # Battle Axe
    GREAT_AXE = "gax"  # Great Axe
    GIANT_AXE = "gix"  # Giant Axe
    WAND = "wnd"  # Wand
    YEW_WAND = "ywn"  # Yew Wand
    BONE_WAND = "bwn"  # Bone Wand
    GRIM_WAND = "gwn"  # Grim Wand
    CLUB = "clb"  # Club
    SCEPTER = "scp"  # Scepter
    GRAND_SCEPTER = "gsc"  # Grand Scepter
    WAR_SCEPTER = "wsp"  # War Scepter
    SPIKED_CLUB = "spc"  # Spiked Club
    MACE = "mac"  # Mace
    MORNING_STAR = "mst"  # Morning Star
    FLAIL = "fla"  # Flail
    WAR_HAMMER = "whm"  # War Hammer
    MAUL = "mau"  # Maul
    GREAT_MAUL = "gma"  # Great Maul
    SHORT_SWORD = "ssd"  # Short Sword
    SCIMITAR = "scm"  # Scimitar
    SABRE = "sbr"  # Sabre
    FALCHION = "flc"  # Falchion
    CRYSTAL_SWORD = "crs"  # Crystal Sword
    BROAD_SWORD = "bsd"  # Broad Sword
    LONG_SWORD = "lsd"  # Long Sword
    WAR_SWORD = "wsd"  # War Sword
    TWO_HANDED_SWORD = "2hs"  # Two-Handed Sword
    CLAYMORE = "clm"  # Claymore
    GIANT_SWORD = "gis"  # Giant Sword
    BASTARD_SWORD = "bsw"  # Bastard Sword
    FLAMBERGE = "flb"  # Flamberge
    GREAT_SWORD = "gsd"  # Great Sword
    DAGGER = "dgr"  # Dagger
    DIRK = "dir"  # Dirk
    KRIS = "kri"  # Kris
    BLADE = "bld"  # Blade
    THROWING_KNIFE = "tkf"  # Throwing Knife
    THROWING_AXE = "tax"  # Throwing Axe
    BALANCED_KNIFE = "bkf"  # Balanced Knife
    BALANCED_AXE = "bal"  # Balanced Axe
    JAVELIN = "jav"  # Javelin
    PILUM = "pil"  # Pilum
    SHORT_SPEAR = "ssp"  # Short Spear
    GLAIVE = "glv"  # Glaive
    THROWING_SPEAR = "tsp"  # Throwing Spear
    SPEAR = "spr"  # Spear
    TRIDENT = "tri"  # Trident
    BRANDISTOCK = "brn"  # Brandistock
    SPETUM = "spt"  # Spetum
    PIKE = "pik"  # Pike
    BARDICHE = "bar"  # Bardiche
    VOULGE = "vou"  # Voulge
    SCYTHE = "scy"  # Scythe
    POLEAXE = "pax"  # Poleaxe
    HALBERD = "hal"  # Halberd
    WAR_SCYTHE = "wsc"  # War Scythe
    SHORT_STAFF = "sst"  # Short Staff
    LONG_STAFF = "lst"  # Long Staff
    GNARLED_STAFF = "cst"  # Gnarled Staff
    BATTLE_STAFF = "bst"  # Battle Staff
    WAR_STAFF = "wst"  # War Staff
    SHORT_BOW = "sbw"  # Short Bow
    HUNTERS_BOW = "hbw"  # Hunter's Bow
    LONG_BOW = "lbw"  # Long Bow
    COMPOSITE_BOW = "cbw"  # Composite Bow
    SHORT_BATTLE_BOW = "sbb"  # Short Battle Bow
    LONG_BATTLE_BOW = "lbb"  # Long Battle Bow
    SHORT_WAR_BOW = "swb"  # Short War Bow
    LONG_WAR_BOW = "lwb"  # Long War Bow
    LIGHT_CROSSBOW = "lxb"  # Light Crossbow
    CROSSBOW = "mxb"  # Crossbow
    HEAVY_CROSSBOW = "hxb"  # Heavy Crossbow
    REPEATING_CROSSBOW = "rxb"  # Repeating Crossbow
    DECOY_GIDBINN = "d33"  # Decoy Gidbinn
    THE_GIDBINN = "g33"  # The Gidbinn
    WIRTS_LEG = "leg"  # Wirt's Leg
    HORADRIC_MALUS = "hdm"  # Horadric Malus
    HELL_FORGE_HAMMER = "hfh"  # Hell Forge Hammer
    HORADRIC_STAFF = "hst"  # Horadric Staff
    SHAFT_OF_THE_HORADRIC_STAFF = "msf"  # Shaft of the Horadric Staff
    HATCHET = "9ha"  # Hatchet
    CLEAVER = "9ax"  # Cleaver
    TWIN_AXE = "92a"  # Twin Axe
    CROWBILL = "9mp"  # Crowbill
    NAGA = "9wa"  # Naga
    MILITARY_AXE = "9la"  # Military Axe
    BEARDED_AXE = "9ba"  # Bearded Axe
    TABAR = "9bt"  # Tabar
    GOTHIC_AXE = "9ga"  # Gothic Axe
    ANCIENT_AXE = "9gi"  # Ancient Axe
    BURNT_WAND = "9wn"  # Burnt Wand
    PETRIFIED_WAND = "9yw"  # Petrified Wand
    TOMB_WAND = "9bw"  # Tomb Wand
    GRAVE_WAND = "9gw"  # Grave Wand
    CUDGEL = "9cl"  # Cudgel
    RUNE_SCEPTER = "9sc"  # Rune Scepter
    HOLY_WATER_SPRINKLER = "9qs"  # Holy Water Sprinkler
    DIVINE_SCEPTER = "9ws"  # Divine Scepter
    BARBED_CLUB = "9sp"  # Barbed Club
    FLANGED_MACE = "9ma"  # Flanged Mace
    JAGGED_STAR = "9mt"  # Jagged Star
    KNOUT = "9fl"  # Knout
    BATTLE_HAMMER = "9wh"  # Battle Hammer
    WAR_CLUB = "9m9"  # War Club
    MARTEL_DE_FER = "9gm"  # Martel de Fer
    GLADIUS = "9ss"  # Gladius
    CUTLASS = "9sm"  # Cutlass
    SHAMSHIR = "9sb"  # Shamshir
    TULWAR = "9fc"  # Tulwar
    DIMENSIONAL_BLADE = "9cr"  # Dimensional Blade
    BATTLE_SWORD = "9bs"  # Battle Sword
    RUNE_SWORD = "9ls"  # Rune Sword
    ANCIENT_SWORD = "9wd"  # Ancient Sword
    ESPANDON = "92h"  # Espandon
    DACIAN_FALX = "9cm"  # Dacian Falx
    TUSK_SWORD = "9gs"  # Tusk Sword
    GOTHIC_SWORD = "9b9"  # Gothic Sword
    ZWEIHANDER = "9fb"  # Zweihander
    EXECUTIONER_SWORD = "9gd"  # Executioner Sword
    POIGNARD = "9dg"  # Poignard
    RONDEL = "9di"  # Rondel
    CINQUEDEAS = "9kr"  # Cinquedeas
    STILETTO = "9bl"  # Stiletto
    BATTLE_DART = "9tk"  # Battle Dart
    FRANCISCA = "9ta"  # Francisca
    WAR_DART = "9bk"  # War Dart
    HURLBAT = "9b8"  # Hurlbat
    WAR_JAVELIN = "9ja"  # War Javelin
    GREAT_PILUM = "9pi"  # Great Pilum
    SIMBILAN = "9s9"  # Simbilan
    SPICULUM = "9gl"  # Spiculum
    HARPOON = "9ts"  # Harpoon
    WAR_SPEAR = "9sr"  # War Spear
    FUSCINA = "9tr"  # Fuscina
    WAR_FORK = "9br"  # War Fork
    YARI = "9st"  # Yari
    LANCE = "9p9"  # Lance
    LOCHABER_AXE = "9b7"  # Lochaber Axe
    BILL = "9vo"  # Bill
    BATTLE_SCYTHE = "9s8"  # Battle Scythe
    PARTIZAN = "9pa"  # Partizan
    BEC_DE_CORBIN = "9h9"  # Bec-de-Corbin
    GRIM_SCYTHE = "9wc"  # Grim Scythe
    JO_STAFF = "8ss"  # Jo Staff
    QUARTERSTAFF = "8ls"  # Quarterstaff
    CEDAR_STAFF = "8cs"  # Cedar Staff
    GOTHIC_STAFF = "8bs"  # Gothic Staff
    RUNE_STAFF = "8ws"  # Rune Staff
    EDGE_BOW = "8sb"  # Edge Bow
    RAZOR_BOW = "8hb"  # Razor Bow
    CEDAR_BOW = "8lb"  # Cedar Bow
    DOUBLE_BOW = "8cb"  # Double Bow
    SHORT_SIEGE_BOW = "8s8"  # Short Siege Bow
    LARGE_SIEGE_BOW = "8l8"  # Large Siege Bow
    RUNE_BOW = "8sw"  # Rune Bow
    GOTHIC_BOW = "8lw"  # Gothic Bow
    ARBALEST = "8lx"  # Arbalest
    SIEGE_CROSSBOW = "8mx"  # Siege Crossbow
    BALLISTA = "8hx"  # Ballista
    CHU_KO_NU = "8rx"  # Chu-Ko-Nu
    KHALIMS_FLAIL = "qf1"  # Khalim's Flail
    KHALIMS_WILL = "qf2"  # Khalim's Will
    KATAR = "ktr"  # Katar
    WRIST_BLADE = "wrb"  # Wrist Blade
    HATCHET_HANDS = "axf"  # Hatchet Hands
    CESTUS = "ces"  # Cestus
    CLAWS = "clw"  # Claws
    BLADE_TALONS = "btl"  # Blade Talons
    SCISSORS_KATAR = "skr"  # Scissors Katar
    QUHAB = "9ar"  # Quhab
    WRIST_SPIKE = "9wb"  # Wrist Spike
    FASCIA = "9xf"  # Fascia
    HAND_SCYTHE = "9cs"  # Hand Scythe
    GREATER_CLAWS = "9lw"  # Greater Claws
    GREATER_TALONS = "9tw"  # Greater Talons
    SCISSORS_QUHAB = "9qr"  # Scissors Quhab
    SUWAYYAH = "7ar"  # Suwayyah
    WRIST_SWORD = "7wb"  # Wrist Sword
    WAR_FIST = "7xf"  # War Fist
    BATTLE_CESTUS = "7cs"  # Battle Cestus
    FERAL_CLAWS = "7lw"  # Feral Claws
    RUNIC_TALONS = "7tw"  # Runic Talons
    SCISSORS_SUWAYYAH = "7qr"  # Scissors Suwayyah
    TOMAHAWK = "7ha"  # Tomahawk
    SMALL_CRESCENT = "7ax"  # Small Crescent
    ETTIN_AXE = "72a"  # Ettin Axe
    WAR_SPIKE = "7mp"  # War Spike
    BERSERKER_AXE = "7wa"  # Berserker Axe
    FERAL_AXE = "7la"  # Feral Axe
    SILVER_EDGED_AXE = "7ba"  # Silver-edged Axe
    DECAPITATOR = "7bt"  # Decapitator
    CHAMPION_AXE = "7ga"  # Champion Axe
    GLORIOUS_AXE = "7gi"  # Glorious Axe
    POLISHED_WAND = "7wn"  # Polished Wand
    GHOST_WAND = "7yw"  # Ghost Wand
    LICH_WAND = "7bw"  # Lich Wand
    UNEARTHED_WAND = "7gw"  # Unearthed Wand
    TRUNCHEON = "7cl"  # Truncheon
    MIGHTY_SCEPTER = "7sc"  # Mighty Scepter
    SERAPH_ROD = "7qs"  # Seraph Rod
    CADUCEUS = "7ws"  # Caduceus
    TYRANT_CLUB = "7sp"  # Tyrant Club
    REINFORCED_MACE = "7ma"  # Reinforced Mace
    DEVIL_STAR = "7mt"  # Devil Star
    SCOURGE = "7fl"  # Scourge
    LEGENDARY_MALLET = "7wh"  # Legendary Mallet
    OGRE_MAUL = "7m7"  # Ogre Maul
    THUNDER_MAUL = "7gm"  # Thunder Maul
    FALCATA = "7ss"  # Falcata
    ATAGHAN = "7sm"  # Ataghan
    ELEGANT_BLADE = "7sb"  # Elegant Blade
    HYDRA_EDGE = "7fc"  # Hydra Edge
    PHASE_BLADE = "7cr"  # Phase Blade
    CONQUEST_SWORD = "7bs"  # Conquest Sword
    CRYPTIC_SWORD = "7ls"  # Cryptic Sword
    MYTHICAL_SWORD = "7wd"  # Mythical Sword
    LEGEND_SWORD = "72h"  # Legend Sword
    HIGHLAND_BLADE = "7cm"  # Highland Blade
    BALROG_BLADE = "7gs"  # Balrog Blade
    CHAMPION_SWORD = "7b7"  # Champion Sword
    COLOSSUS_SWORD = "7fb"  # Colossus Sword
    COLOSSUS_BLADE = "7gd"  # Colossus Blade
    BONE_KNIFE = "7dg"  # Bone Knife
    MITHRIL_POINT = "7di"  # Mithril Point
    FANGED_KNIFE = "7kr"  # Fanged Knife
    LEGEND_SPIKE = "7bl"  # Legend Spike
    FLYING_KNIFE = "7tk"  # Flying Knife
    FLYING_AXE = "7ta"  # Flying Axe
    WINGED_KNIFE = "7bk"  # Winged Knife
    WINGED_AXE = "7b8"  # Winged Axe
    HYPERION_JAVELIN = "7ja"  # Hyperion Javelin
    STYGIAN_PILUM = "7pi"  # Stygian Pilum
    BALROG_SPEAR = "7s7"  # Balrog Spear
    GHOST_GLAIVE = "7gl"  # Ghost Glaive
    WINGED_HARPOON = "7ts"  # Winged Harpoon
    HYPERION_SPEAR = "7sr"  # Hyperion Spear
    STYGIAN_PIKE = "7tr"  # Stygian Pike
    MANCATCHER = "7br"  # Mancatcher
    GHOST_SPEAR = "7st"  # Ghost Spear
    WAR_PIKE = "7p7"  # War Pike
    OGRE_AXE = "7o7"  # Ogre Axe
    COLOSSUS_VOULGE = "7vo"  # Colossus Voulge
    THRESHER = "7s8"  # Thresher
    CRYPTIC_AXE = "7pa"  # Cryptic Axe
    GREAT_POLEAXE = "7h7"  # Great Poleaxe
    GIANT_THRESHER = "7wc"  # Giant Thresher
    WALKING_STICK = "6ss"  # Walking Stick
    STALAGMITE = "6ls"  # Stalagmite
    ELDER_STAFF = "6cs"  # Elder Staff
    SHILLELAGH = "6bs"  # Shillelagh
    ARCHON_STAFF = "6ws"  # Archon Staff
    SPIDER_BOW = "6sb"  # Spider Bow
    BLADE_BOW = "6hb"  # Blade Bow
    SHADOW_BOW = "6lb"  # Shadow Bow
    GREAT_BOW = "6cb"  # Great Bow
    DIAMOND_BOW = "6s7"  # Diamond Bow
    CRUSADER_BOW = "6l7"  # Crusader Bow
    WARD_BOW = "6sw"  # Ward Bow
    HYDRA_BOW = "6lw"  # Hydra Bow
    PELLET_BOW = "6lx"  # Pellet Bow
    GORGON_CROSSBOW = "6mx"  # Gorgon Crossbow
    COLOSSUS_CROSSBOW = "6hx"  # Colossus Crossbow
    DEMON_CROSSBOW = "6rx"  # Demon Crossbow
    EAGLE_ORB = "ob1"  # Eagle Orb
    SACRED_GLOBE = "ob2"  # Sacred Globe
    SMOKED_SPHERE = "ob3"  # Smoked Sphere
    CLASPED_ORB = "ob4"  # Clasped Orb
    JAREDS_STONE = "ob5"  # Jared's Stone
    STAG_BOW = "am1"  # Stag Bow
    REFLEX_BOW = "am2"  # Reflex Bow
    MAIDEN_SPEAR = "am3"  # Maiden Spear
    MAIDEN_PIKE = "am4"  # Maiden Pike
    MAIDEN_JAVELIN = "am5"  # Maiden Javelin
    GLOWING_ORB = "ob6"  # Glowing Orb
    CRYSTALLINE_GLOBE = "ob7"  # Crystalline Globe
    CLOUDY_SPHERE = "ob8"  # Cloudy Sphere
    SPARKLING_BALL = "ob9"  # Sparkling Ball
    SWIRLING_CRYSTAL = "oba"  # Swirling Crystal
    ASHWOOD_BOW = "am6"  # Ashwood Bow
    CEREMONIAL_BOW = "am7"  # Ceremonial Bow
    CEREMONIAL_SPEAR = "am8"  # Ceremonial Spear
    CEREMONIAL_PIKE = "am9"  # Ceremonial Pike
    CEREMONIAL_JAVELIN = "ama"  # Ceremonial Javelin
    HEAVENLY_STONE = "obb"  # Heavenly Stone
    ELDRITCH_ORB = "obc"  # Eldritch Orb
    DEMON_HEART = "obd"  # Demon Heart
    VORTEX_ORB = "obe"  # Vortex Orb
    DIMENSIONAL_SHARD = "obf"  # Dimensional Shard
    MATRIARCHAL_BOW = "amb"  # Matriarchal Bow
    GRAND_MATRON_BOW = "amc"  # Grand Matron Bow
    MATRIARCHAL_SPEAR = "amd"  # Matriarchal Spear
    MATRIARCHAL_PIKE = "ame"  # Matriarchal Pike
    MATRIARCHAL_JAVELIN = "amf"  # Matriarchal Javelin
    FULMINATING_POTION = "tpfs"  # Fulminating Potion
    EXPLODING_POTION = "tpfm"  # Exploding Potion
    OIL_POTION = "tpfl"  # Oil Potion
    STRANGLING_POTION = "tpgs"  # Strangling Potion
    CHOKING_POTION = "tpgm"  # Choking Potion
    RANCID_POTION = "tpgl"  # Rancid Potion
    CHILLING_POTION = "tpcs"  # Chilling Potion
    FROST_POTION = "tpcm"  # Frost Potion
    FREEZING_POTION = "tpcl"  # Freezing Potion
    CHARGED_POTION = "tpls"  # Charged Potion
    STATIC_POTION = "tplm"  # Static Potion
    SHOCK_POTION = "tpll"  # Shock Potion

    def as_node(self) -> BoolRef:
        return BoolRef(self.value)

    @property
    def type(self) -> str:
        return _METADATA[self.name].type

    @property
    def type2(self) -> str:
        return _METADATA[self.name].type2
