# Vince Andriacco
# vandriac@nd.edu

import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from hw6searchsrc import readFile, countLine, getFileName, getFilePath, countInclude, countIncludeLocal, countMemberFuncs, countOneLineFunc

class TestCasesThread(unittest.TestCase):
    def setUp(self):
        self.file = readFile('/escnfs/home/vandriac/cse-20289-repos/student-cse20289-fa24-vandriac/hw/hw06/tests/data/Thread_IO.cc')
    
    def test_countLine_thread(self):
        """Test for countLine"""
        numlines = countLine(self.file)
        self.assertEqual(numlines, 149)

    def test_countInclude_thread(self):
        """Test for countInclude"""
        numincludes = countInclude(self.file)
        self.assertEqual(numincludes, 7)

    def test_countIncludeLocal_thread(self):
        """Test for countIncludeLocal"""
        numlocalincludes = countIncludeLocal(self.file)
        self.assertEqual(numlocalincludes, 5)

    def test_countMemberFuncs_thread(self):
        """Test for countMemberFuncs"""
        nummemberfuncs = countMemberFuncs(self.file)
        self.assertEqual(nummemberfuncs, 0)

    def test_countOneLineFunc_thread(self):
        """Test for countOneLineFunc"""
        numonelinefuncs = countOneLineFunc(self.file)
        self.assertEqual(numonelinefuncs, 0)

if __name__ == "__main__":
    unittest.main(verbosity=2)