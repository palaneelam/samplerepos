# #*************************************************************************************************
# # Generating HTML reports for PyTest Testcases
# #************************************************************************************************
# # to install HTML reporting of pytest - pip install pytest-html
# # and to run/ show the report -----  py.test --html <full_path if u want to generate ur report elsewhere>report.html -v -s
# #************************************************************************************************
#
# import pytest
#
#
# @pytest.mark.usefixtures("setup")
# @pytest.mark.usefixtures("dataLoad")
# class TestExample:
#     # def test_fixtureDemo(self, dataLoad):
#     #     print("Data is:", dataLoad)
#     #     print("First Data is:", dataLoad[0])
#     #     print("\n This is fixture Demo defined in Class")
#     #
#     # def test_AnotherfixtureDemo(self):
#     #     print("\n This is Second fixture Demo defined in Class")
#
#     def test_crossBrowser(self, crossBrowser):
#         print("Printing dynamic data from conf test:",crossBrowser)
#         print("Print first data:",crossBrowser[0])