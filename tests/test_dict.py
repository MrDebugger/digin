import unittest
from digin import NestedDict


class TestNestedDict(unittest.TestCase):
    def setUp(self):
        self.data = {
            "foo":
                {"bar": ["foo", "bar", "baz"]},
            "1": {"2": [3, 4]},
            "2": [{"e": 5}],
            3: "6"
        }
        self.nested_dict = NestedDict(self.data, '.')

    def test_get_item(self):
        self.assertEqual(self.nested_dict["foo.bar.1"], 'bar')
        self.assertEqual(self.nested_dict["1.2.1"], 4)
        self.assertEqual(self.nested_dict[["1", "2", "1"]], 4)
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
        self.nested_dict('2.0.e', 10)
        self.assertEqual(self.nested_dict('2.0.e'), 10)
        self.assertEqual(self.nested_dict('2.0.c', default=10), 10)

    def test_get(self):
        self.assertEqual(self.nested_dict.get('foo.bar.1'), 'bar')
        self.assertEqual(self.nested_dict.get('1.2.1'), 4)
        self.assertEqual(self.nested_dict.get('2.0.e'), 5)
        self.assertEqual(self.nested_dict.get('3'), "6")
        self.assertRaises(KeyError, self.nested_dict.get, '2.0.c')
        self.assertRaises(IndexError, self.nested_dict.get, '2.5')
        self.assertEqual(self.nested_dict.get('2.5', default=0), 0)

    def test_set_attr(self):
        self.nested_dict.foo.bar = 'Hello'
        self.assertEqual(self.nested_dict.foo.bar, 'Hello')
        self.assertEqual(self.nested_dict.get('foo.bar'), 'Hello')


if __name__ == '__main__':
    unittest.main()
