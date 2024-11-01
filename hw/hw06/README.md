Name: Vince Andriacco
email: vandriac@nd.edu

I changed the regex expression for countMemberFuncs so that it no longer checks the start of the string
This caused test_countMemberFuncs_fmncmgr, test_countMemberFuncs_paramdict, test_countMemberFuncs_ripps to fail

I removed --includelocal from the subprocess in hw6searchdir so that that was not calculate the number of include 
This caused test_nonrecursive and test_nonrecursive to fail