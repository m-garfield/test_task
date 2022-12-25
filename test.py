import unittest
from main import  add_new_doc, add_new_shelf, get_doc_shelf, delete_doc

class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_get_doc_shelf(self):
        self.assertEqual(get_doc_shelf('2207 876234'), '1')

    def test_add_new_doc(self):
        self.assertEqual(add_new_doc('test_number_doc', 'test_doc_type', 'test_name', '1'), '1')

    def test_add_new_shelf(self):
        self.assertEqual(add_new_shelf('4'), ('4', True))

    def test_delete_doc(self):
        self.assertEqual(delete_doc("11-2"), ('11-2', True))




