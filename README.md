# AI Lab 01 — Python Programming Foundations for AI

Introductory lab of the **Artificial Intelligence Lab** course (BSCS, Air University). The lab sets up the Python environment used throughout the course and covers the core language fundamentals — variables, data structures, control flow, and functions — followed by a first look at NumPy arrays and vectorized operations.

The exercises are framed around a simple **reflex vacuum-cleaner agent** ("ReflexBot"): battery levels, room grids, and percept-to-action rules give the basic Python concepts an agent-based context that later labs build on.

## Lab Objectives

- Verify the Python scientific stack used in this course (NumPy, Pandas, Matplotlib, scikit-learn, NetworkX)
- Declare variables of different types and inspect them with `type()`
- Convert between `str`, `int`, and `float`
- Use arithmetic and logical operators
- Control program flow with `if/elif/else`, `for`, and `while` (including `break`/`continue`)
- Work with the built-in collections: `list`, `tuple`, and `dict`
- Write functions, including a rule-based simple reflex agent
- Create NumPy arrays and apply vectorized operations (`np.diff`, boolean masking, `np.mean`)

## Tasks Implemented

| # | File | Concept | What it does |
|---|------|---------|--------------|
| 1 | `lab01.py` | Library environment check | Imports NumPy, Pandas, Matplotlib, scikit-learn, and NetworkX and prints each version |
| 2 | `vraibles.py` | Variables & data types | Stores an agent name, battery level, temperature, and an active flag; prints each value with its type |
| 3 | `typeconversion.py` | Type conversion | Converts `"87"` → `87` → `87.0` and checks types |
| 4 | `operators.py` | Operators | Arithmetic (`+`, `-`, `**`, `//`, `%`) and a logical `and` check against the battery level imported from `vraibles.py` |
| 5 | `conditions.py` | Conditional statements | `battery_status()` classifies a battery level as high / medium / low using `if/elif/else` |
| 6 | `forloop.py` | `for` loop | Iterates over a list of visited rooms |
| 7 | `whileloop.py` | `while` loop | Simulates battery drain with `continue` (skip 40) and `break` (stop at ≤ 10) |
| 8 | `List.py` | Lists | Builds a percept list (`dust`, `wall`, `clean_floor`) and appends `obstacles` |
| 9 | `tuples.py` | Tuples | Stores a grid position `(2, 3)` as an immutable tuple |
| 10 | `dictionaries.py` | Dictionaries | Models agent state (battery, location, mode) as a dict and reads a value by key |
| 11 | `functions.py` | Functions | `simple_reflex_agent(percept)` maps percepts to actions (`dust → clean`, `wall → turn`, …) via a rule dictionary |
| 12 | `nestedarray.py` | NumPy 2D arrays | Creates a 3×3 room grid (1 = dirty cell) and prints the array and its shape |
| 13 | `vectorizedoperations.py` | Vectorized operations | Battery readings array: per-step drop with `np.diff`, readings below 80 via boolean mask, and the mean |

## Tech Stack

- **Python 3**
- **NumPy** — arrays and vectorized operations
- **Pandas, Matplotlib, scikit-learn, NetworkX** — verified in `lab01.py`; used in later labs

Most scripts (Tasks 2–11) use only the Python standard library. NumPy is required for Tasks 1, 12, and 13.

## Project Structure

```
ai-lab-01/
├── lab01.py                  # Library environment check
├── vraibles.py               # Variables and data types
├── typeconversion.py         # Type conversion
├── operators.py              # Arithmetic and logical operators
├── conditions.py             # if / elif / else
├── forloop.py                # for loop
├── whileloop.py              # while loop with break/continue
├── List.py                   # Lists
├── tuples.py                 # Tuples
├── dictionaries.py           # Dictionaries
├── functions.py              # Functions — simple reflex agent
├── nestedarray.py            # NumPy 2D arrays
└── vectorizedoperations.py   # NumPy vectorized operations
```

## Setup

Requires Python 3. To run the NumPy and library-check scripts, install the scientific stack:

```bash
pip install numpy pandas matplotlib scikit-learn networkx
```

## How to Run

Every script is standalone — run it from the project directory:

```bash
python lab01.py
python vraibles.py
python typeconversion.py
python operators.py
python conditions.py
python forloop.py
python whileloop.py
python List.py
python tuples.py
python dictionaries.py
python functions.py
python nestedarray.py
python vectorizedoperations.py
```

> Note: `operators.py` imports `battery_level` from `vraibles.py`, so running it first prints the variable/type lines from that file.

## Sample Output

`lab01.py` (versions will differ by machine):

```
Numpy:, 1.26.4
Pandas:, 2.1.4
Matplotlib:, 3.6.3
Sklearn:, 1.9.1
Networkx:, 3.7
All core librarires loaded Successfully.
```

`functions.py` — the simple reflex agent's rule table in action:

```
dust -> clean
wall -> turn
Clean_floor -> no action
obstacles -> turn
```

`vectorizedoperations.py`:

```
Drop per step:  [-8 -8 -8 -8 -8]
Below 80 :  [76 68 60]
mean: 80.0
```

## Notes

- The rule lookup in `functions.py` is case-sensitive: `"Clean_floor"` (capital C) returns `no action` because the rule key is lowercase `"clean_floor"`.
- In `nestedarray.py`, the final print statement outputs only its label — the dirty-cell count itself is not computed.
- Original coursework filenames are kept as submitted (e.g. `vraibles.py`), and `operators.py` depends on it by import, so the names should not be changed without updating that import.

## Course Context

AI Lab 01 — Artificial Intelligence Lab, BSCS (5th semester), Air University, Islamabad.
