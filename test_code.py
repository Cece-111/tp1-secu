import unittest
import os
from datetime import datetime
from code import update_date_file

class TestUpdateDateFile(unittest.TestCase):

    def setUp(self):
        self.test_file_path = 'test_dateRefresh.txt'

    def tearDown(self):
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)

    def test_update_date_file(self):
        current_date = update_date_file(self.test_file_path)
        with open(self.test_file_path, 'r') as file:
            file_content = file.read().strip()
        self.assertEqual(file_content, current_date)

if __name__ == '__main__':
    unittest.main()
