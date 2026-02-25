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


class OperatorsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mod = load_module("operators2", "2_operators.py")

    def test_final_values_of_a_and_b(self):
        # After all operations, the identity section sets both a and b to 10
        self.assertEqual(self.mod.a, 10)
        self.assertEqual(self.mod.b, 10)


if __name__ == "__main__":
    unittest.main()

