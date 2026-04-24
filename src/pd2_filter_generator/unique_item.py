# ruff: noqa: PIE796
"""
Generated UniqueItem enum from PD2 data.

DO NOT EDIT MANUALLY - regenerate with: hatch run ./scripts/generate.py generate
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


@dataclass(frozen=True)
class _Metadata:
    """Item type metadata."""

    ladder: bool  # "ladder"
    code: str  # "code"
    lvl: int  # "lvl"
    lvl_req: int  # "lvl req"


class UniqueItem(Enum):
    """PD2 unique item categories."""

    THE_GNASHER = _Metadata(
        ladder=False,
        code="hax",
        lvl=7,
        lvl_req=5,
    )
    DEATHSPADE = _Metadata(
        ladder=False,
        code="axe",
        lvl=12,
        lvl_req=9,
    )
    BLADEBONE = _Metadata(
        ladder=False,
        code="2ax",
        lvl=20,
        lvl_req=15,
    )
    SKULL_SPLITTER = _Metadata(
        ladder=False,
        code="mpi",
        lvl=28,
        lvl_req=21,
    )
    RAKESCAR = _Metadata(
        ladder=False,
        code="wax",
        lvl=36,
        lvl_req=27,
    )
    AXE_OF_FECHMAR = _Metadata(
        ladder=False,
        code="lax",
        lvl=11,
        lvl_req=8,
    )
    GORESHOVEL = _Metadata(
        ladder=False,
        code="bax",
        lvl=19,
        lvl_req=14,
    )
    THE_CHIEFTAIN = _Metadata(
        ladder=False,
        code="btx",
        lvl=26,
        lvl_req=19,
    )
    BRAINHEW = _Metadata(
        ladder=False,
        code="gax",
        lvl=34,
        lvl_req=25,
    )
    HUMONGOUS = _Metadata(
        ladder=False,
        code="gix",
        lvl=39,
        lvl_req=29,
    )
    TORCH_OF_IRO = _Metadata(
        ladder=False,
        code="wnd",
        lvl=7,
        lvl_req=5,
    )
    MAELSTROM = _Metadata(
        ladder=False,
        code="ywn",
        lvl=19,
        lvl_req=14,
    )
    GRAVENSPINE = _Metadata(
        ladder=False,
        code="bwn",
        lvl=27,
        lvl_req=20,
    )
    UMES_LAMENT = _Metadata(
        ladder=False,
        code="gwn",
        lvl=38,
        lvl_req=28,
    )
    FELLOAK = _Metadata(
        ladder=False,
        code="clb",
        lvl=4,
        lvl_req=3,
    )
    KNELL_STRIKER = _Metadata(
        ladder=False,
        code="scp",
        lvl=7,
        lvl_req=5,
    )
    RUSTHANDLE = _Metadata(
        ladder=False,
        code="gsc",
        lvl=23,
        lvl_req=17,
    )
    STORMEYE = _Metadata(
        ladder=False,
        code="wsp",
        lvl=31,
        lvl_req=23,
    )
    STOUTNAIL = _Metadata(
        ladder=False,
        code="spc",
        lvl=7,
        lvl_req=5,
    )
    CRUSHFLANGE = _Metadata(
        ladder=False,
        code="mac",
        lvl=12,
        lvl_req=9,
    )
    BLOODRISE = _Metadata(
        ladder=False,
        code="mst",
        lvl=20,
        lvl_req=15,
    )
    THE_GENERALS_TAN_DO_LI_GA = _Metadata(
        ladder=False,
        code="fla",
        lvl=28,
        lvl_req=21,
    )
    IRONSTONE = _Metadata(
        ladder=False,
        code="whm",
        lvl=36,
        lvl_req=27,
    )
    BONESNAP = _Metadata(
        ladder=False,
        code="mau",
        lvl=32,
        lvl_req=24,
    )
    STEELDRIVER = _Metadata(
        ladder=False,
        code="gma",
        lvl=39,
        lvl_req=29,
    )
    RIXOTS_KEEN = _Metadata(
        ladder=False,
        code="ssd",
        lvl=3,
        lvl_req=2,
    )
    BLOOD_CRESCENT = _Metadata(
        ladder=False,
        code="scm",
        lvl=10,
        lvl_req=7,
    )
    SKEWER_OF_KRINTIZ = _Metadata(
        ladder=False,
        code="sbr",
        lvl=14,
        lvl_req=10,
    )
    GLEAMSCYTHE = _Metadata(
        ladder=False,
        code="flc",
        lvl=18,
        lvl_req=13,
    )
    GRISWOLDS_EDGE = _Metadata(
        ladder=False,
        code="bsd",
        lvl=23,
        lvl_req=17,
    )
    HELLPLAGUE = _Metadata(
        ladder=False,
        code="lsd",
        lvl=30,
        lvl_req=22,
    )
    CULWENS_POINT = _Metadata(
        ladder=False,
        code="wsd",
        lvl=39,
        lvl_req=29,
    )
    SHADOWFANG = _Metadata(
        ladder=False,
        code="2hs",
        lvl=16,
        lvl_req=12,
    )
    SOULFLAY = _Metadata(
        ladder=False,
        code="clm",
        lvl=26,
        lvl_req=19,
    )
    KINEMILS_AWL = _Metadata(
        ladder=False,
        code="gis",
        lvl=31,
        lvl_req=23,
    )
    BLACKTONGUE = _Metadata(
        ladder=False,
        code="bsw",
        lvl=35,
        lvl_req=26,
    )
    RIPSAW = _Metadata(
        ladder=False,
        code="flb",
        lvl=35,
        lvl_req=26,
    )
    THE_PATRIARCH = _Metadata(
        ladder=False,
        code="gsd",
        lvl=39,
        lvl_req=29,
    )
    GULL = _Metadata(
        ladder=False,
        code="dgr",
        lvl=6,
        lvl_req=4,
    )
    THE_DIGGLER = _Metadata(
        ladder=False,
        code="dir",
        lvl=15,
        lvl_req=11,
    )
    THE_JADE_TAN_DO = _Metadata(
        ladder=False,
        code="kri",
        lvl=26,
        lvl_req=19,
    )
    SPECTRAL_SHARD = _Metadata(
        ladder=False,
        code="bld",
        lvl=34,
        lvl_req=25,
    )
    THE_DRAGON_CHANG = _Metadata(
        ladder=False,
        code="spr",
        lvl=11,
        lvl_req=8,
    )
    RAZORTINE = _Metadata(
        ladder=False,
        code="tri",
        lvl=16,
        lvl_req=12,
    )
    BLOODTHIEF = _Metadata(
        ladder=False,
        code="brn",
        lvl=23,
        lvl_req=17,
    )
    LANCE_OF_YAGGAI = _Metadata(
        ladder=False,
        code="spt",
        lvl=30,
        lvl_req=22,
    )
    THE_TANNR_GOREROD = _Metadata(
        ladder=False,
        code="pik",
        lvl=36,
        lvl_req=27,
    )
    DIMOAKS_HEW = _Metadata(
        ladder=False,
        code="bar",
        lvl=11,
        lvl_req=8,
    )
    STEELGOAD = _Metadata(
        ladder=False,
        code="vou",
        lvl=19,
        lvl_req=14,
    )
    SOUL_HARVEST = _Metadata(
        ladder=False,
        code="scy",
        lvl=26,
        lvl_req=19,
    )
    THE_BATTLEBRANCH = _Metadata(
        ladder=False,
        code="pax",
        lvl=34,
        lvl_req=25,
    )
    WOESTAVE = _Metadata(
        ladder=False,
        code="hal",
        lvl=38,
        lvl_req=28,
    )
    THE_GRIM_REAPER = _Metadata(
        ladder=False,
        code="wsc",
        lvl=39,
        lvl_req=29,
    )
    BANE_ASH = _Metadata(
        ladder=False,
        code="sst",
        lvl=7,
        lvl_req=5,
    )
    SERPENT_LORD = _Metadata(
        ladder=False,
        code="lst",
        lvl=12,
        lvl_req=9,
    )
    SPIRE_OF_LAZARUS = _Metadata(
        ladder=False,
        code="cst",
        lvl=24,
        lvl_req=18,
    )
    THE_SALAMANDER = _Metadata(
        ladder=False,
        code="bst",
        lvl=28,
        lvl_req=21,
    )
    THE_IRON_JANG_BONG = _Metadata(
        ladder=False,
        code="wst",
        lvl=38,
        lvl_req=28,
    )
    PLUCKEYE = _Metadata(
        ladder=False,
        code="sbw",
        lvl=10,
        lvl_req=7,
    )
    WITHERSTRING = _Metadata(
        ladder=False,
        code="hbw",
        lvl=18,
        lvl_req=13,
    )
    RAVEN_CLAW = _Metadata(
        ladder=False,
        code="lbw",
        lvl=20,
        lvl_req=15,
    )
    ROGUES_BOW = _Metadata(
        ladder=False,
        code="cbw",
        lvl=27,
        lvl_req=20,
    )
    STORMSTRIKE = _Metadata(
        ladder=False,
        code="sbb",
        lvl=34,
        lvl_req=25,
    )
    WIZENDRAW = _Metadata(
        ladder=False,
        code="lbb",
        lvl=35,
        lvl_req=26,
    )
    HELLCLAP = _Metadata(
        ladder=False,
        code="swb",
        lvl=36,
        lvl_req=27,
    )
    BLASTBARK = _Metadata(
        ladder=False,
        code="lwb",
        lvl=38,
        lvl_req=28,
    )
    LEADCROW = _Metadata(
        ladder=False,
        code="lxb",
        lvl=12,
        lvl_req=9,
    )
    ICHORSTING = _Metadata(
        ladder=False,
        code="mxb",
        lvl=24,
        lvl_req=18,
    )
    HELLCAST = _Metadata(
        ladder=False,
        code="hxb",
        lvl=36,
        lvl_req=27,
    )
    DOOMSLINGER = _Metadata(
        ladder=False,
        code="rxb",
        lvl=38,
        lvl_req=28,
    )
    BIGGINS_BONNET = _Metadata(
        ladder=False,
        code="cap",
        lvl=4,
        lvl_req=3,
    )
    TARNHELM = _Metadata(
        ladder=False,
        code="skp",
        lvl=20,
        lvl_req=15,
    )
    COIF_OF_GLORY = _Metadata(
        ladder=False,
        code="hlm",
        lvl=19,
        lvl_req=14,
    )
    DUSKDEEP = _Metadata(
        ladder=False,
        code="fhl",
        lvl=23,
        lvl_req=17,
    )
    WORMSKULL = _Metadata(
        ladder=False,
        code="bhm",
        lvl=28,
        lvl_req=21,
    )
    HOWLTUSK = _Metadata(
        ladder=False,
        code="ghm",
        lvl=34,
        lvl_req=25,
    )
    UNDEAD_CROWN = _Metadata(
        ladder=False,
        code="crn",
        lvl=39,
        lvl_req=29,
    )
    THE_FACE_OF_HORROR = _Metadata(
        ladder=False,
        code="msk",
        lvl=27,
        lvl_req=20,
    )
    GREYFORM = _Metadata(
        ladder=False,
        code="qui",
        lvl=10,
        lvl_req=7,
    )
    BLINKBATS_FORM = _Metadata(
        ladder=False,
        code="lea",
        lvl=16,
        lvl_req=12,
    )
    THE_CENTURION = _Metadata(
        ladder=False,
        code="hla",
        lvl=19,
        lvl_req=14,
    )
    TWITCHTHROE = _Metadata(
        ladder=False,
        code="stu",
        lvl=22,
        lvl_req=16,
    )
    DARKGLOW = _Metadata(
        ladder=False,
        code="rng",
        lvl=19,
        lvl_req=14,
    )
    HAWKMAIL = _Metadata(
        ladder=False,
        code="scl",
        lvl=20,
        lvl_req=15,
    )
    SPARKING_MAIL = _Metadata(
        ladder=False,
        code="chn",
        lvl=23,
        lvl_req=17,
    )
    VENOM_WARD = _Metadata(
        ladder=False,
        code="brs",
        lvl=27,
        lvl_req=20,
    )
    ICEBLINK = _Metadata(
        ladder=False,
        code="spl",
        lvl=30,
        lvl_req=22,
    )
    BONEFLESH = _Metadata(
        ladder=False,
        code="plt",
        lvl=35,
        lvl_req=26,
    )
    ROCKFLEECE = _Metadata(
        ladder=False,
        code="fld",
        lvl=38,
        lvl_req=28,
    )
    RATTLECAGE = _Metadata(
        ladder=False,
        code="gth",
        lvl=39,
        lvl_req=29,
    )
    GOLDSKIN = _Metadata(
        ladder=False,
        code="ful",
        lvl=38,
        lvl_req=28,
    )
    SILKS_OF_THE_VICTOR = _Metadata(
        ladder=False,
        code="aar",
        lvl=38,
        lvl_req=28,
    )
    HEAVENLY_GARB = _Metadata(
        ladder=False,
        code="ltp",
        lvl=39,
        lvl_req=29,
    )
    PELTA_LUNATA = _Metadata(
        ladder=False,
        code="buc",
        lvl=3,
        lvl_req=2,
    )
    UMBRAL_DISK = _Metadata(
        ladder=False,
        code="sml",
        lvl=12,
        lvl_req=9,
    )
    STORMGUILD = _Metadata(
        ladder=False,
        code="lrg",
        lvl=18,
        lvl_req=13,
    )
    WALL_OF_THE_EYELESS = _Metadata(
        ladder=False,
        code="bsh",
        lvl=27,
        lvl_req=20,
    )
    SWORDBACK_HOLD = _Metadata(
        ladder=False,
        code="spk",
        lvl=20,
        lvl_req=15,
    )
    STEELCLASH = _Metadata(
        ladder=False,
        code="kit",
        lvl=23,
        lvl_req=17,
    )
    BVERRIT_KEEP = _Metadata(
        ladder=False,
        code="tow",
        lvl=26,
        lvl_req=19,
    )
    THE_WARD = _Metadata(
        ladder=False,
        code="gts",
        lvl=35,
        lvl_req=26,
    )
    THE_HAND_OF_BROC = _Metadata(
        ladder=False,
        code="lgl",
        lvl=7,
        lvl_req=5,
    )
    BLOODFIST = _Metadata(
        ladder=False,
        code="vgl",
        lvl=12,
        lvl_req=9,
    )
    CHANCE_GUARDS = _Metadata(
        ladder=False,
        code="mgl",
        lvl=20,
        lvl_req=15,
    )
    MAGEFIST = _Metadata(
        ladder=False,
        code="tgl",
        lvl=31,
        lvl_req=23,
    )
    FROSTBURN = _Metadata(
        ladder=False,
        code="hgl",
        lvl=39,
        lvl_req=29,
    )
    HOTSPUR = _Metadata(
        ladder=False,
        code="lbt",
        lvl=7,
        lvl_req=5,
    )
    GOREFOOT = _Metadata(
        ladder=False,
        code="vbt",
        lvl=12,
        lvl_req=12,
    )
    TREADS_OF_CTHON = _Metadata(
        ladder=False,
        code="mbt",
        lvl=20,
        lvl_req=15,
    )
    GOBLIN_TOE = _Metadata(
        ladder=False,
        code="tbt",
        lvl=30,
        lvl_req=22,
    )
    TEARHAUNCH = _Metadata(
        ladder=False,
        code="hbt",
        lvl=39,
        lvl_req=29,
    )
    LENYMO = _Metadata(
        ladder=False,
        code="lbl",
        lvl=10,
        lvl_req=7,
    )
    SNAKECORD = _Metadata(
        ladder=False,
        code="vbl",
        lvl=16,
        lvl_req=12,
    )
    NIGHTSMOKE = _Metadata(
        ladder=False,
        code="mbl",
        lvl=27,
        lvl_req=20,
    )
    GOLDWRAP = _Metadata(
        ladder=False,
        code="tbl",
        lvl=36,
        lvl_req=27,
    )
    BLADEBUCKLE = _Metadata(
        ladder=False,
        code="hbl",
        lvl=39,
        lvl_req=39,
    )
    NOKOZAN_RELIC = _Metadata(
        ladder=False,
        code="amu",
        lvl=14,
        lvl_req=10,
    )
    THE_EYE_OF_ETLICH = _Metadata(
        ladder=False,
        code="amu",
        lvl=20,
        lvl_req=15,
    )
    THE_MAHIM_OAK_CURIO = _Metadata(
        ladder=False,
        code="amu",
        lvl=34,
        lvl_req=25,
    )
    NAGELRING = _Metadata(
        ladder=False,
        code="rin",
        lvl=10,
        lvl_req=7,
    )
    MANALD_HEAL = _Metadata(
        ladder=False,
        code="rin",
        lvl=20,
        lvl_req=15,
    )
    THE_STONE_OF_JORDAN = _Metadata(
        ladder=False,
        code="rin",
        lvl=39,
        lvl_req=29,
    )
    AMULET_OF_THE_VIPER = _Metadata(
        ladder=False,
        code="vip",
        lvl=0,
        lvl_req=0,
    )
    STAFF_OF_KINGS = _Metadata(
        ladder=False,
        code="msf",
        lvl=0,
        lvl_req=0,
    )
    HORADRIC_STAFF = _Metadata(
        ladder=False,
        code="hst",
        lvl=0,
        lvl_req=0,
    )
    HELL_FORGE_HAMMER = _Metadata(
        ladder=False,
        code="hfh",
        lvl=0,
        lvl_req=0,
    )
    KHALIMS_FLAIL = _Metadata(
        ladder=False,
        code="qf1",
        lvl=0,
        lvl_req=0,
    )
    KHALIMS_WILL = _Metadata(
        ladder=False,
        code="qf2",
        lvl=0,
        lvl_req=0,
    )
    COLDKILL = _Metadata(
        ladder=False,
        code="9ha",
        lvl=44,
        lvl_req=36,
    )
    BUTCHERS_PUPIL = _Metadata(
        ladder=False,
        code="9ax",
        lvl=47,
        lvl_req=39,
    )
    ISLESTRIKE = _Metadata(
        ladder=False,
        code="92a",
        lvl=51,
        lvl_req=43,
    )
    POMPEIIS_WRATH = _Metadata(
        ladder=False,
        code="9mp",
        lvl=53,
        lvl_req=45,
    )
    GUARDIAN_NAGA = _Metadata(
        ladder=False,
        code="9wa",
        lvl=56,
        lvl_req=48,
    )
    WARLORDS_TRUST = _Metadata(
        ladder=False,
        code="9la",
        lvl=43,
        lvl_req=35,
    )
    SPELLSTEEL = _Metadata(
        ladder=False,
        code="9ba",
        lvl=47,
        lvl_req=39,
    )
    STORMRIDER = _Metadata(
        ladder=False,
        code="9bt",
        lvl=49,
        lvl_req=41,
    )
    BONESLAYER_BLADE = _Metadata(
        ladder=False,
        code="9ga",
        lvl=50,
        lvl_req=42,
    )
    THE_MINOTAUR = _Metadata(
        ladder=False,
        code="9gi",
        lvl=53,
        lvl_req=45,
    )
    SUICIDE_BRANCH = _Metadata(
        ladder=False,
        code="9wn",
        lvl=41,
        lvl_req=33,
    )
    CARIN_SHARD = _Metadata(
        ladder=False,
        code="9yw",
        lvl=43,
        lvl_req=35,
    )
    ARM_OF_KING_LEORIC = _Metadata(
        ladder=False,
        code="9bw",
        lvl=44,
        lvl_req=36,
    )
    BLACKHAND_KEY = _Metadata(
        ladder=False,
        code="9gw",
        lvl=49,
        lvl_req=41,
    )
    DARK_CLAN_CRUSHER = _Metadata(
        ladder=False,
        code="9cl",
        lvl=42,
        lvl_req=34,
    )
    ZAKARUMS_HAND = _Metadata(
        ladder=False,
        code="9sc",
        lvl=45,
        lvl_req=37,
    )
    THE_FETID_SPRINKLER = _Metadata(
        ladder=False,
        code="9qs",
        lvl=46,
        lvl_req=38,
    )
    HAND_OF_BLESSED_LIGHT = _Metadata(
        ladder=False,
        code="9ws",
        lvl=50,
        lvl_req=42,
    )
    FLESHRENDER = _Metadata(
        ladder=False,
        code="9sp",
        lvl=46,
        lvl_req=38,
    )
    SURESHRILL_FROST = _Metadata(
        ladder=False,
        code="9ma",
        lvl=47,
        lvl_req=39,
    )
    MOONFALL = _Metadata(
        ladder=False,
        code="9mt",
        lvl=50,
        lvl_req=42,
    )
    BAEZILS_VORTEX = _Metadata(
        ladder=False,
        code="9fl",
        lvl=53,
        lvl_req=45,
    )
    EARTHSHAKER = _Metadata(
        ladder=False,
        code="9wh",
        lvl=51,
        lvl_req=43,
    )
    BLOODTREE_STUMP = _Metadata(
        ladder=False,
        code="9m9",
        lvl=56,
        lvl_req=48,
    )
    THE_GAVEL_OF_PAIN = _Metadata(
        ladder=False,
        code="9gm",
        lvl=53,
        lvl_req=45,
    )
    BLOODLETTER = _Metadata(
        ladder=False,
        code="9ss",
        lvl=38,
        lvl_req=30,
    )
    COLDSTEEL_EYE = _Metadata(
        ladder=False,
        code="9sm",
        lvl=39,
        lvl_req=31,
    )
    HEXFIRE = _Metadata(
        ladder=False,
        code="9sb",
        lvl=41,
        lvl_req=33,
    )
    BLADE_OF_ALI_BABA = _Metadata(
        ladder=False,
        code="9fc",
        lvl=43,
        lvl_req=35,
    )
    GINTHERS_RIFT = _Metadata(
        ladder=False,
        code="9cr",
        lvl=45,
        lvl_req=37,
    )
    HEADSTRIKER = _Metadata(
        ladder=False,
        code="9bs",
        lvl=47,
        lvl_req=39,
    )
    PLAGUE_BEARER = _Metadata(
        ladder=False,
        code="9ls",
        lvl=49,
        lvl_req=41,
    )
    THE_ATLANTEAN = _Metadata(
        ladder=False,
        code="9wd",
        lvl=50,
        lvl_req=42,
    )
    CRAINTE_VOMIR = _Metadata(
        ladder=False,
        code="92h",
        lvl=50,
        lvl_req=42,
    )
    BING_SZ_WANG = _Metadata(
        ladder=False,
        code="9cm",
        lvl=51,
        lvl_req=43,
    )
    THE_VILE_HUSK = _Metadata(
        ladder=False,
        code="9gs",
        lvl=52,
        lvl_req=44,
    )
    CLOUDCRACK = _Metadata(
        ladder=False,
        code="9b9",
        lvl=53,
        lvl_req=45,
    )
    TODESFAELLE_FLAMME = _Metadata(
        ladder=False,
        code="9fb",
        lvl=54,
        lvl_req=46,
    )
    SWORDGUARD = _Metadata(
        ladder=False,
        code="9gd",
        lvl=55,
        lvl_req=48,
    )
    SPINERIPPER = _Metadata(
        ladder=False,
        code="9dg",
        lvl=40,
        lvl_req=32,
    )
    HEART_CARVER = _Metadata(
        ladder=False,
        code="9di",
        lvl=44,
        lvl_req=36,
    )
    BLACKBOGS_SHARP = _Metadata(
        ladder=False,
        code="9kr",
        lvl=46,
        lvl_req=38,
    )
    STORMSPIKE = _Metadata(
        ladder=False,
        code="9bl",
        lvl=49,
        lvl_req=41,
    )
    THE_IMPALER = _Metadata(
        ladder=False,
        code="9sr",
        lvl=39,
        lvl_req=31,
    )
    KELPIE_SNARE = _Metadata(
        ladder=False,
        code="9tr",
        lvl=41,
        lvl_req=33,
    )
    SOULFEAST_TINE = _Metadata(
        ladder=False,
        code="9br",
        lvl=43,
        lvl_req=35,
    )
    HONE_SUNDAN = _Metadata(
        ladder=False,
        code="9st",
        lvl=45,
        lvl_req=37,
    )
    SPIRE_OF_HONOR = _Metadata(
        ladder=False,
        code="9p9",
        lvl=47,
        lvl_req=39,
    )
    THE_MEAT_SCRAPER = _Metadata(
        ladder=False,
        code="9b7",
        lvl=49,
        lvl_req=41,
    )
    BLACKLEACH_BLADE = _Metadata(
        ladder=False,
        code="9vo",
        lvl=50,
        lvl_req=42,
    )
    ATHENAS_WRATH = _Metadata(
        ladder=False,
        code="9s8",
        lvl=50,
        lvl_req=42,
    )
    PIERRE_TOMBALE_COUANT = _Metadata(
        ladder=False,
        code="9pa",
        lvl=51,
        lvl_req=43,
    )
    HUSOLDAL_EVO = _Metadata(
        ladder=False,
        code="9h9",
        lvl=52,
        lvl_req=44,
    )
    GRIMS_BURNING_DEAD = _Metadata(
        ladder=False,
        code="9wc",
        lvl=52,
        lvl_req=45,
    )
    RAZORSWITCH = _Metadata(
        ladder=False,
        code="8ss",
        lvl=36,
        lvl_req=28,
    )
    RIBCRACKER = _Metadata(
        ladder=False,
        code="8ls",
        lvl=39,
        lvl_req=31,
    )
    CHROMATIC_IRE = _Metadata(
        ladder=False,
        code="8cs",
        lvl=43,
        lvl_req=35,
    )
    WARPSPEAR = _Metadata(
        ladder=False,
        code="8bs",
        lvl=47,
        lvl_req=39,
    )
    SKULL_COLLECTOR = _Metadata(
        ladder=False,
        code="8ws",
        lvl=49,
        lvl_req=41,
    )
    SKYSTRIKE = _Metadata(
        ladder=False,
        code="8sb",
        lvl=36,
        lvl_req=28,
    )
    RIPHOOK = _Metadata(
        ladder=False,
        code="8hb",
        lvl=39,
        lvl_req=31,
    )
    KUKO_SHAKAKU = _Metadata(
        ladder=False,
        code="8lb",
        lvl=41,
        lvl_req=33,
    )
    ENDLESSHAIL = _Metadata(
        ladder=False,
        code="8cb",
        lvl=44,
        lvl_req=36,
    )
    WITCHWILD_STRING = _Metadata(
        ladder=False,
        code="8s8",
        lvl=47,
        lvl_req=39,
    )
    CLIFFKILLER = _Metadata(
        ladder=False,
        code="8l8",
        lvl=49,
        lvl_req=41,
    )
    MAGEWRATH = _Metadata(
        ladder=False,
        code="8sw",
        lvl=51,
        lvl_req=43,
    )
    GOLDSTRIKE_ARCH = _Metadata(
        ladder=False,
        code="8lw",
        lvl=54,
        lvl_req=46,
    )
    LANGER_BRISER = _Metadata(
        ladder=False,
        code="8lx",
        lvl=40,
        lvl_req=32,
    )
    PUS_SPITTER = _Metadata(
        ladder=False,
        code="8mx",
        lvl=44,
        lvl_req=36,
    )
    BURIZA_DO_KYANON = _Metadata(
        ladder=False,
        code="8hx",
        lvl=59,
        lvl_req=41,
    )
    DEMON_MACHINE = _Metadata(
        ladder=False,
        code="8rx",
        lvl=57,
        lvl_req=49,
    )
    PEASANT_CROWN = _Metadata(
        ladder=False,
        code="xap",
        lvl=36,
        lvl_req=28,
    )
    ROCKSTOPPER = _Metadata(
        ladder=False,
        code="xkp",
        lvl=39,
        lvl_req=31,
    )
    STEALSKULL = _Metadata(
        ladder=False,
        code="xlm",
        lvl=43,
        lvl_req=35,
    )
    DARKSIGHT_HELM = _Metadata(
        ladder=False,
        code="xhl",
        lvl=46,
        lvl_req=38,
    )
    VALKYRIE_WING = _Metadata(
        ladder=False,
        code="xhm",
        lvl=52,
        lvl_req=44,
    )
    CROWN_OF_THIEVES = _Metadata(
        ladder=False,
        code="xrn",
        lvl=57,
        lvl_req=49,
    )
    BLACKHORNS_FACE = _Metadata(
        ladder=False,
        code="xsk",
        lvl=49,
        lvl_req=41,
    )
    VAMPIRE_GAZE = _Metadata(
        ladder=False,
        code="xh9",
        lvl=49,
        lvl_req=41,
    )
    THE_SPIRIT_SHROUD = _Metadata(
        ladder=False,
        code="xui",
        lvl=36,
        lvl_req=28,
    )
    SKIN_OF_THE_VIPERMAGI = _Metadata(
        ladder=False,
        code="xea",
        lvl=37,
        lvl_req=29,
    )
    SKIN_OF_THE_FLAYED_ONE = _Metadata(
        ladder=False,
        code="xla",
        lvl=39,
        lvl_req=31,
    )
    IRON_PELT = _Metadata(
        ladder=False,
        code="xtu",
        lvl=41,
        lvl_req=33,
    )
    SPIRIT_FORGE = _Metadata(
        ladder=False,
        code="xng",
        lvl=43,
        lvl_req=35,
    )
    CROW_CAW = _Metadata(
        ladder=False,
        code="xcl",
        lvl=45,
        lvl_req=37,
    )
    SHAFTSTOP = _Metadata(
        ladder=False,
        code="xhn",
        lvl=46,
        lvl_req=38,
    )
    DURIELS_SHELL = _Metadata(
        ladder=False,
        code="xrs",
        lvl=49,
        lvl_req=41,
    )
    SKULLDERS_IRE = _Metadata(
        ladder=False,
        code="xpl",
        lvl=50,
        lvl_req=42,
    )
    GUARDIAN_ANGEL = _Metadata(
        ladder=False,
        code="xlt",
        lvl=53,
        lvl_req=45,
    )
    TOOTHROW = _Metadata(
        ladder=False,
        code="xld",
        lvl=56,
        lvl_req=48,
    )
    ATMAS_WAIL = _Metadata(
        ladder=False,
        code="xth",
        lvl=59,
        lvl_req=51,
    )
    BLACK_HADES = _Metadata(
        ladder=False,
        code="xul",
        lvl=61,
        lvl_req=53,
    )
    CORPSEMOURN = _Metadata(
        ladder=False,
        code="xar",
        lvl=63,
        lvl_req=55,
    )
    QUE_HEGANS_WISDOM = _Metadata(
        ladder=False,
        code="xtp",
        lvl=59,
        lvl_req=51,
    )
    VISCERATUANT = _Metadata(
        ladder=False,
        code="xuc",
        lvl=36,
        lvl_req=28,
    )
    MOSERS_BLESSED_CIRCLE = _Metadata(
        ladder=False,
        code="xml",
        lvl=39,
        lvl_req=31,
    )
    STORMCHASER = _Metadata(
        ladder=False,
        code="xrg",
        lvl=43,
        lvl_req=35,
    )
    TIAMATS_REBUKE = _Metadata(
        ladder=False,
        code="xit",
        lvl=46,
        lvl_req=38,
    )
    GERKES_SANCTUARY = _Metadata(
        ladder=False,
        code="xow",
        lvl=52,
        lvl_req=44,
    )
    RADAMENTS_SPHERE = _Metadata(
        ladder=False,
        code="xts",
        lvl=58,
        lvl_req=50,
    )
    LIDLESS_WALL = _Metadata(
        ladder=False,
        code="xsh",
        lvl=49,
        lvl_req=41,
    )
    LANCE_GUARD = _Metadata(
        ladder=False,
        code="xpk",
        lvl=43,
        lvl_req=35,
    )
    VENOM_GRIP = _Metadata(
        ladder=False,
        code="xlg",
        lvl=37,
        lvl_req=29,
    )
    GRAVEPALM = _Metadata(
        ladder=False,
        code="xvg",
        lvl=39,
        lvl_req=32,
    )
    GHOULHIDE = _Metadata(
        ladder=False,
        code="xmg",
        lvl=44,
        lvl_req=36,
    )
    LAVA_GOUT = _Metadata(
        ladder=False,
        code="xtg",
        lvl=50,
        lvl_req=42,
    )
    HELLMOUTH = _Metadata(
        ladder=False,
        code="xhg",
        lvl=55,
        lvl_req=47,
    )
    INFERNOSTRIDE = _Metadata(
        ladder=False,
        code="xlb",
        lvl=37,
        lvl_req=29,
    )
    WATERWALK = _Metadata(
        ladder=False,
        code="xvb",
        lvl=40,
        lvl_req=32,
    )
    SILKWEAVE = _Metadata(
        ladder=False,
        code="xmb",
        lvl=44,
        lvl_req=36,
    )
    WAR_TRAVELER = _Metadata(
        ladder=False,
        code="xtb",
        lvl=50,
        lvl_req=42,
    )
    GORE_RIDER = _Metadata(
        ladder=False,
        code="xhb",
        lvl=55,
        lvl_req=47,
    )
    STRING_OF_EARS = _Metadata(
        ladder=False,
        code="zlb",
        lvl=37,
        lvl_req=29,
    )
    RAZORTAIL = _Metadata(
        ladder=False,
        code="zvb",
        lvl=39,
        lvl_req=32,
    )
    GLOOMS_TRAP = _Metadata(
        ladder=False,
        code="zmb",
        lvl=45,
        lvl_req=36,
    )
    SNOWCLASH = _Metadata(
        ladder=False,
        code="ztb",
        lvl=49,
        lvl_req=42,
    )
    THUNDERGODS_VIGOR = _Metadata(
        ladder=False,
        code="zhb",
        lvl=55,
        lvl_req=47,
    )
    HARLEQUIN_CREST = _Metadata(
        ladder=False,
        code="uap",
        lvl=69,
        lvl_req=62,
    )
    VEIL_OF_STEEL = _Metadata(
        ladder=False,
        code="uhm",
        lvl=77,
        lvl_req=73,
    )
    THE_GLADIATORS_BANE = _Metadata(
        ladder=False,
        code="utu",
        lvl=85,
        lvl_req=85,
    )
    ARKAINES_VALOR = _Metadata(
        ladder=False,
        code="upl",
        lvl=85,
        lvl_req=85,
    )
    BLACKOAK_SHIELD = _Metadata(
        ladder=False,
        code="uml",
        lvl=67,
        lvl_req=61,
    )
    STORMSHIELD = _Metadata(
        ladder=False,
        code="uit",
        lvl=77,
        lvl_req=73,
    )
    HELLSLAYER = _Metadata(
        ladder=False,
        code="7bt",
        lvl=71,
        lvl_req=66,
    )
    MESSERSCHMIDTS_REAVER = _Metadata(
        ladder=False,
        code="7ga",
        lvl=75,
        lvl_req=70,
    )
    BARANARS_STAR = _Metadata(
        ladder=False,
        code="7mt",
        lvl=70,
        lvl_req=65,
    )
    SCHAEFERS_HAMMER = _Metadata(
        ladder=False,
        code="7wh",
        lvl=83,
        lvl_req=79,
    )
    THE_CRANIUM_BASHER = _Metadata(
        ladder=False,
        code="7gm",
        lvl=85,
        lvl_req=87,
    )
    LIGHTSABRE = _Metadata(
        ladder=False,
        code="7cr",
        lvl=66,
        lvl_req=58,
    )
    DOOMBRINGER = _Metadata(
        ladder=False,
        code="7b7",
        lvl=75,
        lvl_req=69,
    )
    THE_GRANDFATHER = _Metadata(
        ladder=False,
        code="7gd",
        lvl=85,
        lvl_req=81,
    )
    WIZARDSPIKE = _Metadata(
        ladder=False,
        code="7dg",
        lvl=69,
        lvl_req=61,
    )
    CONSTRICTING_LOOP = _Metadata(
        ladder=False,
        code="rin",
        lvl=73,
        lvl_req=65,
    )
    STORMSPIRE = _Metadata(
        ladder=False,
        code="7wc",
        lvl=78,
        lvl_req=70,
    )
    EAGLEHORN = _Metadata(
        ladder=False,
        code="6l7",
        lvl=77,
        lvl_req=69,
    )
    WINDFORCE = _Metadata(
        ladder=False,
        code="6lw",
        lvl=80,
        lvl_req=73,
    )
    BUL_KATHOS_WEDDING_BAND = _Metadata(
        ladder=False,
        code="rin",
        lvl=66,
        lvl_req=58,
    )
    THE_CATS_EYE = _Metadata(
        ladder=False,
        code="amu",
        lvl=58,
        lvl_req=50,
    )
    THE_RISING_SUN = _Metadata(
        ladder=False,
        code="amu",
        lvl=73,
        lvl_req=65,
    )
    CRESCENT_MOON = _Metadata(
        ladder=False,
        code="amu",
        lvl=58,
        lvl_req=50,
    )
    MARAS_KALEIDOSCOPE = _Metadata(
        ladder=False,
        code="amu",
        lvl=80,
        lvl_req=67,
    )
    ATMAS_SCARAB = _Metadata(
        ladder=False,
        code="amu",
        lvl=60,
        lvl_req=60,
    )
    DWARF_STAR = _Metadata(
        ladder=False,
        code="rin",
        lvl=53,
        lvl_req=45,
    )
    RAVEN_FROST = _Metadata(
        ladder=False,
        code="rin",
        lvl=53,
        lvl_req=45,
    )
    HIGHLORDS_WRATH = _Metadata(
        ladder=False,
        code="amu",
        lvl=73,
        lvl_req=65,
    )
    SARACENS_CHANCE = _Metadata(
        ladder=False,
        code="amu",
        lvl=55,
        lvl_req=47,
    )
    ARREATS_FACE = _Metadata(
        ladder=False,
        code="baa",
        lvl=50,
        lvl_req=42,
    )
    HOMUNCULUS = _Metadata(
        ladder=False,
        code="nea",
        lvl=50,
        lvl_req=42,
    )
    TITANS_REVENGE = _Metadata(
        ladder=False,
        code="ama",
        lvl=50,
        lvl_req=42,
    )
    LYCANDERS_AIM = _Metadata(
        ladder=False,
        code="am7",
        lvl=50,
        lvl_req=42,
    )
    LYCANDERS_FLANK = _Metadata(
        ladder=False,
        code="am9",
        lvl=50,
        lvl_req=42,
    )
    THE_OCULUS = _Metadata(
        ladder=False,
        code="oba",
        lvl=50,
        lvl_req=42,
    )
    HERALD_OF_ZAKARUM = _Metadata(
        ladder=False,
        code="pa9",
        lvl=50,
        lvl_req=42,
    )
    BARTUCS_CUT_THROAT = _Metadata(
        ladder=False,
        code="9tw",
        lvl=50,
        lvl_req=42,
    )
    JALALS_MANE = _Metadata(
        ladder=False,
        code="dra",
        lvl=50,
        lvl_req=42,
    )
    THE_SCALPER = _Metadata(
        ladder=False,
        code="9ta",
        lvl=65,
        lvl_req=57,
    )
    BLOODMOON = _Metadata(
        ladder=False,
        code="7sb",
        lvl=69,
        lvl_req=61,
    )
    DJINN_SLAYER = _Metadata(
        ladder=False,
        code="7sm",
        lvl=73,
        lvl_req=65,
    )
    DEATHBIT = _Metadata(
        ladder=False,
        code="9tk",
        lvl=52,
        lvl_req=44,
    )
    WARSHRIKE = _Metadata(
        ladder=False,
        code="7bk",
        lvl=83,
        lvl_req=75,
    )
    GUT_SIPHON = _Metadata(
        ladder=False,
        code="6rx",
        lvl=79,
        lvl_req=71,
    )
    RAZORS_EDGE = _Metadata(
        ladder=False,
        code="7ha",
        lvl=75,
        lvl_req=67,
    )
    DEMON_LIMB = _Metadata(
        ladder=False,
        code="7sp",
        lvl=71,
        lvl_req=63,
    )
    STEEL_SHADE = _Metadata(
        ladder=False,
        code="ulm",
        lvl=70,
        lvl_req=62,
    )
    TOMB_REAVER = _Metadata(
        ladder=False,
        code="7pa",
        lvl=86,
        lvl_req=84,
    )
    DEATHS_WEB = _Metadata(
        ladder=False,
        code="7gw",
        lvl=74,
        lvl_req=66,
    )
    NATURES_PEACE = _Metadata(
        ladder=False,
        code="rin",
        lvl=77,
        lvl_req=69,
    )
    AZUREWRATH = _Metadata(
        ladder=False,
        code="7cr",
        lvl=87,
        lvl_req=85,
    )
    SERAPHS_HYMN = _Metadata(
        ladder=False,
        code="amu",
        lvl=73,
        lvl_req=65,
    )
    FLESHRIPPER = _Metadata(
        ladder=False,
        code="7kr",
        lvl=76,
        lvl_req=68,
    )
    ODIUM = _Metadata(
        ladder=False,
        code="7fb",
        lvl=87,
        lvl_req=80,
    )
    HORIZONS_TORNADO = _Metadata(
        ladder=False,
        code="7fl",
        lvl=72,
        lvl_req=64,
    )
    STONE_CRUSHER = _Metadata(
        ladder=False,
        code="7wh",
        lvl=76,
        lvl_req=68,
    )
    JADE_TALON = _Metadata(
        ladder=False,
        code="7wb",
        lvl=74,
        lvl_req=66,
    )
    SHADOW_DANCER = _Metadata(
        ladder=False,
        code="uhb",
        lvl=79,
        lvl_req=71,
    )
    CEREBUS_BITE = _Metadata(
        ladder=False,
        code="drb",
        lvl=71,
        lvl_req=63,
    )
    TYRAELS_MIGHT = _Metadata(
        ladder=False,
        code="uar",
        lvl=87,
        lvl_req=84,
    )
    SOUL_DRAINER = _Metadata(
        ladder=False,
        code="umg",
        lvl=82,
        lvl_req=74,
    )
    RUNE_MASTER = _Metadata(
        ladder=False,
        code="72a",
        lvl=80,
        lvl_req=72,
    )
    DEATH_CLEAVER = _Metadata(
        ladder=False,
        code="7wa",
        lvl=78,
        lvl_req=70,
    )
    EXECUTIONERS_JUSTICE = _Metadata(
        ladder=False,
        code="7gi",
        lvl=83,
        lvl_req=75,
    )
    STONERAVEN = _Metadata(
        ladder=False,
        code="amd",
        lvl=72,
        lvl_req=64,
    )
    LEVIATHAN = _Metadata(
        ladder=False,
        code="uld",
        lvl=73,
        lvl_req=65,
    )
    WISP_PROJECTOR = _Metadata(
        ladder=False,
        code="rin",
        lvl=84,
        lvl_req=76,
    )
    GARGOYLES_BITE = _Metadata(
        ladder=False,
        code="7ts",
        lvl=78,
        lvl_req=70,
    )
    LACERATOR = _Metadata(
        ladder=False,
        code="7b8",
        lvl=76,
        lvl_req=68,
    )
    MANG_SONGS_LESSON = _Metadata(
        ladder=False,
        code="6ws",
        lvl=86,
        lvl_req=82,
    )
    VIPERFORK = _Metadata(
        ladder=False,
        code="7br",
        lvl=79,
        lvl_req=71,
    )
    ETHEREAL_EDGE = _Metadata(
        ladder=False,
        code="7ba",
        lvl=82,
        lvl_req=74,
    )
    DEMONHORNS_EDGE = _Metadata(
        ladder=False,
        code="bad",
        lvl=69,
        lvl_req=61,
    )
    THE_REAPERS_TOLL = _Metadata(
        ladder=False,
        code="7s8",
        lvl=83,
        lvl_req=75,
    )
    SPIRIT_KEEPER = _Metadata(
        ladder=False,
        code="drd",
        lvl=75,
        lvl_req=67,
    )
    HELLRACK = _Metadata(
        ladder=False,
        code="6hx",
        lvl=84,
        lvl_req=76,
    )
    ALMA_NEGRA = _Metadata(
        ladder=False,
        code="pac",
        lvl=85,
        lvl_req=77,
    )
    DARKFORCE_SPAWN = _Metadata(
        ladder=False,
        code="nef",
        lvl=72,
        lvl_req=64,
    )
    WIDOWMAKER = _Metadata(
        ladder=False,
        code="6sw",
        lvl=73,
        lvl_req=65,
    )
    BLOOD_RAVENS_CHARGE = _Metadata(
        ladder=False,
        code="amb",
        lvl=79,
        lvl_req=71,
    )
    GHOSTFLAME = _Metadata(
        ladder=False,
        code="7bl",
        lvl=70,
        lvl_req=62,
    )
    SHADOW_KILLER = _Metadata(
        ladder=False,
        code="7cs",
        lvl=85,
        lvl_req=78,
    )
    GIMMERSHRED = _Metadata(
        ladder=False,
        code="7ta",
        lvl=78,
        lvl_req=70,
    )
    GRIFFONS_EYE = _Metadata(
        ladder=False,
        code="ci3",
        lvl=84,
        lvl_req=76,
    )
    WINDHAMMER = _Metadata(
        ladder=False,
        code="7m7",
        lvl=76,
        lvl_req=68,
    )
    THUNDERSTROKE = _Metadata(
        ladder=False,
        code="amf",
        lvl=77,
        lvl_req=69,
    )
    DEMONS_ARCH = _Metadata(
        ladder=False,
        code="7s7",
        lvl=76,
        lvl_req=68,
    )
    BONEFLAME = _Metadata(
        ladder=False,
        code="nee",
        lvl=80,
        lvl_req=72,
    )
    STEEL_PILLAR = _Metadata(
        ladder=False,
        code="7p7",
        lvl=77,
        lvl_req=69,
    )
    NIGHTWINGS_VEIL = _Metadata(
        ladder=False,
        code="uhm",
        lvl=75,
        lvl_req=67,
    )
    CROWN_OF_AGES = _Metadata(
        ladder=False,
        code="urn",
        lvl=86,
        lvl_req=82,
    )
    ANDARIELS_VISAGE = _Metadata(
        ladder=False,
        code="usk",
        lvl=85,
        lvl_req=83,
    )
    DRAGONSCALE = _Metadata(
        ladder=False,
        code="pae",
        lvl=84,
        lvl_req=80,
    )
    STEEL_CARAPACE = _Metadata(
        ladder=False,
        code="uul",
        lvl=74,
        lvl_req=66,
    )
    MEDUSAS_GAZE = _Metadata(
        ladder=False,
        code="uow",
        lvl=84,
        lvl_req=76,
    )
    RAVENLORE = _Metadata(
        ladder=False,
        code="dre",
        lvl=82,
        lvl_req=74,
    )
    BONESHADE = _Metadata(
        ladder=False,
        code="7bw",
        lvl=84,
        lvl_req=79,
    )
    FLAMEBELLOW = _Metadata(
        ladder=False,
        code="7gs",
        lvl=79,
        lvl_req=71,
    )
    DEATHS_FATHOM = _Metadata(
        ladder=False,
        code="obf",
        lvl=81,
        lvl_req=73,
    )
    WOLFHOWL = _Metadata(
        ladder=False,
        code="bac",
        lvl=85,
        lvl_req=79,
    )
    SPIRIT_WARD = _Metadata(
        ladder=False,
        code="uts",
        lvl=76,
        lvl_req=68,
    )
    KIRAS_GUARDIAN = _Metadata(
        ladder=False,
        code="ci2",
        lvl=85,
        lvl_req=77,
    )
    ORMUS_ROBES = _Metadata(
        ladder=False,
        code="uui",
        lvl=83,
        lvl_req=75,
    )
    GHEEDS_FORTUNE = _Metadata(
        ladder=False,
        code="cm3",
        lvl=70,
        lvl_req=62,
    )
    STORMLASH = _Metadata(
        ladder=False,
        code="7fl",
        lvl=86,
        lvl_req=82,
    )
    HALABERDS_REIGN = _Metadata(
        ladder=False,
        code="bae",
        lvl=85,
        lvl_req=77,
    )
    SPIKE_THORN = _Metadata(
        ladder=False,
        code="upk",
        lvl=78,
        lvl_req=70,
    )
    DRACULS_GRASP = _Metadata(
        ladder=False,
        code="uvg",
        lvl=84,
        lvl_req=76,
    )
    FROSTWIND = _Metadata(
        ladder=False,
        code="7ls",
        lvl=78,
        lvl_req=70,
    )
    TEMPLARS_MIGHT = _Metadata(
        ladder=False,
        code="uar",
        lvl=82,
        lvl_req=74,
    )
    ESCHUTAS_TEMPER = _Metadata(
        ladder=False,
        code="obc",
        lvl=80,
        lvl_req=72,
    )
    FIRELIZARDS_TALONS = _Metadata(
        ladder=False,
        code="7lw",
        lvl=75,
        lvl_req=67,
    )
    SANDSTORM_TREK = _Metadata(
        ladder=False,
        code="uvb",
        lvl=72,
        lvl_req=64,
    )
    MARROWWALK = _Metadata(
        ladder=False,
        code="umb",
        lvl=74,
        lvl_req=66,
    )
    HEAVENS_LIGHT = _Metadata(
        ladder=False,
        code="7sc",
        lvl=69,
        lvl_req=61,
    )
    MERMANS_SPROCKET = _Metadata(
        ladder=False,
        code="ulb",
        lvl=45,
        lvl_req=45,
    )
    ARACHNID_MESH = _Metadata(
        ladder=False,
        code="ulc",
        lvl=87,
        lvl_req=80,
    )
    NOSFERATUS_COIL = _Metadata(
        ladder=False,
        code="uvc",
        lvl=68,
        lvl_req=51,
    )
    METALGRID = _Metadata(
        ladder=False,
        code="amu",
        lvl=85,
        lvl_req=81,
    )
    VERDUNGOS_HEARTY_CORD = _Metadata(
        ladder=False,
        code="umc",
        lvl=71,
        lvl_req=63,
    )
    SIGGARDS_STAUNCH = _Metadata(
        ladder=False,
        code="uhc",
        lvl=80,
        lvl_req=72,
    )
    CARRION_WIND = _Metadata(
        ladder=False,
        code="rin",
        lvl=68,
        lvl_req=60,
    )
    GIANT_SKULL = _Metadata(
        ladder=False,
        code="uh9",
        lvl=73,
        lvl_req=65,
    )
    ASTREONS_IRON_WARD = _Metadata(
        ladder=False,
        code="7ws",
        lvl=68,
        lvl_req=60,
    )
    ANNIHILUS = _Metadata(
        ladder=False,
        code="cm1",
        lvl=130,
        lvl_req=70,
    )
    ARIOCS_NEEDLE = _Metadata(
        ladder=False,
        code="7sr",
        lvl=85,
        lvl_req=81,
    )
    CRANEBEAK = _Metadata(
        ladder=False,
        code="7mp",
        lvl=71,
        lvl_req=63,
    )
    NORDS_TENDERIZER = _Metadata(
        ladder=False,
        code="7cl",
        lvl=76,
        lvl_req=68,
    )
    EARTH_SHIFTER = _Metadata(
        ladder=False,
        code="7gm",
        lvl=77,
        lvl_req=69,
    )
    WRAITH_FLIGHT = _Metadata(
        ladder=False,
        code="7gl",
        lvl=84,
        lvl_req=76,
    )
    BONEHEW = _Metadata(
        ladder=False,
        code="7o7",
        lvl=72,
        lvl_req=64,
    )
    ONDALS_WISDOM = _Metadata(
        ladder=False,
        code="6cs",
        lvl=74,
        lvl_req=66,
    )
    THE_REDEEMER = _Metadata(
        ladder=False,
        code="7sc",
        lvl=80,
        lvl_req=72,
    )
    HEAD_HUNTERS_GLORY = _Metadata(
        ladder=False,
        code="ush",
        lvl=83,
        lvl_req=75,
    )
    STEELREND = _Metadata(
        ladder=False,
        code="uhg",
        lvl=78,
        lvl_req=70,
    )
    RAINBOW_FACET = _Metadata(
        ladder=False,
        code="jew",
        lvl=85,
        lvl_req=49,
    )
    HELLFIRE_TORCH = _Metadata(
        ladder=False,
        code="cm2",
        lvl=120,
        lvl_req=75,
    )
    ITHERAELS_PATH = _Metadata(
        ladder=False,
        code="utb",
        lvl=131,
        lvl_req=85,
    )
    OVERLORDS_HELM = _Metadata(
        ladder=False,
        code="uhl",
        lvl=131,
        lvl_req=85,
    )
    DARK_ABYSS = _Metadata(
        ladder=False,
        code="uth",
        lvl=131,
        lvl_req=85,
    )
    AIDANS_SCAR = _Metadata(
        ladder=False,
        code="7qr",
        lvl=131,
        lvl_req=85,
    )
    HADRIELS_HAND = _Metadata(
        ladder=False,
        code="7bs",
        lvl=131,
        lvl_req=85,
    )
    TRUE_SILVER = _Metadata(
        ladder=False,
        code="am5",
        lvl=24,
        lvl_req=20,
    )
    QUETZALCOATL = _Metadata(
        ladder=False,
        code="dr2",
        lvl=35,
        lvl_req=29,
    )
    CYCLOPEAN_ROAR = _Metadata(
        ladder=False,
        code="ba6",
        lvl=34,
        lvl_req=28,
    )
    SANKEKURS_FALL = _Metadata(
        ladder=False,
        code="pa3",
        lvl=37,
        lvl_req=29,
    )
    MAGE_SLAYER = _Metadata(
        ladder=False,
        code="9ar",
        lvl=32,
        lvl_req=27,
    )
    KALANS_LEGACY = _Metadata(
        ladder=False,
        code="ne6",
        lvl=30,
        lvl_req=26,
    )
    TEMPEST = _Metadata(
        ladder=False,
        code="ob6",
        lvl=28,
        lvl_req=25,
    )
    BAND_OF_SKULLS = _Metadata(
        ladder=False,
        code="rbe",
        lvl=131,
        lvl_req=90,
    )
    CAGE_OF_THE_UNSULLIED = _Metadata(
        ladder=False,
        code="rar",
        lvl=131,
        lvl_req=90,
    )
    THE_THIRD_EYE = _Metadata(
        ladder=False,
        code="ram",
        lvl=131,
        lvl_req=90,
    )
    ZERAES_RESOLVE = _Metadata(
        ladder=False,
        code="ame",
        lvl=87,
        lvl_req=76,
    )
    OCCULTIST = _Metadata(
        ladder=False,
        code="utg",
        lvl=87,
        lvl_req=70,
    )
    BRIMSTONE_RAIN = _Metadata(
        ladder=False,
        code="6bs",
        lvl=87,
        lvl_req=80,
    )
    AKARATS_DEVOTION = _Metadata(
        ladder=False,
        code="7qs",
        lvl=87,
        lvl_req=74,
    )
    MARTYRDOM = _Metadata(
        ladder=False,
        code="ned",
        lvl=87,
        lvl_req=68,
    )
    STALKERS_CULL = _Metadata(
        ladder=False,
        code="7tw",
        lvl=87,
        lvl_req=65,
    )
    PURGATORY = _Metadata(
        ladder=False,
        code="utp",
        lvl=87,
        lvl_req=75,
    )
    RAEKORS_VIRTUE = _Metadata(
        ladder=False,
        code="baf",
        lvl=87,
        lvl_req=78,
    )
    URSAS_NIGHTMARE = _Metadata(
        ladder=False,
        code="drf",
        lvl=50,
        lvl_req=42,
    )
    ZHARS_SANCTUM = _Metadata(
        ladder=False,
        code="t51",
        lvl=80,
        lvl_req=80,
    )
    WARLORD_OF_BLOOD = _Metadata(
        ladder=False,
        code="t52",
        lvl=80,
        lvl_req=80,
    )
    FALLEN_GARDENS = _Metadata(
        ladder=False,
        code="t53",
        lvl=80,
        lvl_req=80,
    )
    ULDYSSIANS_AWAKENING = _Metadata(
        ladder=False,
        code="7st",
        lvl=80,
        lvl_req=74,
    )
    LEORICS_MITHRIL_BANE = _Metadata(
        ladder=False,
        code="7cm",
        lvl=78,
        lvl_req=68,
    )
    TWILIGHTS_REFLECTION = _Metadata(
        ladder=False,
        code="urg",
        lvl=18,
        lvl_req=13,
    )
    WRAITHSKIN = _Metadata(
        ladder=False,
        code="ung",
        lvl=61,
        lvl_req=53,
    )
    TITANS_GRIP = _Metadata(
        ladder=False,
        code="ulg",
        lvl=45,
        lvl_req=38,
    )
    SHATTERBLADE = _Metadata(
        ladder=False,
        code="7di",
        lvl=73,
        lvl_req=65,
    )
    DENMOTHER = _Metadata(
        ladder=False,
        code="drc",
        lvl=66,
        lvl_req=58,
    )
    EBONBANE = _Metadata(
        ladder=False,
        code="amc",
        lvl=70,
        lvl_req=63,
    )
    WHISPERING_MIRAGE = _Metadata(
        ladder=False,
        code="7xf",
        lvl=76,
        lvl_req=68,
    )
    SKYWARDEN = _Metadata(
        ladder=False,
        code="paf",
        lvl=85,
        lvl_req=77,
    )
    SKORN = _Metadata(
        ladder=False,
        code="ob7",
        lvl=36,
        lvl_req=27,
    )
    ACHILLES_STRIKE = _Metadata(
        ladder=False,
        code="9b8",
        lvl=59,
        lvl_req=51,
    )
    WILDSPEAKER = _Metadata(
        ladder=False,
        code="ba7",
        lvl=52,
        lvl_req=44,
    )
    FENRIS = _Metadata(
        ladder=False,
        code="dr6",
        lvl=48,
        lvl_req=40,
    )
    SACRED_TOTEM = _Metadata(
        ladder=False,
        code="neg",
        lvl=72,
        lvl_req=64,
    )
    IMPERIAL_PALACE = _Metadata(
        ladder=False,
        code="t54",
        lvl=80,
        lvl_req=80,
    )
    OUTER_VOID = _Metadata(
        ladder=False,
        code="t55",
        lvl=80,
        lvl_req=80,
    )
    BALEFIRE = _Metadata(
        ladder=False,
        code="aqv",
        lvl=14,
        lvl_req=14,
    )
    SWIFTWIND_NEEDLE = _Metadata(
        ladder=False,
        code="aqv2",
        lvl=32,
        lvl_req=32,
    )
    TOMBSONG = _Metadata(
        ladder=False,
        code="aqv2",
        lvl=36,
        lvl_req=36,
    )
    AETHERWING = _Metadata(
        ladder=False,
        code="aqv3",
        lvl=55,
        lvl_req=55,
    )
    BASILISKS_QUILL = _Metadata(
        ladder=False,
        code="aqv3",
        lvl=62,
        lvl_req=62,
    )
    DOOMS_FINGER = _Metadata(
        ladder=False,
        code="aqv3",
        lvl=87,
        lvl_req=68,
    )
    RAMFODDER = _Metadata(
        ladder=False,
        code="cqv",
        lvl=8,
        lvl_req=8,
    )
    ANVILGUARD_STRAP = _Metadata(
        ladder=False,
        code="cqv2",
        lvl=34,
        lvl_req=34,
    )
    SHATTERHEAD = _Metadata(
        ladder=False,
        code="cqv2",
        lvl=47,
        lvl_req=47,
    )
    ABYSSAL_WARD = _Metadata(
        ladder=False,
        code="cqv3",
        lvl=60,
        lvl_req=60,
    )
    BANNERLORDS_CALL = _Metadata(
        ladder=False,
        code="cqv3",
        lvl=60,
        lvl_req=65,
    )
    FROZEN_SORROW = _Metadata(
        ladder=False,
        code="cqv3",
        lvl=87,
        lvl_req=72,
    )
    CRACKLESHOT = _Metadata(
        ladder=False,
        code="6hb",
        lvl=87,
        lvl_req=72,
    )
    CITY_OF_UREH = _Metadata(
        ladder=False,
        code="t56",
        lvl=80,
        lvl_req=80,
    )

    @property
    def ladder(self) -> bool:
        return self.value.ladder

    @property
    def code(self) -> str:
        return self.value.code

    @property
    def lvl(self) -> int:
        return self.value.lvl

    @property
    def lvl_req(self) -> int:
        return self.value.lvl_req
