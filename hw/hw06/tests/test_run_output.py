# Vince Andriacco
# vandriac@nd.edu

import unittest
import os
import subprocess
import re

class TestOutput(unittest.TestCase):
    def setUp(self):
        self.path = '/escnfs/home/vandriac/cse-20289-repos/student-cse20289-fa24-vandriac/hw/hw06/tests/data'
        self.files = ['fmnc_manager.cc', 'ParamDictionary.cc', 'PktQueue.cc', 'RIPPS_PktPair.cc', 'Thread_IO.cc']
    
    def test_minargs(self):
        """Tests hw6searchsrc with minimum number of arguments"""
        for file in self.files:
            full_path = os.path.join(self.path, file)
            output = subprocess.run(
                ["python3", "../hw6searchsrc.py", full_path], 
                capture_output=True, 
                text=True
                ).stdout
            self.assertRegex(output, r'path:\s+.+')
            self.assertRegex(output, r'file:\s+'+ re.escape(file))
            self.assertRegex(output, r'lines:\s+\d+')

    def test_maxargs_inorder(self):
        """Tests hw6searchsrc with maximum number of arguments in order"""
        for file in self.files:
            full_path = os.path.join(self.path, file)
            output = subprocess.run(
                ["python3", "../hw6searchsrc.py", full_path, "--include", "--includelocal", "--memberfuncs", "--onelinefunc"], 
                capture_output=True, 
                text=True
                ).stdout
            self.assertRegex(output, r'path:\s+.+')
            self.assertRegex(output, r'file:\s+' + re.escape(file))
            self.assertRegex(output, r'lines:\s+\d+')
            self.assertRegex(output, r'include:\s+\d+')
            self.assertRegex(output, r'includelocal:\s+\d+')
            self.assertRegex(output, r'memberfuncs:\s+\d+')
            self.assertRegex(output, r'onelinefuncs:\s+\d+')

    def test_maxargs_mixedorder(self):
        """Tests hw6searchsrc with maximum number of arguments in random order"""
        for file in self.files:
            full_path = os.path.join(self.path, file)
            output = subprocess.run(
                ["python3", "../hw6searchsrc.py", "--include", "--memberfuncs", full_path, "--onelinefunc", "--includelocal"], 
                capture_output=True, 
                text=True
                ).stdout
            self.assertRegex(output, r'path:\s+.+')
            self.assertRegex(output, r'file:\s+' + re.escape(file))
            self.assertRegex(output, r'lines:\s+\d+')
            self.assertRegex(output, r'include:\s+\d+')
            self.assertRegex(output, r'includelocal:\s+\d+')
            self.assertRegex(output, r'memberfuncs:\s+\d+')
            self.assertRegex(output, r'onelinefuncs:\s+\d+')

    def test_maxargs_pathlast(self):
        """Tests hw6searchsrc with path at the end"""
        for file in self.files:
            full_path = os.path.join(self.path, file)
            output = subprocess.run(
                ["python3", "../hw6searchsrc.py", "--include", "--memberfuncs", "--onelinefunc", "--includelocal", full_path], 
                capture_output=True, 
                text=True
                ).stdout
            self.assertRegex(output, r'path:\s+.+')
            self.assertRegex(output, r'file:\s+' + re.escape(file))
            self.assertRegex(output, r'lines:\s+\d+')
            self.assertRegex(output, r'include:\s+\d+')
            self.assertRegex(output, r'includelocal:\s+\d+')
            self.assertRegex(output, r'memberfuncs:\s+\d+')
            self.assertRegex(output, r'onelinefuncs:\s+\d+')

    def test_maxargs_someargs(self):
        """Tests hw6searchsrc with a few arguments"""
        for file in self.files:
            full_path = os.path.join(self.path, file)
            output = subprocess.run(
                ["python3", "../hw6searchsrc.py", "--include", "--onelinefunc", full_path], 
                capture_output=True, 
                text=True
                ).stdout
            self.assertRegex(output, r'path:\s+.+')
            self.assertRegex(output, r'file:\s+' + re.escape(file))
            self.assertRegex(output, r'lines:\s+\d+')
            self.assertRegex(output, r'include:\s+\d+')
            self.assertRegex(output, r'onelinefuncs:\s+\d+')

if __name__ == '__main__':
    unittest.main(verbosity=2)