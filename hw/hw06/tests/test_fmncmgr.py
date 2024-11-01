# Vince Andriacco
# vandriac@nd.edu

import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from hw6searchsrc import readFile, countLine, getFileName, getFilePath, countInclude, countIncludeLocal, countMemberFuncs, countOneLineFunc

class TestCasesFmncMgr(unittest.TestCase):
    def setUp(self):
        self.file = readFile('/escnfs/home/vandriac/cse-20289-repos/student-cse20289-fa24-vandriac/hw/hw06/tests/data/fmnc_manager.cc')
    
    def test_countLine_fmncmgr(self):
        """Test for countLine"""
        numlines = countLine(self.file)
        self.assertEqual(numlines, 2310)

    def test_countInclude_fmncmgr(self):
        """Test for countInclude"""
        numincludes = countInclude(self.file)
        self.assertEqual(numincludes, 18)

    def test_countIncludeLocal_fmncmgr(self):
        """Test for countIncludeLocal"""
        numlocalincludes = countIncludeLocal(self.file)
        self.assertEqual(numlocalincludes, 11)

    def test_countMemberFuncs_fmncmgr(self):
        """Test for countMemberFuncs"""
        nummemberfuncs = countMemberFuncs(self.file)
        self.assertEqual(nummemberfuncs, 77)

    def test_countOneLineFunc_fmncmgr(self):
        """Test for countOneLineFunc"""
        numonelinefuncs = countOneLineFunc(self.file)
        self.assertEqual(numonelinefuncs, 1)

    def test_getFileName_fmncmgr(self):
        """Test for getFileName"""
        name = getFileName('student-cse20289-fa24-vandriac/hw/hw06/tests/data/fmnc_manager.cc')
        self.assertEqual(name, 'fmnc_manager.cc')

    def test_getFilePath_fmncmgr(self):
        """Test for getFilePath"""
        name = getFilePath('student-cse20289-fa24-vandriac/hw/hw06/tests/data/fmnc_manager.cc')
        self.assertEqual(name, 'student-cse20289-fa24-vandriac/hw/hw06/tests/data')

if __name__ == "__main__":
    unittest.main(verbosity=2)