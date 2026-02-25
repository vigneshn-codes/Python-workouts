import importlib.util
from pathlib import Path
import unittest


BASE_DIR = Path(__file__).resolve().parent.parent


def load_module(module_name: str, filename: str):
    spec = importlib.util.spec_from_file_location(module_name, BASE_DIR / filename)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class FunctionsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mod = load_module("functions4", "4_functions.py")

    def test_add_with_two_arguments(self):
        # The last defined add(a, b=2) should be active
        self.assertEqual(self.mod.add(1, 2), 3)

    def test_add_with_default_second_argument(self):
        self.assertEqual(self.mod.add(1), 3)


if __name__ == "__main__":
    unittest.main()

