# pd2-filter-generator

[![PyPI - Version](https://img.shields.io/pypi/v/pd2-filter-generator.svg)](https://pypi.org/project/pd2-filter-generator)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pd2-filter-generator.svg)](https://pypi.org/project/pd2-filter-generator)

-----

## Table of Contents

- [Installation](#installation)
- [Overview](#overview)
- [Type System](#type-system)
- [Generated Enums](#generated-enums)
- [Development](#development)
- [License](#license)

## Installation

```console
pip install pd2-filter-generator
```

## Overview

Build PD2 filter conditions using Python syntax. The library provides a DSL that maps to PD2 filter expressions.

### Syntax Comparison

Python keywords `and`, `or`, `not` cannot be overloaded, so we use bitwise operators:

| Operation    | PD2 Filter     | Python DSL                      |
|--------------|----------------|---------------------------------|
| AND          | `A B` (implicit) | `A & B`                       |
| OR           | `A OR B`       | `A \| B`                        |
| NOT          | `!A`           | `~A`                            |
| Equal        | `A=5`          | `A == 5`                        |
| Less than    | `A<5`          | `A < 5`                         |
| Greater than | `A>5`          | `A > 5`                         |
| Between      | `A~1-5`        | `(1 < A) & (A < 5)`             |

### Examples

**Simple AND condition:**
```
PD2:    NMAG SOCKETS=1
Python: NMAG & (SOCKETS == 1)
```

**OR with grouping:**
```
PD2:    NMAG (BOOTS OR GLOVES OR BELT)
Python: NMAG & (BOOTS | GLOVES | BELT)
```

**NOT conditions:**
```
PD2:    MAG !ID !(BAR OR DRU)
Python: MAG & ~ID & ~(BAR | DRU)
```

**Complex expression:**
```
PD2:    RARE CLVL>10 SOCKETS~1-2
Python: RARE & (CLVL > 10) & (1 < SOCKETS) & (SOCKETS < 2)
```

### Operator Precedence

Python's bitwise operators (`&`, `|`) have lower precedence than comparisons (`<`, `>`, `==`). Use parentheses around comparisons when combining with AND/OR:

```python
(X < Y) & (A > B)   # Correct: explicit grouping
A & (X < Y)         # Correct
A & X < Y           # Wrong: parses as (A & X) < Y
```

## Type System

The library enforces type safety through two expression types matching PD2's filter system.

### Node Type Hierarchy

```
Node (abstract base)
├── BoolExpr  — supports ~, &, |
└── IntExpr   — supports ==, !=, <, >

Leaf (abstract, base for all leaf nodes)
├── BoolRef(Leaf, BoolExpr)   — boolean flags and item-type predicates
├── IntRef(Leaf, IntExpr)     — integer references (named stats)
└── IntLit(Leaf, IntExpr)     — integer literals (numeric values)
```

Mixins mirror the node hierarchy for use in enums:
- `BoolMixin` — enum members participate in `~`, `&`, `|` expressions
- `IntMixin`  — enum members participate in `==`, `!=`, `<`, `>` expressions

### Leaf Types

**BoolRef** — Boolean flags and item-type predicates:
```python
NMAG = BoolRef("NMAG")   # Item quality flags
BOOTS = BoolRef("BOOTS") # Item group predicates
```
- Supports: `&` (AND), `|` (OR), `~` (NOT)
- Does NOT support: `==`, `!=`, `<`, `>`

**IntRef** — Named integer references:
```python
SOCKETS = IntRef("SOCKETS")
CLVL = IntRef("CLVL")
```
- Supports: `==`, `!=`, `<`, `>`
- Does NOT support: `~`, `&`, `|`

**IntLit** — Numeric integer literals:
```python
ONE = IntLit("1")
TEN = IntLit("10")
```
- Same operators as `IntRef`

### Type Safety

```python
NMAG < RARE           # TypeError: BoolExpr has no '<'
SOCKETS == NMAG       # TypeError: requires IntExpr operands
~SOCKETS              # TypeError: IntExpr has no '__invert__'
1 < SOCKETS < 3       # TypeError: cannot use in boolean context
(1 < SOCKETS) & (SOCKETS < 3)  # Correct range check
```

## Generated Enums

Typed enum classes are auto-generated from PD2 data files. Each member participates directly in filter expressions via `BoolMixin`.

### Available Enums

| Module         | Class       | Example member         |
|----------------|-------------|------------------------|
| `armor`        | `Armor`     | `Armor.FULL_PLATE_MAIL` |
| `weapon`       | `Weapon`    | `Weapon.AXE`           |
| `set`          | `Set`       | `Set.CIVERBS_VESTMENTS` |
| `set_item`     | `SetItem`   | `SetItem.CIVERBS_WARD` |
| `unique_item`  | `UniqueItem`| `UniqueItem.THE_GNASHER` |

### Usage

```python
from pd2_filter_generator.armor import Armor
from pd2_filter_generator.weapon import Weapon
from pd2_filter_generator.expression import BoolRef

NMAG = BoolRef("NMAG")

# Enum members work directly in expressions
expr = NMAG & (Armor.FULL_PLATE_MAIL | Armor.GOTHIC_PLATE)
expr = ~Weapon.AXE & NMAG

# Metadata is accessible as properties
Armor.FULL_PLATE_MAIL.reqstr    # int
Armor.FULL_PLATE_MAIL.levelreq  # int
Weapon.AXE.type                 # str
SetItem.CIVERBS_WARD.set        # Set enum member
UniqueItem.THE_GNASHER.ladder   # bool
```

### Regenerating

Requires a local PD2 installation:
```console
hatch run ./scripts/generate.py generate
```

## Development

### Setup

Install [Hatch](https://hatch.pypa.io/):
```console
pip install hatch
```

### Running Tests

```console
hatch run pytest
```

### Code Quality

**Format and lint** (using Ruff):
```console
hatch fmt
```

**Type checking** (using mypy):
```console
hatch run types:check
```

**Run all checks**:
```console
hatch fmt --check && hatch run types:check && hatch run pytest
```

### Pre-commit Hooks

```console
pip install pre-commit
pre-commit install
```

Runs format, lint, type checking, and tests before each commit.

### Project Structure

```
src/pd2_filter_generator/
├── expression.py       # Core AST and type system
├── armor.py            # Generated Armor enum
├── weapon.py           # Generated Weapon enum
├── set.py              # Generated Set enum
├── set_item.py         # Generated SetItem enum
├── unique_item.py      # Generated UniqueItem enum
└── __init__.py

scripts/
├── generate.py         # Code generation script
└── templates/          # Jinja2 templates for generated files

tests/
├── test_expression.py
├── test_armor.py
├── test_weapon.py
├── test_set.py
├── test_set_item.py
└── test_unique_item.py
```

## Future Ideas

**IN operator** — `A == ANY(X, Y, Z)` expands to `A=X OR A=Y OR A=Z`:
```python
ITEM == ANY(Armor.CAP, Armor.HELM)
```

**Sum operator** — combine stats before comparison:
```python
(FRES + CRES + LRES + PRES) > 79
```

## License

`pd2-filter-generator` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
