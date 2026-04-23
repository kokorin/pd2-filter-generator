"""
Generated Armor enum from PD2 data.

DO NOT EDIT MANUALLY - regenerate with: hatch run ./scripts/generate.py generate
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from pd2_filter_generator.expression import CodeLiteral


@dataclass(frozen=True)
class _Metadata:
    """Item type metadata."""

    code: CodeLiteral  # "code"
    reqstr: int  # "reqstr"
    levelreq: int  # "levelreq"


_METADATA: dict[str, _Metadata] = {
    "CAP": _Metadata(
        code=CodeLiteral("cap"),
        reqstr=0,
        levelreq=0,
    ),
    "SKULL_CAP": _Metadata(
        code=CodeLiteral("skp"),
        reqstr=15,
        levelreq=0,
    ),
    "HELM": _Metadata(
        code=CodeLiteral("hlm"),
        reqstr=26,
        levelreq=0,
    ),
    "FULL_HELM": _Metadata(
        code=CodeLiteral("fhl"),
        reqstr=41,
        levelreq=0,
    ),
    "GREAT_HELM": _Metadata(
        code=CodeLiteral("ghm"),
        reqstr=63,
        levelreq=0,
    ),
    "CROWN": _Metadata(
        code=CodeLiteral("crn"),
        reqstr=55,
        levelreq=0,
    ),
    "MASK": _Metadata(
        code=CodeLiteral("msk"),
        reqstr=23,
        levelreq=0,
    ),
    "QUILTED_ARMOR": _Metadata(
        code=CodeLiteral("qui"),
        reqstr=12,
        levelreq=0,
    ),
    "LEATHER_ARMOR": _Metadata(
        code=CodeLiteral("lea"),
        reqstr=15,
        levelreq=0,
    ),
    "HARD_LEATHER_ARMOR": _Metadata(
        code=CodeLiteral("hla"),
        reqstr=20,
        levelreq=0,
    ),
    "STUDDED_LEATHER": _Metadata(
        code=CodeLiteral("stu"),
        reqstr=27,
        levelreq=0,
    ),
    "RING_MAIL": _Metadata(
        code=CodeLiteral("rng"),
        reqstr=36,
        levelreq=0,
    ),
    "SCALE_MAIL": _Metadata(
        code=CodeLiteral("scl"),
        reqstr=44,
        levelreq=0,
    ),
    "CHAIN_MAIL": _Metadata(
        code=CodeLiteral("chn"),
        reqstr=48,
        levelreq=0,
    ),
    "BREAST_PLATE": _Metadata(
        code=CodeLiteral("brs"),
        reqstr=30,
        levelreq=0,
    ),
    "SPLINT_MAIL": _Metadata(
        code=CodeLiteral("spl"),
        reqstr=51,
        levelreq=0,
    ),
    "PLATE_MAIL": _Metadata(
        code=CodeLiteral("plt"),
        reqstr=65,
        levelreq=0,
    ),
    "FIELD_PLATE": _Metadata(
        code=CodeLiteral("fld"),
        reqstr=55,
        levelreq=0,
    ),
    "GOTHIC_PLATE": _Metadata(
        code=CodeLiteral("gth"),
        reqstr=70,
        levelreq=0,
    ),
    "FULL_PLATE_MAIL": _Metadata(
        code=CodeLiteral("ful"),
        reqstr=80,
        levelreq=0,
    ),
    "ANCIENT_ARMOR": _Metadata(
        code=CodeLiteral("aar"),
        reqstr=100,
        levelreq=0,
    ),
    "LIGHT_PLATE": _Metadata(
        code=CodeLiteral("ltp"),
        reqstr=41,
        levelreq=0,
    ),
    "BUCKLER": _Metadata(
        code=CodeLiteral("buc"),
        reqstr=12,
        levelreq=0,
    ),
    "SMALL_SHIELD": _Metadata(
        code=CodeLiteral("sml"),
        reqstr=22,
        levelreq=0,
    ),
    "LARGE_SHIELD": _Metadata(
        code=CodeLiteral("lrg"),
        reqstr=34,
        levelreq=0,
    ),
    "KITE_SHIELD": _Metadata(
        code=CodeLiteral("kit"),
        reqstr=47,
        levelreq=0,
    ),
    "TOWER_SHIELD": _Metadata(
        code=CodeLiteral("tow"),
        reqstr=75,
        levelreq=0,
    ),
    "GOTHIC_SHIELD": _Metadata(
        code=CodeLiteral("gts"),
        reqstr=60,
        levelreq=0,
    ),
    "LEATHER_GLOVES": _Metadata(
        code=CodeLiteral("lgl"),
        reqstr=0,
        levelreq=0,
    ),
    "HEAVY_GLOVES": _Metadata(
        code=CodeLiteral("vgl"),
        reqstr=0,
        levelreq=0,
    ),
    "CHAIN_GLOVES": _Metadata(
        code=CodeLiteral("mgl"),
        reqstr=25,
        levelreq=0,
    ),
    "LIGHT_GAUNTLETS": _Metadata(
        code=CodeLiteral("tgl"),
        reqstr=45,
        levelreq=0,
    ),
    "GAUNTLETS": _Metadata(
        code=CodeLiteral("hgl"),
        reqstr=60,
        levelreq=0,
    ),
    "BOOTS": _Metadata(
        code=CodeLiteral("lbt"),
        reqstr=0,
        levelreq=0,
    ),
    "HEAVY_BOOTS": _Metadata(
        code=CodeLiteral("vbt"),
        reqstr=18,
        levelreq=0,
    ),
    "CHAIN_BOOTS": _Metadata(
        code=CodeLiteral("mbt"),
        reqstr=30,
        levelreq=0,
    ),
    "LIGHT_PLATED_BOOTS": _Metadata(
        code=CodeLiteral("tbt"),
        reqstr=50,
        levelreq=0,
    ),
    "GREAVES": _Metadata(
        code=CodeLiteral("hbt"),
        reqstr=70,
        levelreq=0,
    ),
    "SASH": _Metadata(
        code=CodeLiteral("lbl"),
        reqstr=0,
        levelreq=0,
    ),
    "LIGHT_BELT": _Metadata(
        code=CodeLiteral("vbl"),
        reqstr=0,
        levelreq=0,
    ),
    "BELT": _Metadata(
        code=CodeLiteral("mbl"),
        reqstr=25,
        levelreq=0,
    ),
    "HEAVY_BELT": _Metadata(
        code=CodeLiteral("tbl"),
        reqstr=45,
        levelreq=0,
    ),
    "PLATED_BELT": _Metadata(
        code=CodeLiteral("hbl"),
        reqstr=60,
        levelreq=0,
    ),
    "BONE_HELM": _Metadata(
        code=CodeLiteral("bhm"),
        reqstr=25,
        levelreq=0,
    ),
    "BONE_SHIELD": _Metadata(
        code=CodeLiteral("bsh"),
        reqstr=25,
        levelreq=0,
    ),
    "SPIKED_SHIELD": _Metadata(
        code=CodeLiteral("spk"),
        reqstr=30,
        levelreq=0,
    ),
    "WAR_HAT": _Metadata(
        code=CodeLiteral("xap"),
        reqstr=20,
        levelreq=22,
    ),
    "SALLET": _Metadata(
        code=CodeLiteral("xkp"),
        reqstr=43,
        levelreq=25,
    ),
    "CASQUE": _Metadata(
        code=CodeLiteral("xlm"),
        reqstr=59,
        levelreq=25,
    ),
    "BASINET": _Metadata(
        code=CodeLiteral("xhl"),
        reqstr=82,
        levelreq=25,
    ),
    "WINGED_HELM": _Metadata(
        code=CodeLiteral("xhm"),
        reqstr=115,
        levelreq=25,
    ),
    "GRAND_CROWN": _Metadata(
        code=CodeLiteral("xrn"),
        reqstr=103,
        levelreq=25,
    ),
    "DEATH_MASK": _Metadata(
        code=CodeLiteral("xsk"),
        reqstr=55,
        levelreq=25,
    ),
    "GHOST_ARMOR": _Metadata(
        code=CodeLiteral("xui"),
        reqstr=38,
        levelreq=22,
    ),
    "SERPENTSKIN_ARMOR": _Metadata(
        code=CodeLiteral("xea"),
        reqstr=43,
        levelreq=24,
    ),
    "DEMONHIDE_ARMOR": _Metadata(
        code=CodeLiteral("xla"),
        reqstr=50,
        levelreq=25,
    ),
    "TRELLISED_ARMOR": _Metadata(
        code=CodeLiteral("xtu"),
        reqstr=61,
        levelreq=25,
    ),
    "LINKED_MAIL": _Metadata(
        code=CodeLiteral("xng"),
        reqstr=74,
        levelreq=25,
    ),
    "TIGULATED_MAIL": _Metadata(
        code=CodeLiteral("xcl"),
        reqstr=86,
        levelreq=25,
    ),
    "MESH_ARMOR": _Metadata(
        code=CodeLiteral("xhn"),
        reqstr=92,
        levelreq=25,
    ),
    "CUIRASS": _Metadata(
        code=CodeLiteral("xrs"),
        reqstr=65,
        levelreq=25,
    ),
    "RUSSET_ARMOR": _Metadata(
        code=CodeLiteral("xpl"),
        reqstr=97,
        levelreq=25,
    ),
    "TEMPLAR_COAT": _Metadata(
        code=CodeLiteral("xlt"),
        reqstr=118,
        levelreq=25,
    ),
    "SHARKTOOTH_ARMOR": _Metadata(
        code=CodeLiteral("xld"),
        reqstr=103,
        levelreq=25,
    ),
    "EMBOSSED_PLATE": _Metadata(
        code=CodeLiteral("xth"),
        reqstr=125,
        levelreq=25,
    ),
    "CHAOS_ARMOR": _Metadata(
        code=CodeLiteral("xul"),
        reqstr=140,
        levelreq=25,
    ),
    "ORNATE_PLATE": _Metadata(
        code=CodeLiteral("xar"),
        reqstr=170,
        levelreq=25,
    ),
    "MAGE_PLATE": _Metadata(
        code=CodeLiteral("xtp"),
        reqstr=55,
        levelreq=25,
    ),
    "DEFENDER": _Metadata(
        code=CodeLiteral("xuc"),
        reqstr=38,
        levelreq=22,
    ),
    "ROUND_SHIELD": _Metadata(
        code=CodeLiteral("xml"),
        reqstr=53,
        levelreq=25,
    ),
    "SCUTUM": _Metadata(
        code=CodeLiteral("xrg"),
        reqstr=71,
        levelreq=25,
    ),
    "DRAGON_SHIELD": _Metadata(
        code=CodeLiteral("xit"),
        reqstr=91,
        levelreq=25,
    ),
    "PAVISE": _Metadata(
        code=CodeLiteral("xow"),
        reqstr=133,
        levelreq=25,
    ),
    "ANCIENT_SHIELD": _Metadata(
        code=CodeLiteral("xts"),
        reqstr=110,
        levelreq=25,
    ),
    "DEMONHIDE_GLOVES": _Metadata(
        code=CodeLiteral("xlg"),
        reqstr=20,
        levelreq=21,
    ),
    "SHARKSKIN_GLOVES": _Metadata(
        code=CodeLiteral("xvg"),
        reqstr=20,
        levelreq=25,
    ),
    "HEAVY_BRACERS": _Metadata(
        code=CodeLiteral("xmg"),
        reqstr=58,
        levelreq=25,
    ),
    "BATTLE_GAUNTLETS": _Metadata(
        code=CodeLiteral("xtg"),
        reqstr=88,
        levelreq=25,
    ),
    "WAR_GAUNTLETS": _Metadata(
        code=CodeLiteral("xhg"),
        reqstr=110,
        levelreq=25,
    ),
    "DEMONHIDE_BOOTS": _Metadata(
        code=CodeLiteral("xlb"),
        reqstr=20,
        levelreq=24,
    ),
    "SHARKSKIN_BOOTS": _Metadata(
        code=CodeLiteral("xvb"),
        reqstr=47,
        levelreq=25,
    ),
    "MESH_BOOTS": _Metadata(
        code=CodeLiteral("xmb"),
        reqstr=65,
        levelreq=25,
    ),
    "BATTLE_BOOTS": _Metadata(
        code=CodeLiteral("xtb"),
        reqstr=95,
        levelreq=25,
    ),
    "WAR_BOOTS": _Metadata(
        code=CodeLiteral("xhb"),
        reqstr=125,
        levelreq=25,
    ),
    "DEMONHIDE_SASH": _Metadata(
        code=CodeLiteral("zlb"),
        reqstr=20,
        levelreq=24,
    ),
    "SHARKSKIN_BELT": _Metadata(
        code=CodeLiteral("zvb"),
        reqstr=20,
        levelreq=25,
    ),
    "MESH_BELT": _Metadata(
        code=CodeLiteral("zmb"),
        reqstr=58,
        levelreq=25,
    ),
    "BATTLE_BELT": _Metadata(
        code=CodeLiteral("ztb"),
        reqstr=88,
        levelreq=25,
    ),
    "WAR_BELT": _Metadata(
        code=CodeLiteral("zhb"),
        reqstr=110,
        levelreq=25,
    ),
    "GRIM_HELM": _Metadata(
        code=CodeLiteral("xh9"),
        reqstr=58,
        levelreq=25,
    ),
    "GRIM_SHIELD": _Metadata(
        code=CodeLiteral("xsh"),
        reqstr=58,
        levelreq=25,
    ),
    "BARBED_SHIELD": _Metadata(
        code=CodeLiteral("xpk"),
        reqstr=65,
        levelreq=25,
    ),
    "WOLF_HEAD": _Metadata(
        code=CodeLiteral("dr1"),
        reqstr=16,
        levelreq=3,
    ),
    "HAWK_HELM": _Metadata(
        code=CodeLiteral("dr2"),
        reqstr=20,
        levelreq=6,
    ),
    "ANTLERS": _Metadata(
        code=CodeLiteral("dr3"),
        reqstr=24,
        levelreq=12,
    ),
    "FALCON_MASK": _Metadata(
        code=CodeLiteral("dr4"),
        reqstr=28,
        levelreq=15,
    ),
    "SPIRIT_MASK": _Metadata(
        code=CodeLiteral("dr5"),
        reqstr=30,
        levelreq=18,
    ),
    "JAWBONE_CAP": _Metadata(
        code=CodeLiteral("ba1"),
        reqstr=25,
        levelreq=3,
    ),
    "FANGED_HELM": _Metadata(
        code=CodeLiteral("ba2"),
        reqstr=35,
        levelreq=6,
    ),
    "HORNED_HELM": _Metadata(
        code=CodeLiteral("ba3"),
        reqstr=45,
        levelreq=12,
    ),
    "ASSAULT_HELMET": _Metadata(
        code=CodeLiteral("ba4"),
        reqstr=55,
        levelreq=15,
    ),
    "AVENGER_GUARD": _Metadata(
        code=CodeLiteral("ba5"),
        reqstr=65,
        levelreq=18,
    ),
    "TARGE": _Metadata(
        code=CodeLiteral("pa1"),
        reqstr=16,
        levelreq=3,
    ),
    "RONDACHE": _Metadata(
        code=CodeLiteral("pa2"),
        reqstr=26,
        levelreq=6,
    ),
    "HERALDIC_SHIELD": _Metadata(
        code=CodeLiteral("pa3"),
        reqstr=40,
        levelreq=12,
    ),
    "AERIN_SHIELD": _Metadata(
        code=CodeLiteral("pa4"),
        reqstr=50,
        levelreq=15,
    ),
    "CROWN_SHIELD": _Metadata(
        code=CodeLiteral("pa5"),
        reqstr=65,
        levelreq=18,
    ),
    "PRESERVED_HEAD": _Metadata(
        code=CodeLiteral("ne1"),
        reqstr=12,
        levelreq=3,
    ),
    "ZOMBIE_HEAD": _Metadata(
        code=CodeLiteral("ne2"),
        reqstr=14,
        levelreq=6,
    ),
    "UNRAVELLER_HEAD": _Metadata(
        code=CodeLiteral("ne3"),
        reqstr=18,
        levelreq=12,
    ),
    "GARGOYLE_HEAD": _Metadata(
        code=CodeLiteral("ne4"),
        reqstr=20,
        levelreq=15,
    ),
    "DEMON_HEAD": _Metadata(
        code=CodeLiteral("ne5"),
        reqstr=25,
        levelreq=18,
    ),
    "CIRCLET": _Metadata(
        code=CodeLiteral("ci0"),
        reqstr=0,
        levelreq=16,
    ),
    "CORONET": _Metadata(
        code=CodeLiteral("ci1"),
        reqstr=0,
        levelreq=39,
    ),
    "TIARA": _Metadata(
        code=CodeLiteral("ci2"),
        reqstr=0,
        levelreq=52,
    ),
    "DIADEM": _Metadata(
        code=CodeLiteral("ci3"),
        reqstr=0,
        levelreq=64,
    ),
    "SHAKO": _Metadata(
        code=CodeLiteral("uap"),
        reqstr=50,
        levelreq=43,
    ),
    "HYDRASKULL": _Metadata(
        code=CodeLiteral("ukp"),
        reqstr=84,
        levelreq=47,
    ),
    "ARMET": _Metadata(
        code=CodeLiteral("ulm"),
        reqstr=109,
        levelreq=51,
    ),
    "GIANT_CONCH": _Metadata(
        code=CodeLiteral("uhl"),
        reqstr=142,
        levelreq=40,
    ),
    "SPIRED_HELM": _Metadata(
        code=CodeLiteral("uhm"),
        reqstr=192,
        levelreq=59,
    ),
    "CORONA": _Metadata(
        code=CodeLiteral("urn"),
        reqstr=174,
        levelreq=66,
    ),
    "DEMONHEAD": _Metadata(
        code=CodeLiteral("usk"),
        reqstr=102,
        levelreq=55,
    ),
    "DUSK_SHROUD": _Metadata(
        code=CodeLiteral("uui"),
        reqstr=77,
        levelreq=49,
    ),
    "WYRMHIDE": _Metadata(
        code=CodeLiteral("uea"),
        reqstr=84,
        levelreq=50,
    ),
    "SCARAB_HUSK": _Metadata(
        code=CodeLiteral("ula"),
        reqstr=95,
        levelreq=51,
    ),
    "WIRE_FLEECE": _Metadata(
        code=CodeLiteral("utu"),
        reqstr=111,
        levelreq=53,
    ),
    "DIAMOND_MAIL": _Metadata(
        code=CodeLiteral("ung"),
        reqstr=131,
        levelreq=54,
    ),
    "LORICATED_MAIL": _Metadata(
        code=CodeLiteral("ucl"),
        reqstr=149,
        levelreq=55,
    ),
    "BONEWEAVE": _Metadata(
        code=CodeLiteral("uhn"),
        reqstr=158,
        levelreq=47,
    ),
    "GREAT_HAUBERK": _Metadata(
        code=CodeLiteral("urs"),
        reqstr=118,
        levelreq=56,
    ),
    "BALROG_SKIN": _Metadata(
        code=CodeLiteral("upl"),
        reqstr=165,
        levelreq=57,
    ),
    "HELLFORGE_PLATE": _Metadata(
        code=CodeLiteral("ult"),
        reqstr=196,
        levelreq=59,
    ),
    "KRAKEN_SHELL": _Metadata(
        code=CodeLiteral("uld"),
        reqstr=174,
        levelreq=61,
    ),
    "LACQUERED_PLATE": _Metadata(
        code=CodeLiteral("uth"),
        reqstr=208,
        levelreq=62,
    ),
    "SHADOW_PLATE": _Metadata(
        code=CodeLiteral("uul"),
        reqstr=220,
        levelreq=64,
    ),
    "SACRED_ARMOR": _Metadata(
        code=CodeLiteral("uar"),
        reqstr=232,
        levelreq=66,
    ),
    "ARCHON_PLATE": _Metadata(
        code=CodeLiteral("utp"),
        reqstr=103,
        levelreq=63,
    ),
    "HEATER": _Metadata(
        code=CodeLiteral("uuc"),
        reqstr=77,
        levelreq=43,
    ),
    "LUNA": _Metadata(
        code=CodeLiteral("uml"),
        reqstr=100,
        levelreq=45,
    ),
    "HYPERION": _Metadata(
        code=CodeLiteral("urg"),
        reqstr=127,
        levelreq=48,
    ),
    "MONARCH": _Metadata(
        code=CodeLiteral("uit"),
        reqstr=156,
        levelreq=54,
    ),
    "AEGIS": _Metadata(
        code=CodeLiteral("uow"),
        reqstr=219,
        levelreq=59,
    ),
    "WARD": _Metadata(
        code=CodeLiteral("uts"),
        reqstr=185,
        levelreq=63,
    ),
    "BRAMBLE_MITTS": _Metadata(
        code=CodeLiteral("ulg"),
        reqstr=50,
        levelreq=42,
    ),
    "VAMPIREBONE_GLOVES": _Metadata(
        code=CodeLiteral("uvg"),
        reqstr=50,
        levelreq=47,
    ),
    "VAMBRACES": _Metadata(
        code=CodeLiteral("umg"),
        reqstr=106,
        levelreq=51,
    ),
    "CRUSADER_GAUNTLETS": _Metadata(
        code=CodeLiteral("utg"),
        reqstr=151,
        levelreq=57,
    ),
    "OGRE_GAUNTLETS": _Metadata(
        code=CodeLiteral("uhg"),
        reqstr=185,
        levelreq=64,
    ),
    "WYRMHIDE_BOOTS": _Metadata(
        code=CodeLiteral("ulb"),
        reqstr=50,
        levelreq=45,
    ),
    "SCARABSHELL_BOOTS": _Metadata(
        code=CodeLiteral("uvb"),
        reqstr=91,
        levelreq=49,
    ),
    "BONEWEAVE_BOOTS": _Metadata(
        code=CodeLiteral("umb"),
        reqstr=118,
        levelreq=54,
    ),
    "MIRRORED_BOOTS": _Metadata(
        code=CodeLiteral("utb"),
        reqstr=163,
        levelreq=60,
    ),
    "MYRMIDON_GREAVES": _Metadata(
        code=CodeLiteral("uhb"),
        reqstr=208,
        levelreq=65,
    ),
    "SPIDERWEB_SASH": _Metadata(
        code=CodeLiteral("ulc"),
        reqstr=50,
        levelreq=46,
    ),
    "VAMPIREFANG_BELT": _Metadata(
        code=CodeLiteral("uvc"),
        reqstr=50,
        levelreq=51,
    ),
    "MITHRIL_COIL": _Metadata(
        code=CodeLiteral("umc"),
        reqstr=106,
        levelreq=56,
    ),
    "TROLL_BELT": _Metadata(
        code=CodeLiteral("utc"),
        reqstr=151,
        levelreq=62,
    ),
    "COLOSSUS_GIRDLE": _Metadata(
        code=CodeLiteral("uhc"),
        reqstr=185,
        levelreq=67,
    ),
    "BONE_VISAGE": _Metadata(
        code=CodeLiteral("uh9"),
        reqstr=106,
        levelreq=63,
    ),
    "TROLL_NEST": _Metadata(
        code=CodeLiteral("ush"),
        reqstr=106,
        levelreq=57,
    ),
    "BLADE_BARRIER": _Metadata(
        code=CodeLiteral("upk"),
        reqstr=118,
        levelreq=51,
    ),
    "ALPHA_HELM": _Metadata(
        code=CodeLiteral("dr6"),
        reqstr=44,
        levelreq=26,
    ),
    "GRIFFON_HEADDRESS": _Metadata(
        code=CodeLiteral("dr7"),
        reqstr=50,
        levelreq=30,
    ),
    "HUNTERS_GUISE": _Metadata(
        code=CodeLiteral("dr8"),
        reqstr=56,
        levelreq=29,
    ),
    "SACRED_FEATHERS": _Metadata(
        code=CodeLiteral("dr9"),
        reqstr=62,
        levelreq=32,
    ),
    "TOTEMIC_MASK": _Metadata(
        code=CodeLiteral("dra"),
        reqstr=65,
        levelreq=41,
    ),
    "JAWBONE_VISOR": _Metadata(
        code=CodeLiteral("ba6"),
        reqstr=58,
        levelreq=25,
    ),
    "LION_HELM": _Metadata(
        code=CodeLiteral("ba7"),
        reqstr=73,
        levelreq=29,
    ),
    "RAGE_MASK": _Metadata(
        code=CodeLiteral("ba8"),
        reqstr=88,
        levelreq=29,
    ),
    "SAVAGE_HELMET": _Metadata(
        code=CodeLiteral("ba9"),
        reqstr=103,
        levelreq=32,
    ),
    "SLAYER_GUARD": _Metadata(
        code=CodeLiteral("baa"),
        reqstr=118,
        levelreq=40,
    ),
    "AKARAN_TARGE": _Metadata(
        code=CodeLiteral("pa6"),
        reqstr=44,
        levelreq=26,
    ),
    "AKARAN_RONDACHE": _Metadata(
        code=CodeLiteral("pa7"),
        reqstr=59,
        levelreq=30,
    ),
    "PROTECTOR_SHIELD": _Metadata(
        code=CodeLiteral("pa8"),
        reqstr=69,
        levelreq=34,
    ),
    "GILDED_SHIELD": _Metadata(
        code=CodeLiteral("pa9"),
        reqstr=89,
        levelreq=38,
    ),
    "ROYAL_SHIELD": _Metadata(
        code=CodeLiteral("paa"),
        reqstr=114,
        levelreq=41,
    ),
    "MUMMIFIED_TROPHY": _Metadata(
        code=CodeLiteral("ne6"),
        reqstr=38,
        levelreq=24,
    ),
    "FETISH_TROPHY": _Metadata(
        code=CodeLiteral("ne7"),
        reqstr=41,
        levelreq=29,
    ),
    "SEXTON_TROPHY": _Metadata(
        code=CodeLiteral("ne8"),
        reqstr=47,
        levelreq=33,
    ),
    "CANTOR_TROPHY": _Metadata(
        code=CodeLiteral("ne9"),
        reqstr=50,
        levelreq=36,
    ),
    "HIEROPHANT_TROPHY": _Metadata(
        code=CodeLiteral("nea"),
        reqstr=58,
        levelreq=40,
    ),
    "BLOOD_SPIRIT": _Metadata(
        code=CodeLiteral("drb"),
        reqstr=86,
        levelreq=46,
    ),
    "SUN_SPIRIT": _Metadata(
        code=CodeLiteral("drc"),
        reqstr=95,
        levelreq=51,
    ),
    "EARTH_SPIRIT": _Metadata(
        code=CodeLiteral("drd"),
        reqstr=104,
        levelreq=57,
    ),
    "SKY_SPIRIT": _Metadata(
        code=CodeLiteral("dre"),
        reqstr=113,
        levelreq=62,
    ),
    "DREAM_SPIRIT": _Metadata(
        code=CodeLiteral("drf"),
        reqstr=118,
        levelreq=66,
    ),
    "CARNAGE_HELM": _Metadata(
        code=CodeLiteral("bab"),
        reqstr=106,
        levelreq=45,
    ),
    "FURY_VISOR": _Metadata(
        code=CodeLiteral("bac"),
        reqstr=129,
        levelreq=49,
    ),
    "DESTROYER_HELM": _Metadata(
        code=CodeLiteral("bad"),
        reqstr=151,
        levelreq=54,
    ),
    "CONQUEROR_CROWN": _Metadata(
        code=CodeLiteral("bae"),
        reqstr=174,
        levelreq=60,
    ),
    "GUARDIAN_CROWN": _Metadata(
        code=CodeLiteral("baf"),
        reqstr=196,
        levelreq=65,
    ),
    "SACRED_TARGE": _Metadata(
        code=CodeLiteral("pab"),
        reqstr=86,
        levelreq=47,
    ),
    "SACRED_RONDACHE": _Metadata(
        code=CodeLiteral("pac"),
        reqstr=109,
        levelreq=52,
    ),
    "KURAST_SHIELD": _Metadata(
        code=CodeLiteral("pad"),
        reqstr=124,
        levelreq=55,
    ),
    "ZAKARUM_SHIELD": _Metadata(
        code=CodeLiteral("pae"),
        reqstr=142,
        levelreq=61,
    ),
    "VORTEX_SHIELD": _Metadata(
        code=CodeLiteral("paf"),
        reqstr=148,
        levelreq=66,
    ),
    "MINION_SKULL": _Metadata(
        code=CodeLiteral("neb"),
        reqstr=77,
        levelreq=44,
    ),
    "HELLSPAWN_SKULL": _Metadata(
        code=CodeLiteral("neg"),
        reqstr=82,
        levelreq=50,
    ),
    "OVERSEER_SKULL": _Metadata(
        code=CodeLiteral("ned"),
        reqstr=91,
        levelreq=49,
    ),
    "SUCCUBUS_SKULL": _Metadata(
        code=CodeLiteral("nee"),
        reqstr=95,
        levelreq=60,
    ),
    "BLOODLORD_SKULL": _Metadata(
        code=CodeLiteral("nef"),
        reqstr=106,
        levelreq=65,
    ),
    "BONEWEAVE_RAR": _Metadata(
        code=CodeLiteral("rar"),
        reqstr=158,
        levelreq=47,
    ),
    "TROLL_BELT_RBE": _Metadata(
        code=CodeLiteral("rbe"),
        reqstr=151,
        levelreq=62,
    ),
}


class Armor(Enum):
    """PD2 armor categories."""

    CAP = CodeLiteral("cap")  # Cap
    SKULL_CAP = CodeLiteral("skp")  # Skull Cap
    HELM = CodeLiteral("hlm")  # Helm
    FULL_HELM = CodeLiteral("fhl")  # Full Helm
    GREAT_HELM = CodeLiteral("ghm")  # Great Helm
    CROWN = CodeLiteral("crn")  # Crown
    MASK = CodeLiteral("msk")  # Mask
    QUILTED_ARMOR = CodeLiteral("qui")  # Quilted Armor
    LEATHER_ARMOR = CodeLiteral("lea")  # Leather Armor
    HARD_LEATHER_ARMOR = CodeLiteral("hla")  # Hard Leather Armor
    STUDDED_LEATHER = CodeLiteral("stu")  # Studded Leather
    RING_MAIL = CodeLiteral("rng")  # Ring Mail
    SCALE_MAIL = CodeLiteral("scl")  # Scale Mail
    CHAIN_MAIL = CodeLiteral("chn")  # Chain Mail
    BREAST_PLATE = CodeLiteral("brs")  # Breast Plate
    SPLINT_MAIL = CodeLiteral("spl")  # Splint Mail
    PLATE_MAIL = CodeLiteral("plt")  # Plate Mail
    FIELD_PLATE = CodeLiteral("fld")  # Field Plate
    GOTHIC_PLATE = CodeLiteral("gth")  # Gothic Plate
    FULL_PLATE_MAIL = CodeLiteral("ful")  # Full Plate Mail
    ANCIENT_ARMOR = CodeLiteral("aar")  # Ancient Armor
    LIGHT_PLATE = CodeLiteral("ltp")  # Light Plate
    BUCKLER = CodeLiteral("buc")  # Buckler
    SMALL_SHIELD = CodeLiteral("sml")  # Small Shield
    LARGE_SHIELD = CodeLiteral("lrg")  # Large Shield
    KITE_SHIELD = CodeLiteral("kit")  # Kite Shield
    TOWER_SHIELD = CodeLiteral("tow")  # Tower Shield
    GOTHIC_SHIELD = CodeLiteral("gts")  # Gothic Shield
    LEATHER_GLOVES = CodeLiteral("lgl")  # Leather Gloves
    HEAVY_GLOVES = CodeLiteral("vgl")  # Heavy Gloves
    CHAIN_GLOVES = CodeLiteral("mgl")  # Chain Gloves
    LIGHT_GAUNTLETS = CodeLiteral("tgl")  # Light Gauntlets
    GAUNTLETS = CodeLiteral("hgl")  # Gauntlets
    BOOTS = CodeLiteral("lbt")  # Boots
    HEAVY_BOOTS = CodeLiteral("vbt")  # Heavy Boots
    CHAIN_BOOTS = CodeLiteral("mbt")  # Chain Boots
    LIGHT_PLATED_BOOTS = CodeLiteral("tbt")  # Light Plated Boots
    GREAVES = CodeLiteral("hbt")  # Greaves
    SASH = CodeLiteral("lbl")  # Sash
    LIGHT_BELT = CodeLiteral("vbl")  # Light Belt
    BELT = CodeLiteral("mbl")  # Belt
    HEAVY_BELT = CodeLiteral("tbl")  # Heavy Belt
    PLATED_BELT = CodeLiteral("hbl")  # Plated Belt
    BONE_HELM = CodeLiteral("bhm")  # Bone Helm
    BONE_SHIELD = CodeLiteral("bsh")  # Bone Shield
    SPIKED_SHIELD = CodeLiteral("spk")  # Spiked Shield
    WAR_HAT = CodeLiteral("xap")  # War Hat
    SALLET = CodeLiteral("xkp")  # Sallet
    CASQUE = CodeLiteral("xlm")  # Casque
    BASINET = CodeLiteral("xhl")  # Basinet
    WINGED_HELM = CodeLiteral("xhm")  # Winged Helm
    GRAND_CROWN = CodeLiteral("xrn")  # Grand Crown
    DEATH_MASK = CodeLiteral("xsk")  # Death Mask
    GHOST_ARMOR = CodeLiteral("xui")  # Ghost Armor
    SERPENTSKIN_ARMOR = CodeLiteral("xea")  # Serpentskin Armor
    DEMONHIDE_ARMOR = CodeLiteral("xla")  # Demonhide Armor
    TRELLISED_ARMOR = CodeLiteral("xtu")  # Trellised Armor
    LINKED_MAIL = CodeLiteral("xng")  # Linked Mail
    TIGULATED_MAIL = CodeLiteral("xcl")  # Tigulated Mail
    MESH_ARMOR = CodeLiteral("xhn")  # Mesh Armor
    CUIRASS = CodeLiteral("xrs")  # Cuirass
    RUSSET_ARMOR = CodeLiteral("xpl")  # Russet Armor
    TEMPLAR_COAT = CodeLiteral("xlt")  # Templar Coat
    SHARKTOOTH_ARMOR = CodeLiteral("xld")  # Sharktooth Armor
    EMBOSSED_PLATE = CodeLiteral("xth")  # Embossed Plate
    CHAOS_ARMOR = CodeLiteral("xul")  # Chaos Armor
    ORNATE_PLATE = CodeLiteral("xar")  # Ornate Plate
    MAGE_PLATE = CodeLiteral("xtp")  # Mage Plate
    DEFENDER = CodeLiteral("xuc")  # Defender
    ROUND_SHIELD = CodeLiteral("xml")  # Round Shield
    SCUTUM = CodeLiteral("xrg")  # Scutum
    DRAGON_SHIELD = CodeLiteral("xit")  # Dragon Shield
    PAVISE = CodeLiteral("xow")  # Pavise
    ANCIENT_SHIELD = CodeLiteral("xts")  # Ancient Shield
    DEMONHIDE_GLOVES = CodeLiteral("xlg")  # Demonhide Gloves
    SHARKSKIN_GLOVES = CodeLiteral("xvg")  # Sharkskin Gloves
    HEAVY_BRACERS = CodeLiteral("xmg")  # Heavy Bracers
    BATTLE_GAUNTLETS = CodeLiteral("xtg")  # Battle Gauntlets
    WAR_GAUNTLETS = CodeLiteral("xhg")  # War Gauntlets
    DEMONHIDE_BOOTS = CodeLiteral("xlb")  # Demonhide Boots
    SHARKSKIN_BOOTS = CodeLiteral("xvb")  # Sharkskin Boots
    MESH_BOOTS = CodeLiteral("xmb")  # Mesh Boots
    BATTLE_BOOTS = CodeLiteral("xtb")  # Battle Boots
    WAR_BOOTS = CodeLiteral("xhb")  # War Boots
    DEMONHIDE_SASH = CodeLiteral("zlb")  # Demonhide Sash
    SHARKSKIN_BELT = CodeLiteral("zvb")  # Sharkskin Belt
    MESH_BELT = CodeLiteral("zmb")  # Mesh Belt
    BATTLE_BELT = CodeLiteral("ztb")  # Battle Belt
    WAR_BELT = CodeLiteral("zhb")  # War Belt
    GRIM_HELM = CodeLiteral("xh9")  # Grim Helm
    GRIM_SHIELD = CodeLiteral("xsh")  # Grim Shield
    BARBED_SHIELD = CodeLiteral("xpk")  # Barbed Shield
    WOLF_HEAD = CodeLiteral("dr1")  # Wolf Head
    HAWK_HELM = CodeLiteral("dr2")  # Hawk Helm
    ANTLERS = CodeLiteral("dr3")  # Antlers
    FALCON_MASK = CodeLiteral("dr4")  # Falcon Mask
    SPIRIT_MASK = CodeLiteral("dr5")  # Spirit Mask
    JAWBONE_CAP = CodeLiteral("ba1")  # Jawbone Cap
    FANGED_HELM = CodeLiteral("ba2")  # Fanged Helm
    HORNED_HELM = CodeLiteral("ba3")  # Horned Helm
    ASSAULT_HELMET = CodeLiteral("ba4")  # Assault Helmet
    AVENGER_GUARD = CodeLiteral("ba5")  # Avenger Guard
    TARGE = CodeLiteral("pa1")  # Targe
    RONDACHE = CodeLiteral("pa2")  # Rondache
    HERALDIC_SHIELD = CodeLiteral("pa3")  # Heraldic Shield
    AERIN_SHIELD = CodeLiteral("pa4")  # Aerin Shield
    CROWN_SHIELD = CodeLiteral("pa5")  # Crown Shield
    PRESERVED_HEAD = CodeLiteral("ne1")  # Preserved Head
    ZOMBIE_HEAD = CodeLiteral("ne2")  # Zombie Head
    UNRAVELLER_HEAD = CodeLiteral("ne3")  # Unraveller Head
    GARGOYLE_HEAD = CodeLiteral("ne4")  # Gargoyle Head
    DEMON_HEAD = CodeLiteral("ne5")  # Demon Head
    CIRCLET = CodeLiteral("ci0")  # Circlet
    CORONET = CodeLiteral("ci1")  # Coronet
    TIARA = CodeLiteral("ci2")  # Tiara
    DIADEM = CodeLiteral("ci3")  # Diadem
    SHAKO = CodeLiteral("uap")  # Shako
    HYDRASKULL = CodeLiteral("ukp")  # Hydraskull
    ARMET = CodeLiteral("ulm")  # Armet
    GIANT_CONCH = CodeLiteral("uhl")  # Giant Conch
    SPIRED_HELM = CodeLiteral("uhm")  # Spired Helm
    CORONA = CodeLiteral("urn")  # Corona
    DEMONHEAD = CodeLiteral("usk")  # Demonhead
    DUSK_SHROUD = CodeLiteral("uui")  # Dusk Shroud
    WYRMHIDE = CodeLiteral("uea")  # Wyrmhide
    SCARAB_HUSK = CodeLiteral("ula")  # Scarab Husk
    WIRE_FLEECE = CodeLiteral("utu")  # Wire Fleece
    DIAMOND_MAIL = CodeLiteral("ung")  # Diamond Mail
    LORICATED_MAIL = CodeLiteral("ucl")  # Loricated Mail
    BONEWEAVE = CodeLiteral("uhn")  # Boneweave
    GREAT_HAUBERK = CodeLiteral("urs")  # Great Hauberk
    BALROG_SKIN = CodeLiteral("upl")  # Balrog Skin
    HELLFORGE_PLATE = CodeLiteral("ult")  # Hellforge Plate
    KRAKEN_SHELL = CodeLiteral("uld")  # Kraken Shell
    LACQUERED_PLATE = CodeLiteral("uth")  # Lacquered Plate
    SHADOW_PLATE = CodeLiteral("uul")  # Shadow Plate
    SACRED_ARMOR = CodeLiteral("uar")  # Sacred Armor
    ARCHON_PLATE = CodeLiteral("utp")  # Archon Plate
    HEATER = CodeLiteral("uuc")  # Heater
    LUNA = CodeLiteral("uml")  # Luna
    HYPERION = CodeLiteral("urg")  # Hyperion
    MONARCH = CodeLiteral("uit")  # Monarch
    AEGIS = CodeLiteral("uow")  # Aegis
    WARD = CodeLiteral("uts")  # Ward
    BRAMBLE_MITTS = CodeLiteral("ulg")  # Bramble Mitts
    VAMPIREBONE_GLOVES = CodeLiteral("uvg")  # Vampirebone Gloves
    VAMBRACES = CodeLiteral("umg")  # Vambraces
    CRUSADER_GAUNTLETS = CodeLiteral("utg")  # Crusader Gauntlets
    OGRE_GAUNTLETS = CodeLiteral("uhg")  # Ogre Gauntlets
    WYRMHIDE_BOOTS = CodeLiteral("ulb")  # Wyrmhide Boots
    SCARABSHELL_BOOTS = CodeLiteral("uvb")  # Scarabshell Boots
    BONEWEAVE_BOOTS = CodeLiteral("umb")  # Boneweave Boots
    MIRRORED_BOOTS = CodeLiteral("utb")  # Mirrored Boots
    MYRMIDON_GREAVES = CodeLiteral("uhb")  # Myrmidon Greaves
    SPIDERWEB_SASH = CodeLiteral("ulc")  # Spiderweb Sash
    VAMPIREFANG_BELT = CodeLiteral("uvc")  # Vampirefang Belt
    MITHRIL_COIL = CodeLiteral("umc")  # Mithril Coil
    TROLL_BELT = CodeLiteral("utc")  # Troll Belt
    COLOSSUS_GIRDLE = CodeLiteral("uhc")  # Colossus Girdle
    BONE_VISAGE = CodeLiteral("uh9")  # Bone Visage
    TROLL_NEST = CodeLiteral("ush")  # Troll Nest
    BLADE_BARRIER = CodeLiteral("upk")  # Blade Barrier
    ALPHA_HELM = CodeLiteral("dr6")  # Alpha Helm
    GRIFFON_HEADDRESS = CodeLiteral("dr7")  # Griffon Headdress
    HUNTERS_GUISE = CodeLiteral("dr8")  # Hunter's Guise
    SACRED_FEATHERS = CodeLiteral("dr9")  # Sacred Feathers
    TOTEMIC_MASK = CodeLiteral("dra")  # Totemic Mask
    JAWBONE_VISOR = CodeLiteral("ba6")  # Jawbone Visor
    LION_HELM = CodeLiteral("ba7")  # Lion Helm
    RAGE_MASK = CodeLiteral("ba8")  # Rage Mask
    SAVAGE_HELMET = CodeLiteral("ba9")  # Savage Helmet
    SLAYER_GUARD = CodeLiteral("baa")  # Slayer Guard
    AKARAN_TARGE = CodeLiteral("pa6")  # Akaran Targe
    AKARAN_RONDACHE = CodeLiteral("pa7")  # Akaran Rondache
    PROTECTOR_SHIELD = CodeLiteral("pa8")  # Protector Shield
    GILDED_SHIELD = CodeLiteral("pa9")  # Gilded Shield
    ROYAL_SHIELD = CodeLiteral("paa")  # Royal Shield
    MUMMIFIED_TROPHY = CodeLiteral("ne6")  # Mummified Trophy
    FETISH_TROPHY = CodeLiteral("ne7")  # Fetish Trophy
    SEXTON_TROPHY = CodeLiteral("ne8")  # Sexton Trophy
    CANTOR_TROPHY = CodeLiteral("ne9")  # Cantor Trophy
    HIEROPHANT_TROPHY = CodeLiteral("nea")  # Hierophant Trophy
    BLOOD_SPIRIT = CodeLiteral("drb")  # Blood Spirit
    SUN_SPIRIT = CodeLiteral("drc")  # Sun Spirit
    EARTH_SPIRIT = CodeLiteral("drd")  # Earth Spirit
    SKY_SPIRIT = CodeLiteral("dre")  # Sky Spirit
    DREAM_SPIRIT = CodeLiteral("drf")  # Dream Spirit
    CARNAGE_HELM = CodeLiteral("bab")  # Carnage Helm
    FURY_VISOR = CodeLiteral("bac")  # Fury Visor
    DESTROYER_HELM = CodeLiteral("bad")  # Destroyer Helm
    CONQUEROR_CROWN = CodeLiteral("bae")  # Conqueror Crown
    GUARDIAN_CROWN = CodeLiteral("baf")  # Guardian Crown
    SACRED_TARGE = CodeLiteral("pab")  # Sacred Targe
    SACRED_RONDACHE = CodeLiteral("pac")  # Sacred Rondache
    KURAST_SHIELD = CodeLiteral("pad")  # Kurast Shield
    ZAKARUM_SHIELD = CodeLiteral("pae")  # Zakarum Shield
    VORTEX_SHIELD = CodeLiteral("paf")  # Vortex Shield
    MINION_SKULL = CodeLiteral("neb")  # Minion Skull
    HELLSPAWN_SKULL = CodeLiteral("neg")  # Hellspawn Skull
    OVERSEER_SKULL = CodeLiteral("ned")  # Overseer Skull
    SUCCUBUS_SKULL = CodeLiteral("nee")  # Succubus Skull
    BLOODLORD_SKULL = CodeLiteral("nef")  # Bloodlord Skull
    BONEWEAVE_RAR = CodeLiteral("rar")  # Boneweave rar
    TROLL_BELT_RBE = CodeLiteral("rbe")  # Troll Belt rbe

    @property
    def code(self) -> CodeLiteral:
        return _METADATA[self.name].code

    @property
    def reqstr(self) -> int:
        return _METADATA[self.name].reqstr

    @property
    def levelreq(self) -> int:
        return _METADATA[self.name].levelreq
