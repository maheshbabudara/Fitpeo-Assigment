import pytest
#Part1:
#Rules of pytest:
# 1.Should start/End with test word either in test case or file name
#Assert means validation of Test case
#we can execute the All Test Module files at once with cmd: py.test or we can execute with specific Module file
# with cmd: py.test filename or we can execute specific test cases in all module files with cmd: py.test -k login -v

#Part2:
#Markers:
#syntax: @pytest.mark.login
#cmd: py.test -m login
#Note: For parallele execution of test cases install package: pip install pytest.xdist
#cmd for parallel execution: py.test filename/all files -n 5(count)

#Part3:
#we can generetae html report, we need package: pip install pytest-html
#cmds to generate html report with selenoum test cases: py.test test_py_Fixture_selenium.py -v --html=demo_app.html
#Note: verbose(-v) is for more information and -s is for printing output on console

#Part3(Reports using Allure package):
#cmd to generate report folder: pytest -m name --alluredir=folder name
#cmd to display the created reports: open folder in Explorer->open in comand prompt -> allure serve exactfoldername run this cmd.
#cmd to check the expected result use markers: @pytest.mark.Xfail

#Notes:
#we cannot use Multiple Fixtures for an test case, if requires cover steps in an fixture and make use of it.

def test_mahesh():
    assert 'mahesh'=='mahesh', 'Test passed'
# def rony_test():   #willl not work becoz test word is not at starting
#     assert 2+3==5, 'Test Case Passed'
# def mah_test_ron():  #willl not work becoz test word is not at starting
#     assert 'mahesh'==2,'Wrong'

def test_m():
    assert 2+3==5
def test_m1():
    assert 'mahesh'==2, 'String not equals to Integer'
def test_ro():
    assert 'mahesh'=='mahesh'