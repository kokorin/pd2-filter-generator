"""Filter and Rule classes for building PD2 loot filters."""

from pd2_filter_generator.expression import BoolExpr


class Rule:
    """A single filter rule."""

    def __init__(self, condition: BoolExpr, name: str):
        self._condition = condition
        self._name = name


class Filter:
    """A PD2 loot filter composed of ordered rules."""

    def __init__(self):
        self._rules: list[Rule] = []

    def show(self, condition: BoolExpr, name: str) -> Rule:
        rule = Rule(condition, name)
        self._rules.append(rule)
        return rule
