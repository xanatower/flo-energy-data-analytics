# Project: Flo Energy Data Analyst Take-Home

## Purpose

This repository contains my solution to the Flo Energy
Data Analyst - Pricing & Revenue Assurance take-home assessment.

The goal is to produce a clear, reproducible and well-reasoned analysis
with an approach that could be extended or scaled if required.

Prefer simple and transparent implementations over unnecessary abstraction.

The primary deliverable is an `.ipynb` notebook, edited and executed in VS Code, used for:

- data exploration;
- data quality investigation;
- cleansing and transformation;
- analytical modelling;
- visualisation;
- documenting assumptions, findings and reasoning.

The notebook should be understandable by both technical and analytical reviewers.


## Environment

- Python managed with `uv`
- VS Code used to edit and execute the `.ipynb` assessment notebook
- pandas / NumPy for data manipulation
- matplotlib for visualisation
- pytest for unit tests where appropriate
- ruff for Python formatting and linting

Useful commands:

```bash
uv sync
uv run pytest
uv run ruff check .
```

## Data handling rules
- Treat files under data/raw/ as immutable source data.
- Never silently modify raw files.
- Validate raw data before cleansing.
- Make cleansing decisions explicit and explain why they are justified.
- Do not impute or interpolate missing market data unless explicitly justified.
- Do not treat unusual electricity prices as invalid solely because they are
  statistical outliers.
- Preserve known data gaps where there is insufficient evidence to repair them.


## Coding conventions
- Use lower-case snake_case names.
- Prefer small functions with one clear responsibility.
- Add type hints where useful.
- Keep business logic separate from plotting where practical.
- Avoid unnecessary classes or frameworks.
- Avoid hidden mutation of input DataFrames; copy before transformation.
- Use descriptive variable names rather than abbreviations.
- Write comments for reasoning, not obvious Python syntax.
- Prefer vectorised pandas / NumPy operations where they remain readable.
- Avoid premature optimisation.
- Keep functions simple enough that their business logic can be explained clearly in an interview.


## Notebook conventions
- The notebook must run from top to bottom in a fresh kernel.
- Avoid relying on hidden notebook state or variables created by cells run out of order.
- Organise the notebook into clear sections using Markdown headings.
- Explain the purpose and reasoning before major analytical steps.
- Keep code cells focused and reasonably small.
- Prefer reusable functions for repeated or business-critical logic.
- Do not duplicate large blocks of code across cells.
- Keep exploratory code only if it contributes to the final analytical narrative.
- Remove temporary debugging output before submission.
- Show important validation results and analytical findings in the notebook.
- Do not overwhelm the notebook with unnecessary intermediate output.
- Use plots and tables only where they help explain an analytical point.


## Claude Code behaviour
Before making a non-trivial change:
- inspect the relevant notebook or code first;
- briefly explain the proposed approach;
- identify assumptions or business rules involved;
- reuse existing functions and conventions where appropriate.
When editing the notebook:
- preserve the existing analytical narrative;
- do not restructure unrelated sections;
- do not remove Markdown explanations unless asked;
- avoid generating excessive boilerplate;
- prefer incremental edits over rewriting the entire notebook;
- keep code and explanations concise enough for a take-home assessment.
Do not:
- invent market assumptions;
- silently remove anomalous records;
- modify raw data;
- add dependencies without a clear reason;
- refactor unrelated code;
- over-engineer the solution;
- optimise for cleverness over readability;
- hide analytical decisions inside large helper functions.
If the business meaning is uncertain, highlight the uncertainty rather than making an unsupported assumption.