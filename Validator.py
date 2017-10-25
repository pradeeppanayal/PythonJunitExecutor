
##############################################################
# Project          : PythonJunitTestFrameWork                #
# Since Version    : 1.0.0                                   #
# Current Version  : 1.0.0                                   #
# Date of creation : 24-Oct-2017                             #
# Author           : Pradeep CH                              #
# Purpose          : Sample source class                     #
##############################################################

__author__ = 'Pradeep CH'
__version__ ='1.0.0'
 

import argparse
from TestExecutor import Tester

parser = argparse.ArgumentParser()
parser.add_argument('-t',"--testDir", help="Root directory to execute the tests",type=str,default='.')
parser.add_argument('-s',"--sourcesDirs", help="Source module/file path need to be tested",nargs = '*',default=[])

def main():
   args = parser.parse_args()
   tester = Tester(args.testDir,args.sourcesDirs)
   tester.scanAndExecuteTests()
   tester.showTestExecutionSummary()
if __name__ =='__main__':
  main() 
