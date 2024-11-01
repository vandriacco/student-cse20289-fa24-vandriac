import unittest
import os
import subprocess
import re

class TestRunErrors(unittest.TestCase):
    def setUp(self):
        self.path = '/escnfs/home/vandriac/cse-20289-repos/student-cse20289-fa24-vandriac/hw/hw06/tests/data'
    
    def test_nofile(self):
        """Tests hw6searchsrc with no file provided"""
        output = subprocess.run(
            ["python3", "/escnfs/home/vandriac/cse-20289-repos/student-cse20289-fa24-vandriac/hw/hw06/hw6searchsrc.py", "--include", "--includelocal", "--memberfuncs", "--onelinefunc"], 
            capture_output=True, 
            text=True
            )
        self.assertNotEqual(output.returncode, 0)
        self.assertIn("the following arguments are required: file_name", output.stderr)

    def test_filenotexist(self):
        """Tests hw6searchsrc with the specified file not existing"""
        output = subprocess.run(
            ["python3", "../hw6searchsrc.py", "nonexistentfile.cc","--include", "--includelocal", "--memberfuncs", "--onelinefunc"], 
            capture_output=True, 
            text=True
            )
        self.assertNotEqual(output.returncode, 0)
        self.assertIn("No such file or directory: ", output.stderr)

    def test_filenotcc(self):
        """Tests hw6searchsrc with wrong file format"""
        full_path = os.path.join(self.path, "notcc.txt")
        output = subprocess.run(
            ["python3", "../hw6searchsrc.py", full_path,"--include", "--includelocal", "--memberfuncs", "--onelinefunc"], 
            capture_output=True, 
            text=True
            )
        self.assertNotEqual(output.returncode, 0)
        self.assertIn(" is not a .cc file", output.stderr)

    def test_fileisdir(self):
        """Tests hw6searchsrc with directory as input"""
        output = subprocess.run(
            ["python3", "../hw6searchsrc.py", self.path,"--include", "--includelocal", "--memberfuncs", "--onelinefunc"], 
            capture_output=True, 
            text=True
            )
        self.assertNotEqual(output.returncode, 0)
        # self.assertIn(" is a directory", output.stderr)

    def test_invalidarg(self):
        """Tests hw6searchsrc with invalid arguments"""
        full_path = os.path.join(self.path, "fmnc_manager.cc")
        output = subprocess.run(
            ["python3", "../hw6searchsrc.py", full_path, "badarg"], 
            capture_output=True, 
            text=True
            )
        self.assertNotEqual(output.returncode, 0)
        self.assertIn("error: unrecognized arguments:", output.stderr)


if __name__ == '__main__':
    unittest.main(verbosity=2)