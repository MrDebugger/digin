import unittest
from digin import NestedDict, NestedList


class TestDefault(unittest.TestCase):
    def setUp(self):
        self.nd = NestedDict({"a": {"b": 5}}, ".")
        self.nl = NestedList([{"x": 1}], ".")

    def test_get_missing_key_with_default(self):
        self.assertEqual(self.nd.get("a.missing", default="fallback"), "fallback")

    def test_get_missing_key_no_default_raises(self):
        self.assertRaises(KeyError, self.nd.get, "a.missing")

    def test_call_missing_key_with_default(self):
        self.assertEqual(self.nd("a.missing", default=0), 0)

    def test_call_missing_key_no_default_raises(self):
        self.assertRaises(KeyError, self.nd, "a.missing")

    def test_get_default_falsy_zero(self):
        self.assertEqual(self.nd.get("a.missing", default=0), 0)

    def test_get_default_falsy_none(self):
        self.assertIsNone(self.nd.get("a.missing", default=None))

    def test_get_default_falsy_false(self):
        self.assertEqual(self.nd.get("a.missing", default=False), False)

    def test_get_index_out_of_range_with_default(self):
        self.assertEqual(self.nl.get("5.x", default="gone"), "gone")

    def test_get_index_out_of_range_no_default_raises(self):
        self.assertRaises(IndexError, self.nl.get, "5.x")


if __name__ == '__main__':
    unittest.main()
