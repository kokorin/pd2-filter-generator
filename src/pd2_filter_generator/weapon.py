"""
Generated Weapon enum from PD2 data.

DO NOT EDIT MANUALLY - regenerate with: hatch run ./scripts/generate.py generate
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from pd2_filter_generator.expression import CodeLiteral


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


class Weapon(Enum):
    """PD2 weapon categories."""

    HAND_AXE = CodeLiteral("hax")  # Hand Axe
    AXE = CodeLiteral("axe")  # Axe
    DOUBLE_AXE = CodeLiteral("2ax")  # Double Axe
    MILITARY_PICK = CodeLiteral("mpi")  # Military Pick
    WAR_AXE = CodeLiteral("wax")  # War Axe
    LARGE_AXE = CodeLiteral("lax")  # Large Axe
    BROAD_AXE = CodeLiteral("bax")  # Broad Axe
    BATTLE_AXE = CodeLiteral("btx")  # Battle Axe
    GREAT_AXE = CodeLiteral("gax")  # Great Axe
    GIANT_AXE = CodeLiteral("gix")  # Giant Axe
    WAND = CodeLiteral("wnd")  # Wand
    YEW_WAND = CodeLiteral("ywn")  # Yew Wand
    BONE_WAND = CodeLiteral("bwn")  # Bone Wand
    GRIM_WAND = CodeLiteral("gwn")  # Grim Wand
    CLUB = CodeLiteral("clb")  # Club
    SCEPTER = CodeLiteral("scp")  # Scepter
    GRAND_SCEPTER = CodeLiteral("gsc")  # Grand Scepter
    WAR_SCEPTER = CodeLiteral("wsp")  # War Scepter
    SPIKED_CLUB = CodeLiteral("spc")  # Spiked Club
    MACE = CodeLiteral("mac")  # Mace
    MORNING_STAR = CodeLiteral("mst")  # Morning Star
    FLAIL = CodeLiteral("fla")  # Flail
    WAR_HAMMER = CodeLiteral("whm")  # War Hammer
    MAUL = CodeLiteral("mau")  # Maul
    GREAT_MAUL = CodeLiteral("gma")  # Great Maul
    SHORT_SWORD = CodeLiteral("ssd")  # Short Sword
    SCIMITAR = CodeLiteral("scm")  # Scimitar
    SABRE = CodeLiteral("sbr")  # Sabre
    FALCHION = CodeLiteral("flc")  # Falchion
    CRYSTAL_SWORD = CodeLiteral("crs")  # Crystal Sword
    BROAD_SWORD = CodeLiteral("bsd")  # Broad Sword
    LONG_SWORD = CodeLiteral("lsd")  # Long Sword
    WAR_SWORD = CodeLiteral("wsd")  # War Sword
    TWO_HANDED_SWORD = CodeLiteral("2hs")  # Two-Handed Sword
    CLAYMORE = CodeLiteral("clm")  # Claymore
    GIANT_SWORD = CodeLiteral("gis")  # Giant Sword
    BASTARD_SWORD = CodeLiteral("bsw")  # Bastard Sword
    FLAMBERGE = CodeLiteral("flb")  # Flamberge
    GREAT_SWORD = CodeLiteral("gsd")  # Great Sword
    DAGGER = CodeLiteral("dgr")  # Dagger
    DIRK = CodeLiteral("dir")  # Dirk
    KRIS = CodeLiteral("kri")  # Kris
    BLADE = CodeLiteral("bld")  # Blade
    THROWING_KNIFE = CodeLiteral("tkf")  # Throwing Knife
    THROWING_AXE = CodeLiteral("tax")  # Throwing Axe
    BALANCED_KNIFE = CodeLiteral("bkf")  # Balanced Knife
    BALANCED_AXE = CodeLiteral("bal")  # Balanced Axe
    JAVELIN = CodeLiteral("jav")  # Javelin
    PILUM = CodeLiteral("pil")  # Pilum
    SHORT_SPEAR = CodeLiteral("ssp")  # Short Spear
    GLAIVE = CodeLiteral("glv")  # Glaive
    THROWING_SPEAR = CodeLiteral("tsp")  # Throwing Spear
    SPEAR = CodeLiteral("spr")  # Spear
    TRIDENT = CodeLiteral("tri")  # Trident
    BRANDISTOCK = CodeLiteral("brn")  # Brandistock
    SPETUM = CodeLiteral("spt")  # Spetum
    PIKE = CodeLiteral("pik")  # Pike
    BARDICHE = CodeLiteral("bar")  # Bardiche
    VOULGE = CodeLiteral("vou")  # Voulge
    SCYTHE = CodeLiteral("scy")  # Scythe
    POLEAXE = CodeLiteral("pax")  # Poleaxe
    HALBERD = CodeLiteral("hal")  # Halberd
    WAR_SCYTHE = CodeLiteral("wsc")  # War Scythe
    SHORT_STAFF = CodeLiteral("sst")  # Short Staff
    LONG_STAFF = CodeLiteral("lst")  # Long Staff
    GNARLED_STAFF = CodeLiteral("cst")  # Gnarled Staff
    BATTLE_STAFF = CodeLiteral("bst")  # Battle Staff
    WAR_STAFF = CodeLiteral("wst")  # War Staff
    SHORT_BOW = CodeLiteral("sbw")  # Short Bow
    HUNTERS_BOW = CodeLiteral("hbw")  # Hunter's Bow
    LONG_BOW = CodeLiteral("lbw")  # Long Bow
    COMPOSITE_BOW = CodeLiteral("cbw")  # Composite Bow
    SHORT_BATTLE_BOW = CodeLiteral("sbb")  # Short Battle Bow
    LONG_BATTLE_BOW = CodeLiteral("lbb")  # Long Battle Bow
    SHORT_WAR_BOW = CodeLiteral("swb")  # Short War Bow
    LONG_WAR_BOW = CodeLiteral("lwb")  # Long War Bow
    LIGHT_CROSSBOW = CodeLiteral("lxb")  # Light Crossbow
    CROSSBOW = CodeLiteral("mxb")  # Crossbow
    HEAVY_CROSSBOW = CodeLiteral("hxb")  # Heavy Crossbow
    REPEATING_CROSSBOW = CodeLiteral("rxb")  # Repeating Crossbow
    DECOY_GIDBINN = CodeLiteral("d33")  # Decoy Gidbinn
    THE_GIDBINN = CodeLiteral("g33")  # The Gidbinn
    WIRTS_LEG = CodeLiteral("leg")  # Wirt's Leg
    HORADRIC_MALUS = CodeLiteral("hdm")  # Horadric Malus
    HELL_FORGE_HAMMER = CodeLiteral("hfh")  # Hell Forge Hammer
    HORADRIC_STAFF = CodeLiteral("hst")  # Horadric Staff
    SHAFT_OF_THE_HORADRIC_STAFF = CodeLiteral("msf")  # Shaft of the Horadric Staff
    HATCHET = CodeLiteral("9ha")  # Hatchet
    CLEAVER = CodeLiteral("9ax")  # Cleaver
    TWIN_AXE = CodeLiteral("92a")  # Twin Axe
    CROWBILL = CodeLiteral("9mp")  # Crowbill
    NAGA = CodeLiteral("9wa")  # Naga
    MILITARY_AXE = CodeLiteral("9la")  # Military Axe
    BEARDED_AXE = CodeLiteral("9ba")  # Bearded Axe
    TABAR = CodeLiteral("9bt")  # Tabar
    GOTHIC_AXE = CodeLiteral("9ga")  # Gothic Axe
    ANCIENT_AXE = CodeLiteral("9gi")  # Ancient Axe
    BURNT_WAND = CodeLiteral("9wn")  # Burnt Wand
    PETRIFIED_WAND = CodeLiteral("9yw")  # Petrified Wand
    TOMB_WAND = CodeLiteral("9bw")  # Tomb Wand
    GRAVE_WAND = CodeLiteral("9gw")  # Grave Wand
    CUDGEL = CodeLiteral("9cl")  # Cudgel
    RUNE_SCEPTER = CodeLiteral("9sc")  # Rune Scepter
    HOLY_WATER_SPRINKLER = CodeLiteral("9qs")  # Holy Water Sprinkler
    DIVINE_SCEPTER = CodeLiteral("9ws")  # Divine Scepter
    BARBED_CLUB = CodeLiteral("9sp")  # Barbed Club
    FLANGED_MACE = CodeLiteral("9ma")  # Flanged Mace
    JAGGED_STAR = CodeLiteral("9mt")  # Jagged Star
    KNOUT = CodeLiteral("9fl")  # Knout
    BATTLE_HAMMER = CodeLiteral("9wh")  # Battle Hammer
    WAR_CLUB = CodeLiteral("9m9")  # War Club
    MARTEL_DE_FER = CodeLiteral("9gm")  # Martel de Fer
    GLADIUS = CodeLiteral("9ss")  # Gladius
    CUTLASS = CodeLiteral("9sm")  # Cutlass
    SHAMSHIR = CodeLiteral("9sb")  # Shamshir
    TULWAR = CodeLiteral("9fc")  # Tulwar
    DIMENSIONAL_BLADE = CodeLiteral("9cr")  # Dimensional Blade
    BATTLE_SWORD = CodeLiteral("9bs")  # Battle Sword
    RUNE_SWORD = CodeLiteral("9ls")  # Rune Sword
    ANCIENT_SWORD = CodeLiteral("9wd")  # Ancient Sword
    ESPANDON = CodeLiteral("92h")  # Espandon
    DACIAN_FALX = CodeLiteral("9cm")  # Dacian Falx
    TUSK_SWORD = CodeLiteral("9gs")  # Tusk Sword
    GOTHIC_SWORD = CodeLiteral("9b9")  # Gothic Sword
    ZWEIHANDER = CodeLiteral("9fb")  # Zweihander
    EXECUTIONER_SWORD = CodeLiteral("9gd")  # Executioner Sword
    POIGNARD = CodeLiteral("9dg")  # Poignard
    RONDEL = CodeLiteral("9di")  # Rondel
    CINQUEDEAS = CodeLiteral("9kr")  # Cinquedeas
    STILETTO = CodeLiteral("9bl")  # Stiletto
    BATTLE_DART = CodeLiteral("9tk")  # Battle Dart
    FRANCISCA = CodeLiteral("9ta")  # Francisca
    WAR_DART = CodeLiteral("9bk")  # War Dart
    HURLBAT = CodeLiteral("9b8")  # Hurlbat
    WAR_JAVELIN = CodeLiteral("9ja")  # War Javelin
    GREAT_PILUM = CodeLiteral("9pi")  # Great Pilum
    SIMBILAN = CodeLiteral("9s9")  # Simbilan
    SPICULUM = CodeLiteral("9gl")  # Spiculum
    HARPOON = CodeLiteral("9ts")  # Harpoon
    WAR_SPEAR = CodeLiteral("9sr")  # War Spear
    FUSCINA = CodeLiteral("9tr")  # Fuscina
    WAR_FORK = CodeLiteral("9br")  # War Fork
    YARI = CodeLiteral("9st")  # Yari
    LANCE = CodeLiteral("9p9")  # Lance
    LOCHABER_AXE = CodeLiteral("9b7")  # Lochaber Axe
    BILL = CodeLiteral("9vo")  # Bill
    BATTLE_SCYTHE = CodeLiteral("9s8")  # Battle Scythe
    PARTIZAN = CodeLiteral("9pa")  # Partizan
    BEC_DE_CORBIN = CodeLiteral("9h9")  # Bec-de-Corbin
    GRIM_SCYTHE = CodeLiteral("9wc")  # Grim Scythe
    JO_STAFF = CodeLiteral("8ss")  # Jo Staff
    QUARTERSTAFF = CodeLiteral("8ls")  # Quarterstaff
    CEDAR_STAFF = CodeLiteral("8cs")  # Cedar Staff
    GOTHIC_STAFF = CodeLiteral("8bs")  # Gothic Staff
    RUNE_STAFF = CodeLiteral("8ws")  # Rune Staff
    EDGE_BOW = CodeLiteral("8sb")  # Edge Bow
    RAZOR_BOW = CodeLiteral("8hb")  # Razor Bow
    CEDAR_BOW = CodeLiteral("8lb")  # Cedar Bow
    DOUBLE_BOW = CodeLiteral("8cb")  # Double Bow
    SHORT_SIEGE_BOW = CodeLiteral("8s8")  # Short Siege Bow
    LARGE_SIEGE_BOW = CodeLiteral("8l8")  # Large Siege Bow
    RUNE_BOW = CodeLiteral("8sw")  # Rune Bow
    GOTHIC_BOW = CodeLiteral("8lw")  # Gothic Bow
    ARBALEST = CodeLiteral("8lx")  # Arbalest
    SIEGE_CROSSBOW = CodeLiteral("8mx")  # Siege Crossbow
    BALLISTA = CodeLiteral("8hx")  # Ballista
    CHU_KO_NU = CodeLiteral("8rx")  # Chu-Ko-Nu
    KHALIMS_FLAIL = CodeLiteral("qf1")  # Khalim's Flail
    KHALIMS_WILL = CodeLiteral("qf2")  # Khalim's Will
    KATAR = CodeLiteral("ktr")  # Katar
    WRIST_BLADE = CodeLiteral("wrb")  # Wrist Blade
    HATCHET_HANDS = CodeLiteral("axf")  # Hatchet Hands
    CESTUS = CodeLiteral("ces")  # Cestus
    CLAWS = CodeLiteral("clw")  # Claws
    BLADE_TALONS = CodeLiteral("btl")  # Blade Talons
    SCISSORS_KATAR = CodeLiteral("skr")  # Scissors Katar
    QUHAB = CodeLiteral("9ar")  # Quhab
    WRIST_SPIKE = CodeLiteral("9wb")  # Wrist Spike
    FASCIA = CodeLiteral("9xf")  # Fascia
    HAND_SCYTHE = CodeLiteral("9cs")  # Hand Scythe
    GREATER_CLAWS = CodeLiteral("9lw")  # Greater Claws
    GREATER_TALONS = CodeLiteral("9tw")  # Greater Talons
    SCISSORS_QUHAB = CodeLiteral("9qr")  # Scissors Quhab
    SUWAYYAH = CodeLiteral("7ar")  # Suwayyah
    WRIST_SWORD = CodeLiteral("7wb")  # Wrist Sword
    WAR_FIST = CodeLiteral("7xf")  # War Fist
    BATTLE_CESTUS = CodeLiteral("7cs")  # Battle Cestus
    FERAL_CLAWS = CodeLiteral("7lw")  # Feral Claws
    RUNIC_TALONS = CodeLiteral("7tw")  # Runic Talons
    SCISSORS_SUWAYYAH = CodeLiteral("7qr")  # Scissors Suwayyah
    TOMAHAWK = CodeLiteral("7ha")  # Tomahawk
    SMALL_CRESCENT = CodeLiteral("7ax")  # Small Crescent
    ETTIN_AXE = CodeLiteral("72a")  # Ettin Axe
    WAR_SPIKE = CodeLiteral("7mp")  # War Spike
    BERSERKER_AXE = CodeLiteral("7wa")  # Berserker Axe
    FERAL_AXE = CodeLiteral("7la")  # Feral Axe
    SILVER_EDGED_AXE = CodeLiteral("7ba")  # Silver-edged Axe
    DECAPITATOR = CodeLiteral("7bt")  # Decapitator
    CHAMPION_AXE = CodeLiteral("7ga")  # Champion Axe
    GLORIOUS_AXE = CodeLiteral("7gi")  # Glorious Axe
    POLISHED_WAND = CodeLiteral("7wn")  # Polished Wand
    GHOST_WAND = CodeLiteral("7yw")  # Ghost Wand
    LICH_WAND = CodeLiteral("7bw")  # Lich Wand
    UNEARTHED_WAND = CodeLiteral("7gw")  # Unearthed Wand
    TRUNCHEON = CodeLiteral("7cl")  # Truncheon
    MIGHTY_SCEPTER = CodeLiteral("7sc")  # Mighty Scepter
    SERAPH_ROD = CodeLiteral("7qs")  # Seraph Rod
    CADUCEUS = CodeLiteral("7ws")  # Caduceus
    TYRANT_CLUB = CodeLiteral("7sp")  # Tyrant Club
    REINFORCED_MACE = CodeLiteral("7ma")  # Reinforced Mace
    DEVIL_STAR = CodeLiteral("7mt")  # Devil Star
    SCOURGE = CodeLiteral("7fl")  # Scourge
    LEGENDARY_MALLET = CodeLiteral("7wh")  # Legendary Mallet
    OGRE_MAUL = CodeLiteral("7m7")  # Ogre Maul
    THUNDER_MAUL = CodeLiteral("7gm")  # Thunder Maul
    FALCATA = CodeLiteral("7ss")  # Falcata
    ATAGHAN = CodeLiteral("7sm")  # Ataghan
    ELEGANT_BLADE = CodeLiteral("7sb")  # Elegant Blade
    HYDRA_EDGE = CodeLiteral("7fc")  # Hydra Edge
    PHASE_BLADE = CodeLiteral("7cr")  # Phase Blade
    CONQUEST_SWORD = CodeLiteral("7bs")  # Conquest Sword
    CRYPTIC_SWORD = CodeLiteral("7ls")  # Cryptic Sword
    MYTHICAL_SWORD = CodeLiteral("7wd")  # Mythical Sword
    LEGEND_SWORD = CodeLiteral("72h")  # Legend Sword
    HIGHLAND_BLADE = CodeLiteral("7cm")  # Highland Blade
    BALROG_BLADE = CodeLiteral("7gs")  # Balrog Blade
    CHAMPION_SWORD = CodeLiteral("7b7")  # Champion Sword
    COLOSSUS_SWORD = CodeLiteral("7fb")  # Colossus Sword
    COLOSSUS_BLADE = CodeLiteral("7gd")  # Colossus Blade
    BONE_KNIFE = CodeLiteral("7dg")  # Bone Knife
    MITHRIL_POINT = CodeLiteral("7di")  # Mithril Point
    FANGED_KNIFE = CodeLiteral("7kr")  # Fanged Knife
    LEGEND_SPIKE = CodeLiteral("7bl")  # Legend Spike
    FLYING_KNIFE = CodeLiteral("7tk")  # Flying Knife
    FLYING_AXE = CodeLiteral("7ta")  # Flying Axe
    WINGED_KNIFE = CodeLiteral("7bk")  # Winged Knife
    WINGED_AXE = CodeLiteral("7b8")  # Winged Axe
    HYPERION_JAVELIN = CodeLiteral("7ja")  # Hyperion Javelin
    STYGIAN_PILUM = CodeLiteral("7pi")  # Stygian Pilum
    BALROG_SPEAR = CodeLiteral("7s7")  # Balrog Spear
    GHOST_GLAIVE = CodeLiteral("7gl")  # Ghost Glaive
    WINGED_HARPOON = CodeLiteral("7ts")  # Winged Harpoon
    HYPERION_SPEAR = CodeLiteral("7sr")  # Hyperion Spear
    STYGIAN_PIKE = CodeLiteral("7tr")  # Stygian Pike
    MANCATCHER = CodeLiteral("7br")  # Mancatcher
    GHOST_SPEAR = CodeLiteral("7st")  # Ghost Spear
    WAR_PIKE = CodeLiteral("7p7")  # War Pike
    OGRE_AXE = CodeLiteral("7o7")  # Ogre Axe
    COLOSSUS_VOULGE = CodeLiteral("7vo")  # Colossus Voulge
    THRESHER = CodeLiteral("7s8")  # Thresher
    CRYPTIC_AXE = CodeLiteral("7pa")  # Cryptic Axe
    GREAT_POLEAXE = CodeLiteral("7h7")  # Great Poleaxe
    GIANT_THRESHER = CodeLiteral("7wc")  # Giant Thresher
    WALKING_STICK = CodeLiteral("6ss")  # Walking Stick
    STALAGMITE = CodeLiteral("6ls")  # Stalagmite
    ELDER_STAFF = CodeLiteral("6cs")  # Elder Staff
    SHILLELAGH = CodeLiteral("6bs")  # Shillelagh
    ARCHON_STAFF = CodeLiteral("6ws")  # Archon Staff
    SPIDER_BOW = CodeLiteral("6sb")  # Spider Bow
    BLADE_BOW = CodeLiteral("6hb")  # Blade Bow
    SHADOW_BOW = CodeLiteral("6lb")  # Shadow Bow
    GREAT_BOW = CodeLiteral("6cb")  # Great Bow
    DIAMOND_BOW = CodeLiteral("6s7")  # Diamond Bow
    CRUSADER_BOW = CodeLiteral("6l7")  # Crusader Bow
    WARD_BOW = CodeLiteral("6sw")  # Ward Bow
    HYDRA_BOW = CodeLiteral("6lw")  # Hydra Bow
    PELLET_BOW = CodeLiteral("6lx")  # Pellet Bow
    GORGON_CROSSBOW = CodeLiteral("6mx")  # Gorgon Crossbow
    COLOSSUS_CROSSBOW = CodeLiteral("6hx")  # Colossus Crossbow
    DEMON_CROSSBOW = CodeLiteral("6rx")  # Demon Crossbow
    EAGLE_ORB = CodeLiteral("ob1")  # Eagle Orb
    SACRED_GLOBE = CodeLiteral("ob2")  # Sacred Globe
    SMOKED_SPHERE = CodeLiteral("ob3")  # Smoked Sphere
    CLASPED_ORB = CodeLiteral("ob4")  # Clasped Orb
    JAREDS_STONE = CodeLiteral("ob5")  # Jared's Stone
    STAG_BOW = CodeLiteral("am1")  # Stag Bow
    REFLEX_BOW = CodeLiteral("am2")  # Reflex Bow
    MAIDEN_SPEAR = CodeLiteral("am3")  # Maiden Spear
    MAIDEN_PIKE = CodeLiteral("am4")  # Maiden Pike
    MAIDEN_JAVELIN = CodeLiteral("am5")  # Maiden Javelin
    GLOWING_ORB = CodeLiteral("ob6")  # Glowing Orb
    CRYSTALLINE_GLOBE = CodeLiteral("ob7")  # Crystalline Globe
    CLOUDY_SPHERE = CodeLiteral("ob8")  # Cloudy Sphere
    SPARKLING_BALL = CodeLiteral("ob9")  # Sparkling Ball
    SWIRLING_CRYSTAL = CodeLiteral("oba")  # Swirling Crystal
    ASHWOOD_BOW = CodeLiteral("am6")  # Ashwood Bow
    CEREMONIAL_BOW = CodeLiteral("am7")  # Ceremonial Bow
    CEREMONIAL_SPEAR = CodeLiteral("am8")  # Ceremonial Spear
    CEREMONIAL_PIKE = CodeLiteral("am9")  # Ceremonial Pike
    CEREMONIAL_JAVELIN = CodeLiteral("ama")  # Ceremonial Javelin
    HEAVENLY_STONE = CodeLiteral("obb")  # Heavenly Stone
    ELDRITCH_ORB = CodeLiteral("obc")  # Eldritch Orb
    DEMON_HEART = CodeLiteral("obd")  # Demon Heart
    VORTEX_ORB = CodeLiteral("obe")  # Vortex Orb
    DIMENSIONAL_SHARD = CodeLiteral("obf")  # Dimensional Shard
    MATRIARCHAL_BOW = CodeLiteral("amb")  # Matriarchal Bow
    GRAND_MATRON_BOW = CodeLiteral("amc")  # Grand Matron Bow
    MATRIARCHAL_SPEAR = CodeLiteral("amd")  # Matriarchal Spear
    MATRIARCHAL_PIKE = CodeLiteral("ame")  # Matriarchal Pike
    MATRIARCHAL_JAVELIN = CodeLiteral("amf")  # Matriarchal Javelin
    FULMINATING_POTION = CodeLiteral("tpfs")  # Fulminating Potion
    EXPLODING_POTION = CodeLiteral("tpfm")  # Exploding Potion
    OIL_POTION = CodeLiteral("tpfl")  # Oil Potion
    STRANGLING_POTION = CodeLiteral("tpgs")  # Strangling Potion
    CHOKING_POTION = CodeLiteral("tpgm")  # Choking Potion
    RANCID_POTION = CodeLiteral("tpgl")  # Rancid Potion
    CHILLING_POTION = CodeLiteral("tpcs")  # Chilling Potion
    FROST_POTION = CodeLiteral("tpcm")  # Frost Potion
    FREEZING_POTION = CodeLiteral("tpcl")  # Freezing Potion
    CHARGED_POTION = CodeLiteral("tpls")  # Charged Potion
    STATIC_POTION = CodeLiteral("tplm")  # Static Potion
    SHOCK_POTION = CodeLiteral("tpll")  # Shock Potion

    @property
    def type(self) -> str:
        return _METADATA[self.name].type

    @property
    def type2(self) -> str:
        return _METADATA[self.name].type2
