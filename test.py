import unittest
import os

from read_api import ReadingSncfApi


#https://stackoverflow.com/questions/33216488/is-there-any-way-to-check-with-python-unittest-assert-if-an-iterable-is-not-empt

class TestStringMethods(unittest.TestCase):
    
    def test_file_exists(self):
        read_api_class = ReadingSncfApi()
        read_api_class.save_my_json()
        read_api_class.request_JSON()
        self.assertTrue(os.path.isfile("marwa_sncf.json"))
        self.assertEquals(type(read_api_class.raw_data), dict)
    
    def test_def_my_endpoints(self):
        
        test_my_endpoints_element = ReadingSncfApi()
        test_my_endpoints_element.request_JSON()
        test_my_endpoints_element.my_endpoints()
        self.assertIn('links', test_my_endpoints_element.raw_data)
        self.assertTrue(len(test_my_endpoints_element.my_endpoints_list) > 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)