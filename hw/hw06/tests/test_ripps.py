# Vince Andriacco
# vandriac@nd.edu

import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from hw6searchsrc import readFile, countLine, getFileName, getFilePath, countInclude, countIncludeLocal, countMemberFuncs, countOneLineFunc

class TestCasesRIPPS(unittest.TestCase):
    def setUp(self):
        self.file = readFile('/escnfs/home/vandriac/cse-20289-repos/student-cse20289-fa24-vandriac/hw/hw06/tests/data/RIPPS_PktPair.cc')
    
    def test_countLine_ripps(self):
        """Test for countLine"""
        numlines = countLine(self.file)
        self.assertEqual(numlines, 607)

    def test_countInclude_ripps(self):
        """Test for countInclude"""
        numincludes = countInclude(self.file)
        self.assertEqual(numincludes, 5)

    def test_countIncludeLocal_ripps(self):
        """Test for countIncludeLocal"""
        numlocalincludes = countIncludeLocal(self.file)
        self.assertEqual(numlocalincludes, 3)

    def test_countMemberFuncs_ripps(self):
        """Test for countMemberFuncs"""
        nummemberfuncs = countMemberFuncs(self.file)
        self.assertEqual(nummemberfuncs, 50)

    def test_countOneLineFunc_ripps(self):
        """Test for countOneLineFunc"""
        numonelinefuncs = countOneLineFunc(self.file)
        self.assertEqual(numonelinefuncs, 23)

if __name__ == "__main__":
    unittest.main(verbosity=2)