import unittest
from digin import NestedDict


class TestFalsyValues(unittest.TestCase):
    def setUp(self):
        self.nd = NestedDict({"a": {"b": 1}}, ".")

    def test_set_zero(self):
        self.nd("a.b", 0)
        self.assertEqual(self.nd("a.b"), 0)

    def test_set_empty_string(self):
        self.nd("a.b", "")
        self.assertEqual(self.nd("a.b"), "")

    def test_set_false(self):
        self.nd("a.b", False)
        self.assertEqual(self.nd("a.b"), False)

    def test_set_empty_list(self):
        self.nd("a.b", [])
        self.assertEqual(self.nd.get("a.b", modify=True), [])

    def test_set_empty_dict(self):
        self.nd("a.b", {})
        self.assertEqual(self.nd.get("a.b", modify=True), {})


if __name__ == '__main__':
    unittest.main()
