import unittest
import os
import sys
import subprocess
import re

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from hw6searchsrc import readFile, countLine, getFileName, getFilePath, countInclude, countIncludeLocal, countMemberFuncs, countOneLineFunc

class TestOutput(unittest.TestCase):
    def setUp(self):
        self.output = subprocess.run(["python3", "../hw6searchsrc.py", full_path, "--include", "--includelocal", "--memberfuncs", "--onelinefunc"], capture_output=True, text=True)
    
    def test_countLine_pkt(self):
        """Test for countLine"""
        numlines = countLine(self.file)
        self.assertEqual(numlines, 42)

# output = subprocess.run(["python3", "searchsrc.py", full_path, "--include", "--includelocal", "--memberfuncs", "--onelinefunc"], capture_output=True, text=True)