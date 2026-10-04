# Flo Energy Take Home Assessment

My solution to the Data Analyst, Pricing & Revenue Assurance take-home assessment. It cleans the merit order and demand files for January 2023, plots the merit order, and estimates the clearing price from it.

## Notebooks

| Notebook | What it covers | Google Colab |
| --- | --- | --- |
| [assessment.ipynb](analysis/assessment.ipynb) | Tasks 1 to 3, and the unit test bonus | [Open in Colab](https://drive.google.com/file/d/1kyd-5o0YGFwylAnNkQDfwt_F3Z_-eI_Y/view?usp=sharing) |
| [bonus_sql_duckdb.ipynb](analysis/bonus_sql_duckdb.ipynb) | Bonus tasks: the Task 1 cleaning repeated in SQL with DuckDB | [Open in Colab](https://drive.google.com/file/d/1CCVc8IkLYfU0xOHDv8mcFptuzmkpxUWF/view?usp=sharing) |

## Run on Google Colab

Nothing to install. Open a notebook with the link above and choose `Runtime > Run all`.

The setup cell at the top clones this repo and installs the packages, so the project structure is the same as the local one.

## Run locally

Requires [uv](https://docs.astral.sh/uv/).

```bash
git clone https://github.com/xanatower/flo-energy-data-analytics.git
cd flo-energy-data-analytics
uv sync
```

Then open the notebooks in `analysis/` with VS Code, select the `.venv` kernel and run all the cells.

To run the unit tests:

```bash
uv run pytest
```

## Project structure

```
analysis/   the 2 notebooks
data/raw/   the original CSV files, never modified
src/        the clearing price function
tests/      the unit tests for the clearing price function
```
