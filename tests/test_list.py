import unittest
from digin import NestedList


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


if __name__ == '__main__':
    unittest.main()
