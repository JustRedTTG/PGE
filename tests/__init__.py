import sys
import unittest
import os
import pygameextra as pe
import atexit
import shutil

script_folder = os.path.dirname(__file__)
temp_directory = os.path.join(script_folder, "_test_temp")
errors_directory = os.path.join(script_folder, "_test_errors")

pe.init()
if os.path.exists(errors_directory):
    shutil.rmtree(errors_directory)
os.makedirs(temp_directory, exist_ok=True)
os.makedirs(errors_directory, exist_ok=True)
atexit.register(lambda: shutil.rmtree(temp_directory))

if __name__ == '__main__':
    suite = unittest.TestLoader().discover(start_dir=script_folder, pattern='test_*.py')

    unittest.TextTestRunner().run(suite)
