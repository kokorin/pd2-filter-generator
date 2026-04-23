"""
Generated ItemType enum from PD2 data.

DO NOT EDIT MANUALLY - regenerate with: hatch run ./scripts/generate.py generate
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from pd2_filter_generator.expression import CodeLiteral


@dataclass(frozen=True)
class _Metadata:
    """Item type metadata."""

    body: bool  # "Body"
    throwable: bool  # "Throwable"
    beltable: bool  # "Beltable"
    shoots: bool  # "Shoots"
    quiver: bool  # "Quiver"


_METADATA: dict[str, _Metadata] = {
    "SHIELD": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "ARMOR": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "GOLD": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "BOW_QUIVER": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "CROSSBOW_QUIVER": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "PLAYER_BODY_PART": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "HERB": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "POTION": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "RING": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "ELIXIR": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "AMULET": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "CHARM": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "BOOTS": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "GLOVES": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "BOOK": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "BELT": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "GEM": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "TORCH": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "SCROLL": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "SCEPTER": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "WAND": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "STAFF": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "BOW": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "AXE": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "CLUB": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "SWORD": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "HAMMER": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "KNIFE": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "SPEAR": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "POLEARM": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "CROSSBOW": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "MACE": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "HELM": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "MISSILE_POTION": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "QUEST": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "BODY_PART": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "KEY": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "THROWING_KNIFE": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "THROWING_AXE": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "JAVELIN": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "WEAPON": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "MELEE_WEAPON": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "MISSILE_WEAPON": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "THROWN_WEAPON": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "COMBO_WEAPON": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "ANY_ARMOR": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "ANY_SHIELD": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "MISCELLANEOUS": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "SOCKET_FILLER": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "SECOND_HAND": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "STAVES_AND_RODS": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "MISSILE": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "BLUNT": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "JEWEL": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "CLASS_SPECIFIC": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "AMAZON_ITEM": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "BARBARIAN_ITEM": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "NECROMANCER_ITEM": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "PALADIN_ITEM": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "SORCERESS_ITEM": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "ASSASSIN_ITEM": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "DRUID_ITEM": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "HAND_TO_HAND": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "ORB": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "VOODOO_HEADS": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "AURIC_SHIELDS": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "PRIMAL_HELM": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "PELT": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "CLOAK": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "RUNE": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "CIRCLET": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "HEALING_POTION": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "MANA_POTION": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "REJUV_POTION": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "STAMINA_POTION": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "ANTIDOTE_POTION": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "THAWING_POTION": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "SMALL_CHARM": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "MEDIUM_CHARM": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "LARGE_CHARM": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "AMAZON_BOW": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "AMAZON_SPEAR": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "AMAZON_JAVELIN": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "HAND_TO_HAND_2": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "MAGIC_BOW_QUIV": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "MAGIC_XBOW_QUIV": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "ASSASSIN_MASTERY": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "CHIPPED_GEM": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "FLAWED_GEM": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "STANDARD_GEM": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "FLAWLESS_GEM": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "PERFECT_GEM": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "AMETHYST": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "DIAMOND": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "EMERALD": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "RUBY": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "SAPPHIRE": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "TOPAZ": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "SKULL": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "WORLDSTONE_SHARD": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "MAP": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "MAP_T1": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "MAP_T2": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "MAP_T3": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "MAP_T4": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "MAP_T1_EXC": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "MAP_T2_EXC": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "MAP_T3_EXC": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "MAP_T4_EXC": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "TWO__HANDED_MELEE_WEAPON": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "GENERAL_WEAPON": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "POLEARM_AND_SPEAR": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "BOX": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "IMBUE_MAG": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "IMBUE_RANDOM": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "IMBUE_RARE": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "REROLL_RARE": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "SCOUR": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "UPGRADE_MAG": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "UPGRADE_MAP": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "DUNGEON_SCARAB": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "PUZZLEBOX": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "STACK_GEM": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "STACK_FLAWLESS_GEM": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "STACK_PERFECT_GEM": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "STACK_AMETHYST": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "STACK_DIAMOND": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "STACK_EMERALD": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "STACK_RUBY": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "STACK_SAPPHIRE": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "STACK_TOPAZ": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "STACK_SKULL": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "STACK_RUNE": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "GENERIC_GEM": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "GENERIC_FLAWLESS_GEM": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "GENERIC_PERFECT_GEM": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "GENERIC_AMETHYST": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "GENERIC_DIAMOND": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "GENERIC_EMERALD": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "GENERIC_RUBY": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "GENERIC_SAPPHIRE": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "GENERIC_TOPAZ": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "GENERIC_SKULL": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "GENERIC_RUNE": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "GENERIC_F_AMETHYST": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "GENERIC_F_DIAMOND": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "GENERIC_F_EMERALD": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "GENERIC_F_RUBY": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "GENERIC_F_SAPPHIRE": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "GENERIC_F_TOPAZ": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "GENERIC_F_SKULL": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "GENERIC_P_AMETHYST": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "GENERIC_P_DIAMOND": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "GENERIC_P_EMERALD": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "GENERIC_P_RUBY": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "GENERIC_P_SAPPHIRE": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "GENERIC_P_TOPAZ": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "GENERIC_P_SKULL": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "EL_RUNE_GENERIC": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "ELD_RUNE_GENERIC": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "TIR_RUNE_GENERIC": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "NEF_RUNE_GENERIC": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "ETH_RUNE_GENERIC": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "ITH_RUNE_GENERIC": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "TAL_RUNE_GENERIC": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "RAL_RUNE_GENERIC": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "ORT_RUNE_GENERIC": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "THUL_RUNE_GENERIC": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "AMN_RUNE_GENERIC": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "SOL_RUNE_GENERIC": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "SHAEL_RUNE_GENERIC": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "DOL_RUNE_GENERIC": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "HEL_RUNE_GENERIC": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "IO_RUNE_GENERIC": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "LUM_RUNE_GENERIC": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "KO_RUNE_GENERIC": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "FAL_RUNE_GENERIC": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "LEM_RUNE_GENERIC": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "PUL_RUNE_GENERIC": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "UM_RUNE_GENERIC": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "MAL_RUNE_GENERIC": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "IST_RUNE_GENERIC": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "GUL_RUNE_GENERIC": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "VEX_RUNE_GENERIC": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "OHM_RUNE_GENERIC": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "LO_RUNE_GENERIC": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "SUR_RUNE_GENERIC": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "BER_RUNE_GENERIC": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "JAH_RUNE_GENERIC": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "CHAM_RUNE_GENERIC": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "ZOD_RUNE_GENERIC": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "RUNE_TEN_PLUS_GENERIC": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "UBER": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "UBER_ORGAN": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "PVP_MAP": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "BELT__S_": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "AMULET__S_": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "JEWEL_GENERIC": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "JEWEL_FRAGMENTS": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "SCYTHE_TYPE": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "PUZZLEPIECE": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "GENERAL_MELEE": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "FORTIFY_MAP": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "UBER_UNIQUE": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "LARZUKS_MALUS": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "UBER_MAP": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "MAP_T5": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "MAP_T5_EXC": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "TORCH_FRAGMENT": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "IMBUE_MAG_READY": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "IMBUE_RANDOM_READY": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "IMBUE_RARE_READY": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "REROLL_RARE_READY": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "UPGRADE_MAG_READY": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "TWO__H_SWORD": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "CRAFT_INGREDIENT": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "P_V_P_CHARM": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "SMALL_CHARM_P_V_P": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "MEDIUM_CHARM_P_V_P": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "LARGE_CHARM_P_V_P": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "TOKEN": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "RANGED_MASTERY": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "PVP_MAP_DESERT": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "CRYSTAL_SWORDS": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "TWO__H_CRYSTAL_SWORD": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "SPIKED_SHIELD": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "BONE_SHIELD": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "HEAVY_ARMOR": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "MEDIUM_ARMOR": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "LIGHT_ARMOR": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "HEAVY_SHIELD": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "MEDIUM_SHIELD": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
    "LIGHT_SHIELD": _Metadata(
        body=False,
        throwable=False,
        beltable=False,
        shoots=False,
        quiver=False,
    ),
}


class ItemType(Enum):
    """PD2 item type categories."""

    SHIELD = CodeLiteral("shie")  # Shield
    ARMOR = CodeLiteral("tors")  # Armor
    GOLD = CodeLiteral("gold")  # Gold
    BOW_QUIVER = CodeLiteral("bowq")  # Bow Quiver
    CROSSBOW_QUIVER = CodeLiteral("xboq")  # Crossbow Quiver
    PLAYER_BODY_PART = CodeLiteral("play")  # Player Body Part
    HERB = CodeLiteral("herb")  # Herb
    POTION = CodeLiteral("poti")  # Potion
    RING = CodeLiteral("ring")  # Ring
    ELIXIR = CodeLiteral("elix")  # Elixir
    AMULET = CodeLiteral("amul")  # Amulet
    CHARM = CodeLiteral("char")  # Charm
    BOOTS = CodeLiteral("boot")  # Boots
    GLOVES = CodeLiteral("glov")  # Gloves
    BOOK = CodeLiteral("book")  # Book
    BELT = CodeLiteral("belt")  # Belt
    GEM = CodeLiteral("gem")  # Gem
    TORCH = CodeLiteral("torc")  # Torch
    SCROLL = CodeLiteral("scro")  # Scroll
    SCEPTER = CodeLiteral("scep")  # Scepter
    WAND = CodeLiteral("wand")  # Wand
    STAFF = CodeLiteral("staf")  # Staff
    BOW = CodeLiteral("bow")  # Bow
    AXE = CodeLiteral("axe")  # Axe
    CLUB = CodeLiteral("club")  # Club
    SWORD = CodeLiteral("swor")  # Sword
    HAMMER = CodeLiteral("hamm")  # Hammer
    KNIFE = CodeLiteral("knif")  # Knife
    SPEAR = CodeLiteral("spea")  # Spear
    POLEARM = CodeLiteral("pole")  # Polearm
    CROSSBOW = CodeLiteral("xbow")  # Crossbow
    MACE = CodeLiteral("mace")  # Mace
    HELM = CodeLiteral("helm")  # Helm
    MISSILE_POTION = CodeLiteral("tpot")  # Missile Potion
    QUEST = CodeLiteral("ques")  # Quest
    BODY_PART = CodeLiteral("body")  # Body Part
    KEY = CodeLiteral("key")  # Key
    THROWING_KNIFE = CodeLiteral("tkni")  # Throwing Knife
    THROWING_AXE = CodeLiteral("taxe")  # Throwing Axe
    JAVELIN = CodeLiteral("jave")  # Javelin
    WEAPON = CodeLiteral("weap")  # Weapon
    MELEE_WEAPON = CodeLiteral("mele")  # Melee Weapon
    MISSILE_WEAPON = CodeLiteral("miss")  # Missile Weapon
    THROWN_WEAPON = CodeLiteral("thro")  # Thrown Weapon
    COMBO_WEAPON = CodeLiteral("comb")  # Combo Weapon
    ANY_ARMOR = CodeLiteral("armo")  # Any Armor
    ANY_SHIELD = CodeLiteral("shld")  # Any Shield
    MISCELLANEOUS = CodeLiteral("misc")  # Miscellaneous
    SOCKET_FILLER = CodeLiteral("sock")  # Socket Filler
    SECOND_HAND = CodeLiteral("seco")  # Second Hand
    STAVES_AND_RODS = CodeLiteral("rod")  # Staves And Rods
    MISSILE = CodeLiteral("misl")  # Missile
    BLUNT = CodeLiteral("blun")  # Blunt
    JEWEL = CodeLiteral("jewl")  # Jewel
    CLASS_SPECIFIC = CodeLiteral("clas")  # Class Specific
    AMAZON_ITEM = CodeLiteral("amaz")  # Amazon Item
    BARBARIAN_ITEM = CodeLiteral("barb")  # Barbarian Item
    NECROMANCER_ITEM = CodeLiteral("necr")  # Necromancer Item
    PALADIN_ITEM = CodeLiteral("pala")  # Paladin Item
    SORCERESS_ITEM = CodeLiteral("sorc")  # Sorceress Item
    ASSASSIN_ITEM = CodeLiteral("assn")  # Assassin Item
    DRUID_ITEM = CodeLiteral("drui")  # Druid Item
    HAND_TO_HAND = CodeLiteral("h2h")  # Hand to Hand
    ORB = CodeLiteral("orb")  # Orb
    VOODOO_HEADS = CodeLiteral("head")  # Voodoo Heads
    AURIC_SHIELDS = CodeLiteral("ashd")  # Auric Shields
    PRIMAL_HELM = CodeLiteral("phlm")  # Primal Helm
    PELT = CodeLiteral("pelt")  # Pelt
    CLOAK = CodeLiteral("cloa")  # Cloak
    RUNE = CodeLiteral("rune")  # Rune
    CIRCLET = CodeLiteral("circ")  # Circlet
    HEALING_POTION = CodeLiteral("hpot")  # Healing Potion
    MANA_POTION = CodeLiteral("mpot")  # Mana Potion
    REJUV_POTION = CodeLiteral("rpot")  # Rejuv Potion
    STAMINA_POTION = CodeLiteral("spot")  # Stamina Potion
    ANTIDOTE_POTION = CodeLiteral("apot")  # Antidote Potion
    THAWING_POTION = CodeLiteral("wpot")  # Thawing Potion
    SMALL_CHARM = CodeLiteral("scha")  # Small Charm
    MEDIUM_CHARM = CodeLiteral("mcha")  # Medium Charm
    LARGE_CHARM = CodeLiteral("lcha")  # Large Charm
    AMAZON_BOW = CodeLiteral("abow")  # Amazon Bow
    AMAZON_SPEAR = CodeLiteral("aspe")  # Amazon Spear
    AMAZON_JAVELIN = CodeLiteral("ajav")  # Amazon Javelin
    HAND_TO_HAND_2 = CodeLiteral("h2h2")  # Hand to Hand 2
    MAGIC_BOW_QUIV = CodeLiteral("mboq")  # Magic Bow Quiv
    MAGIC_XBOW_QUIV = CodeLiteral("mxbq")  # Magic Xbow Quiv
    ASSASSIN_MASTERY = CodeLiteral("asm")  # Assassin Mastery
    CHIPPED_GEM = CodeLiteral("gem0")  # Chipped Gem
    FLAWED_GEM = CodeLiteral("gem1")  # Flawed Gem
    STANDARD_GEM = CodeLiteral("gem2")  # Standard Gem
    FLAWLESS_GEM = CodeLiteral("gem3")  # Flawless Gem
    PERFECT_GEM = CodeLiteral("gem4")  # Perfect Gem
    AMETHYST = CodeLiteral("gema")  # Amethyst
    DIAMOND = CodeLiteral("gemd")  # Diamond
    EMERALD = CodeLiteral("geme")  # Emerald
    RUBY = CodeLiteral("gemr")  # Ruby
    SAPPHIRE = CodeLiteral("gems")  # Sapphire
    TOPAZ = CodeLiteral("gemt")  # Topaz
    SKULL = CodeLiteral("gemz")  # Skull
    WORLDSTONE_SHARD = CodeLiteral("corr")  # Worldstone Shard
    MAP = CodeLiteral("map")  # Map
    MAP_T1 = CodeLiteral("t1m")  # Map T1
    MAP_T2 = CodeLiteral("t2m")  # Map T2
    MAP_T3 = CodeLiteral("t3m")  # Map T3
    MAP_T4 = CodeLiteral("t4m")  # Map T4
    MAP_T1_EXC = CodeLiteral("t1me")  # Map T1 exc
    MAP_T2_EXC = CodeLiteral("t2me")  # Map T2 exc
    MAP_T3_EXC = CodeLiteral("t3me")  # Map T3 exc
    MAP_T4_EXC = CodeLiteral("t4me")  # Map T4 exc
    TWO__HANDED_MELEE_WEAPON = CodeLiteral("2han")  # 2Handed Melee Weapon
    GENERAL_WEAPON = CodeLiteral("gen")  # General Weapon
    POLEARM_AND_SPEAR = CodeLiteral("pas")  # Polearm and Spear
    BOX = CodeLiteral("box")  # Box
    IMBUE_MAG = CodeLiteral("imma")  # ImbueMag
    IMBUE_RANDOM = CodeLiteral("imrn")  # ImbueRandom
    IMBUE_RARE = CodeLiteral("imra")  # ImbueRare
    REROLL_RARE = CodeLiteral("rera")  # RerollRare
    SCOUR = CodeLiteral("scou")  # Scour
    UPGRADE_MAG = CodeLiteral("upma")  # UpgradeMag
    UPGRADE_MAP = CodeLiteral("upmp")  # Upgrade Map
    DUNGEON_SCARAB = CodeLiteral("scrb")  # Dungeon Scarab
    PUZZLEBOX = CodeLiteral("lbox")  # Puzzlebox
    STACK_GEM = CodeLiteral("gsm")  # Stack gem
    STACK_FLAWLESS_GEM = CodeLiteral("gsm3")  # Stack Flawless Gem
    STACK_PERFECT_GEM = CodeLiteral("gsm4")  # Stack Perfect Gem
    STACK_AMETHYST = CodeLiteral("gsma")  # Stack Amethyst
    STACK_DIAMOND = CodeLiteral("gsmd")  # Stack Diamond
    STACK_EMERALD = CodeLiteral("gsme")  # Stack Emerald
    STACK_RUBY = CodeLiteral("gsmr")  # Stack Ruby
    STACK_SAPPHIRE = CodeLiteral("gsms")  # Stack Sapphire
    STACK_TOPAZ = CodeLiteral("gsmt")  # Stack Topaz
    STACK_SKULL = CodeLiteral("gsmz")  # Stack Skull
    STACK_RUNE = CodeLiteral("runs")  # Stack Rune
    GENERIC_GEM = CodeLiteral("ggm")  # Generic Gem
    GENERIC_FLAWLESS_GEM = CodeLiteral("ggm3")  # Generic Flawless Gem
    GENERIC_PERFECT_GEM = CodeLiteral("ggm4")  # Generic Perfect Gem
    GENERIC_AMETHYST = CodeLiteral("ggma")  # Generic Amethyst
    GENERIC_DIAMOND = CodeLiteral("ggmd")  # Generic Diamond
    GENERIC_EMERALD = CodeLiteral("ggme")  # Generic Emerald
    GENERIC_RUBY = CodeLiteral("ggmr")  # Generic Ruby
    GENERIC_SAPPHIRE = CodeLiteral("ggms")  # Generic Sapphire
    GENERIC_TOPAZ = CodeLiteral("ggmt")  # Generic Topaz
    GENERIC_SKULL = CodeLiteral("ggmz")  # Generic Skull
    GENERIC_RUNE = CodeLiteral("rung")  # Generic Rune
    GENERIC_F_AMETHYST = CodeLiteral("gg3a")  # Generic F Amethyst
    GENERIC_F_DIAMOND = CodeLiteral("gg3d")  # Generic F Diamond
    GENERIC_F_EMERALD = CodeLiteral("gg3e")  # Generic F Emerald
    GENERIC_F_RUBY = CodeLiteral("gg3r")  # Generic F Ruby
    GENERIC_F_SAPPHIRE = CodeLiteral("gg3s")  # Generic F Sapphire
    GENERIC_F_TOPAZ = CodeLiteral("gg3t")  # Generic F Topaz
    GENERIC_F_SKULL = CodeLiteral("gg3z")  # Generic F Skull
    GENERIC_P_AMETHYST = CodeLiteral("gg4a")  # Generic P Amethyst
    GENERIC_P_DIAMOND = CodeLiteral("gg4d")  # Generic P Diamond
    GENERIC_P_EMERALD = CodeLiteral("gg4e")  # Generic P Emerald
    GENERIC_P_RUBY = CodeLiteral("gg4r")  # Generic P Ruby
    GENERIC_P_SAPPHIRE = CodeLiteral("gg4s")  # Generic P Sapphire
    GENERIC_P_TOPAZ = CodeLiteral("gg4t")  # Generic P Topaz
    GENERIC_P_SKULL = CodeLiteral("gg4z")  # Generic P Skull
    EL_RUNE_GENERIC = CodeLiteral("r01g")  # El Rune Generic
    ELD_RUNE_GENERIC = CodeLiteral("r02g")  # Eld Rune Generic
    TIR_RUNE_GENERIC = CodeLiteral("r03g")  # Tir Rune Generic
    NEF_RUNE_GENERIC = CodeLiteral("r04g")  # Nef Rune Generic
    ETH_RUNE_GENERIC = CodeLiteral("r05g")  # Eth Rune Generic
    ITH_RUNE_GENERIC = CodeLiteral("r06g")  # Ith Rune Generic
    TAL_RUNE_GENERIC = CodeLiteral("r07g")  # Tal Rune Generic
    RAL_RUNE_GENERIC = CodeLiteral("r08g")  # Ral Rune Generic
    ORT_RUNE_GENERIC = CodeLiteral("r09g")  # Ort Rune Generic
    THUL_RUNE_GENERIC = CodeLiteral("r10g")  # Thul Rune Generic
    AMN_RUNE_GENERIC = CodeLiteral("r11g")  # Amn Rune Generic
    SOL_RUNE_GENERIC = CodeLiteral("r12g")  # Sol Rune Generic
    SHAEL_RUNE_GENERIC = CodeLiteral("r13g")  # Shael Rune Generic
    DOL_RUNE_GENERIC = CodeLiteral("r14g")  # Dol Rune Generic
    HEL_RUNE_GENERIC = CodeLiteral("r15g")  # Hel Rune Generic
    IO_RUNE_GENERIC = CodeLiteral("r16g")  # Io Rune Generic
    LUM_RUNE_GENERIC = CodeLiteral("r17g")  # Lum Rune Generic
    KO_RUNE_GENERIC = CodeLiteral("r18g")  # Ko Rune Generic
    FAL_RUNE_GENERIC = CodeLiteral("r19g")  # Fal Rune Generic
    LEM_RUNE_GENERIC = CodeLiteral("r20g")  # Lem Rune Generic
    PUL_RUNE_GENERIC = CodeLiteral("r21g")  # Pul Rune Generic
    UM_RUNE_GENERIC = CodeLiteral("r22g")  # Um Rune Generic
    MAL_RUNE_GENERIC = CodeLiteral("r23g")  # Mal Rune Generic
    IST_RUNE_GENERIC = CodeLiteral("r24g")  # Ist Rune Generic
    GUL_RUNE_GENERIC = CodeLiteral("r25g")  # Gul Rune Generic
    VEX_RUNE_GENERIC = CodeLiteral("r26g")  # Vex Rune Generic
    OHM_RUNE_GENERIC = CodeLiteral("r27g")  # Ohm Rune Generic
    LO_RUNE_GENERIC = CodeLiteral("r28g")  # Lo Rune Generic
    SUR_RUNE_GENERIC = CodeLiteral("r29g")  # Sur Rune Generic
    BER_RUNE_GENERIC = CodeLiteral("r30g")  # Ber Rune Generic
    JAH_RUNE_GENERIC = CodeLiteral("r31g")  # Jah Rune Generic
    CHAM_RUNE_GENERIC = CodeLiteral("r32g")  # Cham Rune Generic
    ZOD_RUNE_GENERIC = CodeLiteral("r33g")  # Zod Rune Generic
    RUNE_TEN_PLUS_GENERIC = CodeLiteral("r1pg")  # Rune ten plus Generic
    UBER = CodeLiteral("ubr")  # Uber
    UBER_ORGAN = CodeLiteral("ubor")  # UberOrgan
    PVP_MAP = CodeLiteral("pvpm")  # Pvp Map
    BELT__S_ = CodeLiteral("bels")  # Belt [S]
    AMULET__S_ = CodeLiteral("amus")  # Amulet [S]
    JEWEL_GENERIC = CodeLiteral("jewg")  # Jewel Generic
    JEWEL_FRAGMENTS = CodeLiteral("jewf")  # Jewel Fragments
    SCYTHE_TYPE = CodeLiteral("sc9")  # Scythe Type
    PUZZLEPIECE = CodeLiteral("lpp")  # Puzzlepiece
    GENERAL_MELEE = CodeLiteral("mgen")  # General Melee
    FORTIFY_MAP = CodeLiteral("fort")  # Fortify Map
    UBER_UNIQUE = CodeLiteral("ubru")  # UberUnique
    LARZUKS_MALUS = CodeLiteral("lmal")  # Larzuks Malus
    UBER_MAP = CodeLiteral("ubmp")  # UberMap
    MAP_T5 = CodeLiteral("t5m")  # Map T5
    MAP_T5_EXC = CodeLiteral("t5me")  # Map T5 exc
    TORCH_FRAGMENT = CodeLiteral("cm2f")  # Torch Fragment
    IMBUE_MAG_READY = CodeLiteral("irma")  # ImbueMag Ready
    IMBUE_RANDOM_READY = CodeLiteral("irrn")  # ImbueRandom Ready
    IMBUE_RARE_READY = CodeLiteral("irra")  # ImbueRare Ready
    REROLL_RARE_READY = CodeLiteral("rrra")  # RerollRare Ready
    UPGRADE_MAG_READY = CodeLiteral("urma")  # UpgradeMag Ready
    TWO__H_SWORD = CodeLiteral("2hsw")  # 2H Sword
    CRAFT_INGREDIENT = CodeLiteral("crft")  # Craft Ingredient
    P_V_P_CHARM = CodeLiteral("chap")  # PVP Charm
    SMALL_CHARM_P_V_P = CodeLiteral("schp")  # Small Charm PVP
    MEDIUM_CHARM_P_V_P = CodeLiteral("mchp")  # Medium Charm PVP
    LARGE_CHARM_P_V_P = CodeLiteral("lchp")  # Large Charm PVP
    TOKEN = CodeLiteral("toa")  # Token
    RANGED_MASTERY = CodeLiteral("rng")  # Ranged Mastery
    PVP_MAP_DESERT = CodeLiteral("pvpd")  # Pvp Map Desert
    CRYSTAL_SWORDS = CodeLiteral("crys")  # Crystal Swords
    TWO__H_CRYSTAL_SWORD = CodeLiteral("2hcs")  # 2H Crystal Sword
    SPIKED_SHIELD = CodeLiteral("sshi")  # Spiked Shield
    BONE_SHIELD = CodeLiteral("bshi")  # Bone Shield
    HEAVY_ARMOR = CodeLiteral("harm")  # Heavy Armor
    MEDIUM_ARMOR = CodeLiteral("marm")  # Medium Armor
    LIGHT_ARMOR = CodeLiteral("larm")  # Light Armor
    HEAVY_SHIELD = CodeLiteral("hshi")  # Heavy Shield
    MEDIUM_SHIELD = CodeLiteral("mshi")  # Medium Shield
    LIGHT_SHIELD = CodeLiteral("lshi")  # Light Shield

    @property
    def body(self) -> bool:
        return _METADATA[self.name].body

    @property
    def throwable(self) -> bool:
        return _METADATA[self.name].throwable

    @property
    def beltable(self) -> bool:
        return _METADATA[self.name].beltable

    @property
    def shoots(self) -> bool:
        return _METADATA[self.name].shoots

    @property
    def quiver(self) -> bool:
        return _METADATA[self.name].quiver
