"""
Generated Weapon enum from PD2 data.

DO NOT EDIT MANUALLY - regenerate with: hatch run ./scripts/generate.py generate
"""

from __future__ import annotations

from pd2_filter_generator.expression import BoolRef


class _Weapon(BoolRef):
    """Item type metadata."""

    def __init__(self, value: str, type: str, type2: str):  # noqa: A002
        super().__init__(value)
        self._type = type
        self._type2 = type2

    @property
    def type(self) -> str:
        return self._type

    @property
    def type2(self) -> str:
        return self._type2


values = [
    HAND_AXE := _Weapon(
        value="hax",
        type="axe",
        type2="",
    ),
    AXE := _Weapon(
        value="axe",
        type="axe",
        type2="",
    ),
    DOUBLE_AXE := _Weapon(
        value="2ax",
        type="axe",
        type2="",
    ),
    MILITARY_PICK := _Weapon(
        value="mpi",
        type="axe",
        type2="",
    ),
    WAR_AXE := _Weapon(
        value="wax",
        type="axe",
        type2="",
    ),
    LARGE_AXE := _Weapon(
        value="lax",
        type="axe",
        type2="2han",
    ),
    BROAD_AXE := _Weapon(
        value="bax",
        type="axe",
        type2="2han",
    ),
    BATTLE_AXE := _Weapon(
        value="btx",
        type="axe",
        type2="2han",
    ),
    GREAT_AXE := _Weapon(
        value="gax",
        type="axe",
        type2="2han",
    ),
    GIANT_AXE := _Weapon(
        value="gix",
        type="axe",
        type2="2han",
    ),
    WAND := _Weapon(
        value="wnd",
        type="wand",
        type2="",
    ),
    YEW_WAND := _Weapon(
        value="ywn",
        type="wand",
        type2="",
    ),
    BONE_WAND := _Weapon(
        value="bwn",
        type="wand",
        type2="",
    ),
    GRIM_WAND := _Weapon(
        value="gwn",
        type="wand",
        type2="",
    ),
    CLUB := _Weapon(
        value="clb",
        type="club",
        type2="",
    ),
    SCEPTER := _Weapon(
        value="scp",
        type="scep",
        type2="",
    ),
    GRAND_SCEPTER := _Weapon(
        value="gsc",
        type="scep",
        type2="",
    ),
    WAR_SCEPTER := _Weapon(
        value="wsp",
        type="scep",
        type2="",
    ),
    SPIKED_CLUB := _Weapon(
        value="spc",
        type="club",
        type2="",
    ),
    MACE := _Weapon(
        value="mac",
        type="mace",
        type2="",
    ),
    MORNING_STAR := _Weapon(
        value="mst",
        type="mace",
        type2="",
    ),
    FLAIL := _Weapon(
        value="fla",
        type="mace",
        type2="",
    ),
    WAR_HAMMER := _Weapon(
        value="whm",
        type="hamm",
        type2="",
    ),
    MAUL := _Weapon(
        value="mau",
        type="hamm",
        type2="2han",
    ),
    GREAT_MAUL := _Weapon(
        value="gma",
        type="hamm",
        type2="2han",
    ),
    SHORT_SWORD := _Weapon(
        value="ssd",
        type="swor",
        type2="",
    ),
    SCIMITAR := _Weapon(
        value="scm",
        type="swor",
        type2="",
    ),
    SABRE := _Weapon(
        value="sbr",
        type="swor",
        type2="",
    ),
    FALCHION := _Weapon(
        value="flc",
        type="swor",
        type2="",
    ),
    CRYSTAL_SWORD := _Weapon(
        value="crs",
        type="swor",
        type2="crys",
    ),
    BROAD_SWORD := _Weapon(
        value="bsd",
        type="swor",
        type2="",
    ),
    LONG_SWORD := _Weapon(
        value="lsd",
        type="swor",
        type2="",
    ),
    WAR_SWORD := _Weapon(
        value="wsd",
        type="swor",
        type2="",
    ),
    TWO_HANDED_SWORD := _Weapon(
        value="2hs",
        type="swor",
        type2="2hsw",
    ),
    CLAYMORE := _Weapon(
        value="clm",
        type="swor",
        type2="2hsw",
    ),
    GIANT_SWORD := _Weapon(
        value="gis",
        type="swor",
        type2="2hsw",
    ),
    BASTARD_SWORD := _Weapon(
        value="bsw",
        type="swor",
        type2="2hsw",
    ),
    FLAMBERGE := _Weapon(
        value="flb",
        type="swor",
        type2="2hsw",
    ),
    GREAT_SWORD := _Weapon(
        value="gsd",
        type="swor",
        type2="2hsw",
    ),
    DAGGER := _Weapon(
        value="dgr",
        type="knif",
        type2="",
    ),
    DIRK := _Weapon(
        value="dir",
        type="knif",
        type2="",
    ),
    KRIS := _Weapon(
        value="kri",
        type="knif",
        type2="",
    ),
    BLADE := _Weapon(
        value="bld",
        type="knif",
        type2="",
    ),
    THROWING_KNIFE := _Weapon(
        value="tkf",
        type="tkni",
        type2="",
    ),
    THROWING_AXE := _Weapon(
        value="tax",
        type="taxe",
        type2="",
    ),
    BALANCED_KNIFE := _Weapon(
        value="bkf",
        type="tkni",
        type2="",
    ),
    BALANCED_AXE := _Weapon(
        value="bal",
        type="taxe",
        type2="",
    ),
    JAVELIN := _Weapon(
        value="jav",
        type="jave",
        type2="",
    ),
    PILUM := _Weapon(
        value="pil",
        type="jave",
        type2="",
    ),
    SHORT_SPEAR := _Weapon(
        value="ssp",
        type="jave",
        type2="",
    ),
    GLAIVE := _Weapon(
        value="glv",
        type="jave",
        type2="",
    ),
    THROWING_SPEAR := _Weapon(
        value="tsp",
        type="jave",
        type2="",
    ),
    SPEAR := _Weapon(
        value="spr",
        type="spea",
        type2="2han",
    ),
    TRIDENT := _Weapon(
        value="tri",
        type="spea",
        type2="2han",
    ),
    BRANDISTOCK := _Weapon(
        value="brn",
        type="spea",
        type2="2han",
    ),
    SPETUM := _Weapon(
        value="spt",
        type="spea",
        type2="2han",
    ),
    PIKE := _Weapon(
        value="pik",
        type="spea",
        type2="2han",
    ),
    BARDICHE := _Weapon(
        value="bar",
        type="pole",
        type2="2han",
    ),
    VOULGE := _Weapon(
        value="vou",
        type="pole",
        type2="2han",
    ),
    SCYTHE := _Weapon(
        value="scy",
        type="sc9",
        type2="2han",
    ),
    POLEAXE := _Weapon(
        value="pax",
        type="pole",
        type2="2han",
    ),
    HALBERD := _Weapon(
        value="hal",
        type="pole",
        type2="2han",
    ),
    WAR_SCYTHE := _Weapon(
        value="wsc",
        type="sc9",
        type2="2han",
    ),
    SHORT_STAFF := _Weapon(
        value="sst",
        type="staf",
        type2="2han",
    ),
    LONG_STAFF := _Weapon(
        value="lst",
        type="staf",
        type2="2han",
    ),
    GNARLED_STAFF := _Weapon(
        value="cst",
        type="staf",
        type2="2han",
    ),
    BATTLE_STAFF := _Weapon(
        value="bst",
        type="staf",
        type2="2han",
    ),
    WAR_STAFF := _Weapon(
        value="wst",
        type="staf",
        type2="2han",
    ),
    SHORT_BOW := _Weapon(
        value="sbw",
        type="bow",
        type2="",
    ),
    HUNTERS_BOW := _Weapon(
        value="hbw",
        type="bow",
        type2="",
    ),
    LONG_BOW := _Weapon(
        value="lbw",
        type="bow",
        type2="",
    ),
    COMPOSITE_BOW := _Weapon(
        value="cbw",
        type="bow",
        type2="",
    ),
    SHORT_BATTLE_BOW := _Weapon(
        value="sbb",
        type="bow",
        type2="",
    ),
    LONG_BATTLE_BOW := _Weapon(
        value="lbb",
        type="bow",
        type2="",
    ),
    SHORT_WAR_BOW := _Weapon(
        value="swb",
        type="bow",
        type2="",
    ),
    LONG_WAR_BOW := _Weapon(
        value="lwb",
        type="bow",
        type2="",
    ),
    LIGHT_CROSSBOW := _Weapon(
        value="lxb",
        type="xbow",
        type2="",
    ),
    CROSSBOW := _Weapon(
        value="mxb",
        type="xbow",
        type2="",
    ),
    HEAVY_CROSSBOW := _Weapon(
        value="hxb",
        type="xbow",
        type2="",
    ),
    REPEATING_CROSSBOW := _Weapon(
        value="rxb",
        type="xbow",
        type2="",
    ),
    HATCHET := _Weapon(
        value="9ha",
        type="axe",
        type2="",
    ),
    CLEAVER := _Weapon(
        value="9ax",
        type="axe",
        type2="",
    ),
    TWIN_AXE := _Weapon(
        value="92a",
        type="axe",
        type2="",
    ),
    CROWBILL := _Weapon(
        value="9mp",
        type="axe",
        type2="",
    ),
    NAGA := _Weapon(
        value="9wa",
        type="axe",
        type2="",
    ),
    MILITARY_AXE := _Weapon(
        value="9la",
        type="axe",
        type2="2han",
    ),
    BEARDED_AXE := _Weapon(
        value="9ba",
        type="axe",
        type2="2han",
    ),
    TABAR := _Weapon(
        value="9bt",
        type="axe",
        type2="2han",
    ),
    GOTHIC_AXE := _Weapon(
        value="9ga",
        type="axe",
        type2="2han",
    ),
    ANCIENT_AXE := _Weapon(
        value="9gi",
        type="axe",
        type2="2han",
    ),
    BURNT_WAND := _Weapon(
        value="9wn",
        type="wand",
        type2="",
    ),
    PETRIFIED_WAND := _Weapon(
        value="9yw",
        type="wand",
        type2="",
    ),
    TOMB_WAND := _Weapon(
        value="9bw",
        type="wand",
        type2="",
    ),
    GRAVE_WAND := _Weapon(
        value="9gw",
        type="wand",
        type2="",
    ),
    CUDGEL := _Weapon(
        value="9cl",
        type="club",
        type2="",
    ),
    RUNE_SCEPTER := _Weapon(
        value="9sc",
        type="scep",
        type2="",
    ),
    HOLY_WATER_SPRINKLER := _Weapon(
        value="9qs",
        type="scep",
        type2="",
    ),
    DIVINE_SCEPTER := _Weapon(
        value="9ws",
        type="scep",
        type2="",
    ),
    BARBED_CLUB := _Weapon(
        value="9sp",
        type="club",
        type2="",
    ),
    FLANGED_MACE := _Weapon(
        value="9ma",
        type="mace",
        type2="",
    ),
    JAGGED_STAR := _Weapon(
        value="9mt",
        type="mace",
        type2="",
    ),
    KNOUT := _Weapon(
        value="9fl",
        type="mace",
        type2="",
    ),
    BATTLE_HAMMER := _Weapon(
        value="9wh",
        type="hamm",
        type2="",
    ),
    WAR_CLUB := _Weapon(
        value="9m9",
        type="hamm",
        type2="2han",
    ),
    MARTEL_DE_FER := _Weapon(
        value="9gm",
        type="hamm",
        type2="2han",
    ),
    GLADIUS := _Weapon(
        value="9ss",
        type="swor",
        type2="",
    ),
    CUTLASS := _Weapon(
        value="9sm",
        type="swor",
        type2="",
    ),
    SHAMSHIR := _Weapon(
        value="9sb",
        type="swor",
        type2="",
    ),
    TULWAR := _Weapon(
        value="9fc",
        type="swor",
        type2="",
    ),
    DIMENSIONAL_BLADE := _Weapon(
        value="9cr",
        type="swor",
        type2="crys",
    ),
    BATTLE_SWORD := _Weapon(
        value="9bs",
        type="swor",
        type2="",
    ),
    RUNE_SWORD := _Weapon(
        value="9ls",
        type="swor",
        type2="",
    ),
    ANCIENT_SWORD := _Weapon(
        value="9wd",
        type="swor",
        type2="",
    ),
    ESPANDON := _Weapon(
        value="92h",
        type="swor",
        type2="2hsw",
    ),
    DACIAN_FALX := _Weapon(
        value="9cm",
        type="swor",
        type2="2hsw",
    ),
    TUSK_SWORD := _Weapon(
        value="9gs",
        type="swor",
        type2="2hsw",
    ),
    GOTHIC_SWORD := _Weapon(
        value="9b9",
        type="swor",
        type2="2hsw",
    ),
    ZWEIHANDER := _Weapon(
        value="9fb",
        type="swor",
        type2="2hsw",
    ),
    EXECUTIONER_SWORD := _Weapon(
        value="9gd",
        type="swor",
        type2="2hsw",
    ),
    POIGNARD := _Weapon(
        value="9dg",
        type="knif",
        type2="",
    ),
    RONDEL := _Weapon(
        value="9di",
        type="knif",
        type2="",
    ),
    CINQUEDEAS := _Weapon(
        value="9kr",
        type="knif",
        type2="",
    ),
    STILETTO := _Weapon(
        value="9bl",
        type="knif",
        type2="",
    ),
    BATTLE_DART := _Weapon(
        value="9tk",
        type="tkni",
        type2="",
    ),
    FRANCISCA := _Weapon(
        value="9ta",
        type="taxe",
        type2="",
    ),
    WAR_DART := _Weapon(
        value="9bk",
        type="tkni",
        type2="",
    ),
    HURLBAT := _Weapon(
        value="9b8",
        type="taxe",
        type2="",
    ),
    WAR_JAVELIN := _Weapon(
        value="9ja",
        type="jave",
        type2="",
    ),
    GREAT_PILUM := _Weapon(
        value="9pi",
        type="jave",
        type2="",
    ),
    SIMBILAN := _Weapon(
        value="9s9",
        type="jave",
        type2="",
    ),
    SPICULUM := _Weapon(
        value="9gl",
        type="jave",
        type2="",
    ),
    HARPOON := _Weapon(
        value="9ts",
        type="jave",
        type2="",
    ),
    WAR_SPEAR := _Weapon(
        value="9sr",
        type="spea",
        type2="2han",
    ),
    FUSCINA := _Weapon(
        value="9tr",
        type="spea",
        type2="2han",
    ),
    WAR_FORK := _Weapon(
        value="9br",
        type="spea",
        type2="2han",
    ),
    YARI := _Weapon(
        value="9st",
        type="spea",
        type2="2han",
    ),
    LANCE := _Weapon(
        value="9p9",
        type="spea",
        type2="2han",
    ),
    LOCHABER_AXE := _Weapon(
        value="9b7",
        type="pole",
        type2="2han",
    ),
    BILL := _Weapon(
        value="9vo",
        type="pole",
        type2="2han",
    ),
    BATTLE_SCYTHE := _Weapon(
        value="9s8",
        type="sc9",
        type2="2han",
    ),
    PARTIZAN := _Weapon(
        value="9pa",
        type="pole",
        type2="2han",
    ),
    BECDE_CORBIN := _Weapon(
        value="9h9",
        type="pole",
        type2="2han",
    ),
    GRIM_SCYTHE := _Weapon(
        value="9wc",
        type="sc9",
        type2="2han",
    ),
    JO_STAFF := _Weapon(
        value="8ss",
        type="staf",
        type2="2han",
    ),
    QUARTERSTAFF := _Weapon(
        value="8ls",
        type="staf",
        type2="2han",
    ),
    CEDAR_STAFF := _Weapon(
        value="8cs",
        type="staf",
        type2="2han",
    ),
    GOTHIC_STAFF := _Weapon(
        value="8bs",
        type="staf",
        type2="2han",
    ),
    RUNE_STAFF := _Weapon(
        value="8ws",
        type="staf",
        type2="2han",
    ),
    EDGE_BOW := _Weapon(
        value="8sb",
        type="bow",
        type2="",
    ),
    RAZOR_BOW := _Weapon(
        value="8hb",
        type="bow",
        type2="",
    ),
    CEDAR_BOW := _Weapon(
        value="8lb",
        type="bow",
        type2="",
    ),
    DOUBLE_BOW := _Weapon(
        value="8cb",
        type="bow",
        type2="",
    ),
    SHORT_SIEGE_BOW := _Weapon(
        value="8s8",
        type="bow",
        type2="",
    ),
    LARGE_SIEGE_BOW := _Weapon(
        value="8l8",
        type="bow",
        type2="",
    ),
    RUNE_BOW := _Weapon(
        value="8sw",
        type="bow",
        type2="",
    ),
    GOTHIC_BOW := _Weapon(
        value="8lw",
        type="bow",
        type2="",
    ),
    ARBALEST := _Weapon(
        value="8lx",
        type="xbow",
        type2="",
    ),
    SIEGE_CROSSBOW := _Weapon(
        value="8mx",
        type="xbow",
        type2="",
    ),
    BALLISTA := _Weapon(
        value="8hx",
        type="xbow",
        type2="",
    ),
    CHU_KO_NU := _Weapon(
        value="8rx",
        type="xbow",
        type2="",
    ),
    KATAR := _Weapon(
        value="ktr",
        type="h2h",
        type2="",
    ),
    WRIST_BLADE := _Weapon(
        value="wrb",
        type="h2h",
        type2="",
    ),
    HATCHET_HANDS := _Weapon(
        value="axf",
        type="h2h",
        type2="",
    ),
    CESTUS := _Weapon(
        value="ces",
        type="h2h",
        type2="",
    ),
    CLAWS := _Weapon(
        value="clw",
        type="h2h",
        type2="",
    ),
    BLADE_TALONS := _Weapon(
        value="btl",
        type="h2h",
        type2="",
    ),
    SCISSORS_KATAR := _Weapon(
        value="skr",
        type="h2h",
        type2="",
    ),
    QUHAB := _Weapon(
        value="9ar",
        type="h2h",
        type2="",
    ),
    WRIST_SPIKE := _Weapon(
        value="9wb",
        type="h2h",
        type2="",
    ),
    FASCIA := _Weapon(
        value="9xf",
        type="h2h",
        type2="",
    ),
    HAND_SCYTHE := _Weapon(
        value="9cs",
        type="h2h2",
        type2="",
    ),
    GREATER_CLAWS := _Weapon(
        value="9lw",
        type="h2h2",
        type2="",
    ),
    GREATER_TALONS := _Weapon(
        value="9tw",
        type="h2h2",
        type2="",
    ),
    SCISSORS_QUHAB := _Weapon(
        value="9qr",
        type="h2h2",
        type2="",
    ),
    SUWAYYAH := _Weapon(
        value="7ar",
        type="h2h2",
        type2="",
    ),
    WRIST_SWORD := _Weapon(
        value="7wb",
        type="h2h2",
        type2="",
    ),
    WAR_FIST := _Weapon(
        value="7xf",
        type="h2h2",
        type2="",
    ),
    BATTLE_CESTUS := _Weapon(
        value="7cs",
        type="h2h2",
        type2="",
    ),
    FERAL_CLAWS := _Weapon(
        value="7lw",
        type="h2h2",
        type2="",
    ),
    RUNIC_TALONS := _Weapon(
        value="7tw",
        type="h2h2",
        type2="",
    ),
    SCISSORS_SUWAYYAH := _Weapon(
        value="7qr",
        type="h2h2",
        type2="",
    ),
    TOMAHAWK := _Weapon(
        value="7ha",
        type="axe",
        type2="",
    ),
    SMALL_CRESCENT := _Weapon(
        value="7ax",
        type="axe",
        type2="",
    ),
    ETTIN_AXE := _Weapon(
        value="72a",
        type="axe",
        type2="",
    ),
    WAR_SPIKE := _Weapon(
        value="7mp",
        type="axe",
        type2="",
    ),
    BERSERKER_AXE := _Weapon(
        value="7wa",
        type="axe",
        type2="",
    ),
    FERAL_AXE := _Weapon(
        value="7la",
        type="axe",
        type2="2han",
    ),
    SILVEREDGED_AXE := _Weapon(
        value="7ba",
        type="axe",
        type2="2han",
    ),
    DECAPITATOR := _Weapon(
        value="7bt",
        type="axe",
        type2="2han",
    ),
    CHAMPION_AXE := _Weapon(
        value="7ga",
        type="axe",
        type2="2han",
    ),
    GLORIOUS_AXE := _Weapon(
        value="7gi",
        type="axe",
        type2="2han",
    ),
    POLISHED_WAND := _Weapon(
        value="7wn",
        type="wand",
        type2="",
    ),
    GHOST_WAND := _Weapon(
        value="7yw",
        type="wand",
        type2="",
    ),
    LICH_WAND := _Weapon(
        value="7bw",
        type="wand",
        type2="",
    ),
    UNEARTHED_WAND := _Weapon(
        value="7gw",
        type="wand",
        type2="",
    ),
    TRUNCHEON := _Weapon(
        value="7cl",
        type="club",
        type2="",
    ),
    MIGHTY_SCEPTER := _Weapon(
        value="7sc",
        type="scep",
        type2="",
    ),
    SERAPH_ROD := _Weapon(
        value="7qs",
        type="scep",
        type2="",
    ),
    CADUCEUS := _Weapon(
        value="7ws",
        type="scep",
        type2="",
    ),
    TYRANT_CLUB := _Weapon(
        value="7sp",
        type="club",
        type2="",
    ),
    REINFORCED_MACE := _Weapon(
        value="7ma",
        type="mace",
        type2="",
    ),
    DEVIL_STAR := _Weapon(
        value="7mt",
        type="mace",
        type2="",
    ),
    SCOURGE := _Weapon(
        value="7fl",
        type="mace",
        type2="",
    ),
    LEGENDARY_MALLET := _Weapon(
        value="7wh",
        type="hamm",
        type2="",
    ),
    OGRE_MAUL := _Weapon(
        value="7m7",
        type="hamm",
        type2="2han",
    ),
    THUNDER_MAUL := _Weapon(
        value="7gm",
        type="hamm",
        type2="2han",
    ),
    FALCATA := _Weapon(
        value="7ss",
        type="swor",
        type2="",
    ),
    ATAGHAN := _Weapon(
        value="7sm",
        type="swor",
        type2="",
    ),
    ELEGANT_BLADE := _Weapon(
        value="7sb",
        type="swor",
        type2="",
    ),
    HYDRA_EDGE := _Weapon(
        value="7fc",
        type="swor",
        type2="",
    ),
    PHASE_BLADE := _Weapon(
        value="7cr",
        type="swor",
        type2="crys",
    ),
    CONQUEST_SWORD := _Weapon(
        value="7bs",
        type="swor",
        type2="",
    ),
    CRYPTIC_SWORD := _Weapon(
        value="7ls",
        type="swor",
        type2="",
    ),
    MYTHICAL_SWORD := _Weapon(
        value="7wd",
        type="swor",
        type2="",
    ),
    LEGEND_SWORD := _Weapon(
        value="72h",
        type="swor",
        type2="2hsw",
    ),
    HIGHLAND_BLADE := _Weapon(
        value="7cm",
        type="swor",
        type2="2hsw",
    ),
    BALROG_BLADE := _Weapon(
        value="7gs",
        type="swor",
        type2="2hsw",
    ),
    CHAMPION_SWORD := _Weapon(
        value="7b7",
        type="swor",
        type2="2hsw",
    ),
    COLOSSUS_SWORD := _Weapon(
        value="7fb",
        type="swor",
        type2="2hsw",
    ),
    COLOSSUS_BLADE := _Weapon(
        value="7gd",
        type="swor",
        type2="2hsw",
    ),
    BONE_KNIFE := _Weapon(
        value="7dg",
        type="knif",
        type2="",
    ),
    MITHRIL_POINT := _Weapon(
        value="7di",
        type="knif",
        type2="",
    ),
    FANGED_KNIFE := _Weapon(
        value="7kr",
        type="knif",
        type2="",
    ),
    LEGEND_SPIKE := _Weapon(
        value="7bl",
        type="knif",
        type2="",
    ),
    FLYING_KNIFE := _Weapon(
        value="7tk",
        type="tkni",
        type2="",
    ),
    FLYING_AXE := _Weapon(
        value="7ta",
        type="taxe",
        type2="",
    ),
    WINGED_KNIFE := _Weapon(
        value="7bk",
        type="tkni",
        type2="",
    ),
    WINGED_AXE := _Weapon(
        value="7b8",
        type="taxe",
        type2="",
    ),
    HYPERION_JAVELIN := _Weapon(
        value="7ja",
        type="jave",
        type2="",
    ),
    STYGIAN_PILUM := _Weapon(
        value="7pi",
        type="jave",
        type2="",
    ),
    BALROG_SPEAR := _Weapon(
        value="7s7",
        type="jave",
        type2="",
    ),
    GHOST_GLAIVE := _Weapon(
        value="7gl",
        type="jave",
        type2="",
    ),
    WINGED_HARPOON := _Weapon(
        value="7ts",
        type="jave",
        type2="",
    ),
    HYPERION_SPEAR := _Weapon(
        value="7sr",
        type="spea",
        type2="2han",
    ),
    STYGIAN_PIKE := _Weapon(
        value="7tr",
        type="spea",
        type2="2han",
    ),
    MANCATCHER := _Weapon(
        value="7br",
        type="spea",
        type2="2han",
    ),
    GHOST_SPEAR := _Weapon(
        value="7st",
        type="spea",
        type2="2han",
    ),
    WAR_PIKE := _Weapon(
        value="7p7",
        type="spea",
        type2="2han",
    ),
    OGRE_AXE := _Weapon(
        value="7o7",
        type="pole",
        type2="2han",
    ),
    COLOSSUS_VOULGE := _Weapon(
        value="7vo",
        type="pole",
        type2="2han",
    ),
    THRESHER := _Weapon(
        value="7s8",
        type="sc9",
        type2="2han",
    ),
    CRYPTIC_AXE := _Weapon(
        value="7pa",
        type="pole",
        type2="2han",
    ),
    GREAT_POLEAXE := _Weapon(
        value="7h7",
        type="pole",
        type2="2han",
    ),
    GIANT_THRESHER := _Weapon(
        value="7wc",
        type="sc9",
        type2="2han",
    ),
    WALKING_STICK := _Weapon(
        value="6ss",
        type="staf",
        type2="2han",
    ),
    STALAGMITE := _Weapon(
        value="6ls",
        type="staf",
        type2="2han",
    ),
    ELDER_STAFF := _Weapon(
        value="6cs",
        type="staf",
        type2="2han",
    ),
    SHILLELAGH := _Weapon(
        value="6bs",
        type="staf",
        type2="2han",
    ),
    ARCHON_STAFF := _Weapon(
        value="6ws",
        type="staf",
        type2="2han",
    ),
    SPIDER_BOW := _Weapon(
        value="6sb",
        type="bow",
        type2="",
    ),
    BLADE_BOW := _Weapon(
        value="6hb",
        type="bow",
        type2="",
    ),
    SHADOW_BOW := _Weapon(
        value="6lb",
        type="bow",
        type2="",
    ),
    GREAT_BOW := _Weapon(
        value="6cb",
        type="bow",
        type2="",
    ),
    DIAMOND_BOW := _Weapon(
        value="6s7",
        type="bow",
        type2="",
    ),
    CRUSADER_BOW := _Weapon(
        value="6l7",
        type="bow",
        type2="",
    ),
    WARD_BOW := _Weapon(
        value="6sw",
        type="bow",
        type2="",
    ),
    HYDRA_BOW := _Weapon(
        value="6lw",
        type="bow",
        type2="",
    ),
    PELLET_BOW := _Weapon(
        value="6lx",
        type="xbow",
        type2="",
    ),
    GORGON_CROSSBOW := _Weapon(
        value="6mx",
        type="xbow",
        type2="",
    ),
    COLOSSUS_CROSSBOW := _Weapon(
        value="6hx",
        type="xbow",
        type2="",
    ),
    DEMON_CROSSBOW := _Weapon(
        value="6rx",
        type="xbow",
        type2="",
    ),
    EAGLE_ORB := _Weapon(
        value="ob1",
        type="orb",
        type2="",
    ),
    SACRED_GLOBE := _Weapon(
        value="ob2",
        type="orb",
        type2="",
    ),
    SMOKED_SPHERE := _Weapon(
        value="ob3",
        type="orb",
        type2="",
    ),
    CLASPED_ORB := _Weapon(
        value="ob4",
        type="orb",
        type2="",
    ),
    JAREDS_STONE := _Weapon(
        value="ob5",
        type="orb",
        type2="",
    ),
    STAG_BOW := _Weapon(
        value="am1",
        type="abow",
        type2="",
    ),
    REFLEX_BOW := _Weapon(
        value="am2",
        type="abow",
        type2="",
    ),
    MAIDEN_SPEAR := _Weapon(
        value="am3",
        type="aspe",
        type2="2han",
    ),
    MAIDEN_PIKE := _Weapon(
        value="am4",
        type="aspe",
        type2="2han",
    ),
    MAIDEN_JAVELIN := _Weapon(
        value="am5",
        type="ajav",
        type2="",
    ),
    GLOWING_ORB := _Weapon(
        value="ob6",
        type="orb",
        type2="",
    ),
    CRYSTALLINE_GLOBE := _Weapon(
        value="ob7",
        type="orb",
        type2="",
    ),
    CLOUDY_SPHERE := _Weapon(
        value="ob8",
        type="orb",
        type2="",
    ),
    SPARKLING_BALL := _Weapon(
        value="ob9",
        type="orb",
        type2="",
    ),
    SWIRLING_CRYSTAL := _Weapon(
        value="oba",
        type="orb",
        type2="",
    ),
    ASHWOOD_BOW := _Weapon(
        value="am6",
        type="abow",
        type2="",
    ),
    CEREMONIAL_BOW := _Weapon(
        value="am7",
        type="abow",
        type2="",
    ),
    CEREMONIAL_SPEAR := _Weapon(
        value="am8",
        type="aspe",
        type2="2han",
    ),
    CEREMONIAL_PIKE := _Weapon(
        value="am9",
        type="aspe",
        type2="2han",
    ),
    CEREMONIAL_JAVELIN := _Weapon(
        value="ama",
        type="ajav",
        type2="",
    ),
    HEAVENLY_STONE := _Weapon(
        value="obb",
        type="orb",
        type2="",
    ),
    ELDRITCH_ORB := _Weapon(
        value="obc",
        type="orb",
        type2="",
    ),
    DEMON_HEART := _Weapon(
        value="obd",
        type="orb",
        type2="",
    ),
    VORTEX_ORB := _Weapon(
        value="obe",
        type="orb",
        type2="",
    ),
    DIMENSIONAL_SHARD := _Weapon(
        value="obf",
        type="orb",
        type2="",
    ),
    MATRIARCHAL_BOW := _Weapon(
        value="amb",
        type="abow",
        type2="",
    ),
    GRAND_MATRON_BOW := _Weapon(
        value="amc",
        type="abow",
        type2="",
    ),
    MATRIARCHAL_SPEAR := _Weapon(
        value="amd",
        type="aspe",
        type2="2han",
    ),
    MATRIARCHAL_PIKE := _Weapon(
        value="ame",
        type="aspe",
        type2="2han",
    ),
    MATRIARCHAL_JAVELIN := _Weapon(
        value="amf",
        type="ajav",
        type2="",
    ),
    FULMINATING_POTION := _Weapon(
        value="tpfs",
        type="tpot",
        type2="",
    ),
    EXPLODING_POTION := _Weapon(
        value="tpfm",
        type="tpot",
        type2="",
    ),
    OIL_POTION := _Weapon(
        value="tpfl",
        type="tpot",
        type2="",
    ),
    STRANGLING_POTION := _Weapon(
        value="tpgs",
        type="tpot",
        type2="",
    ),
    CHOKING_POTION := _Weapon(
        value="tpgm",
        type="tpot",
        type2="",
    ),
    RANCID_POTION := _Weapon(
        value="tpgl",
        type="tpot",
        type2="",
    ),
    CHILLING_POTION := _Weapon(
        value="tpcs",
        type="tpot",
        type2="",
    ),
    FROST_POTION := _Weapon(
        value="tpcm",
        type="tpot",
        type2="",
    ),
    FREEZING_POTION := _Weapon(
        value="tpcl",
        type="tpot",
        type2="",
    ),
    CHARGED_POTION := _Weapon(
        value="tpls",
        type="tpot",
        type2="",
    ),
    STATIC_POTION := _Weapon(
        value="tplm",
        type="tpot",
        type2="",
    ),
    SHOCK_POTION := _Weapon(
        value="tpll",
        type="tpot",
        type2="",
    ),
]
