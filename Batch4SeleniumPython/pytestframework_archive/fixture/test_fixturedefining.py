import pytest

from BaseClass import BaseClass


@pytest.mark.usefixtures("setup")
@pytest.mark.usefixtures("dataLoad")
class TestFixtureDemo(BaseClass):
    # def test_firstProgram(self):
    #     print("Hello Everyone. Today is a bright sunny thursday morning!")
    #
    # def test_SearchsecondProgram(self):
    #     print("I am not in a mood to work today!")
    #
    # def test_thirdProgram(self):
    #     print("I really love doing what I do!")
    #
    # def test_SearchfourthProgram(self):
    #     print("Day after tomorrow uis much awaited holiday!")
    #
    # def test_fifthProgram(self):
    #     print("Now that means, tomorrow is friyyyyyydayyyyyy. TGIF!!!!!!")
    #
    # # def test_SearchsixthProgram(self):
    # #     print("I just want to netflix and chill on friday!")
    #
    # def test_editProfile(self, dataLoad):
    #     print(dataLoad)
    #
    # def test_crossBrowser(self, crossBrowser):
    #     print(crossBrowser)
    #     print(crossBrowser[0])
    #     print(crossBrowser[1])

    def test_SearchsixthProgram(self):
        log = BaseClass.getLogger(self)
        # log = self.getLogger()
        log.info("This is a log trying to output")
        print("I just want to netflix and chill on friday!")
