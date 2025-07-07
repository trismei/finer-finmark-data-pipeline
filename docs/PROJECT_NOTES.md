# Project Setup & Progress Log

This document summarizes how to get the data pipeline running, what worked, and the current blockers.

## Setup Instructions
### 1. Clone this repository
Use Git or download the archive directly from GitHub.

### 2. macOS / Linux
1. Install Python:
   ```bash
   # macOS
   brew install python3
   # Debian/Ubuntu
   sudo apt-get install python3 python3-pip
   ```
2. *(Optional)* create a virtual environment and install dependencies:
   ```bash
   python3 -m venv env
   source env/bin/activate
   pip install -r requirements.txt
   ```

### 3. Windows
1. Download and install Python from [python.org](https://www.python.org/) (make sure **Add Python to PATH** is checked).
2. *(Optional)* set up a virtual environment in PowerShell:
   ```powershell
   py -m venv env
   .\\env\\Scripts\\Activate.ps1
   pip install -r requirements.txt
   ```

## Running the Cleaning Script
Raw CSV files should be placed in `clean_code_automation/datasets`. Execute the cleaning process with:
```bash
python clean_code_automation/clean_data_main.py datasets/<your_file.csv>
```
Cleaned data is saved to the SQLite database `finmark_database.db`.

## Wins
- Cleaning functions for event logs, marketing summary, and trend reports ran successfully on the initial dataset.
- Database tables were created without manual intervention.

## Blockers / Issues
- Some Python files have truncated lines (e.g. `sql-data-storage/src/db/connection.py`) which leads to syntax errors.
- Missing `.gitignore` causes the large `env/` directory to be tracked.
- Running `pytest` shows that no tests are present.
- Several image references in `README.md` point to a non-existent `visuals/` directory.

## Next Steps
- Repair the affected Python files and verify all imports.
- Add a `.gitignore` and remove unnecessary files from version control.
- Provide screenshots of the working pipeline once available.
- Implement unit tests for the cleaning modules.
