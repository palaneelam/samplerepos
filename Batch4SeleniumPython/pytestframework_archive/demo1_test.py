# **************************  Pre-requisite for any pytest framework: *****************************
# 1.install pytest framework
# 2. test name should begin test_ or end with _test
# 3. All the test cases/scripts should be packed in methods. And the method name must begin with test_
import pytest


# **************************  To run the test  *****************************
# Option 1. Go to the edit configurations and select pytest and then give script path and then apply and run
# Option 2(recommended one) - to run your test from terminal by using command -> py.test -v -s
#                             -v --- gives more information (metadata)
#                             -s --- show console logs
# We can all the test cases in the .py file or run only the few selected ones.
# to run the few selected ones... include the common keyword in your test case name (this process is called
#                                 grouping the test cases)
# In below example --search is the keyword written on second, fourth & sixth test case.
# common used is: py.test -k <keyword> -v -s
# -k here stands for method names execution
# what if you want to run tests based on smoke or regression labels?
# command is - py.test -m smoke -v s
# here -m is denting the mark
# To skip the test from execution command is py.test -v -s and put marker on the test case as @pytest.mark.skip
# To do the execution, but not report the failure in output and neither stop the
# execution abruptly, we use @pytest.mark.xfail
# *********************************************************************************************************************
# to have a common intructions executed for each test case/script before execution and after execution
# setup method and yield is used
# We use them with @pytest.fixture()

@pytest.mark.smoke
def test_firstProgram(setup):
    print("Hello Everyone. Today is a bright sunny thursday morning!")


def test_SearchsecondProgram(setup):
    print("I am not in a mood to work today!")


@pytest.mark.regression
def test_thirdProgram(setup):
    print("I really love doing what I do!")


def test_SearchfourthProgram(setup):
    print("Day after tomorrow uis much awaited holiday!")


@pytest.mark.skip
def test_fifthProgram(setup):
    print("Now that means, tomorrow is friyyyyyydayyyyyy. TGIF!!!!!!")


@pytest.mark.xfail
def test_SearchsixthProgram(setup):
    print("I just want to netflix and chill on friday!")
    print("Division:", 2 / 0)


@pytest.fixture()
def setup():
    print("THIS WILL BE EXECUTED FIRST IN THE BEGINNING")
    yield
    print("THIS IS THE LAST STEP OF THE TEST CASE")
