from digin import NestedDict, NestedList, NestedTuple
import unittest

class TestNestedDict(unittest.TestCase):
    def setUp(self):
        self.data = {
            "foo": 
                {"bar": ["foo","bar","baz"]},
            "1": {"2":[3,4]},
            "2": [{"e":5}],
            3: "6"
        }
        self.nested_dict = NestedDict(self.data, '.')

    def test_get_item(self):
        self.assertEqual(self.nested_dict["foo.bar.1"], 'bar')
        self.assertEqual(self.nested_dict["1.2.1"], 4)
        self.assertEqual(self.nested_dict[["1","2","1"]], 4)
        self.assertEqual(self.nested_dict[[3]], "6")
        self.assertRaises(IndexError, self.nested_dict.__getitem__, '1.2.3')
        self.assertRaises(KeyError, self.nested_dict.__getitem__, '1.3.3')

    def test_set_item(self):
        self.nested_dict["2.0.e"] = 12
        self.assertEqual(self.nested_dict["2.0.e"], 12)
        self.assertEqual(self.nested_dict.get('2.0.e'), 12)
        self.nested_dict[[3]] = "16"
        self.assertEqual(self.nested_dict.get(3), "16")

    def test_set_value(self):
        self.nested_dict.set('2.0.e', 10)
        self.assertEqual(self.nested_dict.get('2.0.e'), 10)

    def test_get_attribute(self):
        self.assertEqual(self.nested_dict.foo.bar[1], 'bar')
        self.assertEqual(self.nested_dict['2.0'].e, 5)
        self.assertRaises(TypeError, self.nested_dict['2'], '0')
        self.assertRaises(IndexError, getattr, self.nested_dict, '1.2.3')
        self.assertRaises(AttributeError, getattr, self.nested_dict, '1.3.3')

    def test_call_attribute(self):
        self.assertEqual(self.nested_dict('foo.bar.1'), 'bar')
        self.assertEqual(self.nested_dict('2.0.e'), 5)
        self.nested_dict(3, "16")
        self.assertEqual(self.nested_dict('3'), "16")
        self.nested_dict('2.0.e',10)
        self.assertEqual(self.nested_dict('2.0.e'), 10)
        self.assertEqual(self.nested_dict('2.0.c', default=10), 10)

    def test_get(self):
        self.assertEqual(self.nested_dict.get('foo.bar.1'), 'bar')
        self.assertEqual(self.nested_dict.get('1.2.1'), 4)
        self.assertEqual(self.nested_dict.get('2.0.e'), 5)
        self.assertEqual(self.nested_dict.get('3'), "6")
        self.assertRaises(KeyError,self.nested_dict.get, '2.0.c')
        self.assertRaises(IndexError,self.nested_dict.get, '2.5')
        self.assertEqual(self.nested_dict.get('2.5', default=0), 0)
    
    def test_set_attr(self):
        self.nested_dict.foo.bar = 'Hello'
        self.assertEqual(self.nested_dict.foo.bar, 'Hello')
        self.assertEqual(self.nested_dict.get('foo.bar'), 'Hello')


class TestNestedList(unittest.TestCase):
    def setUp(self):
        self.data = [{'a': 'b'}, {'c': 'd'}]
        self.nested_list = NestedList(self.data, '.')

    def test_get_item(self):
        self.assertEqual(self.nested_list[0], self.data[0])
        self.assertEqual(self.nested_list[1], self.data[1])

    def test_set_item(self):
        self.nested_list[0] = {'e': 'f'}
        self.assertEqual(self.nested_list[0], {'e': 'f'})
        self.assertEqual(self.nested_list, [{'e': 'f'}, {'c': 'd'}])

    def test_call(self):
        self.assertEqual(self.nested_list('0.a'), self.data[0]['a'])
        self.nested_list('0.a', 'b')
        self.assertEqual(self.nested_list('0.a'), 'b')

    def test_get(self):
        self.assertEqual(self.nested_list.get('0.a'), self.data[0]['a'])
        self.assertEqual(self.nested_list.get('1.c'), self.data[1]['c'])
        self.assertEqual(self.nested_list.get('2.a', 'default'), 'default')
        self.assertRaises(IndexError, self.nested_list.get, '2.a')

class TestNestedTuple(unittest.TestCase):
    def setUp(self):
        self.data = ({"a": (1, 2, 3)}, {"b": (4, 5, 6)})
        self.nested_tuple = NestedTuple(self.data, ".")

    def test_get(self):
        # top-level index access
        inner = self.nested_tuple.get("0")
        self.assertIsInstance(inner, NestedDict)
        self.assertEqual(self.nested_tuple.get("0.a.1"), 2)
        self.assertEqual(self.nested_tuple.get("1.b.0"), 4)

    def test_getitem(self):
        # plain int index returns raw value (no wrapping), consistent with NestedList/NestedDict
        item = self.nested_tuple[0]
        self.assertEqual(item, {"a": (1, 2, 3)})
        # list-key syntax routes through get() and wraps result
        item_wrapped = self.nested_tuple[[0]]
        self.assertIsInstance(item_wrapped, NestedDict)

    def test_call_read(self):
        self.assertEqual(self.nested_tuple("0.a.2"), 3)
        self.assertEqual(self.nested_tuple("1.b.2"), 6)

    def test_nested_tuple_wraps_inner_tuple(self):
        inner_tuple = self.nested_tuple.get("0.a")
        self.assertIsInstance(inner_tuple, NestedTuple)


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


class TestDefaultDelimiter(unittest.TestCase):
    def setUp(self):
        self.data = {"x": {"y": {"z": 42}}, "items": [10, 20, 30]}
        # Use the default "->" delimiter
        self.nd = NestedDict(self.data)

    def test_get_with_default_delimiter(self):
        self.assertEqual(self.nd.get("x->y->z"), 42)

    def test_getitem_with_default_delimiter(self):
        self.assertEqual(self.nd["x->y->z"], 42)

    def test_call_get_with_default_delimiter(self):
        self.assertEqual(self.nd("x->y->z"), 42)

    def test_call_set_with_default_delimiter(self):
        self.nd("x->y->z", 99)
        self.assertEqual(self.nd("x->y->z"), 99)

    def test_list_access_with_default_delimiter(self):
        self.assertEqual(self.nd("items->1"), 20)

    def test_repr_contains_default_delimiter(self):
        r = repr(self.nd)
        self.assertIn("->", r)


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


class TestErrors(unittest.TestCase):
    def setUp(self):
        self.nd = NestedDict({"a": {"b": 1}, "list": [10, 20]}, ".")

    def test_unsupported_key_type_raises_syntax_error(self):
        # Passing a float key (unsupported type) should raise SyntaxError
        self.assertRaises(SyntaxError, self.nd.get, 3.14)

    def test_missing_dict_key_raises_key_error(self):
        self.assertRaises(KeyError, self.nd.get, "a.missing")

    def test_index_out_of_range_raises_index_error(self):
        self.assertRaises(IndexError, self.nd.get, "list.5")

    def test_nested_missing_key_raises_key_error(self):
        # "a" exists, but "a.missing" does not — should raise KeyError
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