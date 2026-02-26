## Day 3 – Python Fundamentals

This folder contains small scripts that cover core Python basics plus unit tests.

### Contents

- **Core scripts**
  - `1_data_types.py`
  - `2_operators.py`
  - `3_control_statements.py`
  - `4_functions.py`
  - `5_error_handling.py`
  - `6_file_handling.py`
  - `7_file_handling_directory.py`
  - `8_init_package.py`
  - `simple-calculator.py`
- **Support files**
  - `example.txt` – used by the file-handling exercises.
  - `test_init8/` – package example used by `8_init_package.py` and related tests.
- **Tests**
  - `tests/` – unittest modules such as:
    - `test_data_types.py`
    - `test_operators.py`
    - `test_functions_module.py`
    - `test_package_module.py`

### Run a script

From the project root:

```bash
python3 Day_3_python_fundamentals/1_data_types.py
```

Or from inside this folder:

```bash
cd Day_3_python_fundamentals
python3 1_data_types.py
```

### Run unit tests

From the project root:

```bash
python3 -m unittest discover -s Day_3_python_fundamentals/tests -p "test_*.py"
```

Run a single test module:

```bash
python3 -m unittest Day_3_python_fundamentals.tests.test_data_types -v
```

### Coverage (optional)

Install coverage:

```bash
uv pip install coverage
# or: pip install coverage
```

Run tests with coverage and show a report:

```bash
coverage run -m unittest discover -s Day_3_python_fundamentals/tests -p "test_*.py"
coverage report
```

Generate an HTML coverage report:

```bash
coverage run -m unittest discover -s Day_3_python_fundamentals/tests -p "test_*.py"
coverage html
open htmlcov/index.html
```

Limit the report to Day 3 source files only:

```bash
coverage run -m unittest discover -s Day_3_python_fundamentals/tests -p "test_*.py"
coverage report --include="Day_3_python_fundamentals/*.py"
coverage html --include="Day_3_python_fundamentals/*.py"
```

