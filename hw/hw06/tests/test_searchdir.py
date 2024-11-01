# Vince Andriacco
# vandriac@nd.edu

import unittest
import os
import subprocess
import re

class TestRunErrors(unittest.TestCase):
    def setUp(self):
        self.path = '/escnfs/home/vandriac/cse-20289-repos/student-cse20289-fa24-vandriac/hw/hw06/tests/data/ex-tests'
        self.dirs = ['nrd-1', 'nrd-2', 'nrd-3', 'rd-1', 'rd-2', 'rd-3', 'rd-4']
        self.nonrecursive_outputs = [5, 10, 3, 5, 5, 3, 1]
        self.recursive_outputs = [5, 10, 3, 7, 11, 14, 1]
    
    def test_nonrecursive(self):
        """Test output for nonrecursive run"""
        for i, directory in enumerate(self.dirs):
            full_path = os.path.join(self.path, directory)
            output = subprocess.run(
                ["python3", "../hw6searchdir.py", full_path], 
                capture_output=True, 
                text=True
                ).stdout
            num_matches = len(re.findall(r'[^\.]+\.cc,\s\d+\sLOC,\s\d+\sI,\s\d+\sLI,\s\d+\sMF,\s\d+\sOLF', output))
            self.assertEqual(num_matches, self.nonrecursive_outputs[i])

    def test_recursive(self):
        """Test output for recursive run"""
        for i, directory in enumerate(self.dirs):
            full_path = os.path.join(self.path, directory)
            output = subprocess.run(
                ["python3", "../hw6searchdir.py", full_path, "-r"], 
                capture_output=True, 
                text=True
                ).stdout
            num_matches = len(re.findall(r'[^\.]+\.cc,\s\d+\sLOC,\s\d+\sI,\s\d+\sLI,\s\d+\sMF,\s\d+\sOLF', output))
            self.assertEqual(num_matches, self.recursive_outputs[i])

    def test_empty(self):
        """Test output with empty folder"""
        full_path = os.path.join(self.path, "empty")
        output = subprocess.run(
            ["python3", "../hw6searchdir.py", full_path, "-r"], 
            capture_output=True, 
            text=True
            ).stdout
        num_matches = len(re.findall(r'[^\.]+\.cc,\s\d+\sLOC,\s\d+\sI,\s\d+\sLI,\s\d+\sMF,\s\d+\sOLF', output))
        self.assertEqual(num_matches, 0)

    def test_nosource(self):
        """Test output for folder with no source files"""
        full_path = os.path.join(self.path, "nosource")
        output = subprocess.run(
            ["python3", "../hw6searchdir.py", full_path, "-r"], 
            capture_output=True, 
            text=True
            ).stdout
        num_matches = len(re.findall(r'[^\.]+\.cc,\s\d+\sLOC,\s\d+\sI,\s\d+\sLI,\s\d+\sMF,\s\d+\sOLF', output))
        self.assertEqual(num_matches, 0)

    def test_baddirrecursive(self):
        """Test output with invalid argument"""
        full_path = os.path.join(self.path, "nosource")
        output = subprocess.run(
            ["python3", "../hw6searchdir.py", full_path, "-r", "--badarg"], 
            capture_output=True, 
            text=True
            )
        self.assertIn("error: unrecognized arguments: ", output.stderr)

    def test_baddirrecursive(self):
        """Test output with invalid argument"""
        full_path = os.path.join(self.path, "doesnotexist")
        output = subprocess.run(
            ["python3", "../hw6searchdir.py", full_path, "-r"], 
            capture_output=True, 
            text=True
            )
        self.assertIn("error: directory does not exist, please enter an existing directory", output.stderr)

if __name__ == '__main__':
    unittest.main(verbosity=2)