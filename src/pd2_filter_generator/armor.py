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

    code: str
    reqstr: int  # "reqstr"
    levelreq: int  # "levelreq"


class Armor(BoolMixin, Enum):
    """PD2 armor categories."""

    CAP = _Metadata(
        code="cap",
        reqstr=0,
        levelreq=0,
    )
    SKULL_CAP = _Metadata(
        code="skp",
        reqstr=15,
        levelreq=0,
    )
    HELM = _Metadata(
        code="hlm",
        reqstr=26,
        levelreq=0,
    )
    FULL_HELM = _Metadata(
        code="fhl",
        reqstr=41,
        levelreq=0,
    )
    GREAT_HELM = _Metadata(
        code="ghm",
        reqstr=63,
        levelreq=0,
    )
    CROWN = _Metadata(
        code="crn",
        reqstr=55,
        levelreq=0,
    )
    MASK = _Metadata(
        code="msk",
        reqstr=23,
        levelreq=0,
    )
    QUILTED_ARMOR = _Metadata(
        code="qui",
        reqstr=12,
        levelreq=0,
    )
    LEATHER_ARMOR = _Metadata(
        code="lea",
        reqstr=15,
        levelreq=0,
    )
    HARD_LEATHER_ARMOR = _Metadata(
        code="hla",
        reqstr=20,
        levelreq=0,
    )
    STUDDED_LEATHER = _Metadata(
        code="stu",
        reqstr=27,
        levelreq=0,
    )
    RING_MAIL = _Metadata(
        code="rng",
        reqstr=36,
        levelreq=0,
    )
    SCALE_MAIL = _Metadata(
        code="scl",
        reqstr=44,
        levelreq=0,
    )
    CHAIN_MAIL = _Metadata(
        code="chn",
        reqstr=48,
        levelreq=0,
    )
    BREAST_PLATE = _Metadata(
        code="brs",
        reqstr=30,
        levelreq=0,
    )
    SPLINT_MAIL = _Metadata(
        code="spl",
        reqstr=51,
        levelreq=0,
    )
    PLATE_MAIL = _Metadata(
        code="plt",
        reqstr=65,
        levelreq=0,
    )
    FIELD_PLATE = _Metadata(
        code="fld",
        reqstr=55,
        levelreq=0,
    )
    GOTHIC_PLATE = _Metadata(
        code="gth",
        reqstr=70,
        levelreq=0,
    )
    FULL_PLATE_MAIL = _Metadata(
        code="ful",
        reqstr=80,
        levelreq=0,
    )
    ANCIENT_ARMOR = _Metadata(
        code="aar",
        reqstr=100,
        levelreq=0,
    )
    LIGHT_PLATE = _Metadata(
        code="ltp",
        reqstr=41,
        levelreq=0,
    )
    BUCKLER = _Metadata(
        code="buc",
        reqstr=12,
        levelreq=0,
    )
    SMALL_SHIELD = _Metadata(
        code="sml",
        reqstr=22,
        levelreq=0,
    )
    LARGE_SHIELD = _Metadata(
        code="lrg",
        reqstr=34,
        levelreq=0,
    )
    KITE_SHIELD = _Metadata(
        code="kit",
        reqstr=47,
        levelreq=0,
    )
    TOWER_SHIELD = _Metadata(
        code="tow",
        reqstr=75,
        levelreq=0,
    )
    GOTHIC_SHIELD = _Metadata(
        code="gts",
        reqstr=60,
        levelreq=0,
    )
    LEATHER_GLOVES = _Metadata(
        code="lgl",
        reqstr=0,
        levelreq=0,
    )
    HEAVY_GLOVES = _Metadata(
        code="vgl",
        reqstr=0,
        levelreq=0,
    )
    CHAIN_GLOVES = _Metadata(
        code="mgl",
        reqstr=25,
        levelreq=0,
    )
    LIGHT_GAUNTLETS = _Metadata(
        code="tgl",
        reqstr=45,
        levelreq=0,
    )
    GAUNTLETS = _Metadata(
        code="hgl",
        reqstr=60,
        levelreq=0,
    )
    BOOTS = _Metadata(
        code="lbt",
        reqstr=0,
        levelreq=0,
    )
    HEAVY_BOOTS = _Metadata(
        code="vbt",
        reqstr=18,
        levelreq=0,
    )
    CHAIN_BOOTS = _Metadata(
        code="mbt",
        reqstr=30,
        levelreq=0,
    )
    LIGHT_PLATED_BOOTS = _Metadata(
        code="tbt",
        reqstr=50,
        levelreq=0,
    )
    GREAVES = _Metadata(
        code="hbt",
        reqstr=70,
        levelreq=0,
    )
    SASH = _Metadata(
        code="lbl",
        reqstr=0,
        levelreq=0,
    )
    LIGHT_BELT = _Metadata(
        code="vbl",
        reqstr=0,
        levelreq=0,
    )
    BELT = _Metadata(
        code="mbl",
        reqstr=25,
        levelreq=0,
    )
    HEAVY_BELT = _Metadata(
        code="tbl",
        reqstr=45,
        levelreq=0,
    )
    PLATED_BELT = _Metadata(
        code="hbl",
        reqstr=60,
        levelreq=0,
    )
    BONE_HELM = _Metadata(
        code="bhm",
        reqstr=25,
        levelreq=0,
    )
    BONE_SHIELD = _Metadata(
        code="bsh",
        reqstr=25,
        levelreq=0,
    )
    SPIKED_SHIELD = _Metadata(
        code="spk",
        reqstr=30,
        levelreq=0,
    )
    WAR_HAT = _Metadata(
        code="xap",
        reqstr=20,
        levelreq=22,
    )
    SALLET = _Metadata(
        code="xkp",
        reqstr=43,
        levelreq=25,
    )
    CASQUE = _Metadata(
        code="xlm",
        reqstr=59,
        levelreq=25,
    )
    BASINET = _Metadata(
        code="xhl",
        reqstr=82,
        levelreq=25,
    )
    WINGED_HELM = _Metadata(
        code="xhm",
        reqstr=115,
        levelreq=25,
    )
    GRAND_CROWN = _Metadata(
        code="xrn",
        reqstr=103,
        levelreq=25,
    )
    DEATH_MASK = _Metadata(
        code="xsk",
        reqstr=55,
        levelreq=25,
    )
    GHOST_ARMOR = _Metadata(
        code="xui",
        reqstr=38,
        levelreq=22,
    )
    SERPENTSKIN_ARMOR = _Metadata(
        code="xea",
        reqstr=43,
        levelreq=24,
    )
    DEMONHIDE_ARMOR = _Metadata(
        code="xla",
        reqstr=50,
        levelreq=25,
    )
    TRELLISED_ARMOR = _Metadata(
        code="xtu",
        reqstr=61,
        levelreq=25,
    )
    LINKED_MAIL = _Metadata(
        code="xng",
        reqstr=74,
        levelreq=25,
    )
    TIGULATED_MAIL = _Metadata(
        code="xcl",
        reqstr=86,
        levelreq=25,
    )
    MESH_ARMOR = _Metadata(
        code="xhn",
        reqstr=92,
        levelreq=25,
    )
    CUIRASS = _Metadata(
        code="xrs",
        reqstr=65,
        levelreq=25,
    )
    RUSSET_ARMOR = _Metadata(
        code="xpl",
        reqstr=97,
        levelreq=25,
    )
    TEMPLAR_COAT = _Metadata(
        code="xlt",
        reqstr=118,
        levelreq=25,
    )
    SHARKTOOTH_ARMOR = _Metadata(
        code="xld",
        reqstr=103,
        levelreq=25,
    )
    EMBOSSED_PLATE = _Metadata(
        code="xth",
        reqstr=125,
        levelreq=25,
    )
    CHAOS_ARMOR = _Metadata(
        code="xul",
        reqstr=140,
        levelreq=25,
    )
    ORNATE_PLATE = _Metadata(
        code="xar",
        reqstr=170,
        levelreq=25,
    )
    MAGE_PLATE = _Metadata(
        code="xtp",
        reqstr=55,
        levelreq=25,
    )
    DEFENDER = _Metadata(
        code="xuc",
        reqstr=38,
        levelreq=22,
    )
    ROUND_SHIELD = _Metadata(
        code="xml",
        reqstr=53,
        levelreq=25,
    )
    SCUTUM = _Metadata(
        code="xrg",
        reqstr=71,
        levelreq=25,
    )
    DRAGON_SHIELD = _Metadata(
        code="xit",
        reqstr=91,
        levelreq=25,
    )
    PAVISE = _Metadata(
        code="xow",
        reqstr=133,
        levelreq=25,
    )
    ANCIENT_SHIELD = _Metadata(
        code="xts",
        reqstr=110,
        levelreq=25,
    )
    DEMONHIDE_GLOVES = _Metadata(
        code="xlg",
        reqstr=20,
        levelreq=21,
    )
    SHARKSKIN_GLOVES = _Metadata(
        code="xvg",
        reqstr=20,
        levelreq=25,
    )
    HEAVY_BRACERS = _Metadata(
        code="xmg",
        reqstr=58,
        levelreq=25,
    )
    BATTLE_GAUNTLETS = _Metadata(
        code="xtg",
        reqstr=88,
        levelreq=25,
    )
    WAR_GAUNTLETS = _Metadata(
        code="xhg",
        reqstr=110,
        levelreq=25,
    )
    DEMONHIDE_BOOTS = _Metadata(
        code="xlb",
        reqstr=20,
        levelreq=24,
    )
    SHARKSKIN_BOOTS = _Metadata(
        code="xvb",
        reqstr=47,
        levelreq=25,
    )
    MESH_BOOTS = _Metadata(
        code="xmb",
        reqstr=65,
        levelreq=25,
    )
    BATTLE_BOOTS = _Metadata(
        code="xtb",
        reqstr=95,
        levelreq=25,
    )
    WAR_BOOTS = _Metadata(
        code="xhb",
        reqstr=125,
        levelreq=25,
    )
    DEMONHIDE_SASH = _Metadata(
        code="zlb",
        reqstr=20,
        levelreq=24,
    )
    SHARKSKIN_BELT = _Metadata(
        code="zvb",
        reqstr=20,
        levelreq=25,
    )
    MESH_BELT = _Metadata(
        code="zmb",
        reqstr=58,
        levelreq=25,
    )
    BATTLE_BELT = _Metadata(
        code="ztb",
        reqstr=88,
        levelreq=25,
    )
    WAR_BELT = _Metadata(
        code="zhb",
        reqstr=110,
        levelreq=25,
    )
    GRIM_HELM = _Metadata(
        code="xh9",
        reqstr=58,
        levelreq=25,
    )
    GRIM_SHIELD = _Metadata(
        code="xsh",
        reqstr=58,
        levelreq=25,
    )
    BARBED_SHIELD = _Metadata(
        code="xpk",
        reqstr=65,
        levelreq=25,
    )
    WOLF_HEAD = _Metadata(
        code="dr1",
        reqstr=16,
        levelreq=3,
    )
    HAWK_HELM = _Metadata(
        code="dr2",
        reqstr=20,
        levelreq=6,
    )
    ANTLERS = _Metadata(
        code="dr3",
        reqstr=24,
        levelreq=12,
    )
    FALCON_MASK = _Metadata(
        code="dr4",
        reqstr=28,
        levelreq=15,
    )
    SPIRIT_MASK = _Metadata(
        code="dr5",
        reqstr=30,
        levelreq=18,
    )
    JAWBONE_CAP = _Metadata(
        code="ba1",
        reqstr=25,
        levelreq=3,
    )
    FANGED_HELM = _Metadata(
        code="ba2",
        reqstr=35,
        levelreq=6,
    )
    HORNED_HELM = _Metadata(
        code="ba3",
        reqstr=45,
        levelreq=12,
    )
    ASSAULT_HELMET = _Metadata(
        code="ba4",
        reqstr=55,
        levelreq=15,
    )
    AVENGER_GUARD = _Metadata(
        code="ba5",
        reqstr=65,
        levelreq=18,
    )
    TARGE = _Metadata(
        code="pa1",
        reqstr=16,
        levelreq=3,
    )
    RONDACHE = _Metadata(
        code="pa2",
        reqstr=26,
        levelreq=6,
    )
    HERALDIC_SHIELD = _Metadata(
        code="pa3",
        reqstr=40,
        levelreq=12,
    )
    AERIN_SHIELD = _Metadata(
        code="pa4",
        reqstr=50,
        levelreq=15,
    )
    CROWN_SHIELD = _Metadata(
        code="pa5",
        reqstr=65,
        levelreq=18,
    )
    PRESERVED_HEAD = _Metadata(
        code="ne1",
        reqstr=12,
        levelreq=3,
    )
    ZOMBIE_HEAD = _Metadata(
        code="ne2",
        reqstr=14,
        levelreq=6,
    )
    UNRAVELLER_HEAD = _Metadata(
        code="ne3",
        reqstr=18,
        levelreq=12,
    )
    GARGOYLE_HEAD = _Metadata(
        code="ne4",
        reqstr=20,
        levelreq=15,
    )
    DEMON_HEAD = _Metadata(
        code="ne5",
        reqstr=25,
        levelreq=18,
    )
    CIRCLET = _Metadata(
        code="ci0",
        reqstr=0,
        levelreq=16,
    )
    CORONET = _Metadata(
        code="ci1",
        reqstr=0,
        levelreq=39,
    )
    TIARA = _Metadata(
        code="ci2",
        reqstr=0,
        levelreq=52,
    )
    DIADEM = _Metadata(
        code="ci3",
        reqstr=0,
        levelreq=64,
    )
    SHAKO = _Metadata(
        code="uap",
        reqstr=50,
        levelreq=43,
    )
    HYDRASKULL = _Metadata(
        code="ukp",
        reqstr=84,
        levelreq=47,
    )
    ARMET = _Metadata(
        code="ulm",
        reqstr=109,
        levelreq=51,
    )
    GIANT_CONCH = _Metadata(
        code="uhl",
        reqstr=142,
        levelreq=40,
    )
    SPIRED_HELM = _Metadata(
        code="uhm",
        reqstr=192,
        levelreq=59,
    )
    CORONA = _Metadata(
        code="urn",
        reqstr=174,
        levelreq=66,
    )
    DEMONHEAD = _Metadata(
        code="usk",
        reqstr=102,
        levelreq=55,
    )
    DUSK_SHROUD = _Metadata(
        code="uui",
        reqstr=77,
        levelreq=49,
    )
    WYRMHIDE = _Metadata(
        code="uea",
        reqstr=84,
        levelreq=50,
    )
    SCARAB_HUSK = _Metadata(
        code="ula",
        reqstr=95,
        levelreq=51,
    )
    WIRE_FLEECE = _Metadata(
        code="utu",
        reqstr=111,
        levelreq=53,
    )
    DIAMOND_MAIL = _Metadata(
        code="ung",
        reqstr=131,
        levelreq=54,
    )
    LORICATED_MAIL = _Metadata(
        code="ucl",
        reqstr=149,
        levelreq=55,
    )
    BONEWEAVE = _Metadata(
        code="uhn",
        reqstr=158,
        levelreq=47,
    )
    GREAT_HAUBERK = _Metadata(
        code="urs",
        reqstr=118,
        levelreq=56,
    )
    BALROG_SKIN = _Metadata(
        code="upl",
        reqstr=165,
        levelreq=57,
    )
    HELLFORGE_PLATE = _Metadata(
        code="ult",
        reqstr=196,
        levelreq=59,
    )
    KRAKEN_SHELL = _Metadata(
        code="uld",
        reqstr=174,
        levelreq=61,
    )
    LACQUERED_PLATE = _Metadata(
        code="uth",
        reqstr=208,
        levelreq=62,
    )
    SHADOW_PLATE = _Metadata(
        code="uul",
        reqstr=220,
        levelreq=64,
    )
    SACRED_ARMOR = _Metadata(
        code="uar",
        reqstr=232,
        levelreq=66,
    )
    ARCHON_PLATE = _Metadata(
        code="utp",
        reqstr=103,
        levelreq=63,
    )
    HEATER = _Metadata(
        code="uuc",
        reqstr=77,
        levelreq=43,
    )
    LUNA = _Metadata(
        code="uml",
        reqstr=100,
        levelreq=45,
    )
    HYPERION = _Metadata(
        code="urg",
        reqstr=127,
        levelreq=48,
    )
    MONARCH = _Metadata(
        code="uit",
        reqstr=156,
        levelreq=54,
    )
    AEGIS = _Metadata(
        code="uow",
        reqstr=219,
        levelreq=59,
    )
    WARD = _Metadata(
        code="uts",
        reqstr=185,
        levelreq=63,
    )
    BRAMBLE_MITTS = _Metadata(
        code="ulg",
        reqstr=50,
        levelreq=42,
    )
    VAMPIREBONE_GLOVES = _Metadata(
        code="uvg",
        reqstr=50,
        levelreq=47,
    )
    VAMBRACES = _Metadata(
        code="umg",
        reqstr=106,
        levelreq=51,
    )
    CRUSADER_GAUNTLETS = _Metadata(
        code="utg",
        reqstr=151,
        levelreq=57,
    )
    OGRE_GAUNTLETS = _Metadata(
        code="uhg",
        reqstr=185,
        levelreq=64,
    )
    WYRMHIDE_BOOTS = _Metadata(
        code="ulb",
        reqstr=50,
        levelreq=45,
    )
    SCARABSHELL_BOOTS = _Metadata(
        code="uvb",
        reqstr=91,
        levelreq=49,
    )
    BONEWEAVE_BOOTS = _Metadata(
        code="umb",
        reqstr=118,
        levelreq=54,
    )
    MIRRORED_BOOTS = _Metadata(
        code="utb",
        reqstr=163,
        levelreq=60,
    )
    MYRMIDON_GREAVES = _Metadata(
        code="uhb",
        reqstr=208,
        levelreq=65,
    )
    SPIDERWEB_SASH = _Metadata(
        code="ulc",
        reqstr=50,
        levelreq=46,
    )
    VAMPIREFANG_BELT = _Metadata(
        code="uvc",
        reqstr=50,
        levelreq=51,
    )
    MITHRIL_COIL = _Metadata(
        code="umc",
        reqstr=106,
        levelreq=56,
    )
    TROLL_BELT = _Metadata(
        code="utc",
        reqstr=151,
        levelreq=62,
    )
    COLOSSUS_GIRDLE = _Metadata(
        code="uhc",
        reqstr=185,
        levelreq=67,
    )
    BONE_VISAGE = _Metadata(
        code="uh9",
        reqstr=106,
        levelreq=63,
    )
    TROLL_NEST = _Metadata(
        code="ush",
        reqstr=106,
        levelreq=57,
    )
    BLADE_BARRIER = _Metadata(
        code="upk",
        reqstr=118,
        levelreq=51,
    )
    ALPHA_HELM = _Metadata(
        code="dr6",
        reqstr=44,
        levelreq=26,
    )
    GRIFFON_HEADDRESS = _Metadata(
        code="dr7",
        reqstr=50,
        levelreq=30,
    )
    HUNTERS_GUISE = _Metadata(
        code="dr8",
        reqstr=56,
        levelreq=29,
    )
    SACRED_FEATHERS = _Metadata(
        code="dr9",
        reqstr=62,
        levelreq=32,
    )
    TOTEMIC_MASK = _Metadata(
        code="dra",
        reqstr=65,
        levelreq=41,
    )
    JAWBONE_VISOR = _Metadata(
        code="ba6",
        reqstr=58,
        levelreq=25,
    )
    LION_HELM = _Metadata(
        code="ba7",
        reqstr=73,
        levelreq=29,
    )
    RAGE_MASK = _Metadata(
        code="ba8",
        reqstr=88,
        levelreq=29,
    )
    SAVAGE_HELMET = _Metadata(
        code="ba9",
        reqstr=103,
        levelreq=32,
    )
    SLAYER_GUARD = _Metadata(
        code="baa",
        reqstr=118,
        levelreq=40,
    )
    AKARAN_TARGE = _Metadata(
        code="pa6",
        reqstr=44,
        levelreq=26,
    )
    AKARAN_RONDACHE = _Metadata(
        code="pa7",
        reqstr=59,
        levelreq=30,
    )
    PROTECTOR_SHIELD = _Metadata(
        code="pa8",
        reqstr=69,
        levelreq=34,
    )
    GILDED_SHIELD = _Metadata(
        code="pa9",
        reqstr=89,
        levelreq=38,
    )
    ROYAL_SHIELD = _Metadata(
        code="paa",
        reqstr=114,
        levelreq=41,
    )
    MUMMIFIED_TROPHY = _Metadata(
        code="ne6",
        reqstr=38,
        levelreq=24,
    )
    FETISH_TROPHY = _Metadata(
        code="ne7",
        reqstr=41,
        levelreq=29,
    )
    SEXTON_TROPHY = _Metadata(
        code="ne8",
        reqstr=47,
        levelreq=33,
    )
    CANTOR_TROPHY = _Metadata(
        code="ne9",
        reqstr=50,
        levelreq=36,
    )
    HIEROPHANT_TROPHY = _Metadata(
        code="nea",
        reqstr=58,
        levelreq=40,
    )
    BLOOD_SPIRIT = _Metadata(
        code="drb",
        reqstr=86,
        levelreq=46,
    )
    SUN_SPIRIT = _Metadata(
        code="drc",
        reqstr=95,
        levelreq=51,
    )
    EARTH_SPIRIT = _Metadata(
        code="drd",
        reqstr=104,
        levelreq=57,
    )
    SKY_SPIRIT = _Metadata(
        code="dre",
        reqstr=113,
        levelreq=62,
    )
    DREAM_SPIRIT = _Metadata(
        code="drf",
        reqstr=118,
        levelreq=66,
    )
    CARNAGE_HELM = _Metadata(
        code="bab",
        reqstr=106,
        levelreq=45,
    )
    FURY_VISOR = _Metadata(
        code="bac",
        reqstr=129,
        levelreq=49,
    )
    DESTROYER_HELM = _Metadata(
        code="bad",
        reqstr=151,
        levelreq=54,
    )
    CONQUEROR_CROWN = _Metadata(
        code="bae",
        reqstr=174,
        levelreq=60,
    )
    GUARDIAN_CROWN = _Metadata(
        code="baf",
        reqstr=196,
        levelreq=65,
    )
    SACRED_TARGE = _Metadata(
        code="pab",
        reqstr=86,
        levelreq=47,
    )
    SACRED_RONDACHE = _Metadata(
        code="pac",
        reqstr=109,
        levelreq=52,
    )
    KURAST_SHIELD = _Metadata(
        code="pad",
        reqstr=124,
        levelreq=55,
    )
    ZAKARUM_SHIELD = _Metadata(
        code="pae",
        reqstr=142,
        levelreq=61,
    )
    VORTEX_SHIELD = _Metadata(
        code="paf",
        reqstr=148,
        levelreq=66,
    )
    MINION_SKULL = _Metadata(
        code="neb",
        reqstr=77,
        levelreq=44,
    )
    HELLSPAWN_SKULL = _Metadata(
        code="neg",
        reqstr=82,
        levelreq=50,
    )
    OVERSEER_SKULL = _Metadata(
        code="ned",
        reqstr=91,
        levelreq=49,
    )
    SUCCUBUS_SKULL = _Metadata(
        code="nee",
        reqstr=95,
        levelreq=60,
    )
    BLOODLORD_SKULL = _Metadata(
        code="nef",
        reqstr=106,
        levelreq=65,
    )
    CAGE_OF_THE_UNSULLIED = _Metadata(
        code="rar",
        reqstr=158,
        levelreq=47,
    )
    BAND_OF_SKULLS = _Metadata(
        code="rbe",
        reqstr=151,
        levelreq=62,
    )

    def as_node(self) -> BoolRef:
        return BoolRef(self.value.code)

    @property
    def reqstr(self) -> int:
        return self.value.reqstr

    @property
    def levelreq(self) -> int:
        return self.value.levelreq
