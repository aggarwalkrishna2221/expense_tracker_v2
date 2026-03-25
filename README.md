# Multi-Day Expense Tracker v1 (Original)
A command-line expense tracker built with Python as part of my FinTech learning journey.
## About
This was my **first attempt** at building a project after learning Python basics (strings, lists, loops, functions, try/except) through the *Python for Everybody* specialization on Coursera.
## Features
- Add daily expenses interactively
- Calculates total, average, highest, and lowest expenses
- Counts days above and below average spending
- Input validation with try/except
- Negative expense detection
## What I Learned
- Using `while True` loops for continuous input
- Storing data in lists
- Basic error handling with try/except
- Writing functions to organize code
## Known Issues (Fixed in v2)
- Program crashes on invalid input (variable used before assignment)
- Negative expenses still get added to the list
- Above/below average calculated mid-loop (incorrect results)
- Highest/lowest recalculated inefficiently every iteration
- No handling for zero expenses edge case
## How to Run
```bash
python expense_tracker_v1.py
