# Notation and programming conventions

This page defines the notation used throughout the exercise collection and the programming conventions followed in the solutions. Note that these are not the only ways to write code, but they are the ways used in this collection.

## Mathematical notation

- `n` denotes the number of items in a sequence; valid positions are `0` through `n - 1` in Python.
- `i` and `j` denote loop indices. Python indexes start at zero, while a displayed position may be numbered from one for the user.
- `A` and `B` denote input values in division exercises; `A = qB + r` describes quotient `q` and remainder `r` when `B > 0`.
- `a`, `b`, and `c` are coefficients in `a*x**2 + b*x + c = 0`; a quadratic equation requires `a != 0`.
- Unless an exercise says otherwise, a year has 365 days, a month has 30 days, and a week has 7 days. These are simplifying exercise conventions, not calendar rules.
- “Mean” means arithmetic mean, thus the sum of the selected values divided by their count. It is undefined when that count is zero.
- A “distinct” character or vowel is counted once, even if it occurs multiple times.

## Names and formatting

- Use `snake_case` for variables and functions, e.g. `days_per_week` and `calculate_total_days`.
- Use `UPPER_SNAKE_CASE` for fixed constants, e.g. `SECONDS_PER_MINUTE`.
- Indent with four spaces and leave blank lines between imports, functions, input, calculation, and output.
- Keep each exercise in one runnable `.py` file. Put the assignment in comments before the solution.
- Add type hints when they clarify the function contract. A type hint documents an expectation; it does not check the value at runtime.
- Use *e.g.* to introduce examples and *i.e.* to restate or clarify a point.

## Comments and algorithms

- Inline comments explain why a step matters, how a loop changes state, or what a key condition separates.
- Keep comments brief and connected to the code they explain; do not narrate obvious assignments.
- Prefer the simplest algorithm that demonstrates the concept. Describe efficiency in plain language when it helps; use Big O notation only when it adds useful information.
- Every loop must make progress toward a clear stopping condition. In recursive functions, base cases stop the calls and each recursive step must reduce the remaining problem.

## Console interaction

- Convert `input()` to a number only when the exercise requires numeric input, e.g. `int(input("Number: "))`.
- Print labels and units so output can be interpreted without reading the code.
- Keep input/output separate from calculations when a small function makes the calculation reusable.
