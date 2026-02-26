# Gen AI (Python Basics)

Small collection of Python practice scripts (data types, operators, functions, files, packages) with a minimal `unittest` setup.

## Structure

- **Day_3_python_fundamentals/** – Python basics workouts and their tests  
  - Lesson scripts: `1_data_types.py`, `2_operators.py`, `3_control_statements.py`, `4_functions.py`, `5_error_handling.py`, `6_file_handling.py`, `7_file_handling_directory.py`, `8_init_package.py`, `simple-calculator.py`  
  - Helper: `example.txt` (used by file-handling scripts)  
  - Tests: `tests/` (e.g. `test_data_types.py`, `test_operators.py`, `test_functions_module.py`, `test_package_module.py`)
- **test_init8/** – Package example used by `8_init_package.py` and package tests

## Day_3: Run a script

From the project root:

```bash
python3 Day_3_python_fundamentals/1_data_types.py
```

Or from inside the folder:

```bash
cd Day_3_python_fundamentals
python3 1_data_types.py
```

## Day_3: Run unit tests

From the project root:

```bash
python3 -m unittest discover -s Day_3_python_fundamentals/tests -p "test_*.py"
```

Or run a single test module:

```bash
python3 -m unittest Day_3_python_fundamentals.tests.test_data_types -v
```

## Day_3: Coverage

Install coverage (optional):

```bash
uv pip install coverage
# or: pip install coverage
```

Run tests with coverage and report in the terminal:

```bash
coverage run -m unittest discover -s Day_3_python_fundamentals/tests -p "test_*.py"
coverage report
```

Generate an HTML report and open it:

```bash
coverage run -m unittest discover -s Day_3_python_fundamentals/tests -p "test_*.py"
coverage html
open htmlcov/index.html
```

To limit the report to Day_3 source files only:

```bash
coverage run -m unittest discover -s Day_3_python_fundamentals/tests -p "test_*.py"
coverage report --include="Day_3_python_fundamentals/*.py"
coverage html --include="Day_3_python_fundamentals/*.py"
```
