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


class DataTypesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mod = load_module("data_types1", "1_data_types.py")

    def test_integer(self):
        self.assertEqual(self.mod.a, 10)
        self.assertIs(type(self.mod.a), int)

    def test_float(self):
        self.assertEqual(self.mod.b, 10.5)
        self.assertIs(type(self.mod.b), float)

    def test_string(self):
        self.assertEqual(self.mod.c, "Hello, World!")
        self.assertIs(type(self.mod.c), str)

    def test_boolean(self):
        self.assertIs(self.mod.d, True)
        self.assertIs(type(self.mod.d), bool)

    def test_list(self):
        self.assertEqual(self.mod.e, [1, 2, 3, 4, 5])
        self.assertIs(type(self.mod.e), list)

    def test_tuple(self):
        self.assertEqual(self.mod.f, (1, 2, 3, 4, 5))
        self.assertIs(type(self.mod.f), tuple)

    def test_dict(self):
        self.assertEqual(self.mod.g, {"name": "John", "age": 30})
        self.assertIs(type(self.mod.g), dict)

    def test_set(self):
        self.assertEqual(self.mod.h, {1, 2, 3, 4, 5})
        self.assertIs(type(self.mod.h), set)

    def test_complex(self):
        self.assertEqual(self.mod.i, 10 + 5j)
        self.assertIs(type(self.mod.i), complex)

    def test_none(self):
        self.assertIsNone(self.mod.j)


if __name__ == "__main__":
    unittest.main()

