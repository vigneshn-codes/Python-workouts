# Gen AI (Python Basics)

Small collection of Python practice scripts (data types, operators, functions, files, packages) with a minimal `unittest` setup.

## Structure

- Lesson scripts: `1_data_types.py`, `2_operators.py`, `3_control_statements.py`, `4_functions.py`, `5_error_handling.py`, `6_file_handling.py`, `7_file_handling_directory.py`, `8_init_package.py`
- Package example: `test_init8/`
- Tests: `tests/` (files named `test_*.py`)

## Run a script

```bash
python3 1_data_types.py
```

## Run unit tests

From this folder:

```bash
python3 -m unittest discover -s tests -p "test_*.py"
```

## Coverage (optional)

```bash
uv pip install coverage
coverage run -m unittest discover -s tests -p "test_*.py"
coverage report
coverage html
open htmlcov/index.html
```

