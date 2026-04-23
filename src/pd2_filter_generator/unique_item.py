"""
Generated UniqueItem enum from PD2 data.

DO NOT EDIT MANUALLY - regenerate with: hatch run ./scripts/generate.py generate
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from pd2_filter_generator.expression import CodeLiteral


@dataclass(frozen=True)
class _Metadata:
    """Item type metadata."""

    ladder: bool  # "ladder"
    code: CodeLiteral  # "code"
    lvl: int  # "lvl"
    lvl_req: int  # "lvl req"


_METADATA: dict[str, _Metadata] = {
    "THE_GNASHER": _Metadata(
        ladder=False,
        code=CodeLiteral("hax"),
        lvl=7,
        lvl_req=0,
    ),
    "DEATHSPADE": _Metadata(
        ladder=False,
        code=CodeLiteral("axe"),
        lvl=12,
        lvl_req=0,
    ),
    "BLADEBONE": _Metadata(
        ladder=False,
        code=CodeLiteral("2ax"),
        lvl=20,
        lvl_req=0,
    ),
    "SKULL_SPLITTER": _Metadata(
        ladder=False,
        code=CodeLiteral("mpi"),
        lvl=28,
        lvl_req=0,
    ),
    "RAKESCAR": _Metadata(
        ladder=False,
        code=CodeLiteral("wax"),
        lvl=36,
        lvl_req=0,
    ),
    "AXE_OF_FECHMAR": _Metadata(
        ladder=False,
        code=CodeLiteral("lax"),
        lvl=11,
        lvl_req=0,
    ),
    "GORESHOVEL": _Metadata(
        ladder=False,
        code=CodeLiteral("bax"),
        lvl=19,
        lvl_req=0,
    ),
    "THE_CHIEFTAIN": _Metadata(
        ladder=False,
        code=CodeLiteral("btx"),
        lvl=26,
        lvl_req=0,
    ),
    "BRAINHEW": _Metadata(
        ladder=False,
        code=CodeLiteral("gax"),
        lvl=34,
        lvl_req=0,
    ),
    "HUMONGOUS": _Metadata(
        ladder=False,
        code=CodeLiteral("gix"),
        lvl=39,
        lvl_req=0,
    ),
    "TORCH_OF_IRO": _Metadata(
        ladder=False,
        code=CodeLiteral("wnd"),
        lvl=7,
        lvl_req=0,
    ),
    "MAELSTROM": _Metadata(
        ladder=False,
        code=CodeLiteral("ywn"),
        lvl=19,
        lvl_req=0,
    ),
    "GRAVENSPINE": _Metadata(
        ladder=False,
        code=CodeLiteral("bwn"),
        lvl=27,
        lvl_req=0,
    ),
    "UMES_LAMENT": _Metadata(
        ladder=False,
        code=CodeLiteral("gwn"),
        lvl=38,
        lvl_req=0,
    ),
    "FELLOAK": _Metadata(
        ladder=False,
        code=CodeLiteral("clb"),
        lvl=4,
        lvl_req=0,
    ),
    "KNELL_STRIKER": _Metadata(
        ladder=False,
        code=CodeLiteral("scp"),
        lvl=7,
        lvl_req=0,
    ),
    "RUSTHANDLE": _Metadata(
        ladder=False,
        code=CodeLiteral("gsc"),
        lvl=23,
        lvl_req=0,
    ),
    "STORMEYE": _Metadata(
        ladder=False,
        code=CodeLiteral("wsp"),
        lvl=31,
        lvl_req=0,
    ),
    "STOUTNAIL": _Metadata(
        ladder=False,
        code=CodeLiteral("spc"),
        lvl=7,
        lvl_req=0,
    ),
    "CRUSHFLANGE": _Metadata(
        ladder=False,
        code=CodeLiteral("mac"),
        lvl=12,
        lvl_req=0,
    ),
    "BLOODRISE": _Metadata(
        ladder=False,
        code=CodeLiteral("mst"),
        lvl=20,
        lvl_req=0,
    ),
    "THE_GENERALS_TAN_DO_LI_GA": _Metadata(
        ladder=False,
        code=CodeLiteral("fla"),
        lvl=28,
        lvl_req=0,
    ),
    "IRONSTONE": _Metadata(
        ladder=False,
        code=CodeLiteral("whm"),
        lvl=36,
        lvl_req=0,
    ),
    "BONESNAP": _Metadata(
        ladder=False,
        code=CodeLiteral("mau"),
        lvl=32,
        lvl_req=0,
    ),
    "STEELDRIVER": _Metadata(
        ladder=False,
        code=CodeLiteral("gma"),
        lvl=39,
        lvl_req=0,
    ),
    "RIXOTS_KEEN": _Metadata(
        ladder=False,
        code=CodeLiteral("ssd"),
        lvl=3,
        lvl_req=0,
    ),
    "BLOOD_CRESCENT": _Metadata(
        ladder=False,
        code=CodeLiteral("scm"),
        lvl=10,
        lvl_req=0,
    ),
    "SKEWER_OF_KRINTIZ": _Metadata(
        ladder=False,
        code=CodeLiteral("sbr"),
        lvl=14,
        lvl_req=0,
    ),
    "GLEAMSCYTHE": _Metadata(
        ladder=False,
        code=CodeLiteral("flc"),
        lvl=18,
        lvl_req=0,
    ),
    "GRISWOLDS_EDGE": _Metadata(
        ladder=False,
        code=CodeLiteral("bsd"),
        lvl=23,
        lvl_req=0,
    ),
    "HELLPLAGUE": _Metadata(
        ladder=False,
        code=CodeLiteral("lsd"),
        lvl=30,
        lvl_req=0,
    ),
    "CULWENS_POINT": _Metadata(
        ladder=False,
        code=CodeLiteral("wsd"),
        lvl=39,
        lvl_req=0,
    ),
    "SHADOWFANG": _Metadata(
        ladder=False,
        code=CodeLiteral("2hs"),
        lvl=16,
        lvl_req=0,
    ),
    "SOULFLAY": _Metadata(
        ladder=False,
        code=CodeLiteral("clm"),
        lvl=26,
        lvl_req=0,
    ),
    "KINEMILS_AWL": _Metadata(
        ladder=False,
        code=CodeLiteral("gis"),
        lvl=31,
        lvl_req=0,
    ),
    "BLACKTONGUE": _Metadata(
        ladder=False,
        code=CodeLiteral("bsw"),
        lvl=35,
        lvl_req=0,
    ),
    "RIPSAW": _Metadata(
        ladder=False,
        code=CodeLiteral("flb"),
        lvl=35,
        lvl_req=0,
    ),
    "THE_PATRIARCH": _Metadata(
        ladder=False,
        code=CodeLiteral("gsd"),
        lvl=39,
        lvl_req=0,
    ),
    "GULL": _Metadata(
        ladder=False,
        code=CodeLiteral("dgr"),
        lvl=6,
        lvl_req=0,
    ),
    "THE_DIGGLER": _Metadata(
        ladder=False,
        code=CodeLiteral("dir"),
        lvl=15,
        lvl_req=0,
    ),
    "THE_JADE_TAN_DO": _Metadata(
        ladder=False,
        code=CodeLiteral("kri"),
        lvl=26,
        lvl_req=0,
    ),
    "SPECTRAL_SHARD": _Metadata(
        ladder=False,
        code=CodeLiteral("bld"),
        lvl=34,
        lvl_req=0,
    ),
    "THE_DRAGON_CHANG": _Metadata(
        ladder=False,
        code=CodeLiteral("spr"),
        lvl=11,
        lvl_req=0,
    ),
    "RAZORTINE": _Metadata(
        ladder=False,
        code=CodeLiteral("tri"),
        lvl=16,
        lvl_req=0,
    ),
    "BLOODTHIEF": _Metadata(
        ladder=False,
        code=CodeLiteral("brn"),
        lvl=23,
        lvl_req=0,
    ),
    "LANCE_OF_YAGGAI": _Metadata(
        ladder=False,
        code=CodeLiteral("spt"),
        lvl=30,
        lvl_req=0,
    ),
    "THE_TANNR_GOREROD": _Metadata(
        ladder=False,
        code=CodeLiteral("pik"),
        lvl=36,
        lvl_req=0,
    ),
    "DIMOAKS_HEW": _Metadata(
        ladder=False,
        code=CodeLiteral("bar"),
        lvl=11,
        lvl_req=0,
    ),
    "STEELGOAD": _Metadata(
        ladder=False,
        code=CodeLiteral("vou"),
        lvl=19,
        lvl_req=0,
    ),
    "SOUL_HARVEST": _Metadata(
        ladder=False,
        code=CodeLiteral("scy"),
        lvl=26,
        lvl_req=0,
    ),
    "THE_BATTLEBRANCH": _Metadata(
        ladder=False,
        code=CodeLiteral("pax"),
        lvl=34,
        lvl_req=0,
    ),
    "WOESTAVE": _Metadata(
        ladder=False,
        code=CodeLiteral("hal"),
        lvl=38,
        lvl_req=0,
    ),
    "THE_GRIM_REAPER": _Metadata(
        ladder=False,
        code=CodeLiteral("wsc"),
        lvl=39,
        lvl_req=0,
    ),
    "BANE_ASH": _Metadata(
        ladder=False,
        code=CodeLiteral("sst"),
        lvl=7,
        lvl_req=0,
    ),
    "SERPENT_LORD": _Metadata(
        ladder=False,
        code=CodeLiteral("lst"),
        lvl=12,
        lvl_req=0,
    ),
    "SPIRE_OF_LAZARUS": _Metadata(
        ladder=False,
        code=CodeLiteral("cst"),
        lvl=24,
        lvl_req=0,
    ),
    "THE_SALAMANDER": _Metadata(
        ladder=False,
        code=CodeLiteral("bst"),
        lvl=28,
        lvl_req=0,
    ),
    "THE_IRON_JANG_BONG": _Metadata(
        ladder=False,
        code=CodeLiteral("wst"),
        lvl=38,
        lvl_req=0,
    ),
    "PLUCKEYE": _Metadata(
        ladder=False,
        code=CodeLiteral("sbw"),
        lvl=10,
        lvl_req=0,
    ),
    "WITHERSTRING": _Metadata(
        ladder=False,
        code=CodeLiteral("hbw"),
        lvl=18,
        lvl_req=0,
    ),
    "RAVEN_CLAW": _Metadata(
        ladder=False,
        code=CodeLiteral("lbw"),
        lvl=20,
        lvl_req=0,
    ),
    "ROGUES_BOW": _Metadata(
        ladder=False,
        code=CodeLiteral("cbw"),
        lvl=27,
        lvl_req=0,
    ),
    "STORMSTRIKE": _Metadata(
        ladder=False,
        code=CodeLiteral("sbb"),
        lvl=34,
        lvl_req=0,
    ),
    "WIZENDRAW": _Metadata(
        ladder=False,
        code=CodeLiteral("lbb"),
        lvl=35,
        lvl_req=0,
    ),
    "HELLCLAP": _Metadata(
        ladder=False,
        code=CodeLiteral("swb"),
        lvl=36,
        lvl_req=0,
    ),
    "BLASTBARK": _Metadata(
        ladder=False,
        code=CodeLiteral("lwb"),
        lvl=38,
        lvl_req=0,
    ),
    "LEADCROW": _Metadata(
        ladder=False,
        code=CodeLiteral("lxb"),
        lvl=12,
        lvl_req=0,
    ),
    "ICHORSTING": _Metadata(
        ladder=False,
        code=CodeLiteral("mxb"),
        lvl=24,
        lvl_req=0,
    ),
    "HELLCAST": _Metadata(
        ladder=False,
        code=CodeLiteral("hxb"),
        lvl=36,
        lvl_req=0,
    ),
    "DOOMSLINGER": _Metadata(
        ladder=False,
        code=CodeLiteral("rxb"),
        lvl=38,
        lvl_req=0,
    ),
    "BIGGINS_BONNET": _Metadata(
        ladder=False,
        code=CodeLiteral("cap"),
        lvl=4,
        lvl_req=0,
    ),
    "TARNHELM": _Metadata(
        ladder=False,
        code=CodeLiteral("skp"),
        lvl=20,
        lvl_req=0,
    ),
    "COIF_OF_GLORY": _Metadata(
        ladder=False,
        code=CodeLiteral("hlm"),
        lvl=19,
        lvl_req=0,
    ),
    "DUSKDEEP": _Metadata(
        ladder=False,
        code=CodeLiteral("fhl"),
        lvl=23,
        lvl_req=0,
    ),
    "WORMSKULL": _Metadata(
        ladder=False,
        code=CodeLiteral("bhm"),
        lvl=28,
        lvl_req=0,
    ),
    "HOWLTUSK": _Metadata(
        ladder=False,
        code=CodeLiteral("ghm"),
        lvl=34,
        lvl_req=0,
    ),
    "UNDEAD_CROWN": _Metadata(
        ladder=False,
        code=CodeLiteral("crn"),
        lvl=39,
        lvl_req=0,
    ),
    "THE_FACE_OF_HORROR": _Metadata(
        ladder=False,
        code=CodeLiteral("msk"),
        lvl=27,
        lvl_req=0,
    ),
    "GREYFORM": _Metadata(
        ladder=False,
        code=CodeLiteral("qui"),
        lvl=10,
        lvl_req=0,
    ),
    "BLINKBATS_FORM": _Metadata(
        ladder=False,
        code=CodeLiteral("lea"),
        lvl=16,
        lvl_req=0,
    ),
    "THE_CENTURION": _Metadata(
        ladder=False,
        code=CodeLiteral("hla"),
        lvl=19,
        lvl_req=0,
    ),
    "TWITCHTHROE": _Metadata(
        ladder=False,
        code=CodeLiteral("stu"),
        lvl=22,
        lvl_req=0,
    ),
    "DARKGLOW": _Metadata(
        ladder=False,
        code=CodeLiteral("rng"),
        lvl=19,
        lvl_req=0,
    ),
    "HAWKMAIL": _Metadata(
        ladder=False,
        code=CodeLiteral("scl"),
        lvl=20,
        lvl_req=0,
    ),
    "SPARKING_MAIL": _Metadata(
        ladder=False,
        code=CodeLiteral("chn"),
        lvl=23,
        lvl_req=0,
    ),
    "VENOM_WARD": _Metadata(
        ladder=False,
        code=CodeLiteral("brs"),
        lvl=27,
        lvl_req=0,
    ),
    "ICEBLINK": _Metadata(
        ladder=False,
        code=CodeLiteral("spl"),
        lvl=30,
        lvl_req=0,
    ),
    "BONEFLESH": _Metadata(
        ladder=False,
        code=CodeLiteral("plt"),
        lvl=35,
        lvl_req=0,
    ),
    "ROCKFLEECE": _Metadata(
        ladder=False,
        code=CodeLiteral("fld"),
        lvl=38,
        lvl_req=0,
    ),
    "RATTLECAGE": _Metadata(
        ladder=False,
        code=CodeLiteral("gth"),
        lvl=39,
        lvl_req=0,
    ),
    "GOLDSKIN": _Metadata(
        ladder=False,
        code=CodeLiteral("ful"),
        lvl=38,
        lvl_req=0,
    ),
    "SILKS_OF_THE_VICTOR": _Metadata(
        ladder=False,
        code=CodeLiteral("aar"),
        lvl=38,
        lvl_req=0,
    ),
    "HEAVENLY_GARB": _Metadata(
        ladder=False,
        code=CodeLiteral("ltp"),
        lvl=39,
        lvl_req=0,
    ),
    "PELTA_LUNATA": _Metadata(
        ladder=False,
        code=CodeLiteral("buc"),
        lvl=3,
        lvl_req=0,
    ),
    "UMBRAL_DISK": _Metadata(
        ladder=False,
        code=CodeLiteral("sml"),
        lvl=12,
        lvl_req=0,
    ),
    "STORMGUILD": _Metadata(
        ladder=False,
        code=CodeLiteral("lrg"),
        lvl=18,
        lvl_req=0,
    ),
    "WALL_OF_THE_EYELESS": _Metadata(
        ladder=False,
        code=CodeLiteral("bsh"),
        lvl=27,
        lvl_req=0,
    ),
    "SWORDBACK_HOLD": _Metadata(
        ladder=False,
        code=CodeLiteral("spk"),
        lvl=20,
        lvl_req=0,
    ),
    "STEELCLASH": _Metadata(
        ladder=False,
        code=CodeLiteral("kit"),
        lvl=23,
        lvl_req=0,
    ),
    "BVERRIT_KEEP": _Metadata(
        ladder=False,
        code=CodeLiteral("tow"),
        lvl=26,
        lvl_req=0,
    ),
    "THE_WARD": _Metadata(
        ladder=False,
        code=CodeLiteral("gts"),
        lvl=35,
        lvl_req=0,
    ),
    "THE_HAND_OF_BROC": _Metadata(
        ladder=False,
        code=CodeLiteral("lgl"),
        lvl=7,
        lvl_req=0,
    ),
    "BLOODFIST": _Metadata(
        ladder=False,
        code=CodeLiteral("vgl"),
        lvl=12,
        lvl_req=0,
    ),
    "CHANCE_GUARDS": _Metadata(
        ladder=False,
        code=CodeLiteral("mgl"),
        lvl=20,
        lvl_req=0,
    ),
    "MAGEFIST": _Metadata(
        ladder=False,
        code=CodeLiteral("tgl"),
        lvl=31,
        lvl_req=0,
    ),
    "FROSTBURN": _Metadata(
        ladder=False,
        code=CodeLiteral("hgl"),
        lvl=39,
        lvl_req=0,
    ),
    "HOTSPUR": _Metadata(
        ladder=False,
        code=CodeLiteral("lbt"),
        lvl=7,
        lvl_req=0,
    ),
    "GOREFOOT": _Metadata(
        ladder=False,
        code=CodeLiteral("vbt"),
        lvl=12,
        lvl_req=0,
    ),
    "TREADS_OF_CTHON": _Metadata(
        ladder=False,
        code=CodeLiteral("mbt"),
        lvl=20,
        lvl_req=0,
    ),
    "GOBLIN_TOE": _Metadata(
        ladder=False,
        code=CodeLiteral("tbt"),
        lvl=30,
        lvl_req=0,
    ),
    "TEARHAUNCH": _Metadata(
        ladder=False,
        code=CodeLiteral("hbt"),
        lvl=39,
        lvl_req=0,
    ),
    "LENYMO": _Metadata(
        ladder=False,
        code=CodeLiteral("lbl"),
        lvl=10,
        lvl_req=0,
    ),
    "SNAKECORD": _Metadata(
        ladder=False,
        code=CodeLiteral("vbl"),
        lvl=16,
        lvl_req=0,
    ),
    "NIGHTSMOKE": _Metadata(
        ladder=False,
        code=CodeLiteral("mbl"),
        lvl=27,
        lvl_req=0,
    ),
    "GOLDWRAP": _Metadata(
        ladder=False,
        code=CodeLiteral("tbl"),
        lvl=36,
        lvl_req=0,
    ),
    "BLADEBUCKLE": _Metadata(
        ladder=False,
        code=CodeLiteral("hbl"),
        lvl=39,
        lvl_req=0,
    ),
    "NOKOZAN_RELIC": _Metadata(
        ladder=False,
        code=CodeLiteral("amu"),
        lvl=14,
        lvl_req=0,
    ),
    "THE_EYE_OF_ETLICH": _Metadata(
        ladder=False,
        code=CodeLiteral("amu"),
        lvl=20,
        lvl_req=0,
    ),
    "THE_MAHIM_OAK_CURIO": _Metadata(
        ladder=False,
        code=CodeLiteral("amu"),
        lvl=34,
        lvl_req=0,
    ),
    "NAGELRING": _Metadata(
        ladder=False,
        code=CodeLiteral("rin"),
        lvl=10,
        lvl_req=0,
    ),
    "MANALD_HEAL": _Metadata(
        ladder=False,
        code=CodeLiteral("rin"),
        lvl=20,
        lvl_req=0,
    ),
    "THE_STONE_OF_JORDAN": _Metadata(
        ladder=False,
        code=CodeLiteral("rin"),
        lvl=39,
        lvl_req=0,
    ),
    "AMULET_OF_THE_VIPER": _Metadata(
        ladder=False,
        code=CodeLiteral("vip"),
        lvl=0,
        lvl_req=0,
    ),
    "STAFF_OF_KINGS": _Metadata(
        ladder=False,
        code=CodeLiteral("msf"),
        lvl=0,
        lvl_req=0,
    ),
    "HORADRIC_STAFF": _Metadata(
        ladder=False,
        code=CodeLiteral("hst"),
        lvl=0,
        lvl_req=0,
    ),
    "HELL_FORGE_HAMMER": _Metadata(
        ladder=False,
        code=CodeLiteral("hfh"),
        lvl=0,
        lvl_req=0,
    ),
    "KHALIMS_FLAIL": _Metadata(
        ladder=False,
        code=CodeLiteral("qf1"),
        lvl=0,
        lvl_req=0,
    ),
    "KHALIMS_WILL": _Metadata(
        ladder=False,
        code=CodeLiteral("qf2"),
        lvl=0,
        lvl_req=0,
    ),
    "COLDKILL": _Metadata(
        ladder=False,
        code=CodeLiteral("9ha"),
        lvl=44,
        lvl_req=0,
    ),
    "BUTCHERS_PUPIL": _Metadata(
        ladder=False,
        code=CodeLiteral("9ax"),
        lvl=47,
        lvl_req=0,
    ),
    "ISLESTRIKE": _Metadata(
        ladder=False,
        code=CodeLiteral("92a"),
        lvl=51,
        lvl_req=0,
    ),
    "POMPEIIS_WRATH": _Metadata(
        ladder=False,
        code=CodeLiteral("9mp"),
        lvl=53,
        lvl_req=0,
    ),
    "GUARDIAN_NAGA": _Metadata(
        ladder=False,
        code=CodeLiteral("9wa"),
        lvl=56,
        lvl_req=0,
    ),
    "WARLORDS_TRUST": _Metadata(
        ladder=False,
        code=CodeLiteral("9la"),
        lvl=43,
        lvl_req=0,
    ),
    "SPELLSTEEL": _Metadata(
        ladder=False,
        code=CodeLiteral("9ba"),
        lvl=47,
        lvl_req=0,
    ),
    "STORMRIDER": _Metadata(
        ladder=False,
        code=CodeLiteral("9bt"),
        lvl=49,
        lvl_req=0,
    ),
    "BONESLAYER_BLADE": _Metadata(
        ladder=False,
        code=CodeLiteral("9ga"),
        lvl=50,
        lvl_req=0,
    ),
    "THE_MINOTAUR": _Metadata(
        ladder=False,
        code=CodeLiteral("9gi"),
        lvl=53,
        lvl_req=0,
    ),
    "SUICIDE_BRANCH": _Metadata(
        ladder=False,
        code=CodeLiteral("9wn"),
        lvl=41,
        lvl_req=0,
    ),
    "CARIN_SHARD": _Metadata(
        ladder=False,
        code=CodeLiteral("9yw"),
        lvl=43,
        lvl_req=0,
    ),
    "ARM_OF_KING_LEORIC": _Metadata(
        ladder=False,
        code=CodeLiteral("9bw"),
        lvl=44,
        lvl_req=0,
    ),
    "BLACKHAND_KEY": _Metadata(
        ladder=False,
        code=CodeLiteral("9gw"),
        lvl=49,
        lvl_req=0,
    ),
    "DARK_CLAN_CRUSHER": _Metadata(
        ladder=False,
        code=CodeLiteral("9cl"),
        lvl=42,
        lvl_req=0,
    ),
    "ZAKARUMS_HAND": _Metadata(
        ladder=False,
        code=CodeLiteral("9sc"),
        lvl=45,
        lvl_req=0,
    ),
    "THE_FETID_SPRINKLER": _Metadata(
        ladder=False,
        code=CodeLiteral("9qs"),
        lvl=46,
        lvl_req=0,
    ),
    "HAND_OF_BLESSED_LIGHT": _Metadata(
        ladder=False,
        code=CodeLiteral("9ws"),
        lvl=50,
        lvl_req=0,
    ),
    "FLESHRENDER": _Metadata(
        ladder=False,
        code=CodeLiteral("9sp"),
        lvl=46,
        lvl_req=0,
    ),
    "SURESHRILL_FROST": _Metadata(
        ladder=False,
        code=CodeLiteral("9ma"),
        lvl=47,
        lvl_req=0,
    ),
    "MOONFALL": _Metadata(
        ladder=False,
        code=CodeLiteral("9mt"),
        lvl=50,
        lvl_req=0,
    ),
    "BAEZILS_VORTEX": _Metadata(
        ladder=False,
        code=CodeLiteral("9fl"),
        lvl=53,
        lvl_req=0,
    ),
    "EARTHSHAKER": _Metadata(
        ladder=False,
        code=CodeLiteral("9wh"),
        lvl=51,
        lvl_req=0,
    ),
    "BLOODTREE_STUMP": _Metadata(
        ladder=False,
        code=CodeLiteral("9m9"),
        lvl=56,
        lvl_req=0,
    ),
    "THE_GAVEL_OF_PAIN": _Metadata(
        ladder=False,
        code=CodeLiteral("9gm"),
        lvl=53,
        lvl_req=0,
    ),
    "BLOODLETTER": _Metadata(
        ladder=False,
        code=CodeLiteral("9ss"),
        lvl=38,
        lvl_req=0,
    ),
    "COLDSTEEL_EYE": _Metadata(
        ladder=False,
        code=CodeLiteral("9sm"),
        lvl=39,
        lvl_req=0,
    ),
    "HEXFIRE": _Metadata(
        ladder=False,
        code=CodeLiteral("9sb"),
        lvl=41,
        lvl_req=0,
    ),
    "BLADE_OF_ALI_BABA": _Metadata(
        ladder=False,
        code=CodeLiteral("9fc"),
        lvl=43,
        lvl_req=0,
    ),
    "GINTHERS_RIFT": _Metadata(
        ladder=False,
        code=CodeLiteral("9cr"),
        lvl=45,
        lvl_req=0,
    ),
    "HEADSTRIKER": _Metadata(
        ladder=False,
        code=CodeLiteral("9bs"),
        lvl=47,
        lvl_req=0,
    ),
    "PLAGUE_BEARER": _Metadata(
        ladder=False,
        code=CodeLiteral("9ls"),
        lvl=49,
        lvl_req=0,
    ),
    "THE_ATLANTEAN": _Metadata(
        ladder=False,
        code=CodeLiteral("9wd"),
        lvl=50,
        lvl_req=0,
    ),
    "CRAINTE_VOMIR": _Metadata(
        ladder=False,
        code=CodeLiteral("92h"),
        lvl=50,
        lvl_req=0,
    ),
    "BING_SZ_WANG": _Metadata(
        ladder=False,
        code=CodeLiteral("9cm"),
        lvl=51,
        lvl_req=0,
    ),
    "THE_VILE_HUSK": _Metadata(
        ladder=False,
        code=CodeLiteral("9gs"),
        lvl=52,
        lvl_req=0,
    ),
    "CLOUDCRACK": _Metadata(
        ladder=False,
        code=CodeLiteral("9b9"),
        lvl=53,
        lvl_req=0,
    ),
    "TODESFAELLE_FLAMME": _Metadata(
        ladder=False,
        code=CodeLiteral("9fb"),
        lvl=54,
        lvl_req=0,
    ),
    "SWORDGUARD": _Metadata(
        ladder=False,
        code=CodeLiteral("9gd"),
        lvl=55,
        lvl_req=0,
    ),
    "SPINERIPPER": _Metadata(
        ladder=False,
        code=CodeLiteral("9dg"),
        lvl=40,
        lvl_req=0,
    ),
    "HEART_CARVER": _Metadata(
        ladder=False,
        code=CodeLiteral("9di"),
        lvl=44,
        lvl_req=0,
    ),
    "BLACKBOGS_SHARP": _Metadata(
        ladder=False,
        code=CodeLiteral("9kr"),
        lvl=46,
        lvl_req=0,
    ),
    "STORMSPIKE": _Metadata(
        ladder=False,
        code=CodeLiteral("9bl"),
        lvl=49,
        lvl_req=0,
    ),
    "THE_IMPALER": _Metadata(
        ladder=False,
        code=CodeLiteral("9sr"),
        lvl=39,
        lvl_req=0,
    ),
    "KELPIE_SNARE": _Metadata(
        ladder=False,
        code=CodeLiteral("9tr"),
        lvl=41,
        lvl_req=0,
    ),
    "SOULFEAST_TINE": _Metadata(
        ladder=False,
        code=CodeLiteral("9br"),
        lvl=43,
        lvl_req=0,
    ),
    "HONE_SUNDAN": _Metadata(
        ladder=False,
        code=CodeLiteral("9st"),
        lvl=45,
        lvl_req=0,
    ),
    "SPIRE_OF_HONOR": _Metadata(
        ladder=False,
        code=CodeLiteral("9p9"),
        lvl=47,
        lvl_req=0,
    ),
    "THE_MEAT_SCRAPER": _Metadata(
        ladder=False,
        code=CodeLiteral("9b7"),
        lvl=49,
        lvl_req=0,
    ),
    "BLACKLEACH_BLADE": _Metadata(
        ladder=False,
        code=CodeLiteral("9vo"),
        lvl=50,
        lvl_req=0,
    ),
    "ATHENAS_WRATH": _Metadata(
        ladder=False,
        code=CodeLiteral("9s8"),
        lvl=50,
        lvl_req=0,
    ),
    "PIERRE_TOMBALE_COUANT": _Metadata(
        ladder=False,
        code=CodeLiteral("9pa"),
        lvl=51,
        lvl_req=0,
    ),
    "HUSOLDAL_EVO": _Metadata(
        ladder=False,
        code=CodeLiteral("9h9"),
        lvl=52,
        lvl_req=0,
    ),
    "GRIMS_BURNING_DEAD": _Metadata(
        ladder=False,
        code=CodeLiteral("9wc"),
        lvl=52,
        lvl_req=0,
    ),
    "RAZORSWITCH": _Metadata(
        ladder=False,
        code=CodeLiteral("8ss"),
        lvl=36,
        lvl_req=0,
    ),
    "RIBCRACKER": _Metadata(
        ladder=False,
        code=CodeLiteral("8ls"),
        lvl=39,
        lvl_req=0,
    ),
    "CHROMATIC_IRE": _Metadata(
        ladder=False,
        code=CodeLiteral("8cs"),
        lvl=43,
        lvl_req=0,
    ),
    "WARPSPEAR": _Metadata(
        ladder=False,
        code=CodeLiteral("8bs"),
        lvl=47,
        lvl_req=0,
    ),
    "SKULL_COLLECTOR": _Metadata(
        ladder=False,
        code=CodeLiteral("8ws"),
        lvl=49,
        lvl_req=0,
    ),
    "SKYSTRIKE": _Metadata(
        ladder=False,
        code=CodeLiteral("8sb"),
        lvl=36,
        lvl_req=0,
    ),
    "RIPHOOK": _Metadata(
        ladder=False,
        code=CodeLiteral("8hb"),
        lvl=39,
        lvl_req=0,
    ),
    "KUKO_SHAKAKU": _Metadata(
        ladder=False,
        code=CodeLiteral("8lb"),
        lvl=41,
        lvl_req=0,
    ),
    "ENDLESSHAIL": _Metadata(
        ladder=False,
        code=CodeLiteral("8cb"),
        lvl=44,
        lvl_req=0,
    ),
    "WITCHWILD_STRING": _Metadata(
        ladder=False,
        code=CodeLiteral("8s8"),
        lvl=47,
        lvl_req=0,
    ),
    "CLIFFKILLER": _Metadata(
        ladder=False,
        code=CodeLiteral("8l8"),
        lvl=49,
        lvl_req=0,
    ),
    "MAGEWRATH": _Metadata(
        ladder=False,
        code=CodeLiteral("8sw"),
        lvl=51,
        lvl_req=0,
    ),
    "GOLDSTRIKE_ARCH": _Metadata(
        ladder=False,
        code=CodeLiteral("8lw"),
        lvl=54,
        lvl_req=0,
    ),
    "LANGER_BRISER": _Metadata(
        ladder=False,
        code=CodeLiteral("8lx"),
        lvl=40,
        lvl_req=0,
    ),
    "PUS_SPITTER": _Metadata(
        ladder=False,
        code=CodeLiteral("8mx"),
        lvl=44,
        lvl_req=0,
    ),
    "BURIZA_DO_KYANON": _Metadata(
        ladder=False,
        code=CodeLiteral("8hx"),
        lvl=59,
        lvl_req=0,
    ),
    "DEMON_MACHINE": _Metadata(
        ladder=False,
        code=CodeLiteral("8rx"),
        lvl=57,
        lvl_req=0,
    ),
    "PEASANT_CROWN": _Metadata(
        ladder=False,
        code=CodeLiteral("xap"),
        lvl=36,
        lvl_req=0,
    ),
    "ROCKSTOPPER": _Metadata(
        ladder=False,
        code=CodeLiteral("xkp"),
        lvl=39,
        lvl_req=0,
    ),
    "STEALSKULL": _Metadata(
        ladder=False,
        code=CodeLiteral("xlm"),
        lvl=43,
        lvl_req=0,
    ),
    "DARKSIGHT_HELM": _Metadata(
        ladder=False,
        code=CodeLiteral("xhl"),
        lvl=46,
        lvl_req=0,
    ),
    "VALKYRIE_WING": _Metadata(
        ladder=False,
        code=CodeLiteral("xhm"),
        lvl=52,
        lvl_req=0,
    ),
    "CROWN_OF_THIEVES": _Metadata(
        ladder=False,
        code=CodeLiteral("xrn"),
        lvl=57,
        lvl_req=0,
    ),
    "BLACKHORNS_FACE": _Metadata(
        ladder=False,
        code=CodeLiteral("xsk"),
        lvl=49,
        lvl_req=0,
    ),
    "VAMPIRE_GAZE": _Metadata(
        ladder=False,
        code=CodeLiteral("xh9"),
        lvl=49,
        lvl_req=0,
    ),
    "THE_SPIRIT_SHROUD": _Metadata(
        ladder=False,
        code=CodeLiteral("xui"),
        lvl=36,
        lvl_req=0,
    ),
    "SKIN_OF_THE_VIPERMAGI": _Metadata(
        ladder=False,
        code=CodeLiteral("xea"),
        lvl=37,
        lvl_req=0,
    ),
    "SKIN_OF_THE_FLAYED_ONE": _Metadata(
        ladder=False,
        code=CodeLiteral("xla"),
        lvl=39,
        lvl_req=0,
    ),
    "IRON_PELT": _Metadata(
        ladder=False,
        code=CodeLiteral("xtu"),
        lvl=41,
        lvl_req=0,
    ),
    "SPIRIT_FORGE": _Metadata(
        ladder=False,
        code=CodeLiteral("xng"),
        lvl=43,
        lvl_req=0,
    ),
    "CROW_CAW": _Metadata(
        ladder=False,
        code=CodeLiteral("xcl"),
        lvl=45,
        lvl_req=0,
    ),
    "SHAFTSTOP": _Metadata(
        ladder=False,
        code=CodeLiteral("xhn"),
        lvl=46,
        lvl_req=0,
    ),
    "DURIELS_SHELL": _Metadata(
        ladder=False,
        code=CodeLiteral("xrs"),
        lvl=49,
        lvl_req=0,
    ),
    "SKULLDERS_IRE": _Metadata(
        ladder=False,
        code=CodeLiteral("xpl"),
        lvl=50,
        lvl_req=0,
    ),
    "GUARDIAN_ANGEL": _Metadata(
        ladder=False,
        code=CodeLiteral("xlt"),
        lvl=53,
        lvl_req=0,
    ),
    "TOOTHROW": _Metadata(
        ladder=False,
        code=CodeLiteral("xld"),
        lvl=56,
        lvl_req=0,
    ),
    "ATMAS_WAIL": _Metadata(
        ladder=False,
        code=CodeLiteral("xth"),
        lvl=59,
        lvl_req=0,
    ),
    "BLACK_HADES": _Metadata(
        ladder=False,
        code=CodeLiteral("xul"),
        lvl=61,
        lvl_req=0,
    ),
    "CORPSEMOURN": _Metadata(
        ladder=False,
        code=CodeLiteral("xar"),
        lvl=63,
        lvl_req=0,
    ),
    "QUE_HEGANS_WISDOM": _Metadata(
        ladder=False,
        code=CodeLiteral("xtp"),
        lvl=59,
        lvl_req=0,
    ),
    "VISCERATUANT": _Metadata(
        ladder=False,
        code=CodeLiteral("xuc"),
        lvl=36,
        lvl_req=0,
    ),
    "MOSERS_BLESSED_CIRCLE": _Metadata(
        ladder=False,
        code=CodeLiteral("xml"),
        lvl=39,
        lvl_req=0,
    ),
    "STORMCHASER": _Metadata(
        ladder=False,
        code=CodeLiteral("xrg"),
        lvl=43,
        lvl_req=0,
    ),
    "TIAMATS_REBUKE": _Metadata(
        ladder=False,
        code=CodeLiteral("xit"),
        lvl=46,
        lvl_req=0,
    ),
    "GERKES_SANCTUARY": _Metadata(
        ladder=False,
        code=CodeLiteral("xow"),
        lvl=52,
        lvl_req=0,
    ),
    "RADAMENTS_SPHERE": _Metadata(
        ladder=False,
        code=CodeLiteral("xts"),
        lvl=58,
        lvl_req=0,
    ),
    "LIDLESS_WALL": _Metadata(
        ladder=False,
        code=CodeLiteral("xsh"),
        lvl=49,
        lvl_req=0,
    ),
    "LANCE_GUARD": _Metadata(
        ladder=False,
        code=CodeLiteral("xpk"),
        lvl=43,
        lvl_req=0,
    ),
    "VENOM_GRIP": _Metadata(
        ladder=False,
        code=CodeLiteral("xlg"),
        lvl=37,
        lvl_req=0,
    ),
    "GRAVEPALM": _Metadata(
        ladder=False,
        code=CodeLiteral("xvg"),
        lvl=39,
        lvl_req=0,
    ),
    "GHOULHIDE": _Metadata(
        ladder=False,
        code=CodeLiteral("xmg"),
        lvl=44,
        lvl_req=0,
    ),
    "LAVA_GOUT": _Metadata(
        ladder=False,
        code=CodeLiteral("xtg"),
        lvl=50,
        lvl_req=0,
    ),
    "HELLMOUTH": _Metadata(
        ladder=False,
        code=CodeLiteral("xhg"),
        lvl=55,
        lvl_req=0,
    ),
    "INFERNOSTRIDE": _Metadata(
        ladder=False,
        code=CodeLiteral("xlb"),
        lvl=37,
        lvl_req=0,
    ),
    "WATERWALK": _Metadata(
        ladder=False,
        code=CodeLiteral("xvb"),
        lvl=40,
        lvl_req=0,
    ),
    "SILKWEAVE": _Metadata(
        ladder=False,
        code=CodeLiteral("xmb"),
        lvl=44,
        lvl_req=0,
    ),
    "WAR_TRAVELER": _Metadata(
        ladder=False,
        code=CodeLiteral("xtb"),
        lvl=50,
        lvl_req=0,
    ),
    "GORE_RIDER": _Metadata(
        ladder=False,
        code=CodeLiteral("xhb"),
        lvl=55,
        lvl_req=0,
    ),
    "STRING_OF_EARS": _Metadata(
        ladder=False,
        code=CodeLiteral("zlb"),
        lvl=37,
        lvl_req=0,
    ),
    "RAZORTAIL": _Metadata(
        ladder=False,
        code=CodeLiteral("zvb"),
        lvl=39,
        lvl_req=0,
    ),
    "GLOOMS_TRAP": _Metadata(
        ladder=False,
        code=CodeLiteral("zmb"),
        lvl=45,
        lvl_req=0,
    ),
    "SNOWCLASH": _Metadata(
        ladder=False,
        code=CodeLiteral("ztb"),
        lvl=49,
        lvl_req=0,
    ),
    "THUNDERGODS_VIGOR": _Metadata(
        ladder=False,
        code=CodeLiteral("zhb"),
        lvl=55,
        lvl_req=0,
    ),
    "HARLEQUIN_CREST": _Metadata(
        ladder=False,
        code=CodeLiteral("uap"),
        lvl=69,
        lvl_req=0,
    ),
    "VEIL_OF_STEEL": _Metadata(
        ladder=False,
        code=CodeLiteral("uhm"),
        lvl=77,
        lvl_req=0,
    ),
    "THE_GLADIATORS_BANE": _Metadata(
        ladder=False,
        code=CodeLiteral("utu"),
        lvl=85,
        lvl_req=0,
    ),
    "ARKAINES_VALOR": _Metadata(
        ladder=False,
        code=CodeLiteral("upl"),
        lvl=85,
        lvl_req=0,
    ),
    "BLACKOAK_SHIELD": _Metadata(
        ladder=False,
        code=CodeLiteral("uml"),
        lvl=67,
        lvl_req=0,
    ),
    "STORMSHIELD": _Metadata(
        ladder=False,
        code=CodeLiteral("uit"),
        lvl=77,
        lvl_req=0,
    ),
    "HELLSLAYER": _Metadata(
        ladder=False,
        code=CodeLiteral("7bt"),
        lvl=71,
        lvl_req=0,
    ),
    "MESSERSCHMIDTS_REAVER": _Metadata(
        ladder=False,
        code=CodeLiteral("7ga"),
        lvl=75,
        lvl_req=0,
    ),
    "BARANARS_STAR": _Metadata(
        ladder=False,
        code=CodeLiteral("7mt"),
        lvl=70,
        lvl_req=0,
    ),
    "SCHAEFERS_HAMMER": _Metadata(
        ladder=False,
        code=CodeLiteral("7wh"),
        lvl=83,
        lvl_req=0,
    ),
    "THE_CRANIUM_BASHER": _Metadata(
        ladder=False,
        code=CodeLiteral("7gm"),
        lvl=85,
        lvl_req=0,
    ),
    "LIGHTSABRE": _Metadata(
        ladder=False,
        code=CodeLiteral("7cr"),
        lvl=66,
        lvl_req=0,
    ),
    "DOOMBRINGER": _Metadata(
        ladder=False,
        code=CodeLiteral("7b7"),
        lvl=75,
        lvl_req=0,
    ),
    "THE_GRANDFATHER": _Metadata(
        ladder=False,
        code=CodeLiteral("7gd"),
        lvl=85,
        lvl_req=0,
    ),
    "WIZARDSPIKE": _Metadata(
        ladder=False,
        code=CodeLiteral("7dg"),
        lvl=69,
        lvl_req=0,
    ),
    "CONSTRICTING_LOOP": _Metadata(
        ladder=False,
        code=CodeLiteral("rin"),
        lvl=73,
        lvl_req=0,
    ),
    "STORMSPIRE": _Metadata(
        ladder=False,
        code=CodeLiteral("7wc"),
        lvl=78,
        lvl_req=0,
    ),
    "EAGLEHORN": _Metadata(
        ladder=False,
        code=CodeLiteral("6l7"),
        lvl=77,
        lvl_req=0,
    ),
    "WINDFORCE": _Metadata(
        ladder=False,
        code=CodeLiteral("6lw"),
        lvl=80,
        lvl_req=0,
    ),
    "BUL_KATHOS_WEDDING_BAND": _Metadata(
        ladder=False,
        code=CodeLiteral("rin"),
        lvl=66,
        lvl_req=0,
    ),
    "THE_CATS_EYE": _Metadata(
        ladder=False,
        code=CodeLiteral("amu"),
        lvl=58,
        lvl_req=0,
    ),
    "THE_RISING_SUN": _Metadata(
        ladder=False,
        code=CodeLiteral("amu"),
        lvl=73,
        lvl_req=0,
    ),
    "CRESCENT_MOON": _Metadata(
        ladder=False,
        code=CodeLiteral("amu"),
        lvl=58,
        lvl_req=0,
    ),
    "MARAS_KALEIDOSCOPE": _Metadata(
        ladder=False,
        code=CodeLiteral("amu"),
        lvl=80,
        lvl_req=0,
    ),
    "ATMAS_SCARAB": _Metadata(
        ladder=False,
        code=CodeLiteral("amu"),
        lvl=60,
        lvl_req=0,
    ),
    "DWARF_STAR": _Metadata(
        ladder=False,
        code=CodeLiteral("rin"),
        lvl=53,
        lvl_req=0,
    ),
    "RAVEN_FROST": _Metadata(
        ladder=False,
        code=CodeLiteral("rin"),
        lvl=53,
        lvl_req=0,
    ),
    "HIGHLORDS_WRATH": _Metadata(
        ladder=False,
        code=CodeLiteral("amu"),
        lvl=73,
        lvl_req=0,
    ),
    "SARACENS_CHANCE": _Metadata(
        ladder=False,
        code=CodeLiteral("amu"),
        lvl=55,
        lvl_req=0,
    ),
    "ARREATS_FACE": _Metadata(
        ladder=False,
        code=CodeLiteral("baa"),
        lvl=50,
        lvl_req=0,
    ),
    "HOMUNCULUS": _Metadata(
        ladder=False,
        code=CodeLiteral("nea"),
        lvl=50,
        lvl_req=0,
    ),
    "TITANS_REVENGE": _Metadata(
        ladder=False,
        code=CodeLiteral("ama"),
        lvl=50,
        lvl_req=0,
    ),
    "LYCANDERS_AIM": _Metadata(
        ladder=False,
        code=CodeLiteral("am7"),
        lvl=50,
        lvl_req=0,
    ),
    "LYCANDERS_FLANK": _Metadata(
        ladder=False,
        code=CodeLiteral("am9"),
        lvl=50,
        lvl_req=0,
    ),
    "THE_OCULUS": _Metadata(
        ladder=False,
        code=CodeLiteral("oba"),
        lvl=50,
        lvl_req=0,
    ),
    "HERALD_OF_ZAKARUM": _Metadata(
        ladder=False,
        code=CodeLiteral("pa9"),
        lvl=50,
        lvl_req=0,
    ),
    "BARTUCS_CUT_THROAT": _Metadata(
        ladder=False,
        code=CodeLiteral("9tw"),
        lvl=50,
        lvl_req=0,
    ),
    "JALALS_MANE": _Metadata(
        ladder=False,
        code=CodeLiteral("dra"),
        lvl=50,
        lvl_req=0,
    ),
    "THE_SCALPER": _Metadata(
        ladder=False,
        code=CodeLiteral("9ta"),
        lvl=65,
        lvl_req=0,
    ),
    "BLOODMOON": _Metadata(
        ladder=False,
        code=CodeLiteral("7sb"),
        lvl=69,
        lvl_req=0,
    ),
    "DJINN_SLAYER": _Metadata(
        ladder=False,
        code=CodeLiteral("7sm"),
        lvl=73,
        lvl_req=0,
    ),
    "DEATHBIT": _Metadata(
        ladder=False,
        code=CodeLiteral("9tk"),
        lvl=52,
        lvl_req=0,
    ),
    "WARSHRIKE": _Metadata(
        ladder=False,
        code=CodeLiteral("7bk"),
        lvl=83,
        lvl_req=0,
    ),
    "GUT_SIPHON": _Metadata(
        ladder=False,
        code=CodeLiteral("6rx"),
        lvl=79,
        lvl_req=0,
    ),
    "RAZORS_EDGE": _Metadata(
        ladder=False,
        code=CodeLiteral("7ha"),
        lvl=75,
        lvl_req=0,
    ),
    "DEMON_LIMB": _Metadata(
        ladder=False,
        code=CodeLiteral("7sp"),
        lvl=71,
        lvl_req=0,
    ),
    "STEEL_SHADE": _Metadata(
        ladder=False,
        code=CodeLiteral("ulm"),
        lvl=70,
        lvl_req=0,
    ),
    "TOMB_REAVER": _Metadata(
        ladder=False,
        code=CodeLiteral("7pa"),
        lvl=86,
        lvl_req=0,
    ),
    "DEATHS_WEB": _Metadata(
        ladder=False,
        code=CodeLiteral("7gw"),
        lvl=74,
        lvl_req=0,
    ),
    "NATURES_PEACE": _Metadata(
        ladder=False,
        code=CodeLiteral("rin"),
        lvl=77,
        lvl_req=0,
    ),
    "AZUREWRATH": _Metadata(
        ladder=False,
        code=CodeLiteral("7cr"),
        lvl=87,
        lvl_req=0,
    ),
    "SERAPHS_HYMN": _Metadata(
        ladder=False,
        code=CodeLiteral("amu"),
        lvl=73,
        lvl_req=0,
    ),
    "FLESHRIPPER": _Metadata(
        ladder=False,
        code=CodeLiteral("7kr"),
        lvl=76,
        lvl_req=0,
    ),
    "ODIUM": _Metadata(
        ladder=False,
        code=CodeLiteral("7fb"),
        lvl=87,
        lvl_req=0,
    ),
    "HORIZONS_TORNADO": _Metadata(
        ladder=False,
        code=CodeLiteral("7fl"),
        lvl=72,
        lvl_req=0,
    ),
    "STONE_CRUSHER": _Metadata(
        ladder=False,
        code=CodeLiteral("7wh"),
        lvl=76,
        lvl_req=0,
    ),
    "JADE_TALON": _Metadata(
        ladder=False,
        code=CodeLiteral("7wb"),
        lvl=74,
        lvl_req=0,
    ),
    "SHADOW_DANCER": _Metadata(
        ladder=False,
        code=CodeLiteral("uhb"),
        lvl=79,
        lvl_req=0,
    ),
    "CEREBUS_BITE": _Metadata(
        ladder=False,
        code=CodeLiteral("drb"),
        lvl=71,
        lvl_req=0,
    ),
    "TYRAELS_MIGHT": _Metadata(
        ladder=False,
        code=CodeLiteral("uar"),
        lvl=87,
        lvl_req=0,
    ),
    "SOUL_DRAINER": _Metadata(
        ladder=False,
        code=CodeLiteral("umg"),
        lvl=82,
        lvl_req=0,
    ),
    "RUNE_MASTER": _Metadata(
        ladder=False,
        code=CodeLiteral("72a"),
        lvl=80,
        lvl_req=0,
    ),
    "DEATH_CLEAVER": _Metadata(
        ladder=False,
        code=CodeLiteral("7wa"),
        lvl=78,
        lvl_req=0,
    ),
    "EXECUTIONERS_JUSTICE": _Metadata(
        ladder=False,
        code=CodeLiteral("7gi"),
        lvl=83,
        lvl_req=0,
    ),
    "STONERAVEN": _Metadata(
        ladder=False,
        code=CodeLiteral("amd"),
        lvl=72,
        lvl_req=0,
    ),
    "LEVIATHAN": _Metadata(
        ladder=False,
        code=CodeLiteral("uld"),
        lvl=73,
        lvl_req=0,
    ),
    "WISP_PROJECTOR": _Metadata(
        ladder=False,
        code=CodeLiteral("rin"),
        lvl=84,
        lvl_req=0,
    ),
    "GARGOYLES_BITE": _Metadata(
        ladder=False,
        code=CodeLiteral("7ts"),
        lvl=78,
        lvl_req=0,
    ),
    "LACERATOR": _Metadata(
        ladder=False,
        code=CodeLiteral("7b8"),
        lvl=76,
        lvl_req=0,
    ),
    "MANG_SONGS_LESSON": _Metadata(
        ladder=False,
        code=CodeLiteral("6ws"),
        lvl=86,
        lvl_req=0,
    ),
    "VIPERFORK": _Metadata(
        ladder=False,
        code=CodeLiteral("7br"),
        lvl=79,
        lvl_req=0,
    ),
    "ETHEREAL_EDGE": _Metadata(
        ladder=False,
        code=CodeLiteral("7ba"),
        lvl=82,
        lvl_req=0,
    ),
    "DEMONHORNS_EDGE": _Metadata(
        ladder=False,
        code=CodeLiteral("bad"),
        lvl=69,
        lvl_req=0,
    ),
    "THE_REAPERS_TOLL": _Metadata(
        ladder=False,
        code=CodeLiteral("7s8"),
        lvl=83,
        lvl_req=0,
    ),
    "SPIRIT_KEEPER": _Metadata(
        ladder=False,
        code=CodeLiteral("drd"),
        lvl=75,
        lvl_req=0,
    ),
    "HELLRACK": _Metadata(
        ladder=False,
        code=CodeLiteral("6hx"),
        lvl=84,
        lvl_req=0,
    ),
    "ALMA_NEGRA": _Metadata(
        ladder=False,
        code=CodeLiteral("pac"),
        lvl=85,
        lvl_req=0,
    ),
    "DARKFORCE_SPAWN": _Metadata(
        ladder=False,
        code=CodeLiteral("nef"),
        lvl=72,
        lvl_req=0,
    ),
    "WIDOWMAKER": _Metadata(
        ladder=False,
        code=CodeLiteral("6sw"),
        lvl=73,
        lvl_req=0,
    ),
    "BLOOD_RAVENS_CHARGE": _Metadata(
        ladder=False,
        code=CodeLiteral("amb"),
        lvl=79,
        lvl_req=0,
    ),
    "GHOSTFLAME": _Metadata(
        ladder=False,
        code=CodeLiteral("7bl"),
        lvl=70,
        lvl_req=0,
    ),
    "SHADOW_KILLER": _Metadata(
        ladder=False,
        code=CodeLiteral("7cs"),
        lvl=85,
        lvl_req=0,
    ),
    "GIMMERSHRED": _Metadata(
        ladder=False,
        code=CodeLiteral("7ta"),
        lvl=78,
        lvl_req=0,
    ),
    "GRIFFONS_EYE": _Metadata(
        ladder=False,
        code=CodeLiteral("ci3"),
        lvl=84,
        lvl_req=0,
    ),
    "WINDHAMMER": _Metadata(
        ladder=False,
        code=CodeLiteral("7m7"),
        lvl=76,
        lvl_req=0,
    ),
    "THUNDERSTROKE": _Metadata(
        ladder=False,
        code=CodeLiteral("amf"),
        lvl=77,
        lvl_req=0,
    ),
    "DEMONS_ARCH": _Metadata(
        ladder=False,
        code=CodeLiteral("7s7"),
        lvl=76,
        lvl_req=0,
    ),
    "BONEFLAME": _Metadata(
        ladder=False,
        code=CodeLiteral("nee"),
        lvl=80,
        lvl_req=0,
    ),
    "STEEL_PILLAR": _Metadata(
        ladder=False,
        code=CodeLiteral("7p7"),
        lvl=77,
        lvl_req=0,
    ),
    "NIGHTWINGS_VEIL": _Metadata(
        ladder=False,
        code=CodeLiteral("uhm"),
        lvl=75,
        lvl_req=0,
    ),
    "CROWN_OF_AGES": _Metadata(
        ladder=False,
        code=CodeLiteral("urn"),
        lvl=86,
        lvl_req=0,
    ),
    "ANDARIELS_VISAGE": _Metadata(
        ladder=False,
        code=CodeLiteral("usk"),
        lvl=85,
        lvl_req=0,
    ),
    "DRAGONSCALE": _Metadata(
        ladder=False,
        code=CodeLiteral("pae"),
        lvl=84,
        lvl_req=0,
    ),
    "STEEL_CARAPACE": _Metadata(
        ladder=False,
        code=CodeLiteral("uul"),
        lvl=74,
        lvl_req=0,
    ),
    "MEDUSAS_GAZE": _Metadata(
        ladder=False,
        code=CodeLiteral("uow"),
        lvl=84,
        lvl_req=0,
    ),
    "RAVENLORE": _Metadata(
        ladder=False,
        code=CodeLiteral("dre"),
        lvl=82,
        lvl_req=0,
    ),
    "BONESHADE": _Metadata(
        ladder=False,
        code=CodeLiteral("7bw"),
        lvl=84,
        lvl_req=0,
    ),
    "FLAMEBELLOW": _Metadata(
        ladder=False,
        code=CodeLiteral("7gs"),
        lvl=79,
        lvl_req=0,
    ),
    "DEATHS_FATHOM": _Metadata(
        ladder=False,
        code=CodeLiteral("obf"),
        lvl=81,
        lvl_req=0,
    ),
    "WOLFHOWL": _Metadata(
        ladder=False,
        code=CodeLiteral("bac"),
        lvl=85,
        lvl_req=0,
    ),
    "SPIRIT_WARD": _Metadata(
        ladder=False,
        code=CodeLiteral("uts"),
        lvl=76,
        lvl_req=0,
    ),
    "KIRAS_GUARDIAN": _Metadata(
        ladder=False,
        code=CodeLiteral("ci2"),
        lvl=85,
        lvl_req=0,
    ),
    "ORMUS_ROBES": _Metadata(
        ladder=False,
        code=CodeLiteral("uui"),
        lvl=83,
        lvl_req=0,
    ),
    "GHEEDS_FORTUNE": _Metadata(
        ladder=False,
        code=CodeLiteral("cm3"),
        lvl=70,
        lvl_req=0,
    ),
    "STORMLASH": _Metadata(
        ladder=False,
        code=CodeLiteral("7fl"),
        lvl=86,
        lvl_req=0,
    ),
    "HALABERDS_REIGN": _Metadata(
        ladder=False,
        code=CodeLiteral("bae"),
        lvl=85,
        lvl_req=0,
    ),
    "SPIKE_THORN": _Metadata(
        ladder=False,
        code=CodeLiteral("upk"),
        lvl=78,
        lvl_req=0,
    ),
    "DRACULS_GRASP": _Metadata(
        ladder=False,
        code=CodeLiteral("uvg"),
        lvl=84,
        lvl_req=0,
    ),
    "FROSTWIND": _Metadata(
        ladder=False,
        code=CodeLiteral("7ls"),
        lvl=78,
        lvl_req=0,
    ),
    "TEMPLARS_MIGHT": _Metadata(
        ladder=False,
        code=CodeLiteral("uar"),
        lvl=82,
        lvl_req=0,
    ),
    "ESCHUTAS_TEMPER": _Metadata(
        ladder=False,
        code=CodeLiteral("obc"),
        lvl=80,
        lvl_req=0,
    ),
    "FIRELIZARDS_TALONS": _Metadata(
        ladder=False,
        code=CodeLiteral("7lw"),
        lvl=75,
        lvl_req=0,
    ),
    "SANDSTORM_TREK": _Metadata(
        ladder=False,
        code=CodeLiteral("uvb"),
        lvl=72,
        lvl_req=0,
    ),
    "MARROWWALK": _Metadata(
        ladder=False,
        code=CodeLiteral("umb"),
        lvl=74,
        lvl_req=0,
    ),
    "HEAVENS_LIGHT": _Metadata(
        ladder=False,
        code=CodeLiteral("7sc"),
        lvl=69,
        lvl_req=0,
    ),
    "MERMANS_SPROCKET": _Metadata(
        ladder=False,
        code=CodeLiteral("ulb"),
        lvl=45,
        lvl_req=0,
    ),
    "ARACHNID_MESH": _Metadata(
        ladder=False,
        code=CodeLiteral("ulc"),
        lvl=87,
        lvl_req=0,
    ),
    "NOSFERATUS_COIL": _Metadata(
        ladder=False,
        code=CodeLiteral("uvc"),
        lvl=68,
        lvl_req=0,
    ),
    "METALGRID": _Metadata(
        ladder=False,
        code=CodeLiteral("amu"),
        lvl=85,
        lvl_req=0,
    ),
    "VERDUNGOS_HEARTY_CORD": _Metadata(
        ladder=False,
        code=CodeLiteral("umc"),
        lvl=71,
        lvl_req=0,
    ),
    "SIGGARDS_STAUNCH": _Metadata(
        ladder=False,
        code=CodeLiteral("uhc"),
        lvl=80,
        lvl_req=0,
    ),
    "CARRION_WIND": _Metadata(
        ladder=False,
        code=CodeLiteral("rin"),
        lvl=68,
        lvl_req=0,
    ),
    "GIANT_SKULL": _Metadata(
        ladder=False,
        code=CodeLiteral("uh9"),
        lvl=73,
        lvl_req=0,
    ),
    "ASTREONS_IRON_WARD": _Metadata(
        ladder=False,
        code=CodeLiteral("7ws"),
        lvl=68,
        lvl_req=0,
    ),
    "ANNIHILUS": _Metadata(
        ladder=False,
        code=CodeLiteral("cm1"),
        lvl=130,
        lvl_req=0,
    ),
    "ARIOCS_NEEDLE": _Metadata(
        ladder=False,
        code=CodeLiteral("7sr"),
        lvl=85,
        lvl_req=0,
    ),
    "CRANEBEAK": _Metadata(
        ladder=False,
        code=CodeLiteral("7mp"),
        lvl=71,
        lvl_req=0,
    ),
    "NORDS_TENDERIZER": _Metadata(
        ladder=False,
        code=CodeLiteral("7cl"),
        lvl=76,
        lvl_req=0,
    ),
    "EARTH_SHIFTER": _Metadata(
        ladder=False,
        code=CodeLiteral("7gm"),
        lvl=77,
        lvl_req=0,
    ),
    "WRAITH_FLIGHT": _Metadata(
        ladder=False,
        code=CodeLiteral("7gl"),
        lvl=84,
        lvl_req=0,
    ),
    "BONEHEW": _Metadata(
        ladder=False,
        code=CodeLiteral("7o7"),
        lvl=72,
        lvl_req=0,
    ),
    "ONDALS_WISDOM": _Metadata(
        ladder=False,
        code=CodeLiteral("6cs"),
        lvl=74,
        lvl_req=0,
    ),
    "THE_REDEEMER": _Metadata(
        ladder=False,
        code=CodeLiteral("7sc"),
        lvl=80,
        lvl_req=0,
    ),
    "HEAD_HUNTERS_GLORY": _Metadata(
        ladder=False,
        code=CodeLiteral("ush"),
        lvl=83,
        lvl_req=0,
    ),
    "STEELREND": _Metadata(
        ladder=False,
        code=CodeLiteral("uhg"),
        lvl=78,
        lvl_req=0,
    ),
    "RAINBOW_FACET": _Metadata(
        ladder=False,
        code=CodeLiteral("jew"),
        lvl=85,
        lvl_req=0,
    ),
    "HELLFIRE_TORCH": _Metadata(
        ladder=False,
        code=CodeLiteral("cm2"),
        lvl=120,
        lvl_req=0,
    ),
    "ITHERAELS_PATH": _Metadata(
        ladder=False,
        code=CodeLiteral("utb"),
        lvl=131,
        lvl_req=0,
    ),
    "OVERLORDS_HELM": _Metadata(
        ladder=False,
        code=CodeLiteral("uhl"),
        lvl=131,
        lvl_req=0,
    ),
    "DARK_ABYSS": _Metadata(
        ladder=False,
        code=CodeLiteral("uth"),
        lvl=131,
        lvl_req=0,
    ),
    "AIDANS_SCAR": _Metadata(
        ladder=False,
        code=CodeLiteral("7qr"),
        lvl=131,
        lvl_req=0,
    ),
    "HADRIELS_HAND": _Metadata(
        ladder=False,
        code=CodeLiteral("7bs"),
        lvl=131,
        lvl_req=0,
    ),
    "TRUE_SILVER": _Metadata(
        ladder=False,
        code=CodeLiteral("am5"),
        lvl=24,
        lvl_req=0,
    ),
    "QUETZALCOATL": _Metadata(
        ladder=False,
        code=CodeLiteral("dr2"),
        lvl=35,
        lvl_req=0,
    ),
    "CYCLOPEAN_ROAR": _Metadata(
        ladder=False,
        code=CodeLiteral("ba6"),
        lvl=34,
        lvl_req=0,
    ),
    "SANKEKURS_FALL": _Metadata(
        ladder=False,
        code=CodeLiteral("pa3"),
        lvl=37,
        lvl_req=0,
    ),
    "MAGE_SLAYER": _Metadata(
        ladder=False,
        code=CodeLiteral("9ar"),
        lvl=32,
        lvl_req=0,
    ),
    "KALANS_LEGACY": _Metadata(
        ladder=False,
        code=CodeLiteral("ne6"),
        lvl=30,
        lvl_req=0,
    ),
    "TEMPEST": _Metadata(
        ladder=False,
        code=CodeLiteral("ob6"),
        lvl=28,
        lvl_req=0,
    ),
    "BAND_OF_SKULLS": _Metadata(
        ladder=False,
        code=CodeLiteral("rbe"),
        lvl=131,
        lvl_req=0,
    ),
    "CAGE_OF_THE_UNSULLIED": _Metadata(
        ladder=False,
        code=CodeLiteral("rar"),
        lvl=131,
        lvl_req=0,
    ),
    "THE_THIRD_EYE": _Metadata(
        ladder=False,
        code=CodeLiteral("ram"),
        lvl=131,
        lvl_req=0,
    ),
    "ZERAES_RESOLVE": _Metadata(
        ladder=False,
        code=CodeLiteral("ame"),
        lvl=87,
        lvl_req=0,
    ),
    "OCCULTIST": _Metadata(
        ladder=False,
        code=CodeLiteral("utg"),
        lvl=87,
        lvl_req=0,
    ),
    "BRIMSTONE_RAIN": _Metadata(
        ladder=False,
        code=CodeLiteral("6bs"),
        lvl=87,
        lvl_req=0,
    ),
    "AKARATS_DEVOTION": _Metadata(
        ladder=False,
        code=CodeLiteral("7qs"),
        lvl=87,
        lvl_req=0,
    ),
    "MARTYRDOM": _Metadata(
        ladder=False,
        code=CodeLiteral("ned"),
        lvl=87,
        lvl_req=0,
    ),
    "STALKERS_CULL": _Metadata(
        ladder=False,
        code=CodeLiteral("7tw"),
        lvl=87,
        lvl_req=0,
    ),
    "PURGATORY": _Metadata(
        ladder=False,
        code=CodeLiteral("utp"),
        lvl=87,
        lvl_req=0,
    ),
    "RAEKORS_VIRTUE": _Metadata(
        ladder=False,
        code=CodeLiteral("baf"),
        lvl=87,
        lvl_req=0,
    ),
    "URSAS_NIGHTMARE": _Metadata(
        ladder=False,
        code=CodeLiteral("drf"),
        lvl=50,
        lvl_req=0,
    ),
    "ZHARS_SANCTUM": _Metadata(
        ladder=False,
        code=CodeLiteral("t51"),
        lvl=80,
        lvl_req=0,
    ),
    "WARLORD_OF_BLOOD": _Metadata(
        ladder=False,
        code=CodeLiteral("t52"),
        lvl=80,
        lvl_req=0,
    ),
    "FALLEN_GARDENS": _Metadata(
        ladder=False,
        code=CodeLiteral("t53"),
        lvl=80,
        lvl_req=0,
    ),
    "ULDYSSIANS_AWAKENING": _Metadata(
        ladder=False,
        code=CodeLiteral("7st"),
        lvl=80,
        lvl_req=0,
    ),
    "LEORICS_MITHRIL_BANE": _Metadata(
        ladder=False,
        code=CodeLiteral("7cm"),
        lvl=78,
        lvl_req=0,
    ),
    "TWILIGHTS_REFLECTION": _Metadata(
        ladder=False,
        code=CodeLiteral("urg"),
        lvl=18,
        lvl_req=0,
    ),
    "WRAITHSKIN": _Metadata(
        ladder=False,
        code=CodeLiteral("ung"),
        lvl=61,
        lvl_req=0,
    ),
    "TITANS_GRIP": _Metadata(
        ladder=False,
        code=CodeLiteral("ulg"),
        lvl=45,
        lvl_req=0,
    ),
    "SHATTERBLADE": _Metadata(
        ladder=False,
        code=CodeLiteral("7di"),
        lvl=73,
        lvl_req=0,
    ),
    "DENMOTHER": _Metadata(
        ladder=False,
        code=CodeLiteral("drc"),
        lvl=66,
        lvl_req=0,
    ),
    "EBONBANE": _Metadata(
        ladder=False,
        code=CodeLiteral("amc"),
        lvl=70,
        lvl_req=0,
    ),
    "WHISPERING_MIRAGE": _Metadata(
        ladder=False,
        code=CodeLiteral("7xf"),
        lvl=76,
        lvl_req=0,
    ),
    "SKYWARDEN": _Metadata(
        ladder=False,
        code=CodeLiteral("paf"),
        lvl=85,
        lvl_req=0,
    ),
    "SKORN": _Metadata(
        ladder=False,
        code=CodeLiteral("ob7"),
        lvl=36,
        lvl_req=0,
    ),
    "ACHILLES_STRIKE": _Metadata(
        ladder=False,
        code=CodeLiteral("9b8"),
        lvl=59,
        lvl_req=0,
    ),
    "WILDSPEAKER": _Metadata(
        ladder=False,
        code=CodeLiteral("ba7"),
        lvl=52,
        lvl_req=0,
    ),
    "FENRIS": _Metadata(
        ladder=False,
        code=CodeLiteral("dr6"),
        lvl=48,
        lvl_req=0,
    ),
    "SACRED_TOTEM": _Metadata(
        ladder=False,
        code=CodeLiteral("neg"),
        lvl=72,
        lvl_req=0,
    ),
    "IMPERIAL_PALACE": _Metadata(
        ladder=False,
        code=CodeLiteral("t54"),
        lvl=80,
        lvl_req=0,
    ),
    "OUTER_VOID": _Metadata(
        ladder=False,
        code=CodeLiteral("t55"),
        lvl=80,
        lvl_req=0,
    ),
    "BALEFIRE": _Metadata(
        ladder=False,
        code=CodeLiteral("aqv"),
        lvl=14,
        lvl_req=0,
    ),
    "SWIFTWIND_NEEDLE": _Metadata(
        ladder=False,
        code=CodeLiteral("aqv2"),
        lvl=32,
        lvl_req=0,
    ),
    "TOMBSONG": _Metadata(
        ladder=False,
        code=CodeLiteral("aqv2"),
        lvl=36,
        lvl_req=0,
    ),
    "AETHERWING": _Metadata(
        ladder=False,
        code=CodeLiteral("aqv3"),
        lvl=55,
        lvl_req=0,
    ),
    "BASILISKS_QUILL": _Metadata(
        ladder=False,
        code=CodeLiteral("aqv3"),
        lvl=62,
        lvl_req=0,
    ),
    "DOOMS_FINGER": _Metadata(
        ladder=False,
        code=CodeLiteral("aqv3"),
        lvl=87,
        lvl_req=0,
    ),
    "RAMFODDER": _Metadata(
        ladder=False,
        code=CodeLiteral("cqv"),
        lvl=8,
        lvl_req=0,
    ),
    "ANVILGUARD_STRAP": _Metadata(
        ladder=False,
        code=CodeLiteral("cqv2"),
        lvl=34,
        lvl_req=0,
    ),
    "SHATTERHEAD": _Metadata(
        ladder=False,
        code=CodeLiteral("cqv2"),
        lvl=47,
        lvl_req=0,
    ),
    "ABYSSAL_WARD": _Metadata(
        ladder=False,
        code=CodeLiteral("cqv3"),
        lvl=60,
        lvl_req=0,
    ),
    "BANNERLORDS_CALL": _Metadata(
        ladder=False,
        code=CodeLiteral("cqv3"),
        lvl=60,
        lvl_req=0,
    ),
    "FROZEN_SORROW": _Metadata(
        ladder=False,
        code=CodeLiteral("cqv3"),
        lvl=87,
        lvl_req=0,
    ),
    "CRACKLESHOT": _Metadata(
        ladder=False,
        code=CodeLiteral("6hb"),
        lvl=87,
        lvl_req=0,
    ),
    "CITY_OF_UREH": _Metadata(
        ladder=False,
        code=CodeLiteral("t56"),
        lvl=80,
        lvl_req=0,
    ),
}


class UniqueItem(Enum):
    """PD2 unique item categories."""

    THE_GNASHER = "The Gnasher"
    DEATHSPADE = "Deathspade"
    BLADEBONE = "Bladebone"
    SKULL_SPLITTER = "Skull Splitter"
    RAKESCAR = "Rakescar"
    AXE_OF_FECHMAR = "Axe of Fechmar"
    GORESHOVEL = "Goreshovel"
    THE_CHIEFTAIN = "The Chieftain"
    BRAINHEW = "Brainhew"
    HUMONGOUS = "Humongous"
    TORCH_OF_IRO = "Torch of Iro"
    MAELSTROM = "Maelstrom"
    GRAVENSPINE = "Gravenspine"
    UMES_LAMENT = "Ume's Lament"
    FELLOAK = "Felloak"
    KNELL_STRIKER = "Knell Striker"
    RUSTHANDLE = "Rusthandle"
    STORMEYE = "Stormeye"
    STOUTNAIL = "Stoutnail"
    CRUSHFLANGE = "Crushflange"
    BLOODRISE = "Bloodrise"
    THE_GENERALS_TAN_DO_LI_GA = "The General's Tan Do Li Ga"
    IRONSTONE = "Ironstone"
    BONESNAP = "Bonesnap"
    STEELDRIVER = "Steeldriver"
    RIXOTS_KEEN = "Rixot's Keen"
    BLOOD_CRESCENT = "Blood Crescent"
    SKEWER_OF_KRINTIZ = "Skewer of Krintiz"
    GLEAMSCYTHE = "Gleamscythe"
    GRISWOLDS_EDGE = "Griswold's Edge"
    HELLPLAGUE = "Hellplague"
    CULWENS_POINT = "Culwen's Point"
    SHADOWFANG = "Shadowfang"
    SOULFLAY = "Soulflay"
    KINEMILS_AWL = "Kinemil's Awl"
    BLACKTONGUE = "Blacktongue"
    RIPSAW = "Ripsaw"
    THE_PATRIARCH = "The Patriarch"
    GULL = "Gull"
    THE_DIGGLER = "The Diggler"
    THE_JADE_TAN_DO = "The Jade Tan Do"
    SPECTRAL_SHARD = "Spectral Shard"
    THE_DRAGON_CHANG = "The Dragon Chang"
    RAZORTINE = "Razortine"
    BLOODTHIEF = "Bloodthief"
    LANCE_OF_YAGGAI = "Lance of Yaggai"
    THE_TANNR_GOREROD = "The Tannr Gorerod"
    DIMOAKS_HEW = "Dimoak's Hew"
    STEELGOAD = "Steelgoad"
    SOUL_HARVEST = "Soul Harvest"
    THE_BATTLEBRANCH = "The Battlebranch"
    WOESTAVE = "Woestave"
    THE_GRIM_REAPER = "The Grim Reaper"
    BANE_ASH = "Bane Ash"
    SERPENT_LORD = "Serpent Lord"
    SPIRE_OF_LAZARUS = "Spire of Lazarus"
    THE_SALAMANDER = "The Salamander"
    THE_IRON_JANG_BONG = "The Iron Jang Bong"
    PLUCKEYE = "Pluckeye"
    WITHERSTRING = "Witherstring"
    RAVEN_CLAW = "Raven Claw"
    ROGUES_BOW = "Rogue's Bow"
    STORMSTRIKE = "Stormstrike"
    WIZENDRAW = "Wizendraw"
    HELLCLAP = "Hellclap"
    BLASTBARK = "Blastbark"
    LEADCROW = "Leadcrow"
    ICHORSTING = "Ichorsting"
    HELLCAST = "Hellcast"
    DOOMSLINGER = "Doomslinger"
    BIGGINS_BONNET = "Biggin's Bonnet"
    TARNHELM = "Tarnhelm"
    COIF_OF_GLORY = "Coif of Glory"
    DUSKDEEP = "Duskdeep"
    WORMSKULL = "Wormskull"
    HOWLTUSK = "Howltusk"
    UNDEAD_CROWN = "Undead Crown"
    THE_FACE_OF_HORROR = "The Face of Horror"
    GREYFORM = "Greyform"
    BLINKBATS_FORM = "Blinkbat's Form"
    THE_CENTURION = "The Centurion"
    TWITCHTHROE = "Twitchthroe"
    DARKGLOW = "Darkglow"
    HAWKMAIL = "Hawkmail"
    SPARKING_MAIL = "Sparking Mail"
    VENOM_WARD = "Venom Ward"
    ICEBLINK = "Iceblink"
    BONEFLESH = "Boneflesh"
    ROCKFLEECE = "Rockfleece"
    RATTLECAGE = "Rattlecage"
    GOLDSKIN = "Goldskin"
    SILKS_OF_THE_VICTOR = "Silks of the Victor"
    HEAVENLY_GARB = "Heavenly Garb"
    PELTA_LUNATA = "Pelta Lunata"
    UMBRAL_DISK = "Umbral Disk"
    STORMGUILD = "Stormguild"
    WALL_OF_THE_EYELESS = "Wall of the Eyeless"
    SWORDBACK_HOLD = "Swordback Hold"
    STEELCLASH = "Steelclash"
    BVERRIT_KEEP = "Bverrit Keep"
    THE_WARD = "The Ward"
    THE_HAND_OF_BROC = "The Hand of Broc"
    BLOODFIST = "Bloodfist"
    CHANCE_GUARDS = "Chance Guards"
    MAGEFIST = "Magefist"
    FROSTBURN = "Frostburn"
    HOTSPUR = "Hotspur"
    GOREFOOT = "Gorefoot"
    TREADS_OF_CTHON = "Treads of Cthon"
    GOBLIN_TOE = "Goblin Toe"
    TEARHAUNCH = "Tearhaunch"
    LENYMO = "Lenymo"
    SNAKECORD = "Snakecord"
    NIGHTSMOKE = "Nightsmoke"
    GOLDWRAP = "Goldwrap"
    BLADEBUCKLE = "Bladebuckle"
    NOKOZAN_RELIC = "Nokozan Relic"
    THE_EYE_OF_ETLICH = "The Eye of Etlich"
    THE_MAHIM_OAK_CURIO = "The Mahim-Oak Curio"
    NAGELRING = "Nagelring"
    MANALD_HEAL = "Manald Heal"
    THE_STONE_OF_JORDAN = "The Stone of Jordan"
    AMULET_OF_THE_VIPER = "Amulet of the Viper"
    STAFF_OF_KINGS = "Staff of Kings"
    HORADRIC_STAFF = "Horadric Staff"
    HELL_FORGE_HAMMER = "Hell Forge Hammer"
    KHALIMS_FLAIL = "Khalim's Flail"
    KHALIMS_WILL = "Khalim's Will"
    COLDKILL = "Coldkill"
    BUTCHERS_PUPIL = "Butcher's Pupil"
    ISLESTRIKE = "Islestrike"
    POMPEIIS_WRATH = "Pompeii's Wrath"
    GUARDIAN_NAGA = "Guardian Naga"
    WARLORDS_TRUST = "Warlord's Trust"
    SPELLSTEEL = "Spellsteel"
    STORMRIDER = "Stormrider"
    BONESLAYER_BLADE = "Boneslayer Blade"
    THE_MINOTAUR = "The Minotaur"
    SUICIDE_BRANCH = "Suicide Branch"
    CARIN_SHARD = "Carin Shard"
    ARM_OF_KING_LEORIC = "Arm of King Leoric"
    BLACKHAND_KEY = "Blackhand Key"
    DARK_CLAN_CRUSHER = "Dark Clan Crusher"
    ZAKARUMS_HAND = "Zakarum's Hand"
    THE_FETID_SPRINKLER = "The Fetid Sprinkler"
    HAND_OF_BLESSED_LIGHT = "Hand of Blessed Light"
    FLESHRENDER = "Fleshrender"
    SURESHRILL_FROST = "Sureshrill Frost"
    MOONFALL = "Moonfall"
    BAEZILS_VORTEX = "Baezil's Vortex"
    EARTHSHAKER = "Earthshaker"
    BLOODTREE_STUMP = "Bloodtree Stump"
    THE_GAVEL_OF_PAIN = "The Gavel of Pain"
    BLOODLETTER = "Bloodletter"
    COLDSTEEL_EYE = "Coldsteel Eye"
    HEXFIRE = "Hexfire"
    BLADE_OF_ALI_BABA = "Blade of Ali Baba"
    GINTHERS_RIFT = "Ginther's Rift"
    HEADSTRIKER = "Headstriker"
    PLAGUE_BEARER = "Plague Bearer"
    THE_ATLANTEAN = "The Atlantean"
    CRAINTE_VOMIR = "Crainte Vomir"
    BING_SZ_WANG = "Bing Sz Wang"
    THE_VILE_HUSK = "The Vile Husk"
    CLOUDCRACK = "Cloudcrack"
    TODESFAELLE_FLAMME = "Todesfaelle Flamme"
    SWORDGUARD = "Swordguard"
    SPINERIPPER = "Spineripper"
    HEART_CARVER = "Heart Carver"
    BLACKBOGS_SHARP = "Blackbog's Sharp"
    STORMSPIKE = "Stormspike"
    THE_IMPALER = "The Impaler"
    KELPIE_SNARE = "Kelpie Snare"
    SOULFEAST_TINE = "Soulfeast Tine"
    HONE_SUNDAN = "Hone Sundan"
    SPIRE_OF_HONOR = "Spire of Honor"
    THE_MEAT_SCRAPER = "The Meat Scraper"
    BLACKLEACH_BLADE = "Blackleach Blade"
    ATHENAS_WRATH = "Athena's Wrath"
    PIERRE_TOMBALE_COUANT = "Pierre Tombale Couant"
    HUSOLDAL_EVO = "Husoldal Evo"
    GRIMS_BURNING_DEAD = "Grim's Burning Dead"
    RAZORSWITCH = "Razorswitch"
    RIBCRACKER = "Ribcracker"
    CHROMATIC_IRE = "Chromatic Ire"
    WARPSPEAR = "Warpspear"
    SKULL_COLLECTOR = "Skull Collector"
    SKYSTRIKE = "Skystrike"
    RIPHOOK = "Riphook"
    KUKO_SHAKAKU = "Kuko Shakaku"
    ENDLESSHAIL = "Endlesshail"
    WITCHWILD_STRING = "Witchwild String"
    CLIFFKILLER = "Cliffkiller"
    MAGEWRATH = "Magewrath"
    GOLDSTRIKE_ARCH = "Goldstrike Arch"
    LANGER_BRISER = "Langer Briser"
    PUS_SPITTER = "Pus Spitter"
    BURIZA_DO_KYANON = "Buriza-Do Kyanon"
    DEMON_MACHINE = "Demon Machine"
    PEASANT_CROWN = "Peasant Crown"
    ROCKSTOPPER = "Rockstopper"
    STEALSKULL = "Stealskull"
    DARKSIGHT_HELM = "Darksight Helm"
    VALKYRIE_WING = "Valkyrie Wing"
    CROWN_OF_THIEVES = "Crown of Thieves"
    BLACKHORNS_FACE = "Blackhorn's Face"
    VAMPIRE_GAZE = "Vampire Gaze"
    THE_SPIRIT_SHROUD = "The Spirit Shroud"
    SKIN_OF_THE_VIPERMAGI = "Skin of the Vipermagi"
    SKIN_OF_THE_FLAYED_ONE = "Skin of the Flayed One"
    IRON_PELT = "Iron Pelt"
    SPIRIT_FORGE = "Spirit Forge"
    CROW_CAW = "Crow Caw"
    SHAFTSTOP = "Shaftstop"
    DURIELS_SHELL = "Duriel's Shell"
    SKULLDERS_IRE = "Skullder's Ire"
    GUARDIAN_ANGEL = "Guardian Angel"
    TOOTHROW = "Toothrow"
    ATMAS_WAIL = "Atma's Wail"
    BLACK_HADES = "Black Hades"
    CORPSEMOURN = "Corpsemourn"
    QUE_HEGANS_WISDOM = "Que-Hegan's Wisdom"
    VISCERATUANT = "Visceratuant"
    MOSERS_BLESSED_CIRCLE = "Moser's Blessed Circle"
    STORMCHASER = "Stormchaser"
    TIAMATS_REBUKE = "Tiamat's Rebuke"
    GERKES_SANCTUARY = "Gerke's Sanctuary"
    RADAMENTS_SPHERE = "Radament's Sphere"
    LIDLESS_WALL = "Lidless Wall"
    LANCE_GUARD = "Lance Guard"
    VENOM_GRIP = "Venom Grip"
    GRAVEPALM = "Gravepalm"
    GHOULHIDE = "Ghoulhide"
    LAVA_GOUT = "Lava Gout"
    HELLMOUTH = "Hellmouth"
    INFERNOSTRIDE = "Infernostride"
    WATERWALK = "Waterwalk"
    SILKWEAVE = "Silkweave"
    WAR_TRAVELER = "War Traveler"
    GORE_RIDER = "Gore Rider"
    STRING_OF_EARS = "String of Ears"
    RAZORTAIL = "Razortail"
    GLOOMS_TRAP = "Gloom's Trap"
    SNOWCLASH = "Snowclash"
    THUNDERGODS_VIGOR = "Thundergod's Vigor"
    HARLEQUIN_CREST = "Harlequin Crest"
    VEIL_OF_STEEL = "Veil of Steel"
    THE_GLADIATORS_BANE = "The Gladiator's Bane"
    ARKAINES_VALOR = "Arkaine's Valor"
    BLACKOAK_SHIELD = "Blackoak Shield"
    STORMSHIELD = "Stormshield"
    HELLSLAYER = "Hellslayer"
    MESSERSCHMIDTS_REAVER = "Messerschmidt's Reaver"
    BARANARS_STAR = "Baranar's Star"
    SCHAEFERS_HAMMER = "Schaefer's Hammer"
    THE_CRANIUM_BASHER = "The Cranium Basher"
    LIGHTSABRE = "Lightsabre"
    DOOMBRINGER = "Doombringer"
    THE_GRANDFATHER = "The Grandfather"
    WIZARDSPIKE = "Wizardspike"
    CONSTRICTING_LOOP = "Constricting Loop"
    STORMSPIRE = "Stormspire"
    EAGLEHORN = "Eaglehorn"
    WINDFORCE = "Windforce"
    BUL_KATHOS_WEDDING_BAND = "Bul-Kathos' Wedding Band"
    THE_CATS_EYE = "The Cat's Eye"
    THE_RISING_SUN = "The Rising Sun"
    CRESCENT_MOON = "Crescent Moon"
    MARAS_KALEIDOSCOPE = "Mara's Kaleidoscope"
    ATMAS_SCARAB = "Atma's Scarab"
    DWARF_STAR = "Dwarf Star"
    RAVEN_FROST = "Raven Frost"
    HIGHLORDS_WRATH = "Highlord's Wrath"
    SARACENS_CHANCE = "Saracen's Chance"
    ARREATS_FACE = "Arreat's Face"
    HOMUNCULUS = "Homunculus"
    TITANS_REVENGE = "Titan's Revenge"
    LYCANDERS_AIM = "Lycander's Aim"
    LYCANDERS_FLANK = "Lycander's Flank"
    THE_OCULUS = "The Oculus"
    HERALD_OF_ZAKARUM = "Herald of Zakarum"
    BARTUCS_CUT_THROAT = "Bartuc's Cut-Throat"
    JALALS_MANE = "Jalal's Mane"
    THE_SCALPER = "The Scalper"
    BLOODMOON = "Bloodmoon"
    DJINN_SLAYER = "Djinn Slayer"
    DEATHBIT = "Deathbit"
    WARSHRIKE = "Warshrike"
    GUT_SIPHON = "Gut Siphon"
    RAZORS_EDGE = "Razor's Edge"
    DEMON_LIMB = "Demon Limb"
    STEEL_SHADE = "Steel Shade"
    TOMB_REAVER = "Tomb Reaver"
    DEATHS_WEB = "Death's Web"
    NATURES_PEACE = "Nature's Peace"
    AZUREWRATH = "Azurewrath"
    SERAPHS_HYMN = "Seraph's Hymn"
    FLESHRIPPER = "Fleshripper"
    ODIUM = "Odium"
    HORIZONS_TORNADO = "Horizon's Tornado"
    STONE_CRUSHER = "Stone Crusher"
    JADE_TALON = "Jade Talon"
    SHADOW_DANCER = "Shadow Dancer"
    CEREBUS_BITE = "Cerebus' Bite"
    TYRAELS_MIGHT = "Tyrael's Might"
    SOUL_DRAINER = "Soul Drainer"
    RUNE_MASTER = "Rune Master"
    DEATH_CLEAVER = "Death Cleaver"
    EXECUTIONERS_JUSTICE = "Executioner's Justice"
    STONERAVEN = "Stoneraven"
    LEVIATHAN = "Leviathan"
    WISP_PROJECTOR = "Wisp Projector"
    GARGOYLES_BITE = "Gargoyle's Bite"
    LACERATOR = "Lacerator"
    MANG_SONGS_LESSON = "Mang Song's Lesson"
    VIPERFORK = "Viperfork"
    ETHEREAL_EDGE = "Ethereal Edge"
    DEMONHORNS_EDGE = "Demonhorn's Edge"
    THE_REAPERS_TOLL = "The Reaper's Toll"
    SPIRIT_KEEPER = "Spirit Keeper"
    HELLRACK = "Hellrack"
    ALMA_NEGRA = "Alma Negra"
    DARKFORCE_SPAWN = "Darkforce Spawn"
    WIDOWMAKER = "Widowmaker"
    BLOOD_RAVENS_CHARGE = "Blood Raven's Charge"
    GHOSTFLAME = "Ghostflame"
    SHADOW_KILLER = "Shadow Killer"
    GIMMERSHRED = "Gimmershred"
    GRIFFONS_EYE = "Griffon's Eye"
    WINDHAMMER = "Windhammer"
    THUNDERSTROKE = "Thunderstroke"
    DEMONS_ARCH = "Demon's Arch"
    BONEFLAME = "Boneflame"
    STEEL_PILLAR = "Steel Pillar"
    NIGHTWINGS_VEIL = "Nightwing's Veil"
    CROWN_OF_AGES = "Crown of Ages"
    ANDARIELS_VISAGE = "Andariel's Visage"
    DRAGONSCALE = "Dragonscale"
    STEEL_CARAPACE = "Steel Carapace"
    MEDUSAS_GAZE = "Medusa's Gaze"
    RAVENLORE = "Ravenlore"
    BONESHADE = "Boneshade"
    FLAMEBELLOW = "Flamebellow"
    DEATHS_FATHOM = "Death's Fathom"
    WOLFHOWL = "Wolfhowl"
    SPIRIT_WARD = "Spirit Ward"
    KIRAS_GUARDIAN = "Kira's Guardian"
    ORMUS_ROBES = "Ormus' Robes"
    GHEEDS_FORTUNE = "Gheed's Fortune"
    STORMLASH = "Stormlash"
    HALABERDS_REIGN = "Halaberd's Reign"
    SPIKE_THORN = "Spike Thorn"
    DRACULS_GRASP = "Dracul's Grasp"
    FROSTWIND = "Frostwind"
    TEMPLARS_MIGHT = "Templar's Might"
    ESCHUTAS_TEMPER = "Eschuta's Temper"
    FIRELIZARDS_TALONS = "Firelizard's Talons"
    SANDSTORM_TREK = "Sandstorm Trek"
    MARROWWALK = "Marrowwalk"
    HEAVENS_LIGHT = "Heaven's Light"
    MERMANS_SPROCKET = "Merman's Sprocket"
    ARACHNID_MESH = "Arachnid Mesh"
    NOSFERATUS_COIL = "Nosferatu's Coil"
    METALGRID = "Metalgrid"
    VERDUNGOS_HEARTY_CORD = "Verdungo's Hearty Cord"
    SIGGARDS_STAUNCH = "Siggard's Staunch"
    CARRION_WIND = "Carrion Wind"
    GIANT_SKULL = "Giant Skull"
    ASTREONS_IRON_WARD = "Astreon's Iron Ward"
    ANNIHILUS = "Annihilus"
    ARIOCS_NEEDLE = "Arioc's Needle"
    CRANEBEAK = "Cranebeak"
    NORDS_TENDERIZER = "Nord's Tenderizer"
    EARTH_SHIFTER = "Earth Shifter"
    WRAITH_FLIGHT = "Wraith Flight"
    BONEHEW = "Bonehew"
    ONDALS_WISDOM = "Ondal's Wisdom"
    THE_REDEEMER = "The Redeemer"
    HEAD_HUNTERS_GLORY = "Head Hunter's Glory"
    STEELREND = "Steelrend"
    RAINBOW_FACET = "Rainbow Facet"
    HELLFIRE_TORCH = "Hellfire Torch"
    ITHERAELS_PATH = "Itherael's Path"
    OVERLORDS_HELM = "Overlord's Helm"
    DARK_ABYSS = "Dark Abyss"
    AIDANS_SCAR = "Aidan's Scar"
    HADRIELS_HAND = "Hadriel's Hand"
    TRUE_SILVER = "True Silver"
    QUETZALCOATL = "Quetzalcoatl"
    CYCLOPEAN_ROAR = "Cyclopean Roar"
    SANKEKURS_FALL = "Sankekur's Fall"
    MAGE_SLAYER = "Mage Slayer"
    KALANS_LEGACY = "Kalan's Legacy"
    TEMPEST = "Tempest"
    BAND_OF_SKULLS = "Band of Skulls"
    CAGE_OF_THE_UNSULLIED = "Cage of the Unsullied"
    THE_THIRD_EYE = "The Third Eye"
    ZERAES_RESOLVE = "Zerae's Resolve"
    OCCULTIST = "Occultist"
    BRIMSTONE_RAIN = "Brimstone Rain"
    AKARATS_DEVOTION = "Akarat's Devotion"
    MARTYRDOM = "Martyrdom"
    STALKERS_CULL = "Stalker's Cull"
    PURGATORY = "Purgatory"
    RAEKORS_VIRTUE = "Raekor's Virtue"
    URSAS_NIGHTMARE = "Ursa's Nightmare"
    ZHARS_SANCTUM = "Zhar's Sanctum"
    WARLORD_OF_BLOOD = "Warlord of Blood"
    FALLEN_GARDENS = "Fallen Gardens"
    ULDYSSIANS_AWAKENING = "Uldyssian's Awakening"
    LEORICS_MITHRIL_BANE = "Leoric's Mithril Bane"
    TWILIGHTS_REFLECTION = "Twilight's Reflection"
    WRAITHSKIN = "Wraithskin"
    TITANS_GRIP = "Titan's Grip"
    SHATTERBLADE = "Shatterblade"
    DENMOTHER = "Denmother"
    EBONBANE = "Ebonbane"
    WHISPERING_MIRAGE = "Whispering Mirage"
    SKYWARDEN = "Skywarden"
    SKORN = "Skorn"
    ACHILLES_STRIKE = "Achilles Strike"
    WILDSPEAKER = "Wildspeaker"
    FENRIS = "Fenris"
    SACRED_TOTEM = "Sacred Totem"
    IMPERIAL_PALACE = "Imperial Palace"
    OUTER_VOID = "Outer Void"
    BALEFIRE = "Balefire"
    SWIFTWIND_NEEDLE = "Swiftwind Needle"
    TOMBSONG = "Tombsong"
    AETHERWING = "Aetherwing"
    BASILISKS_QUILL = "Basilisk's Quill"
    DOOMS_FINGER = "Doom's Finger"
    RAMFODDER = "Ramfodder"
    ANVILGUARD_STRAP = "Anvilguard Strap"
    SHATTERHEAD = "Shatterhead"
    ABYSSAL_WARD = "Abyssal Ward"
    BANNERLORDS_CALL = "Bannerlord's Call"
    FROZEN_SORROW = "Frozen Sorrow"
    CRACKLESHOT = "Crackleshot"
    CITY_OF_UREH = "City of Ureh"

    @property
    def ladder(self) -> bool:
        return _METADATA[self.name].ladder

    @property
    def code(self) -> CodeLiteral:
        return _METADATA[self.name].code

    @property
    def lvl(self) -> int:
        return _METADATA[self.name].lvl

    @property
    def lvl_req(self) -> int:
        return _METADATA[self.name].lvl_req
