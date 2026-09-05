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

    code: str
    type: str  # "type"
    type2: str  # "type2"


class Weapon(BoolMixin, Enum):
    """PD2 weapon categories."""

    HAND_AXE = _Metadata(
        code="hax",
        type="axe",
        type2="",
    )
    AXE = _Metadata(
        code="axe",
        type="axe",
        type2="",
    )
    DOUBLE_AXE = _Metadata(
        code="2ax",
        type="axe",
        type2="",
    )
    MILITARY_PICK = _Metadata(
        code="mpi",
        type="axe",
        type2="",
    )
    WAR_AXE = _Metadata(
        code="wax",
        type="axe",
        type2="",
    )
    LARGE_AXE = _Metadata(
        code="lax",
        type="axe",
        type2="2han",
    )
    BROAD_AXE = _Metadata(
        code="bax",
        type="axe",
        type2="2han",
    )
    BATTLE_AXE = _Metadata(
        code="btx",
        type="axe",
        type2="2han",
    )
    GREAT_AXE = _Metadata(
        code="gax",
        type="axe",
        type2="2han",
    )
    GIANT_AXE = _Metadata(
        code="gix",
        type="axe",
        type2="2han",
    )
    WAND = _Metadata(
        code="wnd",
        type="wand",
        type2="",
    )
    YEW_WAND = _Metadata(
        code="ywn",
        type="wand",
        type2="",
    )
    BONE_WAND = _Metadata(
        code="bwn",
        type="wand",
        type2="",
    )
    GRIM_WAND = _Metadata(
        code="gwn",
        type="wand",
        type2="",
    )
    CLUB = _Metadata(
        code="clb",
        type="club",
        type2="",
    )
    SCEPTER = _Metadata(
        code="scp",
        type="scep",
        type2="",
    )
    GRAND_SCEPTER = _Metadata(
        code="gsc",
        type="scep",
        type2="",
    )
    WAR_SCEPTER = _Metadata(
        code="wsp",
        type="scep",
        type2="",
    )
    SPIKED_CLUB = _Metadata(
        code="spc",
        type="club",
        type2="",
    )
    MACE = _Metadata(
        code="mac",
        type="mace",
        type2="",
    )
    MORNING_STAR = _Metadata(
        code="mst",
        type="mace",
        type2="",
    )
    FLAIL = _Metadata(
        code="fla",
        type="mace",
        type2="",
    )
    WAR_HAMMER = _Metadata(
        code="whm",
        type="hamm",
        type2="",
    )
    MAUL = _Metadata(
        code="mau",
        type="hamm",
        type2="2han",
    )
    GREAT_MAUL = _Metadata(
        code="gma",
        type="hamm",
        type2="2han",
    )
    SHORT_SWORD = _Metadata(
        code="ssd",
        type="swor",
        type2="",
    )
    SCIMITAR = _Metadata(
        code="scm",
        type="swor",
        type2="",
    )
    SABRE = _Metadata(
        code="sbr",
        type="swor",
        type2="",
    )
    FALCHION = _Metadata(
        code="flc",
        type="swor",
        type2="",
    )
    CRYSTAL_SWORD = _Metadata(
        code="crs",
        type="swor",
        type2="crys",
    )
    BROAD_SWORD = _Metadata(
        code="bsd",
        type="swor",
        type2="",
    )
    LONG_SWORD = _Metadata(
        code="lsd",
        type="swor",
        type2="",
    )
    WAR_SWORD = _Metadata(
        code="wsd",
        type="swor",
        type2="",
    )
    TWO_HANDED_SWORD = _Metadata(
        code="2hs",
        type="swor",
        type2="2hsw",
    )
    CLAYMORE = _Metadata(
        code="clm",
        type="swor",
        type2="2hsw",
    )
    GIANT_SWORD = _Metadata(
        code="gis",
        type="swor",
        type2="2hsw",
    )
    BASTARD_SWORD = _Metadata(
        code="bsw",
        type="swor",
        type2="2hsw",
    )
    FLAMBERGE = _Metadata(
        code="flb",
        type="swor",
        type2="2hsw",
    )
    GREAT_SWORD = _Metadata(
        code="gsd",
        type="swor",
        type2="2hsw",
    )
    DAGGER = _Metadata(
        code="dgr",
        type="knif",
        type2="",
    )
    DIRK = _Metadata(
        code="dir",
        type="knif",
        type2="",
    )
    KRIS = _Metadata(
        code="kri",
        type="knif",
        type2="",
    )
    BLADE = _Metadata(
        code="bld",
        type="knif",
        type2="",
    )
    THROWING_KNIFE = _Metadata(
        code="tkf",
        type="tkni",
        type2="",
    )
    THROWING_AXE = _Metadata(
        code="tax",
        type="taxe",
        type2="",
    )
    BALANCED_KNIFE = _Metadata(
        code="bkf",
        type="tkni",
        type2="",
    )
    BALANCED_AXE = _Metadata(
        code="bal",
        type="taxe",
        type2="",
    )
    JAVELIN = _Metadata(
        code="jav",
        type="jave",
        type2="",
    )
    PILUM = _Metadata(
        code="pil",
        type="jave",
        type2="",
    )
    SHORT_SPEAR = _Metadata(
        code="ssp",
        type="jave",
        type2="",
    )
    GLAIVE = _Metadata(
        code="glv",
        type="jave",
        type2="",
    )
    THROWING_SPEAR = _Metadata(
        code="tsp",
        type="jave",
        type2="",
    )
    SPEAR = _Metadata(
        code="spr",
        type="spea",
        type2="2han",
    )
    TRIDENT = _Metadata(
        code="tri",
        type="spea",
        type2="2han",
    )
    BRANDISTOCK = _Metadata(
        code="brn",
        type="spea",
        type2="2han",
    )
    SPETUM = _Metadata(
        code="spt",
        type="spea",
        type2="2han",
    )
    PIKE = _Metadata(
        code="pik",
        type="spea",
        type2="2han",
    )
    BARDICHE = _Metadata(
        code="bar",
        type="pole",
        type2="2han",
    )
    VOULGE = _Metadata(
        code="vou",
        type="pole",
        type2="2han",
    )
    SCYTHE = _Metadata(
        code="scy",
        type="sc9",
        type2="2han",
    )
    POLEAXE = _Metadata(
        code="pax",
        type="pole",
        type2="2han",
    )
    HALBERD = _Metadata(
        code="hal",
        type="pole",
        type2="2han",
    )
    WAR_SCYTHE = _Metadata(
        code="wsc",
        type="sc9",
        type2="2han",
    )
    SHORT_STAFF = _Metadata(
        code="sst",
        type="staf",
        type2="2han",
    )
    LONG_STAFF = _Metadata(
        code="lst",
        type="staf",
        type2="2han",
    )
    GNARLED_STAFF = _Metadata(
        code="cst",
        type="staf",
        type2="2han",
    )
    BATTLE_STAFF = _Metadata(
        code="bst",
        type="staf",
        type2="2han",
    )
    WAR_STAFF = _Metadata(
        code="wst",
        type="staf",
        type2="2han",
    )
    SHORT_BOW = _Metadata(
        code="sbw",
        type="bow",
        type2="",
    )
    HUNTERS_BOW = _Metadata(
        code="hbw",
        type="bow",
        type2="",
    )
    LONG_BOW = _Metadata(
        code="lbw",
        type="bow",
        type2="",
    )
    COMPOSITE_BOW = _Metadata(
        code="cbw",
        type="bow",
        type2="",
    )
    SHORT_BATTLE_BOW = _Metadata(
        code="sbb",
        type="bow",
        type2="",
    )
    LONG_BATTLE_BOW = _Metadata(
        code="lbb",
        type="bow",
        type2="",
    )
    SHORT_WAR_BOW = _Metadata(
        code="swb",
        type="bow",
        type2="",
    )
    LONG_WAR_BOW = _Metadata(
        code="lwb",
        type="bow",
        type2="",
    )
    LIGHT_CROSSBOW = _Metadata(
        code="lxb",
        type="xbow",
        type2="",
    )
    CROSSBOW = _Metadata(
        code="mxb",
        type="xbow",
        type2="",
    )
    HEAVY_CROSSBOW = _Metadata(
        code="hxb",
        type="xbow",
        type2="",
    )
    REPEATING_CROSSBOW = _Metadata(
        code="rxb",
        type="xbow",
        type2="",
    )
    HATCHET = _Metadata(
        code="9ha",
        type="axe",
        type2="",
    )
    CLEAVER = _Metadata(
        code="9ax",
        type="axe",
        type2="",
    )
    TWIN_AXE = _Metadata(
        code="92a",
        type="axe",
        type2="",
    )
    CROWBILL = _Metadata(
        code="9mp",
        type="axe",
        type2="",
    )
    NAGA = _Metadata(
        code="9wa",
        type="axe",
        type2="",
    )
    MILITARY_AXE = _Metadata(
        code="9la",
        type="axe",
        type2="2han",
    )
    BEARDED_AXE = _Metadata(
        code="9ba",
        type="axe",
        type2="2han",
    )
    TABAR = _Metadata(
        code="9bt",
        type="axe",
        type2="2han",
    )
    GOTHIC_AXE = _Metadata(
        code="9ga",
        type="axe",
        type2="2han",
    )
    ANCIENT_AXE = _Metadata(
        code="9gi",
        type="axe",
        type2="2han",
    )
    BURNT_WAND = _Metadata(
        code="9wn",
        type="wand",
        type2="",
    )
    PETRIFIED_WAND = _Metadata(
        code="9yw",
        type="wand",
        type2="",
    )
    TOMB_WAND = _Metadata(
        code="9bw",
        type="wand",
        type2="",
    )
    GRAVE_WAND = _Metadata(
        code="9gw",
        type="wand",
        type2="",
    )
    CUDGEL = _Metadata(
        code="9cl",
        type="club",
        type2="",
    )
    RUNE_SCEPTER = _Metadata(
        code="9sc",
        type="scep",
        type2="",
    )
    HOLY_WATER_SPRINKLER = _Metadata(
        code="9qs",
        type="scep",
        type2="",
    )
    DIVINE_SCEPTER = _Metadata(
        code="9ws",
        type="scep",
        type2="",
    )
    BARBED_CLUB = _Metadata(
        code="9sp",
        type="club",
        type2="",
    )
    FLANGED_MACE = _Metadata(
        code="9ma",
        type="mace",
        type2="",
    )
    JAGGED_STAR = _Metadata(
        code="9mt",
        type="mace",
        type2="",
    )
    KNOUT = _Metadata(
        code="9fl",
        type="mace",
        type2="",
    )
    BATTLE_HAMMER = _Metadata(
        code="9wh",
        type="hamm",
        type2="",
    )
    WAR_CLUB = _Metadata(
        code="9m9",
        type="hamm",
        type2="2han",
    )
    MARTEL_DE_FER = _Metadata(
        code="9gm",
        type="hamm",
        type2="2han",
    )
    GLADIUS = _Metadata(
        code="9ss",
        type="swor",
        type2="",
    )
    CUTLASS = _Metadata(
        code="9sm",
        type="swor",
        type2="",
    )
    SHAMSHIR = _Metadata(
        code="9sb",
        type="swor",
        type2="",
    )
    TULWAR = _Metadata(
        code="9fc",
        type="swor",
        type2="",
    )
    DIMENSIONAL_BLADE = _Metadata(
        code="9cr",
        type="swor",
        type2="crys",
    )
    BATTLE_SWORD = _Metadata(
        code="9bs",
        type="swor",
        type2="",
    )
    RUNE_SWORD = _Metadata(
        code="9ls",
        type="swor",
        type2="",
    )
    ANCIENT_SWORD = _Metadata(
        code="9wd",
        type="swor",
        type2="",
    )
    ESPANDON = _Metadata(
        code="92h",
        type="swor",
        type2="2hsw",
    )
    DACIAN_FALX = _Metadata(
        code="9cm",
        type="swor",
        type2="2hsw",
    )
    TUSK_SWORD = _Metadata(
        code="9gs",
        type="swor",
        type2="2hsw",
    )
    GOTHIC_SWORD = _Metadata(
        code="9b9",
        type="swor",
        type2="2hsw",
    )
    ZWEIHANDER = _Metadata(
        code="9fb",
        type="swor",
        type2="2hsw",
    )
    EXECUTIONER_SWORD = _Metadata(
        code="9gd",
        type="swor",
        type2="2hsw",
    )
    POIGNARD = _Metadata(
        code="9dg",
        type="knif",
        type2="",
    )
    RONDEL = _Metadata(
        code="9di",
        type="knif",
        type2="",
    )
    CINQUEDEAS = _Metadata(
        code="9kr",
        type="knif",
        type2="",
    )
    STILETTO = _Metadata(
        code="9bl",
        type="knif",
        type2="",
    )
    BATTLE_DART = _Metadata(
        code="9tk",
        type="tkni",
        type2="",
    )
    FRANCISCA = _Metadata(
        code="9ta",
        type="taxe",
        type2="",
    )
    WAR_DART = _Metadata(
        code="9bk",
        type="tkni",
        type2="",
    )
    HURLBAT = _Metadata(
        code="9b8",
        type="taxe",
        type2="",
    )
    WAR_JAVELIN = _Metadata(
        code="9ja",
        type="jave",
        type2="",
    )
    GREAT_PILUM = _Metadata(
        code="9pi",
        type="jave",
        type2="",
    )
    SIMBILAN = _Metadata(
        code="9s9",
        type="jave",
        type2="",
    )
    SPICULUM = _Metadata(
        code="9gl",
        type="jave",
        type2="",
    )
    HARPOON = _Metadata(
        code="9ts",
        type="jave",
        type2="",
    )
    WAR_SPEAR = _Metadata(
        code="9sr",
        type="spea",
        type2="2han",
    )
    FUSCINA = _Metadata(
        code="9tr",
        type="spea",
        type2="2han",
    )
    WAR_FORK = _Metadata(
        code="9br",
        type="spea",
        type2="2han",
    )
    YARI = _Metadata(
        code="9st",
        type="spea",
        type2="2han",
    )
    LANCE = _Metadata(
        code="9p9",
        type="spea",
        type2="2han",
    )
    LOCHABER_AXE = _Metadata(
        code="9b7",
        type="pole",
        type2="2han",
    )
    BILL = _Metadata(
        code="9vo",
        type="pole",
        type2="2han",
    )
    BATTLE_SCYTHE = _Metadata(
        code="9s8",
        type="sc9",
        type2="2han",
    )
    PARTIZAN = _Metadata(
        code="9pa",
        type="pole",
        type2="2han",
    )
    BECDE_CORBIN = _Metadata(
        code="9h9",
        type="pole",
        type2="2han",
    )
    GRIM_SCYTHE = _Metadata(
        code="9wc",
        type="sc9",
        type2="2han",
    )
    JO_STAFF = _Metadata(
        code="8ss",
        type="staf",
        type2="2han",
    )
    QUARTERSTAFF = _Metadata(
        code="8ls",
        type="staf",
        type2="2han",
    )
    CEDAR_STAFF = _Metadata(
        code="8cs",
        type="staf",
        type2="2han",
    )
    GOTHIC_STAFF = _Metadata(
        code="8bs",
        type="staf",
        type2="2han",
    )
    RUNE_STAFF = _Metadata(
        code="8ws",
        type="staf",
        type2="2han",
    )
    EDGE_BOW = _Metadata(
        code="8sb",
        type="bow",
        type2="",
    )
    RAZOR_BOW = _Metadata(
        code="8hb",
        type="bow",
        type2="",
    )
    CEDAR_BOW = _Metadata(
        code="8lb",
        type="bow",
        type2="",
    )
    DOUBLE_BOW = _Metadata(
        code="8cb",
        type="bow",
        type2="",
    )
    SHORT_SIEGE_BOW = _Metadata(
        code="8s8",
        type="bow",
        type2="",
    )
    LARGE_SIEGE_BOW = _Metadata(
        code="8l8",
        type="bow",
        type2="",
    )
    RUNE_BOW = _Metadata(
        code="8sw",
        type="bow",
        type2="",
    )
    GOTHIC_BOW = _Metadata(
        code="8lw",
        type="bow",
        type2="",
    )
    ARBALEST = _Metadata(
        code="8lx",
        type="xbow",
        type2="",
    )
    SIEGE_CROSSBOW = _Metadata(
        code="8mx",
        type="xbow",
        type2="",
    )
    BALLISTA = _Metadata(
        code="8hx",
        type="xbow",
        type2="",
    )
    CHU_KO_NU = _Metadata(
        code="8rx",
        type="xbow",
        type2="",
    )
    KATAR = _Metadata(
        code="ktr",
        type="h2h",
        type2="",
    )
    WRIST_BLADE = _Metadata(
        code="wrb",
        type="h2h",
        type2="",
    )
    HATCHET_HANDS = _Metadata(
        code="axf",
        type="h2h",
        type2="",
    )
    CESTUS = _Metadata(
        code="ces",
        type="h2h",
        type2="",
    )
    CLAWS = _Metadata(
        code="clw",
        type="h2h",
        type2="",
    )
    BLADE_TALONS = _Metadata(
        code="btl",
        type="h2h",
        type2="",
    )
    SCISSORS_KATAR = _Metadata(
        code="skr",
        type="h2h",
        type2="",
    )
    QUHAB = _Metadata(
        code="9ar",
        type="h2h",
        type2="",
    )
    WRIST_SPIKE = _Metadata(
        code="9wb",
        type="h2h",
        type2="",
    )
    FASCIA = _Metadata(
        code="9xf",
        type="h2h",
        type2="",
    )
    HAND_SCYTHE = _Metadata(
        code="9cs",
        type="h2h2",
        type2="",
    )
    GREATER_CLAWS = _Metadata(
        code="9lw",
        type="h2h2",
        type2="",
    )
    GREATER_TALONS = _Metadata(
        code="9tw",
        type="h2h2",
        type2="",
    )
    SCISSORS_QUHAB = _Metadata(
        code="9qr",
        type="h2h2",
        type2="",
    )
    SUWAYYAH = _Metadata(
        code="7ar",
        type="h2h2",
        type2="",
    )
    WRIST_SWORD = _Metadata(
        code="7wb",
        type="h2h2",
        type2="",
    )
    WAR_FIST = _Metadata(
        code="7xf",
        type="h2h2",
        type2="",
    )
    BATTLE_CESTUS = _Metadata(
        code="7cs",
        type="h2h2",
        type2="",
    )
    FERAL_CLAWS = _Metadata(
        code="7lw",
        type="h2h2",
        type2="",
    )
    RUNIC_TALONS = _Metadata(
        code="7tw",
        type="h2h2",
        type2="",
    )
    SCISSORS_SUWAYYAH = _Metadata(
        code="7qr",
        type="h2h2",
        type2="",
    )
    TOMAHAWK = _Metadata(
        code="7ha",
        type="axe",
        type2="",
    )
    SMALL_CRESCENT = _Metadata(
        code="7ax",
        type="axe",
        type2="",
    )
    ETTIN_AXE = _Metadata(
        code="72a",
        type="axe",
        type2="",
    )
    WAR_SPIKE = _Metadata(
        code="7mp",
        type="axe",
        type2="",
    )
    BERSERKER_AXE = _Metadata(
        code="7wa",
        type="axe",
        type2="",
    )
    FERAL_AXE = _Metadata(
        code="7la",
        type="axe",
        type2="2han",
    )
    SILVEREDGED_AXE = _Metadata(
        code="7ba",
        type="axe",
        type2="2han",
    )
    DECAPITATOR = _Metadata(
        code="7bt",
        type="axe",
        type2="2han",
    )
    CHAMPION_AXE = _Metadata(
        code="7ga",
        type="axe",
        type2="2han",
    )
    GLORIOUS_AXE = _Metadata(
        code="7gi",
        type="axe",
        type2="2han",
    )
    POLISHED_WAND = _Metadata(
        code="7wn",
        type="wand",
        type2="",
    )
    GHOST_WAND = _Metadata(
        code="7yw",
        type="wand",
        type2="",
    )
    LICH_WAND = _Metadata(
        code="7bw",
        type="wand",
        type2="",
    )
    UNEARTHED_WAND = _Metadata(
        code="7gw",
        type="wand",
        type2="",
    )
    TRUNCHEON = _Metadata(
        code="7cl",
        type="club",
        type2="",
    )
    MIGHTY_SCEPTER = _Metadata(
        code="7sc",
        type="scep",
        type2="",
    )
    SERAPH_ROD = _Metadata(
        code="7qs",
        type="scep",
        type2="",
    )
    CADUCEUS = _Metadata(
        code="7ws",
        type="scep",
        type2="",
    )
    TYRANT_CLUB = _Metadata(
        code="7sp",
        type="club",
        type2="",
    )
    REINFORCED_MACE = _Metadata(
        code="7ma",
        type="mace",
        type2="",
    )
    DEVIL_STAR = _Metadata(
        code="7mt",
        type="mace",
        type2="",
    )
    SCOURGE = _Metadata(
        code="7fl",
        type="mace",
        type2="",
    )
    LEGENDARY_MALLET = _Metadata(
        code="7wh",
        type="hamm",
        type2="",
    )
    OGRE_MAUL = _Metadata(
        code="7m7",
        type="hamm",
        type2="2han",
    )
    THUNDER_MAUL = _Metadata(
        code="7gm",
        type="hamm",
        type2="2han",
    )
    FALCATA = _Metadata(
        code="7ss",
        type="swor",
        type2="",
    )
    ATAGHAN = _Metadata(
        code="7sm",
        type="swor",
        type2="",
    )
    ELEGANT_BLADE = _Metadata(
        code="7sb",
        type="swor",
        type2="",
    )
    HYDRA_EDGE = _Metadata(
        code="7fc",
        type="swor",
        type2="",
    )
    PHASE_BLADE = _Metadata(
        code="7cr",
        type="swor",
        type2="crys",
    )
    CONQUEST_SWORD = _Metadata(
        code="7bs",
        type="swor",
        type2="",
    )
    CRYPTIC_SWORD = _Metadata(
        code="7ls",
        type="swor",
        type2="",
    )
    MYTHICAL_SWORD = _Metadata(
        code="7wd",
        type="swor",
        type2="",
    )
    LEGEND_SWORD = _Metadata(
        code="72h",
        type="swor",
        type2="2hsw",
    )
    HIGHLAND_BLADE = _Metadata(
        code="7cm",
        type="swor",
        type2="2hsw",
    )
    BALROG_BLADE = _Metadata(
        code="7gs",
        type="swor",
        type2="2hsw",
    )
    CHAMPION_SWORD = _Metadata(
        code="7b7",
        type="swor",
        type2="2hsw",
    )
    COLOSSUS_SWORD = _Metadata(
        code="7fb",
        type="swor",
        type2="2hsw",
    )
    COLOSSUS_BLADE = _Metadata(
        code="7gd",
        type="swor",
        type2="2hsw",
    )
    BONE_KNIFE = _Metadata(
        code="7dg",
        type="knif",
        type2="",
    )
    MITHRIL_POINT = _Metadata(
        code="7di",
        type="knif",
        type2="",
    )
    FANGED_KNIFE = _Metadata(
        code="7kr",
        type="knif",
        type2="",
    )
    LEGEND_SPIKE = _Metadata(
        code="7bl",
        type="knif",
        type2="",
    )
    FLYING_KNIFE = _Metadata(
        code="7tk",
        type="tkni",
        type2="",
    )
    FLYING_AXE = _Metadata(
        code="7ta",
        type="taxe",
        type2="",
    )
    WINGED_KNIFE = _Metadata(
        code="7bk",
        type="tkni",
        type2="",
    )
    WINGED_AXE = _Metadata(
        code="7b8",
        type="taxe",
        type2="",
    )
    HYPERION_JAVELIN = _Metadata(
        code="7ja",
        type="jave",
        type2="",
    )
    STYGIAN_PILUM = _Metadata(
        code="7pi",
        type="jave",
        type2="",
    )
    BALROG_SPEAR = _Metadata(
        code="7s7",
        type="jave",
        type2="",
    )
    GHOST_GLAIVE = _Metadata(
        code="7gl",
        type="jave",
        type2="",
    )
    WINGED_HARPOON = _Metadata(
        code="7ts",
        type="jave",
        type2="",
    )
    HYPERION_SPEAR = _Metadata(
        code="7sr",
        type="spea",
        type2="2han",
    )
    STYGIAN_PIKE = _Metadata(
        code="7tr",
        type="spea",
        type2="2han",
    )
    MANCATCHER = _Metadata(
        code="7br",
        type="spea",
        type2="2han",
    )
    GHOST_SPEAR = _Metadata(
        code="7st",
        type="spea",
        type2="2han",
    )
    WAR_PIKE = _Metadata(
        code="7p7",
        type="spea",
        type2="2han",
    )
    OGRE_AXE = _Metadata(
        code="7o7",
        type="pole",
        type2="2han",
    )
    COLOSSUS_VOULGE = _Metadata(
        code="7vo",
        type="pole",
        type2="2han",
    )
    THRESHER = _Metadata(
        code="7s8",
        type="sc9",
        type2="2han",
    )
    CRYPTIC_AXE = _Metadata(
        code="7pa",
        type="pole",
        type2="2han",
    )
    GREAT_POLEAXE = _Metadata(
        code="7h7",
        type="pole",
        type2="2han",
    )
    GIANT_THRESHER = _Metadata(
        code="7wc",
        type="sc9",
        type2="2han",
    )
    WALKING_STICK = _Metadata(
        code="6ss",
        type="staf",
        type2="2han",
    )
    STALAGMITE = _Metadata(
        code="6ls",
        type="staf",
        type2="2han",
    )
    ELDER_STAFF = _Metadata(
        code="6cs",
        type="staf",
        type2="2han",
    )
    SHILLELAGH = _Metadata(
        code="6bs",
        type="staf",
        type2="2han",
    )
    ARCHON_STAFF = _Metadata(
        code="6ws",
        type="staf",
        type2="2han",
    )
    SPIDER_BOW = _Metadata(
        code="6sb",
        type="bow",
        type2="",
    )
    BLADE_BOW = _Metadata(
        code="6hb",
        type="bow",
        type2="",
    )
    SHADOW_BOW = _Metadata(
        code="6lb",
        type="bow",
        type2="",
    )
    GREAT_BOW = _Metadata(
        code="6cb",
        type="bow",
        type2="",
    )
    DIAMOND_BOW = _Metadata(
        code="6s7",
        type="bow",
        type2="",
    )
    CRUSADER_BOW = _Metadata(
        code="6l7",
        type="bow",
        type2="",
    )
    WARD_BOW = _Metadata(
        code="6sw",
        type="bow",
        type2="",
    )
    HYDRA_BOW = _Metadata(
        code="6lw",
        type="bow",
        type2="",
    )
    PELLET_BOW = _Metadata(
        code="6lx",
        type="xbow",
        type2="",
    )
    GORGON_CROSSBOW = _Metadata(
        code="6mx",
        type="xbow",
        type2="",
    )
    COLOSSUS_CROSSBOW = _Metadata(
        code="6hx",
        type="xbow",
        type2="",
    )
    DEMON_CROSSBOW = _Metadata(
        code="6rx",
        type="xbow",
        type2="",
    )
    EAGLE_ORB = _Metadata(
        code="ob1",
        type="orb",
        type2="",
    )
    SACRED_GLOBE = _Metadata(
        code="ob2",
        type="orb",
        type2="",
    )
    SMOKED_SPHERE = _Metadata(
        code="ob3",
        type="orb",
        type2="",
    )
    CLASPED_ORB = _Metadata(
        code="ob4",
        type="orb",
        type2="",
    )
    JAREDS_STONE = _Metadata(
        code="ob5",
        type="orb",
        type2="",
    )
    STAG_BOW = _Metadata(
        code="am1",
        type="abow",
        type2="",
    )
    REFLEX_BOW = _Metadata(
        code="am2",
        type="abow",
        type2="",
    )
    MAIDEN_SPEAR = _Metadata(
        code="am3",
        type="aspe",
        type2="2han",
    )
    MAIDEN_PIKE = _Metadata(
        code="am4",
        type="aspe",
        type2="2han",
    )
    MAIDEN_JAVELIN = _Metadata(
        code="am5",
        type="ajav",
        type2="",
    )
    GLOWING_ORB = _Metadata(
        code="ob6",
        type="orb",
        type2="",
    )
    CRYSTALLINE_GLOBE = _Metadata(
        code="ob7",
        type="orb",
        type2="",
    )
    CLOUDY_SPHERE = _Metadata(
        code="ob8",
        type="orb",
        type2="",
    )
    SPARKLING_BALL = _Metadata(
        code="ob9",
        type="orb",
        type2="",
    )
    SWIRLING_CRYSTAL = _Metadata(
        code="oba",
        type="orb",
        type2="",
    )
    ASHWOOD_BOW = _Metadata(
        code="am6",
        type="abow",
        type2="",
    )
    CEREMONIAL_BOW = _Metadata(
        code="am7",
        type="abow",
        type2="",
    )
    CEREMONIAL_SPEAR = _Metadata(
        code="am8",
        type="aspe",
        type2="2han",
    )
    CEREMONIAL_PIKE = _Metadata(
        code="am9",
        type="aspe",
        type2="2han",
    )
    CEREMONIAL_JAVELIN = _Metadata(
        code="ama",
        type="ajav",
        type2="",
    )
    HEAVENLY_STONE = _Metadata(
        code="obb",
        type="orb",
        type2="",
    )
    ELDRITCH_ORB = _Metadata(
        code="obc",
        type="orb",
        type2="",
    )
    DEMON_HEART = _Metadata(
        code="obd",
        type="orb",
        type2="",
    )
    VORTEX_ORB = _Metadata(
        code="obe",
        type="orb",
        type2="",
    )
    DIMENSIONAL_SHARD = _Metadata(
        code="obf",
        type="orb",
        type2="",
    )
    MATRIARCHAL_BOW = _Metadata(
        code="amb",
        type="abow",
        type2="",
    )
    GRAND_MATRON_BOW = _Metadata(
        code="amc",
        type="abow",
        type2="",
    )
    MATRIARCHAL_SPEAR = _Metadata(
        code="amd",
        type="aspe",
        type2="2han",
    )
    MATRIARCHAL_PIKE = _Metadata(
        code="ame",
        type="aspe",
        type2="2han",
    )
    MATRIARCHAL_JAVELIN = _Metadata(
        code="amf",
        type="ajav",
        type2="",
    )
    FULMINATING_POTION = _Metadata(
        code="tpfs",
        type="tpot",
        type2="",
    )
    EXPLODING_POTION = _Metadata(
        code="tpfm",
        type="tpot",
        type2="",
    )
    OIL_POTION = _Metadata(
        code="tpfl",
        type="tpot",
        type2="",
    )
    STRANGLING_POTION = _Metadata(
        code="tpgs",
        type="tpot",
        type2="",
    )
    CHOKING_POTION = _Metadata(
        code="tpgm",
        type="tpot",
        type2="",
    )
    RANCID_POTION = _Metadata(
        code="tpgl",
        type="tpot",
        type2="",
    )
    CHILLING_POTION = _Metadata(
        code="tpcs",
        type="tpot",
        type2="",
    )
    FROST_POTION = _Metadata(
        code="tpcm",
        type="tpot",
        type2="",
    )
    FREEZING_POTION = _Metadata(
        code="tpcl",
        type="tpot",
        type2="",
    )
    CHARGED_POTION = _Metadata(
        code="tpls",
        type="tpot",
        type2="",
    )
    STATIC_POTION = _Metadata(
        code="tplm",
        type="tpot",
        type2="",
    )
    SHOCK_POTION = _Metadata(
        code="tpll",
        type="tpot",
        type2="",
    )

    def as_node(self) -> BoolRef:
        return BoolRef(self.value.code)

    @property
    def type(self) -> str:
        return self.value.type

    @property
    def type2(self) -> str:
        return self.value.type2
