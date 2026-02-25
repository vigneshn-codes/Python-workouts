import unittest

from test_init8.package import print_hello


class PackageTests(unittest.TestCase):
    def test_print_hello_returns_expected_string(self):
        self.assertEqual(print_hello(), "Hello, World!")


if __name__ == "__main__":
    unittest.main()

