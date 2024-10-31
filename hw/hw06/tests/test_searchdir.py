import unittest
import os
import subprocess
import re

class TestRunErrors(unittest.TestCase):
    def setUp(self):
        self.path = '/escnfs/home/vandriac/cse-20289-repos/student-cse20289-fa24-vandriac/hw/hw06/tests/data'
    
    def test_nonrecursive(self):
        full_path = os.path.join(self.path, "nrd-1")
        output = subprocess.run(
            ["python3", "../hw6searchdir.py", full_path, "--quiet"], 
            capture_output=True, 
            text=True
            )

if __name__ == '__main__':
    unittest.main(verbosity=2)