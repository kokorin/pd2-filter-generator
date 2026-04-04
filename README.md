# pd2-filter-generator

[![PyPI - Version](https://img.shields.io/pypi/v/pd2-filter-generator.svg)](https://pypi.org/project/pd2-filter-generator)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pd2-filter-generator.svg)](https://pypi.org/project/pd2-filter-generator)

-----

## Table of Contents

- [Installation](#installation)
- [Overview](#overview)
- [License](#license)

## Installation

```console
pip install pd2-filter-generator
```

## Overview

Build PD2 filter conditions using Python syntax. The library provides a DSL that maps to PD2 filter expressions.

### Syntax Comparison

Python keywords `and`, `or`, `not` cannot be overloaded, so we use bitwise operators:

| Operation | PD2 Filter | Python DSL |
|-----------|------------|------------|
| AND | `A B` (implicit) | `A & B` |
| OR | `A OR B` | `A \| B` |
| NOT | `!A` | `~A` |
| Equal | `A=5` | `A == 5` |
| Less than | `A<5` | `A < 5` |
| Greater than | `A>5` | `A > 5` |
| Between | `A~1-5` | `(1 < A) & (A < 5)` |

### Examples

**Simple AND condition:**
```
PD2:    NMAG SOCKETS=1
Python: NMAG & SOCKETS == 1
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

**Note:** Python's bitwise operators (`&`, `|`) have higher precedence than comparisons (`<`, `>`, `==`). Use parentheses around comparisons when combining with AND/OR:

```python
(X < Y) & (A > B)   # Correct: explicit grouping
A & (X < Y)         # Correct
A & X < Y           # Wrong: parses as (A & X) < Y
```

## Type System

The library enforces type safety through three literal types that match PD2's filter system.

### Node Type Hierarchy

```
Node (abstract base)
├── EqNode - supports ==, !=
│   └── ComparableNode - supports <, >, ==, !=
└── BooleanNode - supports ~, &, |

Concrete literal types:
- BoolLiteral(Literal, BooleanNode)
- CodeLiteral(Literal, EqNode)
- IntLiteral(Literal, ComparableNode)
```

### Literal Types

**BoolLiteral** — Boolean flags (presence checks):
```python
NMAG, RARE, UNI, SET       # Item quality
BOOTS, GLOVES, ARMOR       # Item groups
ETH, ID, SOCK              # Item properties
SHOP, GROUND, EQUIPPED     # Item state
```
- Supports: `&` (AND), `|` (OR), `~` (NOT)
- Does NOT support: `==`, `!=`, `<`, `>`
- Example: `NMAG & BOOTS | GLOVES`

**IntLiteral** — Integer values (fully comparable):
```python
SOCKETS, CLVL, ILVL, QLVL  # Levels and counts
GOLD, PRICE, QTY           # Quantities
FRES, CRES, LRES, PRES     # Resistances
RUNE                       # Rune number (1-33)
```
- Supports: `==`, `!=`, `<`, `>`, `&`, `|`
- Range check: `(1 < SOCKETS) & (SOCKETS < 3)` for PD2's `SOCKETS~1-3`
- Example: `RARE & (CLVL > 10) & (1 < SOCKETS) & (SOCKETS < 3)`

**CodeLiteral** — 3-letter item codes (equality only):
```python
'cap', 'hlm', 'msk'        # Helmets
'tbt', 'tgl'               # Boots, gloves
'aqv', 'cqv'               # Arrows, bolts
```
- Supports: `==`, `!=`, `&`, `|`
- Does NOT support: `<`, `>` (no ordering)
- Example: `ITEM == 'cap' | ITEM == 'hlm'`

### Type Safety

The type system prevents nonsensical operations at construction time:

```python
NMAG < RARE           # ❌ AttributeError: BoolLiteral has no '<' operator
SOCKETS == NMAG       # ❌ TypeError: NMAG does not support equality
'cap' < 'hlm'         # ❌ AttributeError: CodeLiteral has no '<' operator
~SOCKETS              # ❌ AttributeError: IntLiteral has no '__invert__'

SOCKETS == 1          # ✅ Both are IntLiteral (Comparable)
NMAG & BOOTS          # ✅ Both are BoolLiteral (Boolean)
ITEM == 'cap'         # ✅ Both are CodeLiteral (Eq)
1 < SOCKETS < 3       # ❌ TypeError: Cannot use in boolean context
(1 < SOCKETS) & (SOCKETS < 3)  # ✅ Explicit range check
```

### Design Goals

1. **Fail fast** — Invalid expressions raise errors immediately
2. **IDE support** — Type hints enable autocomplete
3. **Future-proof** — Will generate typed constants for all PD2 items
4. **Semantic clarity** — Type restrictions match PD2 filter semantics

### Known Limitations

**Current limitation:** All integers share the same `IntLiteral` type, allowing semantically invalid comparisons:

```python
SOCKETS == GOLD       # ✅ Type-safe but semantically wrong
CLVL < FRES           # ✅ Type-safe but meaningless
```

**Future improvement:** Introduce semantic integer types:

```python
# Different semantic types for integers
CountLiteral          # SOCKETS, QTY (item counts)
LevelLiteral          # CLVL, ILVL, QLVL (character/item levels)
CurrencyLiteral       # GOLD, PRICE (currency values)
ResistanceLiteral     # FRES, CRES, LRES, PRES (resistances)
StatLiteral           # Generic stats that can be compared

# Only allow comparisons within compatible types
SOCKETS == 1          # ✅ CountLiteral == int
CLVL > ILVL           # ✅ LevelLiteral > LevelLiteral
SOCKETS == GOLD       # ❌ TypeError: Cannot compare CountLiteral with CurrencyLiteral
```

This would require a more granular type system but would catch more semantic errors at construction time.

## Development

### Setup

Install [Hatch](https://hatch.pypa.io/):
```console
pip install hatch
```

Hatch automatically manages virtual environments and dependencies.

### Running Tests

```console
hatch run pytest
```

Run tests with coverage:
```console
hatch run pytest --cov=src/pd2_filter_generator
```

### Code Quality

**Format and lint** (using Ruff):
```console
hatch fmt
```

Check without fixing:
```console
hatch fmt --check
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

Install pre-commit to run checks automatically before each commit:

```console
pip install pre-commit
pre-commit install
```

This will run:
- File hygiene checks (trailing whitespace, EOF newlines, mixed line endings)
- Ruff format & lint
- Mypy type checking
- Pytest test suite

Run manually on all files:
```console
pre-commit run --all-files
```

### Project Structure

```
src/pd2_filter_generator/
├── expression.py       # Core AST and type system
└── __init__.py

tests/
└── test_expression.py  # Comprehensive test suite
```

## Future Ideas

**IN operator** — `A == ANY(X, Y, Z)` expands to `A=X OR A=Y OR A=Z`:
```python
A == ANY(X, Y, Z)   # Python DSL
A=X OR A=Y OR A=Z   # PD2 output
```

**Sum operator** — combine stats before comparison:
```python
(FRES + CRES + LRES + PRES) > 79   # Python DSL
FRES+CRES+LRES+PRES>79             # PD2 output
```

**Generated constants** — Auto-generate typed Python constants from PD2 data:
```python
# Auto-generated from PD2 database
from pd2_filter_generator.constants import *

my_filter = NMAG & SOCKETS == 1 & CLVL > 10  # Fully typed!
```

## License

`pd2-filter-generator` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
