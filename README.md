# Data Cleaning script for examination schedule explorer.
This script can be used to clean the raw data output of unitime into a standard that the explorer accepts.

# Usage
1. Create and activate a  Virtual Environment.
- on linux:
```bash
python -m venv env-name
source env-name/bin/activate
```
- on windows:
```
python -m venv <env-name>
<env-name>\Scripts\activate
```

2. Install project dependencies.
```
pip install -r requirements.txt
```
3. Include your raw data from unitime in the same directory as the script.
example [raw-data.xlsx](/raw-data.xlsx) or `.csv.`
4. Run 
```bash
python clean.py raw-data.xlsx
```
The cleaned File will be saved as cleaned-<original-file-name> in the same directory as the script.

> [!NOTE] The script accepts raw-data in `csv` and `xlsx` formats only.

Currently working on integrating this process directly into the explorer.