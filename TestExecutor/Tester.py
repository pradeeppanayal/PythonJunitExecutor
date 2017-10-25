
##############################################################
# Project          : PythonJunitTestFrameWork                #
# Since Version    : 1.0.0                                   #
# Current Version  : 1.0.0                                   #
# Date of creation : 24-Oct-2017                             #
# Author           : Pradeep CH                              #
# Purpose          : Tester class, performs test execution   #
##############################################################

import os
import sys
import argparse

def log(msg=''):
   print(msg)


class Tester(object):
   def __init__(self,testDir = '.', sourceDirs =[]):
      self.testDir = testDir
      self.sourceDirs = sourceDirs
      self.totalTests = 0
      self.successTests = 0

   def _scanTestDirectory(self):
      testFileMapper ={}
      for   dirname, subdirList, fileList in os.walk(self.testDir):
         testFileNames =[]
         log('Scanning directory :' +dirname )
         for filename in fileList:
            if filename.endswith('Test.py'):
               testFileNames.append(filename)
         log('Scanning completed. %d test file(s) found' %len(testFileNames)) 
         log()

         testFileMapper[dirname]= testFileNames
      return testFileMapper

   def _loadAndExecuteFiles(self,testfilenames):
      for testfilename in testfilenames:
         log('Executing tests from ' + testfilename)
         log('==============================================') 
         modulename= testfilename[:-3] 
         module = __import__(modulename)
         [totalTests,successTests] = self._executeTests(module)
         log('status: %d/%d success' %(successTests,totalTests))
         self.totalTests +=totalTests
         self.successTests +=successTests
         log()

   def _executeTests(self,module):
      total = 0
      success =0
      for dirname in dir(module):
         if not dirname.startswith('test'):
            continue
       
         m = getattr(module,dirname)
         if not callable(m):
            continue
         log('Executing test '+ dirname)
         total +=1
         try:
            m()
            success +=1
         except Exception as e:
            log(e)             
      return [total,success]

   def _loadSourceFiles(self):
      sys.path.extend(self.sourceDirs)

   def scanAndExecuteTests(self):
      self._loadSourceFiles()
      testFileMapper = self._scanTestDirectory()
      for directory in testFileMapper.keys():
         testfilenames = testFileMapper[directory]
         sys.path.append(directory)
         self._loadAndExecuteFiles(testfilenames)

   def showTestExecutionSummary(self): 
      log()   
      log('============ Execution Summary ===============')   
      log('Tests executed :' + str(self.totalTests))
      log('Success :' + str(self.successTests))
      log('Failure :' + str(self.totalTests - self.successTests))
      log('==============================================') 
      log() 
     
      
      
