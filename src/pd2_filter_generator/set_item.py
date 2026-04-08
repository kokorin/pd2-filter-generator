
"""
Generated SetItem enum from PD2 data.

DO NOT EDIT MANUALLY - regenerate with: hatch run ./scripts/generate.py generate
"""

from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
from pd2_filter_generator.expression import CodeLiteral
from pd2_filter_generator.set import Set
@dataclass(frozen=True)
class _Metadata:
    """Item type metadata."""
    set: Set # "set"
    item: CodeLiteral # "item"

_METADATA: dict[str, _Metadata] = {
    "CIVERBS_WARD": _Metadata(
        set=Set("Civerb's Vestments"),
        item=CodeLiteral("lrg"),
    ),
    "CIVERBS_ICON": _Metadata(
        set=Set("Civerb's Vestments"),
        item=CodeLiteral("amu"),
    ),
    "CIVERBS_CUDGEL": _Metadata(
        set=Set("Civerb's Vestments"),
        item=CodeLiteral("gsc"),
    ),
    "HSARUS_IRON_HEEL": _Metadata(
        set=Set("Hsarus' Defense"),
        item=CodeLiteral("mbt"),
    ),
    "HSARUS_IRON_FIST": _Metadata(
        set=Set("Hsarus' Defense"),
        item=CodeLiteral("buc"),
    ),
    "HSARUS_IRON_STAY": _Metadata(
        set=Set("Hsarus' Defense"),
        item=CodeLiteral("mbl"),
    ),
    "CLEGLAWS_TOOTH": _Metadata(
        set=Set("Cleglaw's Brace"),
        item=CodeLiteral("lsd"),
    ),
    "CLEGLAWS_CLAW": _Metadata(
        set=Set("Cleglaw's Brace"),
        item=CodeLiteral("sml"),
    ),
    "CLEGLAWS_PINCERS": _Metadata(
        set=Set("Cleglaw's Brace"),
        item=CodeLiteral("mgl"),
    ),
    "IRATHAS_COLLAR": _Metadata(
        set=Set("Iratha's Finery"),
        item=CodeLiteral("amu"),
    ),
    "IRATHAS_CUFF": _Metadata(
        set=Set("Iratha's Finery"),
        item=CodeLiteral("tgl"),
    ),
    "IRATHAS_COIL": _Metadata(
        set=Set("Iratha's Finery"),
        item=CodeLiteral("crn"),
    ),
    "IRATHAS_CORD": _Metadata(
        set=Set("Iratha's Finery"),
        item=CodeLiteral("tbl"),
    ),
    "ISENHARTS_LIGHTBRAND": _Metadata(
        set=Set("Isenhart's Armory"),
        item=CodeLiteral("bsd"),
    ),
    "ISENHARTS_PARRY": _Metadata(
        set=Set("Isenhart's Armory"),
        item=CodeLiteral("gts"),
    ),
    "ISENHARTS_CASE": _Metadata(
        set=Set("Isenhart's Armory"),
        item=CodeLiteral("brs"),
    ),
    "ISENHARTS_HORNS": _Metadata(
        set=Set("Isenhart's Armory"),
        item=CodeLiteral("fhl"),
    ),
    "VIDALAS_BARB": _Metadata(
        set=Set("Vidala's Rig"),
        item=CodeLiteral("lbb"),
    ),
    "VIDALAS_FETLOCK": _Metadata(
        set=Set("Vidala's Rig"),
        item=CodeLiteral("tbt"),
    ),
    "VIDALAS_AMBUSH": _Metadata(
        set=Set("Vidala's Rig"),
        item=CodeLiteral("lea"),
    ),
    "VIDALAS_SNARE": _Metadata(
        set=Set("Vidala's Rig"),
        item=CodeLiteral("amu"),
    ),
    "MILABREGAS_ORB": _Metadata(
        set=Set("Milabrega's Regalia"),
        item=CodeLiteral("kit"),
    ),
    "MILABREGAS_ROD": _Metadata(
        set=Set("Milabrega's Regalia"),
        item=CodeLiteral("wsp"),
    ),
    "MILABREGAS_DIADEM": _Metadata(
        set=Set("Milabrega's Regalia"),
        item=CodeLiteral("crn"),
    ),
    "MILABREGAS_ROBE": _Metadata(
        set=Set("Milabrega's Regalia"),
        item=CodeLiteral("aar"),
    ),
    "CATHANS_RULE": _Metadata(
        set=Set("Cathan's Traps"),
        item=CodeLiteral("bst"),
    ),
    "CATHANS_MESH": _Metadata(
        set=Set("Cathan's Traps"),
        item=CodeLiteral("chn"),
    ),
    "CATHANS_VISAGE": _Metadata(
        set=Set("Cathan's Traps"),
        item=CodeLiteral("msk"),
    ),
    "CATHANS_SIGIL": _Metadata(
        set=Set("Cathan's Traps"),
        item=CodeLiteral("amu"),
    ),
    "CATHANS_SEAL": _Metadata(
        set=Set("Cathan's Traps"),
        item=CodeLiteral("rin"),
    ),
    "TANCREDS_CROWBILL": _Metadata(
        set=Set("Tancred's Battlegear"),
        item=CodeLiteral("mpi"),
    ),
    "TANCREDS_SPINE": _Metadata(
        set=Set("Tancred's Battlegear"),
        item=CodeLiteral("ful"),
    ),
    "TANCREDS_HOBNAILS": _Metadata(
        set=Set("Tancred's Battlegear"),
        item=CodeLiteral("lbt"),
    ),
    "TANCREDS_WEIRD": _Metadata(
        set=Set("Tancred's Battlegear"),
        item=CodeLiteral("amu"),
    ),
    "TANCREDS_SKULL": _Metadata(
        set=Set("Tancred's Battlegear"),
        item=CodeLiteral("bhm"),
    ),
    "SIGONS_GAGE": _Metadata(
        set=Set("Sigon's Complete Steel"),
        item=CodeLiteral("hgl"),
    ),
    "SIGONS_VISOR": _Metadata(
        set=Set("Sigon's Complete Steel"),
        item=CodeLiteral("ghm"),
    ),
    "SIGONS_SHELTER": _Metadata(
        set=Set("Sigon's Complete Steel"),
        item=CodeLiteral("gth"),
    ),
    "SIGONS_SABOT": _Metadata(
        set=Set("Sigon's Complete Steel"),
        item=CodeLiteral("hbt"),
    ),
    "SIGONS_WRAP": _Metadata(
        set=Set("Sigon's Complete Steel"),
        item=CodeLiteral("hbl"),
    ),
    "SIGONS_GUARD": _Metadata(
        set=Set("Sigon's Complete Steel"),
        item=CodeLiteral("tow"),
    ),
    "INFERNAL_CRANIUM": _Metadata(
        set=Set("Infernal Tools"),
        item=CodeLiteral("cap"),
    ),
    "INFERNAL_SPIRE": _Metadata(
        set=Set("Infernal Tools"),
        item=CodeLiteral("dgr"),
    ),
    "INFERNAL_SIGN": _Metadata(
        set=Set("Infernal Tools"),
        item=CodeLiteral("tbl"),
    ),
    "BERSERKERS_HEADGEAR": _Metadata(
        set=Set("Berserker's Garb"),
        item=CodeLiteral("hlm"),
    ),
    "BERSERKERS_HAUBERK": _Metadata(
        set=Set("Berserker's Garb"),
        item=CodeLiteral("spl"),
    ),
    "BERSERKERS_HATCHET": _Metadata(
        set=Set("Berserker's Garb"),
        item=CodeLiteral("2ax"),
    ),
    "DEATHS_HAND": _Metadata(
        set=Set("Death's Disguise"),
        item=CodeLiteral("lgl"),
    ),
    "DEATHS_GUARD": _Metadata(
        set=Set("Death's Disguise"),
        item=CodeLiteral("lbl"),
    ),
    "DEATHS_TOUCH": _Metadata(
        set=Set("Death's Disguise"),
        item=CodeLiteral("wsd"),
    ),
    "ANGELIC_SICKLE": _Metadata(
        set=Set("Angelical Raiment"),
        item=CodeLiteral("sbr"),
    ),
    "ANGELIC_MANTLE": _Metadata(
        set=Set("Angelical Raiment"),
        item=CodeLiteral("rng"),
    ),
    "ANGELIC_HALO": _Metadata(
        set=Set("Angelical Raiment"),
        item=CodeLiteral("rin"),
    ),
    "ANGELIC_WINGS": _Metadata(
        set=Set("Angelical Raiment"),
        item=CodeLiteral("amu"),
    ),
    "ARCTIC_HORN": _Metadata(
        set=Set("Arctic Gear"),
        item=CodeLiteral("swb"),
    ),
    "ARCTIC_FURS": _Metadata(
        set=Set("Arctic Gear"),
        item=CodeLiteral("qui"),
    ),
    "ARCTIC_BINDING": _Metadata(
        set=Set("Arctic Gear"),
        item=CodeLiteral("vbl"),
    ),
    "ARCTIC_MITTS": _Metadata(
        set=Set("Arctic Gear"),
        item=CodeLiteral("tgl"),
    ),
    "ARCANNAS_SIGN": _Metadata(
        set=Set("Arcanna's Tricks"),
        item=CodeLiteral("amu"),
    ),
    "ARCANNAS_DEATHWAND": _Metadata(
        set=Set("Arcanna's Tricks"),
        item=CodeLiteral("wst"),
    ),
    "ARCANNAS_HEAD": _Metadata(
        set=Set("Arcanna's Tricks"),
        item=CodeLiteral("skp"),
    ),
    "ARCANNAS_FLESH": _Metadata(
        set=Set("Arcanna's Tricks"),
        item=CodeLiteral("ltp"),
    ),
    "NATALYAS_TOTEM": _Metadata(
        set=Set("Natalya's Odium"),
        item=CodeLiteral("xh9"),
    ),
    "NATALYAS_MARK": _Metadata(
        set=Set("Natalya's Odium"),
        item=CodeLiteral("7qr"),
    ),
    "NATALYAS_SHADOW": _Metadata(
        set=Set("Natalya's Odium"),
        item=CodeLiteral("ucl"),
    ),
    "NATALYAS_SOUL": _Metadata(
        set=Set("Natalya's Odium"),
        item=CodeLiteral("xmb"),
    ),
    "ALDURS_STONY_GAZE": _Metadata(
        set=Set("Aldur's Watchtower"),
        item=CodeLiteral("dr8"),
    ),
    "ALDURS_DECEPTION": _Metadata(
        set=Set("Aldur's Watchtower"),
        item=CodeLiteral("uul"),
    ),
    "ALDURS_GAUNTLET": _Metadata(
        set=Set("Aldur's Watchtower"),
        item=CodeLiteral("9mt"),
    ),
    "ALDURS_ADVANCE": _Metadata(
        set=Set("Aldur's Watchtower"),
        item=CodeLiteral("xtb"),
    ),
    "IMMORTAL_KINGS_WILL": _Metadata(
        set=Set("Immortal King"),
        item=CodeLiteral("ba5"),
    ),
    "IMMORTAL_KINGS_SOUL_CAGE_": _Metadata(
        set=Set("Immortal King"),
        item=CodeLiteral("uar"),
    ),
    "IMMORTAL_KINGS_DETAIL": _Metadata(
        set=Set("Immortal King"),
        item=CodeLiteral("zhb"),
    ),
    "IMMORTAL_KINGS_FORGE": _Metadata(
        set=Set("Immortal King"),
        item=CodeLiteral("xhg"),
    ),
    "IMMORTAL_KINGS_PILLAR": _Metadata(
        set=Set("Immortal King"),
        item=CodeLiteral("xhb"),
    ),
    "IMMORTAL_KINGS_STONE_CRUSHER": _Metadata(
        set=Set("Immortal King"),
        item=CodeLiteral("7m7"),
    ),
    "TAL_RASHAS_FIRE_SPUN_CLOTH": _Metadata(
        set=Set("Tal Rasha's Wrappings"),
        item=CodeLiteral("zmb"),
    ),
    "TAL_RASHAS_ADJUDICATION": _Metadata(
        set=Set("Tal Rasha's Wrappings"),
        item=CodeLiteral("amu"),
    ),
    "TAL_RASHAS_LIDLESS_EYE": _Metadata(
        set=Set("Tal Rasha's Wrappings"),
        item=CodeLiteral("oba"),
    ),
    "TAL_RASHAS_HOWLING_WIND": _Metadata(
        set=Set("Tal Rasha's Wrappings"),
        item=CodeLiteral("uth"),
    ),
    "TAL_RASHAS_HORADRIC_CREST": _Metadata(
        set=Set("Tal Rasha's Wrappings"),
        item=CodeLiteral("xsk"),
    ),
    "GRISWOLDS_VALOR": _Metadata(
        set=Set("Griswold's Legacy"),
        item=CodeLiteral("urn"),
    ),
    "GRISWOLDS_HEART": _Metadata(
        set=Set("Griswold's Legacy"),
        item=CodeLiteral("xar"),
    ),
    "GRISWOLDSS_REDEMPTION": _Metadata(
        set=Set("Griswold's Legacy"),
        item=CodeLiteral("7ws"),
    ),
    "GRISWOLDS_HONOR": _Metadata(
        set=Set("Griswold's Legacy"),
        item=CodeLiteral("paf"),
    ),
    "TRANG_OULS_GUISE": _Metadata(
        set=Set("Trang-Oul's Avatar"),
        item=CodeLiteral("uh9"),
    ),
    "TRANG_OULS_SCALES": _Metadata(
        set=Set("Trang-Oul's Avatar"),
        item=CodeLiteral("xul"),
    ),
    "TRANG_OULS_WING": _Metadata(
        set=Set("Trang-Oul's Avatar"),
        item=CodeLiteral("ne9"),
    ),
    "TRANG_OULS_CLAWS": _Metadata(
        set=Set("Trang-Oul's Avatar"),
        item=CodeLiteral("xmg"),
    ),
    "TRANG_OULS_GIRTH": _Metadata(
        set=Set("Trang-Oul's Avatar"),
        item=CodeLiteral("utc"),
    ),
    "MAVINAS_TRUE_SIGHT": _Metadata(
        set=Set("M'avina's Battle Hymn"),
        item=CodeLiteral("ci3"),
    ),
    "MAVINAS_EMBRACE": _Metadata(
        set=Set("M'avina's Battle Hymn"),
        item=CodeLiteral("uld"),
    ),
    "MAVINAS_ICY_CLUTCH": _Metadata(
        set=Set("M'avina's Battle Hymn"),
        item=CodeLiteral("xtg"),
    ),
    "MAVINAS_TENET": _Metadata(
        set=Set("M'avina's Battle Hymn"),
        item=CodeLiteral("zvb"),
    ),
    "MAVINAS_CASTER": _Metadata(
        set=Set("M'avina's Battle Hymn"),
        item=CodeLiteral("amc"),
    ),
    "TELLING_OF_BEADS": _Metadata(
        set=Set("The Disciple"),
        item=CodeLiteral("amu"),
    ),
    "LAYING_OF_HANDS": _Metadata(
        set=Set("The Disciple"),
        item=CodeLiteral("ulg"),
    ),
    "RITE_OF_PASSAGE": _Metadata(
        set=Set("The Disciple"),
        item=CodeLiteral("xlb"),
    ),
    "SPIRITUAL_CUSTODIAN": _Metadata(
        set=Set("The Disciple"),
        item=CodeLiteral("uui"),
    ),
    "CREDENDUM": _Metadata(
        set=Set("The Disciple"),
        item=CodeLiteral("umc"),
    ),
    "DANGOONS_TEACHING": _Metadata(
        set=Set("Heaven's Brethren"),
        item=CodeLiteral("7ma"),
    ),
    "HEAVENS_TAEBAEK": _Metadata(
        set=Set("Heaven's Brethren"),
        item=CodeLiteral("uts"),
    ),
    "HAEMOSUS_ADAMENT": _Metadata(
        set=Set("Heaven's Brethren"),
        item=CodeLiteral("xrs"),
    ),
    "ONDALS_ALMIGHTY": _Metadata(
        set=Set("Heaven's Brethren"),
        item=CodeLiteral("uhm"),
    ),
    "GUILLAUMES_FACE": _Metadata(
        set=Set("Orphan's Call"),
        item=CodeLiteral("xhm"),
    ),
    "WILHELMS_PRIDE": _Metadata(
        set=Set("Orphan's Call"),
        item=CodeLiteral("ztb"),
    ),
    "MAGNUS_SKIN": _Metadata(
        set=Set("Orphan's Call"),
        item=CodeLiteral("xvg"),
    ),
    "WIHTSTANS_GUARD": _Metadata(
        set=Set("Orphan's Call"),
        item=CodeLiteral("xml"),
    ),
    "HWANINS_SPLENDOR": _Metadata(
        set=Set("Hwanin's Majesty"),
        item=CodeLiteral("xrn"),
    ),
    "HWANINS_REFUGE": _Metadata(
        set=Set("Hwanin's Majesty"),
        item=CodeLiteral("xcl"),
    ),
    "HWANINS_SEAL": _Metadata(
        set=Set("Hwanin's Majesty"),
        item=CodeLiteral("mbl"),
    ),
    "HWANINS_JUSTICE": _Metadata(
        set=Set("Hwanin's Majesty"),
        item=CodeLiteral("9vo"),
    ),
    "SAZABIS_COBALT_REDEEMER": _Metadata(
        set=Set("Sazabi's Grand Tribute"),
        item=CodeLiteral("7ls"),
    ),
    "SAZABIS_GHOST_LIBERATOR": _Metadata(
        set=Set("Sazabi's Grand Tribute"),
        item=CodeLiteral("upl"),
    ),
    "SAZABIS_MENTAL_SHEATH": _Metadata(
        set=Set("Sazabi's Grand Tribute"),
        item=CodeLiteral("xhl"),
    ),
    "BUL_KATHOS_SACRED_CHARGE": _Metadata(
        set=Set("Bul-Kathos' Children"),
        item=CodeLiteral("7gd"),
    ),
    "BUL_KATHOS_TRIBAL_GUARDIAN": _Metadata(
        set=Set("Bul-Kathos' Children"),
        item=CodeLiteral("7fb"),
    ),
    "BUL_KATHOS_DEATH_BAND": _Metadata(
        set=Set("Bul-Kathos' Children"),
        item=CodeLiteral("rin"),
    ),
    "COW_KINGS_HORNS": _Metadata(
        set=Set("Cow King's Leathers"),
        item=CodeLiteral("xap"),
    ),
    "COW_KINGS_HIDE": _Metadata(
        set=Set("Cow King's Leathers"),
        item=CodeLiteral("stu"),
    ),
    "COW_KINGS_HOOFS": _Metadata(
        set=Set("Cow King's Leathers"),
        item=CodeLiteral("vbt"),
    ),
    "NAJS_PUZZLER": _Metadata(
        set=Set("Naj's Ancient Set"),
        item=CodeLiteral("6cs"),
    ),
    "NAJS_LIGHT_PLATE": _Metadata(
        set=Set("Naj's Ancient Set"),
        item=CodeLiteral("ult"),
    ),
    "NAJS_CIRCLET": _Metadata(
        set=Set("Naj's Ancient Set"),
        item=CodeLiteral("ci0"),
    ),
    "MC_AULEYS_PARAGON": _Metadata(
        set=Set("McAuley's Folly"),
        item=CodeLiteral("cap"),
    ),
    "MC_AULEYS_RIPRAP": _Metadata(
        set=Set("McAuley's Folly"),
        item=CodeLiteral("vbt"),
    ),
    "MC_AULEYS_TABOO": _Metadata(
        set=Set("McAuley's Folly"),
        item=CodeLiteral("vgl"),
    ),
    "MC_AULEYS_SUPERSTITION": _Metadata(
        set=Set("McAuley's Folly"),
        item=CodeLiteral("bwn"),
    ),
}

class SetItem(Enum):
    """PD2 set item categories."""

    CIVERBS_WARD =  "Civerb's Ward"
    CIVERBS_ICON =  "Civerb's Icon"
    CIVERBS_CUDGEL =  "Civerb's Cudgel"
    HSARUS_IRON_HEEL =  "Hsarus' Iron Heel"
    HSARUS_IRON_FIST =  "Hsarus' Iron Fist"
    HSARUS_IRON_STAY =  "Hsarus' Iron Stay"
    CLEGLAWS_TOOTH =  "Cleglaw's Tooth"
    CLEGLAWS_CLAW =  "Cleglaw's Claw"
    CLEGLAWS_PINCERS =  "Cleglaw's Pincers"
    IRATHAS_COLLAR =  "Iratha's Collar"
    IRATHAS_CUFF =  "Iratha's Cuff"
    IRATHAS_COIL =  "Iratha's Coil"
    IRATHAS_CORD =  "Iratha's Cord"
    ISENHARTS_LIGHTBRAND =  "Isenhart's Lightbrand"
    ISENHARTS_PARRY =  "Isenhart's Parry"
    ISENHARTS_CASE =  "Isenhart's Case"
    ISENHARTS_HORNS =  "Isenhart's Horns"
    VIDALAS_BARB =  "Vidala's Barb"
    VIDALAS_FETLOCK =  "Vidala's Fetlock"
    VIDALAS_AMBUSH =  "Vidala's Ambush"
    VIDALAS_SNARE =  "Vidala's Snare"
    MILABREGAS_ORB =  "Milabrega's Orb"
    MILABREGAS_ROD =  "Milabrega's Rod"
    MILABREGAS_DIADEM =  "Milabrega's Diadem"
    MILABREGAS_ROBE =  "Milabrega's Robe"
    CATHANS_RULE =  "Cathan's Rule"
    CATHANS_MESH =  "Cathan's Mesh"
    CATHANS_VISAGE =  "Cathan's Visage"
    CATHANS_SIGIL =  "Cathan's Sigil"
    CATHANS_SEAL =  "Cathan's Seal"
    TANCREDS_CROWBILL =  "Tancred's Crowbill"
    TANCREDS_SPINE =  "Tancred's Spine"
    TANCREDS_HOBNAILS =  "Tancred's Hobnails"
    TANCREDS_WEIRD =  "Tancred's Weird"
    TANCREDS_SKULL =  "Tancred's Skull"
    SIGONS_GAGE =  "Sigon's Gage"
    SIGONS_VISOR =  "Sigon's Visor"
    SIGONS_SHELTER =  "Sigon's Shelter"
    SIGONS_SABOT =  "Sigon's Sabot"
    SIGONS_WRAP =  "Sigon's Wrap"
    SIGONS_GUARD =  "Sigon's Guard"
    INFERNAL_CRANIUM =  "Infernal Cranium"
    INFERNAL_SPIRE =  "Infernal Spire"
    INFERNAL_SIGN =  "Infernal Sign"
    BERSERKERS_HEADGEAR =  "Berserker's Headgear"
    BERSERKERS_HAUBERK =  "Berserker's Hauberk"
    BERSERKERS_HATCHET =  "Berserker's Hatchet"
    DEATHS_HAND =  "Death's Hand"
    DEATHS_GUARD =  "Death's Guard"
    DEATHS_TOUCH =  "Death's Touch"
    ANGELIC_SICKLE =  "Angelic Sickle"
    ANGELIC_MANTLE =  "Angelic Mantle"
    ANGELIC_HALO =  "Angelic Halo"
    ANGELIC_WINGS =  "Angelic Wings"
    ARCTIC_HORN =  "Arctic Horn"
    ARCTIC_FURS =  "Arctic Furs"
    ARCTIC_BINDING =  "Arctic Binding"
    ARCTIC_MITTS =  "Arctic Mitts"
    ARCANNAS_SIGN =  "Arcanna's Sign"
    ARCANNAS_DEATHWAND =  "Arcanna's Deathwand"
    ARCANNAS_HEAD =  "Arcanna's Head"
    ARCANNAS_FLESH =  "Arcanna's Flesh"
    NATALYAS_TOTEM =  "Natalya's Totem"
    NATALYAS_MARK =  "Natalya's Mark"
    NATALYAS_SHADOW =  "Natalya's Shadow"
    NATALYAS_SOUL =  "Natalya's Soul"
    ALDURS_STONY_GAZE =  "Aldur's Stony Gaze"
    ALDURS_DECEPTION =  "Aldur's Deception"
    ALDURS_GAUNTLET =  "Aldur's Gauntlet"
    ALDURS_ADVANCE =  "Aldur's Advance"
    IMMORTAL_KINGS_WILL =  "Immortal King's Will"
    IMMORTAL_KINGS_SOUL_CAGE_ =  "Immortal King's Soul Cage "
    IMMORTAL_KINGS_DETAIL =  "Immortal King's Detail"
    IMMORTAL_KINGS_FORGE =  "Immortal King's Forge"
    IMMORTAL_KINGS_PILLAR =  "Immortal King's Pillar"
    IMMORTAL_KINGS_STONE_CRUSHER =  "Immortal King's Stone Crusher"
    TAL_RASHAS_FIRE_SPUN_CLOTH =  "Tal Rasha's Fire-Spun Cloth"
    TAL_RASHAS_ADJUDICATION =  "Tal Rasha's Adjudication"
    TAL_RASHAS_LIDLESS_EYE =  "Tal Rasha's Lidless Eye"
    TAL_RASHAS_HOWLING_WIND =  "Tal Rasha's Howling Wind"
    TAL_RASHAS_HORADRIC_CREST =  "Tal Rasha's Horadric Crest"
    GRISWOLDS_VALOR =  "Griswold's Valor"
    GRISWOLDS_HEART =  "Griswold's Heart"
    GRISWOLDSS_REDEMPTION =  "Griswolds's Redemption"
    GRISWOLDS_HONOR =  "Griswold's Honor"
    TRANG_OULS_GUISE =  "Trang-Oul's Guise"
    TRANG_OULS_SCALES =  "Trang-Oul's Scales"
    TRANG_OULS_WING =  "Trang-Oul's Wing"
    TRANG_OULS_CLAWS =  "Trang-Oul's Claws"
    TRANG_OULS_GIRTH =  "Trang-Oul's Girth"
    MAVINAS_TRUE_SIGHT =  "M'avina's True Sight"
    MAVINAS_EMBRACE =  "M'avina's Embrace"
    MAVINAS_ICY_CLUTCH =  "M'avina's Icy Clutch"
    MAVINAS_TENET =  "M'avina's Tenet"
    MAVINAS_CASTER =  "M'avina's Caster"
    TELLING_OF_BEADS =  "Telling of Beads"
    LAYING_OF_HANDS =  "Laying of Hands"
    RITE_OF_PASSAGE =  "Rite of Passage"
    SPIRITUAL_CUSTODIAN =  "Spiritual Custodian"
    CREDENDUM =  "Credendum"
    DANGOONS_TEACHING =  "Dangoon's Teaching"
    HEAVENS_TAEBAEK =  "Heaven's Taebaek"
    HAEMOSUS_ADAMENT =  "Haemosu's Adament"
    ONDALS_ALMIGHTY =  "Ondal's Almighty"
    GUILLAUMES_FACE =  "Guillaume's Face"
    WILHELMS_PRIDE =  "Wilhelm's Pride"
    MAGNUS_SKIN =  "Magnus' Skin"
    WIHTSTANS_GUARD =  "Wihtstan's Guard"
    HWANINS_SPLENDOR =  "Hwanin's Splendor"
    HWANINS_REFUGE =  "Hwanin's Refuge"
    HWANINS_SEAL =  "Hwanin's Seal"
    HWANINS_JUSTICE =  "Hwanin's Justice"
    SAZABIS_COBALT_REDEEMER =  "Sazabi's Cobalt Redeemer"
    SAZABIS_GHOST_LIBERATOR =  "Sazabi's Ghost Liberator"
    SAZABIS_MENTAL_SHEATH =  "Sazabi's Mental Sheath"
    BUL_KATHOS_SACRED_CHARGE =  "Bul-Kathos' Sacred Charge"
    BUL_KATHOS_TRIBAL_GUARDIAN =  "Bul-Kathos' Tribal Guardian"
    BUL_KATHOS_DEATH_BAND =  "Bul-Kathos' Death Band"
    COW_KINGS_HORNS =  "Cow King's Horns"
    COW_KINGS_HIDE =  "Cow King's Hide"
    COW_KINGS_HOOFS =  "Cow King's Hoofs"
    NAJS_PUZZLER =  "Naj's Puzzler"
    NAJS_LIGHT_PLATE =  "Naj's Light Plate"
    NAJS_CIRCLET =  "Naj's Circlet"
    MC_AULEYS_PARAGON =  "McAuley's Paragon"
    MC_AULEYS_RIPRAP =  "McAuley's Riprap"
    MC_AULEYS_TABOO =  "McAuley's Taboo"
    MC_AULEYS_SUPERSTITION =  "McAuley's Superstition"


    @property
    def set(self) -> Set:
        return _METADATA[self.name].set

    @property
    def item(self) -> CodeLiteral:
        return _METADATA[self.name].item
