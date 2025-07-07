# Troubleshooting Guide

This guide lists common problems you may encounter when setting up or running the data pipeline.

## Windows: "execution of scripts is disabled"
If PowerShell blocks activation of the virtual environment, run:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Then re-run `Activate.ps1`.

## Missing Python or `pip`
Ensure Python 3 is installed and available in your `PATH`.
On Debian/Ubuntu:
```bash
sudo apt-get install python3 python3-pip
```
On macOS with Homebrew:
```bash
brew install python3
```

## Database Permission Errors
If `clean_data_main.py` fails to write to `finmark_database.db`, verify you have write permission in the project directory or choose another output path with the `--output` flag.

## Dataset Not Found
Place your raw CSV files in `clean_code_automation/datasets`. The cleaner expects this directory structure. Use absolute paths if running the script from a different location.

## Still Stuck?
Consult [`docs/PROJECT_NOTES.md`](PROJECT_NOTES.md) for the full setup workflow and additional context.
