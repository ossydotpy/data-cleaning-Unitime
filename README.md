## Data Cleaning script for examination schedule explorer.
This script can be used to clean the raw data output of unitime into a standard that the explorer accepts.

# Setting Up

---
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

## Install the package using
```bash
pip3 install \
https://github.com/ossydotpy/data-cleaning-Unitime/\
unitime_cleaner-0.1.0-py3-none-any.whl
```
# Usage

---
The cleaner can work on two files formats; `csv` and `xlsx`.

Don't make any changes to your Unitime results.

Run:
```bash
clean -f path-to-your-raw-file --type xlsx-or-csv
```
The  resulting cleaned file will be in the same directory where you ran the command.

| Flag   | Description                         |
|--------|-------------------------------------|
| -f     | name of raw file                    |
| --type | raw file's extension (csv or xlsx ) |


> [!NOTE] The script accepts raw-data in `csv` and `xlsx` formats only.

or
## Using the script without installation
1. Clone the repo
```bash
git clone https://github.com/ossydotpy/data-cleaning-Unitime.git
```
2. In the root directory of the repo create a virtual environment and activate it.
- on linux:
```bash
python -m venv env-name
source env-name/bin/activate
```
- on windows:
```commandline
python -m venv env-name
env-name\Scripts\activate
```
3. Add your raw file to the root directory.
4. Run

```commandline
python3 clean/main.py -f raw-file-name --type raw-file-type
```

Happy Usage.\
Feel free to open an Issue or PR if you encounter a problem or have an improvement code.