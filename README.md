# PythonJunitExecutor
Simple python application which can be used to scan and execute python test files.

# Usage
It is simple to use, just call the Tester.py with the following syntax

    Tester.py [-h] [-t TESTDIR] [-s [SOURCESDIRS [SOURCESDIRS ...]]]
    
 * TESTDIR : Path to the folder where the test files are located
 * SOURCESDIRS : Space seperated source file locations. If its already available in `Sys.path`, no need to mention
 
# How it works ?
 * Step 1: Scan provided test directory recursively and fetch all the python files which ends with "Test.py"
 * Step 2: Each file will be scanned and all the test methods (starts with "test") will be identifed
 * Step 3: Execute each test
 * Step 4: Generate the summary
 
# Sample output
   
    Test  Tester.py  TestExecutor  Validator.py  Validator.pyc
    Scanning directory :Test/Sample/tests
    Scanning completed. 1 test file(s) found

    Executing tests from SampleTest.py
    ==============================================
    Executing test testSayHai1
    Executing test testSayHai2
    Executing test testSayHai3
    Executing test testSayHai4
    status: 4/4 success

    ============ Execution Summary ===============
    Tests executed :4
    Success :4
    Failure :0
    ==============================================
  
