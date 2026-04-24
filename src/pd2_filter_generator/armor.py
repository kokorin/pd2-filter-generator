"""
Generated Armor enum from PD2 data.

DO NOT EDIT MANUALLY - regenerate with: hatch run ./scripts/generate.py generate
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from pd2_filter_generator.expression import BoolMixin, BoolRef


@dataclass(frozen=True)
class _Metadata:
    """Item type metadata."""

    code: str  # "code"
    reqstr: int  # "reqstr"
    levelreq: int  # "levelreq"


_METADATA: dict[str, _Metadata] = {
    "CAP": _Metadata(
        code="cap",
        reqstr=0,
        levelreq=0,
    ),
    "SKULL_CAP": _Metadata(
        code="skp",
        reqstr=15,
        levelreq=0,
    ),
    "HELM": _Metadata(
        code="hlm",
        reqstr=26,
        levelreq=0,
    ),
    "FULL_HELM": _Metadata(
        code="fhl",
        reqstr=41,
        levelreq=0,
    ),
    "GREAT_HELM": _Metadata(
        code="ghm",
        reqstr=63,
        levelreq=0,
    ),
    "CROWN": _Metadata(
        code="crn",
        reqstr=55,
        levelreq=0,
    ),
    "MASK": _Metadata(
        code="msk",
        reqstr=23,
        levelreq=0,
    ),
    "QUILTED_ARMOR": _Metadata(
        code="qui",
        reqstr=12,
        levelreq=0,
    ),
    "LEATHER_ARMOR": _Metadata(
        code="lea",
        reqstr=15,
        levelreq=0,
    ),
    "HARD_LEATHER_ARMOR": _Metadata(
        code="hla",
        reqstr=20,
        levelreq=0,
    ),
    "STUDDED_LEATHER": _Metadata(
        code="stu",
        reqstr=27,
        levelreq=0,
    ),
    "RING_MAIL": _Metadata(
        code="rng",
        reqstr=36,
        levelreq=0,
    ),
    "SCALE_MAIL": _Metadata(
        code="scl",
        reqstr=44,
        levelreq=0,
    ),
    "CHAIN_MAIL": _Metadata(
        code="chn",
        reqstr=48,
        levelreq=0,
    ),
    "BREAST_PLATE": _Metadata(
        code="brs",
        reqstr=30,
        levelreq=0,
    ),
    "SPLINT_MAIL": _Metadata(
        code="spl",
        reqstr=51,
        levelreq=0,
    ),
    "PLATE_MAIL": _Metadata(
        code="plt",
        reqstr=65,
        levelreq=0,
    ),
    "FIELD_PLATE": _Metadata(
        code="fld",
        reqstr=55,
        levelreq=0,
    ),
    "GOTHIC_PLATE": _Metadata(
        code="gth",
        reqstr=70,
        levelreq=0,
    ),
    "FULL_PLATE_MAIL": _Metadata(
        code="ful",
        reqstr=80,
        levelreq=0,
    ),
    "ANCIENT_ARMOR": _Metadata(
        code="aar",
        reqstr=100,
        levelreq=0,
    ),
    "LIGHT_PLATE": _Metadata(
        code="ltp",
        reqstr=41,
        levelreq=0,
    ),
    "BUCKLER": _Metadata(
        code="buc",
        reqstr=12,
        levelreq=0,
    ),
    "SMALL_SHIELD": _Metadata(
        code="sml",
        reqstr=22,
        levelreq=0,
    ),
    "LARGE_SHIELD": _Metadata(
        code="lrg",
        reqstr=34,
        levelreq=0,
    ),
    "KITE_SHIELD": _Metadata(
        code="kit",
        reqstr=47,
        levelreq=0,
    ),
    "TOWER_SHIELD": _Metadata(
        code="tow",
        reqstr=75,
        levelreq=0,
    ),
    "GOTHIC_SHIELD": _Metadata(
        code="gts",
        reqstr=60,
        levelreq=0,
    ),
    "LEATHER_GLOVES": _Metadata(
        code="lgl",
        reqstr=0,
        levelreq=0,
    ),
    "HEAVY_GLOVES": _Metadata(
        code="vgl",
        reqstr=0,
        levelreq=0,
    ),
    "CHAIN_GLOVES": _Metadata(
        code="mgl",
        reqstr=25,
        levelreq=0,
    ),
    "LIGHT_GAUNTLETS": _Metadata(
        code="tgl",
        reqstr=45,
        levelreq=0,
    ),
    "GAUNTLETS": _Metadata(
        code="hgl",
        reqstr=60,
        levelreq=0,
    ),
    "BOOTS": _Metadata(
        code="lbt",
        reqstr=0,
        levelreq=0,
    ),
    "HEAVY_BOOTS": _Metadata(
        code="vbt",
        reqstr=18,
        levelreq=0,
    ),
    "CHAIN_BOOTS": _Metadata(
        code="mbt",
        reqstr=30,
        levelreq=0,
    ),
    "LIGHT_PLATED_BOOTS": _Metadata(
        code="tbt",
        reqstr=50,
        levelreq=0,
    ),
    "GREAVES": _Metadata(
        code="hbt",
        reqstr=70,
        levelreq=0,
    ),
    "SASH": _Metadata(
        code="lbl",
        reqstr=0,
        levelreq=0,
    ),
    "LIGHT_BELT": _Metadata(
        code="vbl",
        reqstr=0,
        levelreq=0,
    ),
    "BELT": _Metadata(
        code="mbl",
        reqstr=25,
        levelreq=0,
    ),
    "HEAVY_BELT": _Metadata(
        code="tbl",
        reqstr=45,
        levelreq=0,
    ),
    "PLATED_BELT": _Metadata(
        code="hbl",
        reqstr=60,
        levelreq=0,
    ),
    "BONE_HELM": _Metadata(
        code="bhm",
        reqstr=25,
        levelreq=0,
    ),
    "BONE_SHIELD": _Metadata(
        code="bsh",
        reqstr=25,
        levelreq=0,
    ),
    "SPIKED_SHIELD": _Metadata(
        code="spk",
        reqstr=30,
        levelreq=0,
    ),
    "WAR_HAT": _Metadata(
        code="xap",
        reqstr=20,
        levelreq=22,
    ),
    "SALLET": _Metadata(
        code="xkp",
        reqstr=43,
        levelreq=25,
    ),
    "CASQUE": _Metadata(
        code="xlm",
        reqstr=59,
        levelreq=25,
    ),
    "BASINET": _Metadata(
        code="xhl",
        reqstr=82,
        levelreq=25,
    ),
    "WINGED_HELM": _Metadata(
        code="xhm",
        reqstr=115,
        levelreq=25,
    ),
    "GRAND_CROWN": _Metadata(
        code="xrn",
        reqstr=103,
        levelreq=25,
    ),
    "DEATH_MASK": _Metadata(
        code="xsk",
        reqstr=55,
        levelreq=25,
    ),
    "GHOST_ARMOR": _Metadata(
        code="xui",
        reqstr=38,
        levelreq=22,
    ),
    "SERPENTSKIN_ARMOR": _Metadata(
        code="xea",
        reqstr=43,
        levelreq=24,
    ),
    "DEMONHIDE_ARMOR": _Metadata(
        code="xla",
        reqstr=50,
        levelreq=25,
    ),
    "TRELLISED_ARMOR": _Metadata(
        code="xtu",
        reqstr=61,
        levelreq=25,
    ),
    "LINKED_MAIL": _Metadata(
        code="xng",
        reqstr=74,
        levelreq=25,
    ),
    "TIGULATED_MAIL": _Metadata(
        code="xcl",
        reqstr=86,
        levelreq=25,
    ),
    "MESH_ARMOR": _Metadata(
        code="xhn",
        reqstr=92,
        levelreq=25,
    ),
    "CUIRASS": _Metadata(
        code="xrs",
        reqstr=65,
        levelreq=25,
    ),
    "RUSSET_ARMOR": _Metadata(
        code="xpl",
        reqstr=97,
        levelreq=25,
    ),
    "TEMPLAR_COAT": _Metadata(
        code="xlt",
        reqstr=118,
        levelreq=25,
    ),
    "SHARKTOOTH_ARMOR": _Metadata(
        code="xld",
        reqstr=103,
        levelreq=25,
    ),
    "EMBOSSED_PLATE": _Metadata(
        code="xth",
        reqstr=125,
        levelreq=25,
    ),
    "CHAOS_ARMOR": _Metadata(
        code="xul",
        reqstr=140,
        levelreq=25,
    ),
    "ORNATE_PLATE": _Metadata(
        code="xar",
        reqstr=170,
        levelreq=25,
    ),
    "MAGE_PLATE": _Metadata(
        code="xtp",
        reqstr=55,
        levelreq=25,
    ),
    "DEFENDER": _Metadata(
        code="xuc",
        reqstr=38,
        levelreq=22,
    ),
    "ROUND_SHIELD": _Metadata(
        code="xml",
        reqstr=53,
        levelreq=25,
    ),
    "SCUTUM": _Metadata(
        code="xrg",
        reqstr=71,
        levelreq=25,
    ),
    "DRAGON_SHIELD": _Metadata(
        code="xit",
        reqstr=91,
        levelreq=25,
    ),
    "PAVISE": _Metadata(
        code="xow",
        reqstr=133,
        levelreq=25,
    ),
    "ANCIENT_SHIELD": _Metadata(
        code="xts",
        reqstr=110,
        levelreq=25,
    ),
    "DEMONHIDE_GLOVES": _Metadata(
        code="xlg",
        reqstr=20,
        levelreq=21,
    ),
    "SHARKSKIN_GLOVES": _Metadata(
        code="xvg",
        reqstr=20,
        levelreq=25,
    ),
    "HEAVY_BRACERS": _Metadata(
        code="xmg",
        reqstr=58,
        levelreq=25,
    ),
    "BATTLE_GAUNTLETS": _Metadata(
        code="xtg",
        reqstr=88,
        levelreq=25,
    ),
    "WAR_GAUNTLETS": _Metadata(
        code="xhg",
        reqstr=110,
        levelreq=25,
    ),
    "DEMONHIDE_BOOTS": _Metadata(
        code="xlb",
        reqstr=20,
        levelreq=24,
    ),
    "SHARKSKIN_BOOTS": _Metadata(
        code="xvb",
        reqstr=47,
        levelreq=25,
    ),
    "MESH_BOOTS": _Metadata(
        code="xmb",
        reqstr=65,
        levelreq=25,
    ),
    "BATTLE_BOOTS": _Metadata(
        code="xtb",
        reqstr=95,
        levelreq=25,
    ),
    "WAR_BOOTS": _Metadata(
        code="xhb",
        reqstr=125,
        levelreq=25,
    ),
    "DEMONHIDE_SASH": _Metadata(
        code="zlb",
        reqstr=20,
        levelreq=24,
    ),
    "SHARKSKIN_BELT": _Metadata(
        code="zvb",
        reqstr=20,
        levelreq=25,
    ),
    "MESH_BELT": _Metadata(
        code="zmb",
        reqstr=58,
        levelreq=25,
    ),
    "BATTLE_BELT": _Metadata(
        code="ztb",
        reqstr=88,
        levelreq=25,
    ),
    "WAR_BELT": _Metadata(
        code="zhb",
        reqstr=110,
        levelreq=25,
    ),
    "GRIM_HELM": _Metadata(
        code="xh9",
        reqstr=58,
        levelreq=25,
    ),
    "GRIM_SHIELD": _Metadata(
        code="xsh",
        reqstr=58,
        levelreq=25,
    ),
    "BARBED_SHIELD": _Metadata(
        code="xpk",
        reqstr=65,
        levelreq=25,
    ),
    "WOLF_HEAD": _Metadata(
        code="dr1",
        reqstr=16,
        levelreq=3,
    ),
    "HAWK_HELM": _Metadata(
        code="dr2",
        reqstr=20,
        levelreq=6,
    ),
    "ANTLERS": _Metadata(
        code="dr3",
        reqstr=24,
        levelreq=12,
    ),
    "FALCON_MASK": _Metadata(
        code="dr4",
        reqstr=28,
        levelreq=15,
    ),
    "SPIRIT_MASK": _Metadata(
        code="dr5",
        reqstr=30,
        levelreq=18,
    ),
    "JAWBONE_CAP": _Metadata(
        code="ba1",
        reqstr=25,
        levelreq=3,
    ),
    "FANGED_HELM": _Metadata(
        code="ba2",
        reqstr=35,
        levelreq=6,
    ),
    "HORNED_HELM": _Metadata(
        code="ba3",
        reqstr=45,
        levelreq=12,
    ),
    "ASSAULT_HELMET": _Metadata(
        code="ba4",
        reqstr=55,
        levelreq=15,
    ),
    "AVENGER_GUARD": _Metadata(
        code="ba5",
        reqstr=65,
        levelreq=18,
    ),
    "TARGE": _Metadata(
        code="pa1",
        reqstr=16,
        levelreq=3,
    ),
    "RONDACHE": _Metadata(
        code="pa2",
        reqstr=26,
        levelreq=6,
    ),
    "HERALDIC_SHIELD": _Metadata(
        code="pa3",
        reqstr=40,
        levelreq=12,
    ),
    "AERIN_SHIELD": _Metadata(
        code="pa4",
        reqstr=50,
        levelreq=15,
    ),
    "CROWN_SHIELD": _Metadata(
        code="pa5",
        reqstr=65,
        levelreq=18,
    ),
    "PRESERVED_HEAD": _Metadata(
        code="ne1",
        reqstr=12,
        levelreq=3,
    ),
    "ZOMBIE_HEAD": _Metadata(
        code="ne2",
        reqstr=14,
        levelreq=6,
    ),
    "UNRAVELLER_HEAD": _Metadata(
        code="ne3",
        reqstr=18,
        levelreq=12,
    ),
    "GARGOYLE_HEAD": _Metadata(
        code="ne4",
        reqstr=20,
        levelreq=15,
    ),
    "DEMON_HEAD": _Metadata(
        code="ne5",
        reqstr=25,
        levelreq=18,
    ),
    "CIRCLET": _Metadata(
        code="ci0",
        reqstr=0,
        levelreq=16,
    ),
    "CORONET": _Metadata(
        code="ci1",
        reqstr=0,
        levelreq=39,
    ),
    "TIARA": _Metadata(
        code="ci2",
        reqstr=0,
        levelreq=52,
    ),
    "DIADEM": _Metadata(
        code="ci3",
        reqstr=0,
        levelreq=64,
    ),
    "SHAKO": _Metadata(
        code="uap",
        reqstr=50,
        levelreq=43,
    ),
    "HYDRASKULL": _Metadata(
        code="ukp",
        reqstr=84,
        levelreq=47,
    ),
    "ARMET": _Metadata(
        code="ulm",
        reqstr=109,
        levelreq=51,
    ),
    "GIANT_CONCH": _Metadata(
        code="uhl",
        reqstr=142,
        levelreq=40,
    ),
    "SPIRED_HELM": _Metadata(
        code="uhm",
        reqstr=192,
        levelreq=59,
    ),
    "CORONA": _Metadata(
        code="urn",
        reqstr=174,
        levelreq=66,
    ),
    "DEMONHEAD": _Metadata(
        code="usk",
        reqstr=102,
        levelreq=55,
    ),
    "DUSK_SHROUD": _Metadata(
        code="uui",
        reqstr=77,
        levelreq=49,
    ),
    "WYRMHIDE": _Metadata(
        code="uea",
        reqstr=84,
        levelreq=50,
    ),
    "SCARAB_HUSK": _Metadata(
        code="ula",
        reqstr=95,
        levelreq=51,
    ),
    "WIRE_FLEECE": _Metadata(
        code="utu",
        reqstr=111,
        levelreq=53,
    ),
    "DIAMOND_MAIL": _Metadata(
        code="ung",
        reqstr=131,
        levelreq=54,
    ),
    "LORICATED_MAIL": _Metadata(
        code="ucl",
        reqstr=149,
        levelreq=55,
    ),
    "BONEWEAVE": _Metadata(
        code="uhn",
        reqstr=158,
        levelreq=47,
    ),
    "GREAT_HAUBERK": _Metadata(
        code="urs",
        reqstr=118,
        levelreq=56,
    ),
    "BALROG_SKIN": _Metadata(
        code="upl",
        reqstr=165,
        levelreq=57,
    ),
    "HELLFORGE_PLATE": _Metadata(
        code="ult",
        reqstr=196,
        levelreq=59,
    ),
    "KRAKEN_SHELL": _Metadata(
        code="uld",
        reqstr=174,
        levelreq=61,
    ),
    "LACQUERED_PLATE": _Metadata(
        code="uth",
        reqstr=208,
        levelreq=62,
    ),
    "SHADOW_PLATE": _Metadata(
        code="uul",
        reqstr=220,
        levelreq=64,
    ),
    "SACRED_ARMOR": _Metadata(
        code="uar",
        reqstr=232,
        levelreq=66,
    ),
    "ARCHON_PLATE": _Metadata(
        code="utp",
        reqstr=103,
        levelreq=63,
    ),
    "HEATER": _Metadata(
        code="uuc",
        reqstr=77,
        levelreq=43,
    ),
    "LUNA": _Metadata(
        code="uml",
        reqstr=100,
        levelreq=45,
    ),
    "HYPERION": _Metadata(
        code="urg",
        reqstr=127,
        levelreq=48,
    ),
    "MONARCH": _Metadata(
        code="uit",
        reqstr=156,
        levelreq=54,
    ),
    "AEGIS": _Metadata(
        code="uow",
        reqstr=219,
        levelreq=59,
    ),
    "WARD": _Metadata(
        code="uts",
        reqstr=185,
        levelreq=63,
    ),
    "BRAMBLE_MITTS": _Metadata(
        code="ulg",
        reqstr=50,
        levelreq=42,
    ),
    "VAMPIREBONE_GLOVES": _Metadata(
        code="uvg",
        reqstr=50,
        levelreq=47,
    ),
    "VAMBRACES": _Metadata(
        code="umg",
        reqstr=106,
        levelreq=51,
    ),
    "CRUSADER_GAUNTLETS": _Metadata(
        code="utg",
        reqstr=151,
        levelreq=57,
    ),
    "OGRE_GAUNTLETS": _Metadata(
        code="uhg",
        reqstr=185,
        levelreq=64,
    ),
    "WYRMHIDE_BOOTS": _Metadata(
        code="ulb",
        reqstr=50,
        levelreq=45,
    ),
    "SCARABSHELL_BOOTS": _Metadata(
        code="uvb",
        reqstr=91,
        levelreq=49,
    ),
    "BONEWEAVE_BOOTS": _Metadata(
        code="umb",
        reqstr=118,
        levelreq=54,
    ),
    "MIRRORED_BOOTS": _Metadata(
        code="utb",
        reqstr=163,
        levelreq=60,
    ),
    "MYRMIDON_GREAVES": _Metadata(
        code="uhb",
        reqstr=208,
        levelreq=65,
    ),
    "SPIDERWEB_SASH": _Metadata(
        code="ulc",
        reqstr=50,
        levelreq=46,
    ),
    "VAMPIREFANG_BELT": _Metadata(
        code="uvc",
        reqstr=50,
        levelreq=51,
    ),
    "MITHRIL_COIL": _Metadata(
        code="umc",
        reqstr=106,
        levelreq=56,
    ),
    "TROLL_BELT": _Metadata(
        code="utc",
        reqstr=151,
        levelreq=62,
    ),
    "COLOSSUS_GIRDLE": _Metadata(
        code="uhc",
        reqstr=185,
        levelreq=67,
    ),
    "BONE_VISAGE": _Metadata(
        code="uh9",
        reqstr=106,
        levelreq=63,
    ),
    "TROLL_NEST": _Metadata(
        code="ush",
        reqstr=106,
        levelreq=57,
    ),
    "BLADE_BARRIER": _Metadata(
        code="upk",
        reqstr=118,
        levelreq=51,
    ),
    "ALPHA_HELM": _Metadata(
        code="dr6",
        reqstr=44,
        levelreq=26,
    ),
    "GRIFFON_HEADDRESS": _Metadata(
        code="dr7",
        reqstr=50,
        levelreq=30,
    ),
    "HUNTERS_GUISE": _Metadata(
        code="dr8",
        reqstr=56,
        levelreq=29,
    ),
    "SACRED_FEATHERS": _Metadata(
        code="dr9",
        reqstr=62,
        levelreq=32,
    ),
    "TOTEMIC_MASK": _Metadata(
        code="dra",
        reqstr=65,
        levelreq=41,
    ),
    "JAWBONE_VISOR": _Metadata(
        code="ba6",
        reqstr=58,
        levelreq=25,
    ),
    "LION_HELM": _Metadata(
        code="ba7",
        reqstr=73,
        levelreq=29,
    ),
    "RAGE_MASK": _Metadata(
        code="ba8",
        reqstr=88,
        levelreq=29,
    ),
    "SAVAGE_HELMET": _Metadata(
        code="ba9",
        reqstr=103,
        levelreq=32,
    ),
    "SLAYER_GUARD": _Metadata(
        code="baa",
        reqstr=118,
        levelreq=40,
    ),
    "AKARAN_TARGE": _Metadata(
        code="pa6",
        reqstr=44,
        levelreq=26,
    ),
    "AKARAN_RONDACHE": _Metadata(
        code="pa7",
        reqstr=59,
        levelreq=30,
    ),
    "PROTECTOR_SHIELD": _Metadata(
        code="pa8",
        reqstr=69,
        levelreq=34,
    ),
    "GILDED_SHIELD": _Metadata(
        code="pa9",
        reqstr=89,
        levelreq=38,
    ),
    "ROYAL_SHIELD": _Metadata(
        code="paa",
        reqstr=114,
        levelreq=41,
    ),
    "MUMMIFIED_TROPHY": _Metadata(
        code="ne6",
        reqstr=38,
        levelreq=24,
    ),
    "FETISH_TROPHY": _Metadata(
        code="ne7",
        reqstr=41,
        levelreq=29,
    ),
    "SEXTON_TROPHY": _Metadata(
        code="ne8",
        reqstr=47,
        levelreq=33,
    ),
    "CANTOR_TROPHY": _Metadata(
        code="ne9",
        reqstr=50,
        levelreq=36,
    ),
    "HIEROPHANT_TROPHY": _Metadata(
        code="nea",
        reqstr=58,
        levelreq=40,
    ),
    "BLOOD_SPIRIT": _Metadata(
        code="drb",
        reqstr=86,
        levelreq=46,
    ),
    "SUN_SPIRIT": _Metadata(
        code="drc",
        reqstr=95,
        levelreq=51,
    ),
    "EARTH_SPIRIT": _Metadata(
        code="drd",
        reqstr=104,
        levelreq=57,
    ),
    "SKY_SPIRIT": _Metadata(
        code="dre",
        reqstr=113,
        levelreq=62,
    ),
    "DREAM_SPIRIT": _Metadata(
        code="drf",
        reqstr=118,
        levelreq=66,
    ),
    "CARNAGE_HELM": _Metadata(
        code="bab",
        reqstr=106,
        levelreq=45,
    ),
    "FURY_VISOR": _Metadata(
        code="bac",
        reqstr=129,
        levelreq=49,
    ),
    "DESTROYER_HELM": _Metadata(
        code="bad",
        reqstr=151,
        levelreq=54,
    ),
    "CONQUEROR_CROWN": _Metadata(
        code="bae",
        reqstr=174,
        levelreq=60,
    ),
    "GUARDIAN_CROWN": _Metadata(
        code="baf",
        reqstr=196,
        levelreq=65,
    ),
    "SACRED_TARGE": _Metadata(
        code="pab",
        reqstr=86,
        levelreq=47,
    ),
    "SACRED_RONDACHE": _Metadata(
        code="pac",
        reqstr=109,
        levelreq=52,
    ),
    "KURAST_SHIELD": _Metadata(
        code="pad",
        reqstr=124,
        levelreq=55,
    ),
    "ZAKARUM_SHIELD": _Metadata(
        code="pae",
        reqstr=142,
        levelreq=61,
    ),
    "VORTEX_SHIELD": _Metadata(
        code="paf",
        reqstr=148,
        levelreq=66,
    ),
    "MINION_SKULL": _Metadata(
        code="neb",
        reqstr=77,
        levelreq=44,
    ),
    "HELLSPAWN_SKULL": _Metadata(
        code="neg",
        reqstr=82,
        levelreq=50,
    ),
    "OVERSEER_SKULL": _Metadata(
        code="ned",
        reqstr=91,
        levelreq=49,
    ),
    "SUCCUBUS_SKULL": _Metadata(
        code="nee",
        reqstr=95,
        levelreq=60,
    ),
    "BLOODLORD_SKULL": _Metadata(
        code="nef",
        reqstr=106,
        levelreq=65,
    ),
    "BONEWEAVE_RAR": _Metadata(
        code="rar",
        reqstr=158,
        levelreq=47,
    ),
    "TROLL_BELT_RBE": _Metadata(
        code="rbe",
        reqstr=151,
        levelreq=62,
    ),
}


class Armor(BoolMixin, Enum):
    """PD2 armor categories."""

    CAP = "cap"  # Cap
    SKULL_CAP = "skp"  # Skull Cap
    HELM = "hlm"  # Helm
    FULL_HELM = "fhl"  # Full Helm
    GREAT_HELM = "ghm"  # Great Helm
    CROWN = "crn"  # Crown
    MASK = "msk"  # Mask
    QUILTED_ARMOR = "qui"  # Quilted Armor
    LEATHER_ARMOR = "lea"  # Leather Armor
    HARD_LEATHER_ARMOR = "hla"  # Hard Leather Armor
    STUDDED_LEATHER = "stu"  # Studded Leather
    RING_MAIL = "rng"  # Ring Mail
    SCALE_MAIL = "scl"  # Scale Mail
    CHAIN_MAIL = "chn"  # Chain Mail
    BREAST_PLATE = "brs"  # Breast Plate
    SPLINT_MAIL = "spl"  # Splint Mail
    PLATE_MAIL = "plt"  # Plate Mail
    FIELD_PLATE = "fld"  # Field Plate
    GOTHIC_PLATE = "gth"  # Gothic Plate
    FULL_PLATE_MAIL = "ful"  # Full Plate Mail
    ANCIENT_ARMOR = "aar"  # Ancient Armor
    LIGHT_PLATE = "ltp"  # Light Plate
    BUCKLER = "buc"  # Buckler
    SMALL_SHIELD = "sml"  # Small Shield
    LARGE_SHIELD = "lrg"  # Large Shield
    KITE_SHIELD = "kit"  # Kite Shield
    TOWER_SHIELD = "tow"  # Tower Shield
    GOTHIC_SHIELD = "gts"  # Gothic Shield
    LEATHER_GLOVES = "lgl"  # Leather Gloves
    HEAVY_GLOVES = "vgl"  # Heavy Gloves
    CHAIN_GLOVES = "mgl"  # Chain Gloves
    LIGHT_GAUNTLETS = "tgl"  # Light Gauntlets
    GAUNTLETS = "hgl"  # Gauntlets
    BOOTS = "lbt"  # Boots
    HEAVY_BOOTS = "vbt"  # Heavy Boots
    CHAIN_BOOTS = "mbt"  # Chain Boots
    LIGHT_PLATED_BOOTS = "tbt"  # Light Plated Boots
    GREAVES = "hbt"  # Greaves
    SASH = "lbl"  # Sash
    LIGHT_BELT = "vbl"  # Light Belt
    BELT = "mbl"  # Belt
    HEAVY_BELT = "tbl"  # Heavy Belt
    PLATED_BELT = "hbl"  # Plated Belt
    BONE_HELM = "bhm"  # Bone Helm
    BONE_SHIELD = "bsh"  # Bone Shield
    SPIKED_SHIELD = "spk"  # Spiked Shield
    WAR_HAT = "xap"  # War Hat
    SALLET = "xkp"  # Sallet
    CASQUE = "xlm"  # Casque
    BASINET = "xhl"  # Basinet
    WINGED_HELM = "xhm"  # Winged Helm
    GRAND_CROWN = "xrn"  # Grand Crown
    DEATH_MASK = "xsk"  # Death Mask
    GHOST_ARMOR = "xui"  # Ghost Armor
    SERPENTSKIN_ARMOR = "xea"  # Serpentskin Armor
    DEMONHIDE_ARMOR = "xla"  # Demonhide Armor
    TRELLISED_ARMOR = "xtu"  # Trellised Armor
    LINKED_MAIL = "xng"  # Linked Mail
    TIGULATED_MAIL = "xcl"  # Tigulated Mail
    MESH_ARMOR = "xhn"  # Mesh Armor
    CUIRASS = "xrs"  # Cuirass
    RUSSET_ARMOR = "xpl"  # Russet Armor
    TEMPLAR_COAT = "xlt"  # Templar Coat
    SHARKTOOTH_ARMOR = "xld"  # Sharktooth Armor
    EMBOSSED_PLATE = "xth"  # Embossed Plate
    CHAOS_ARMOR = "xul"  # Chaos Armor
    ORNATE_PLATE = "xar"  # Ornate Plate
    MAGE_PLATE = "xtp"  # Mage Plate
    DEFENDER = "xuc"  # Defender
    ROUND_SHIELD = "xml"  # Round Shield
    SCUTUM = "xrg"  # Scutum
    DRAGON_SHIELD = "xit"  # Dragon Shield
    PAVISE = "xow"  # Pavise
    ANCIENT_SHIELD = "xts"  # Ancient Shield
    DEMONHIDE_GLOVES = "xlg"  # Demonhide Gloves
    SHARKSKIN_GLOVES = "xvg"  # Sharkskin Gloves
    HEAVY_BRACERS = "xmg"  # Heavy Bracers
    BATTLE_GAUNTLETS = "xtg"  # Battle Gauntlets
    WAR_GAUNTLETS = "xhg"  # War Gauntlets
    DEMONHIDE_BOOTS = "xlb"  # Demonhide Boots
    SHARKSKIN_BOOTS = "xvb"  # Sharkskin Boots
    MESH_BOOTS = "xmb"  # Mesh Boots
    BATTLE_BOOTS = "xtb"  # Battle Boots
    WAR_BOOTS = "xhb"  # War Boots
    DEMONHIDE_SASH = "zlb"  # Demonhide Sash
    SHARKSKIN_BELT = "zvb"  # Sharkskin Belt
    MESH_BELT = "zmb"  # Mesh Belt
    BATTLE_BELT = "ztb"  # Battle Belt
    WAR_BELT = "zhb"  # War Belt
    GRIM_HELM = "xh9"  # Grim Helm
    GRIM_SHIELD = "xsh"  # Grim Shield
    BARBED_SHIELD = "xpk"  # Barbed Shield
    WOLF_HEAD = "dr1"  # Wolf Head
    HAWK_HELM = "dr2"  # Hawk Helm
    ANTLERS = "dr3"  # Antlers
    FALCON_MASK = "dr4"  # Falcon Mask
    SPIRIT_MASK = "dr5"  # Spirit Mask
    JAWBONE_CAP = "ba1"  # Jawbone Cap
    FANGED_HELM = "ba2"  # Fanged Helm
    HORNED_HELM = "ba3"  # Horned Helm
    ASSAULT_HELMET = "ba4"  # Assault Helmet
    AVENGER_GUARD = "ba5"  # Avenger Guard
    TARGE = "pa1"  # Targe
    RONDACHE = "pa2"  # Rondache
    HERALDIC_SHIELD = "pa3"  # Heraldic Shield
    AERIN_SHIELD = "pa4"  # Aerin Shield
    CROWN_SHIELD = "pa5"  # Crown Shield
    PRESERVED_HEAD = "ne1"  # Preserved Head
    ZOMBIE_HEAD = "ne2"  # Zombie Head
    UNRAVELLER_HEAD = "ne3"  # Unraveller Head
    GARGOYLE_HEAD = "ne4"  # Gargoyle Head
    DEMON_HEAD = "ne5"  # Demon Head
    CIRCLET = "ci0"  # Circlet
    CORONET = "ci1"  # Coronet
    TIARA = "ci2"  # Tiara
    DIADEM = "ci3"  # Diadem
    SHAKO = "uap"  # Shako
    HYDRASKULL = "ukp"  # Hydraskull
    ARMET = "ulm"  # Armet
    GIANT_CONCH = "uhl"  # Giant Conch
    SPIRED_HELM = "uhm"  # Spired Helm
    CORONA = "urn"  # Corona
    DEMONHEAD = "usk"  # Demonhead
    DUSK_SHROUD = "uui"  # Dusk Shroud
    WYRMHIDE = "uea"  # Wyrmhide
    SCARAB_HUSK = "ula"  # Scarab Husk
    WIRE_FLEECE = "utu"  # Wire Fleece
    DIAMOND_MAIL = "ung"  # Diamond Mail
    LORICATED_MAIL = "ucl"  # Loricated Mail
    BONEWEAVE = "uhn"  # Boneweave
    GREAT_HAUBERK = "urs"  # Great Hauberk
    BALROG_SKIN = "upl"  # Balrog Skin
    HELLFORGE_PLATE = "ult"  # Hellforge Plate
    KRAKEN_SHELL = "uld"  # Kraken Shell
    LACQUERED_PLATE = "uth"  # Lacquered Plate
    SHADOW_PLATE = "uul"  # Shadow Plate
    SACRED_ARMOR = "uar"  # Sacred Armor
    ARCHON_PLATE = "utp"  # Archon Plate
    HEATER = "uuc"  # Heater
    LUNA = "uml"  # Luna
    HYPERION = "urg"  # Hyperion
    MONARCH = "uit"  # Monarch
    AEGIS = "uow"  # Aegis
    WARD = "uts"  # Ward
    BRAMBLE_MITTS = "ulg"  # Bramble Mitts
    VAMPIREBONE_GLOVES = "uvg"  # Vampirebone Gloves
    VAMBRACES = "umg"  # Vambraces
    CRUSADER_GAUNTLETS = "utg"  # Crusader Gauntlets
    OGRE_GAUNTLETS = "uhg"  # Ogre Gauntlets
    WYRMHIDE_BOOTS = "ulb"  # Wyrmhide Boots
    SCARABSHELL_BOOTS = "uvb"  # Scarabshell Boots
    BONEWEAVE_BOOTS = "umb"  # Boneweave Boots
    MIRRORED_BOOTS = "utb"  # Mirrored Boots
    MYRMIDON_GREAVES = "uhb"  # Myrmidon Greaves
    SPIDERWEB_SASH = "ulc"  # Spiderweb Sash
    VAMPIREFANG_BELT = "uvc"  # Vampirefang Belt
    MITHRIL_COIL = "umc"  # Mithril Coil
    TROLL_BELT = "utc"  # Troll Belt
    COLOSSUS_GIRDLE = "uhc"  # Colossus Girdle
    BONE_VISAGE = "uh9"  # Bone Visage
    TROLL_NEST = "ush"  # Troll Nest
    BLADE_BARRIER = "upk"  # Blade Barrier
    ALPHA_HELM = "dr6"  # Alpha Helm
    GRIFFON_HEADDRESS = "dr7"  # Griffon Headdress
    HUNTERS_GUISE = "dr8"  # Hunter's Guise
    SACRED_FEATHERS = "dr9"  # Sacred Feathers
    TOTEMIC_MASK = "dra"  # Totemic Mask
    JAWBONE_VISOR = "ba6"  # Jawbone Visor
    LION_HELM = "ba7"  # Lion Helm
    RAGE_MASK = "ba8"  # Rage Mask
    SAVAGE_HELMET = "ba9"  # Savage Helmet
    SLAYER_GUARD = "baa"  # Slayer Guard
    AKARAN_TARGE = "pa6"  # Akaran Targe
    AKARAN_RONDACHE = "pa7"  # Akaran Rondache
    PROTECTOR_SHIELD = "pa8"  # Protector Shield
    GILDED_SHIELD = "pa9"  # Gilded Shield
    ROYAL_SHIELD = "paa"  # Royal Shield
    MUMMIFIED_TROPHY = "ne6"  # Mummified Trophy
    FETISH_TROPHY = "ne7"  # Fetish Trophy
    SEXTON_TROPHY = "ne8"  # Sexton Trophy
    CANTOR_TROPHY = "ne9"  # Cantor Trophy
    HIEROPHANT_TROPHY = "nea"  # Hierophant Trophy
    BLOOD_SPIRIT = "drb"  # Blood Spirit
    SUN_SPIRIT = "drc"  # Sun Spirit
    EARTH_SPIRIT = "drd"  # Earth Spirit
    SKY_SPIRIT = "dre"  # Sky Spirit
    DREAM_SPIRIT = "drf"  # Dream Spirit
    CARNAGE_HELM = "bab"  # Carnage Helm
    FURY_VISOR = "bac"  # Fury Visor
    DESTROYER_HELM = "bad"  # Destroyer Helm
    CONQUEROR_CROWN = "bae"  # Conqueror Crown
    GUARDIAN_CROWN = "baf"  # Guardian Crown
    SACRED_TARGE = "pab"  # Sacred Targe
    SACRED_RONDACHE = "pac"  # Sacred Rondache
    KURAST_SHIELD = "pad"  # Kurast Shield
    ZAKARUM_SHIELD = "pae"  # Zakarum Shield
    VORTEX_SHIELD = "paf"  # Vortex Shield
    MINION_SKULL = "neb"  # Minion Skull
    HELLSPAWN_SKULL = "neg"  # Hellspawn Skull
    OVERSEER_SKULL = "ned"  # Overseer Skull
    SUCCUBUS_SKULL = "nee"  # Succubus Skull
    BLOODLORD_SKULL = "nef"  # Bloodlord Skull
    BONEWEAVE_RAR = "rar"  # Boneweave rar
    TROLL_BELT_RBE = "rbe"  # Troll Belt rbe

    def as_node(self) -> BoolRef:
        return BoolRef(self.value)

    @property
    def code(self) -> str:
        return _METADATA[self.name].code

    @property
    def reqstr(self) -> int:
        return _METADATA[self.name].reqstr

    @property
    def levelreq(self) -> int:
        return _METADATA[self.name].levelreq
