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
| Between | `A~1-5` | `1 < A < 5` |

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
Python: RARE & CLVL > 10 & 1 < SOCKETS < 2
```

### Operator Precedence

**Note:** Python's bitwise operators (`&`, `|`) have higher precedence than comparisons (`<`, `>`, `==`). Use parentheses around comparisons when combining with AND/OR:

```python
(X < Y) & (A > B)   # Correct: explicit grouping
A & (X < Y)         # Correct
A & X < Y           # Wrong: parses as (A & X) < Y
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

## License

`pd2-filter-generator` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
