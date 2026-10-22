# (Elements of) Programming and Algorithms for Data Science

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Exercises](https://img.shields.io/badge/Exercises-73%20Total-f39c12?logo=codeforces&logoColor=white)](https://github.com/aldojacopovirno/pa4ds)
[![Focus: Algorithms](https://img.shields.io/badge/Focus-Algorithms-6f42c1)](https://github.com/topics/algorithms)
[![Focus: Data Science](https://img.shields.io/badge/Focus-Data%20Science-4c8c4a)](https://github.com/topics/data-science)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen.svg)](https://github.com/aldojacopovirno/pa4ds/pulls)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

---

This repository is designed as an approachable, hands-on practice space for the Python building blocks used in data science (and general programming). The aim is to provide a (beginner-friendly) collection of bite-sized exercises that can be solved with a few lines of code, illustrating clear, readable, and intuitive problem-solving patterns.

## Repository Structure

```text
pa4ds/
├── arithmetic/       # 9 exercises
├── conditionals/     # 3 exercises
├── functions/        # 18 exercises
├── games/            # 2 exercises
├── lists/            # 10 exercises
├── loops/            # 11 exercises
├── randomness/       # 3 exercises
├── recursion/        # 3 exercises
├── strings/          # 9 exercises
├── tuples/           # 5 exercises
├── .gitignore
├── CONVENTIONS.md
├── LICENSE
├── requirements.txt
└── README.md
```

## Topics & Exercises

These exercises are strictly for educational purposes and are not intended for production environments. Solutions prioritize clarity, readability, and step-by-step logic over premature optimization (which is outside the scope of this repository).

Exercises within each topic folder progress from trivial one-liners to "more complex" problems that require multiple steps and (deeper) reasoning. Each exercise is self-contained in a single `.py` file, with the assignment described in comments at the top.

| Topic | Exercises | Core Concepts & Highlights |
| :--- | :---: | :--- |
| [`arithmetic/`](arithmetic/) | **9** | Calculations, numeric representations, and units |
| [`conditionals/`](conditionals/) | **3** | Branching logic, decisions, and boundary cases |
| [`functions/`](functions/) | **18** | Reusable calculations, scope, and input helper wrappers |
| [`games/`](games/) | **2** | Interactive mini-games built with simple data structures |
| [`lists/`](lists/) | **10** | Sequence operations, slicing, and search algorithms |
| [`loops/`](loops/) | **11** | Iterative algorithms, accumulators, and repetition patterns |
| [`randomness/`](randomness/) | **3** | Pseudo-random values, dice simulations, and shuffling |
| [`recursion/`](recursion/) | **3** | Divide-and-conquer base cases and recursive call traces |
| [`strings/`](strings/) | **9** | Character traversal, pattern checking, and text transformations |
| [`tuples/`](tuples/) | **5** | Immutable records, unpacking, and sequence comparisons |

## Getting Started

### Prerequisites

- **[Python 3.9+](https://www.python.org/downloads/)** (or higher)
- **[Git](https://git-scm.com/downloads)**

### Local Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/aldojacopovirno/pa4ds.git
   cd pa4ds
   ```

2. **(Recommended) Create and activate a virtual environment:**
   - On **macOS / Linux**:
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```
   - On **Windows**:
     ```powershell
     python -m venv .venv
     .venv\Scripts\activate
     ```

3. **Install dependencies:**
   Most exercises rely exclusively on Python's standard library. Check `requirements.txt` for optional dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   > [!NOTE]
   > `functions/01_try_pcinput.py` requires the external `pcinput` helper module. It is not included in this repository and must be provided separately if you run that specific exercise.

### Running an Exercise

Run any exercise script directly using Python from the repository root:

```bash
python3 arithmetic/01_seconds_in_a_week.py
```

> [!TIP]
> Interactive exercises prompt for input in the terminal: make sure to run them in an active terminal session.

## Conventions

See [CONVENTIONS.md](CONVENTIONS.md) for shared mathematical notation, naming conventions (`snake_case`, `UPPER_SNAKE_CASE`), and coding standards followed across all solutions.

## Contributing

All code solutions proposed are intended as educational examples. Given that there are many ways to approach each problem, the solutions provided are not the only correct ones. There are plenty of ways to solve the exercises, and the solutions here are not necessarily the most efficient or elegant. Nevertheless, the goal is to provide a clear and understandable approach to each problem. If you find a better solution, feel free to fork the repository and submit a pull request!

## License

This repository is a personal project and is in no way affiliated with any educational institution or organization. Any resemblance to external materials is purely coincidental.

Original code and documentation in this collection are licensed under the **MIT License**; see [LICENSE](LICENSE). External modules and materials not owned by the author are excluded and remain under their respective terms.
