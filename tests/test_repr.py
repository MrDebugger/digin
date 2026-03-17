import unittest
from digin import NestedDict, NestedList, NestedTuple


class TestRepr(unittest.TestCase):
    def test_nested_dict_repr(self):
        nd = NestedDict({"a": 1}, ".")
        r = repr(nd)
        self.assertIn("NestedDict", r)
        self.assertIn(".", r)

    def test_nested_list_repr(self):
        nl = NestedList([1, 2, 3], ".")
        r = repr(nl)
        self.assertIn("NestedList", r)

    def test_nested_tuple_repr(self):
        nt = NestedTuple((1, 2, 3), "->")
        r = repr(nt)
        self.assertIn("NestedTuple", r)

    def test_repr_shows_delimiter(self):
        nd = NestedDict({}, "::")
        r = repr(nd)
        self.assertIn("::", r)

    def test_repr_shows_data(self):
        nd = NestedDict({"key": "val"}, ".")
        r = repr(nd)
        self.assertIn("key", r)
        self.assertIn("val", r)


if __name__ == '__main__':
    unittest.main()
