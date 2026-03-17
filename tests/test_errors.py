import unittest
from digin import NestedDict, NestedList


class TestErrors(unittest.TestCase):
    def setUp(self):
        self.nd = NestedDict({"a": {"b": 1}, "list": [10, 20]}, ".")

    def test_unsupported_key_type_raises_syntax_error(self):
        self.assertRaises(SyntaxError, self.nd.get, 3.14)

    def test_missing_dict_key_raises_key_error(self):
        self.assertRaises(KeyError, self.nd.get, "a.missing")

    def test_index_out_of_range_raises_index_error(self):
        self.assertRaises(IndexError, self.nd.get, "list.5")

    def test_nested_missing_key_raises_key_error(self):
        self.assertRaises(KeyError, self.nd.get, "a.missing.deeper")

    def test_getitem_missing_key_raises_key_error(self):
        self.assertRaises(KeyError, self.nd.__getitem__, "a.missing")

    def test_getitem_index_out_of_range_raises_index_error(self):
        self.assertRaises(IndexError, self.nd.__getitem__, "list.99")

    def test_nested_list_index_out_of_range_raises_index_error(self):
        nl = NestedList([1, 2, 3], ".")
        self.assertRaises(IndexError, nl.get, "10")


if __name__ == '__main__':
    unittest.main()
