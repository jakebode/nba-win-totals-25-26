# nba-win-totals-25-26

A personal research project analyzing NBA team win totals and trends for the 2025–26 season using the `nba_api` Python package.

-----

## Project Structure

nba-win-totals-25-26/
│
├── .venv/ # virtual environment (ignored by git)
├── tools/ # reusable code modules
│ └── stats/
│ ├── endpoint_analysis.py
│ └── static_players_update/
│ ├── update.py
│ └── template.py
├── scripts/ # scripts to run analyses
│ ├── run_analysis.py
│ └── smoke_test.py
├── data/ # raw and processed data (gitignored if large)
│ ├── raw/
│ └── processed/
├── output/ # generated plots, CSVs, logs
├── notebooks/ # exploratory Jupyter notebooks
├── tests/ # unit tests
├── requirements.txt # project dependencies
└── README.md

-----

## Setup

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd nba-win-totals-25-26
```

2. **Create a virtual environment**

python3 -m venv .venv
source .venv/bin/activate    # macOS / Linux
# OR
.\.venv\Scripts\activate     # Windows

3. **Install dependencies**

pip install -r requirements.txt

-----

## Usage


-----

## Dependencies


-----

## Notes


-----
