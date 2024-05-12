import unittest
import os

script_folder = os.path.dirname(__file__)

if __name__ == '__main__':
    suite = unittest.TestLoader().discover(start_dir=script_folder, pattern='test_*.py')

    unittest.TextTestRunner().run(suite)

