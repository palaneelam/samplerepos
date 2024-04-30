import inspect

from _pytest import logging


class BaseClass:
    # def test_loggingDemo(self):
    def getLogger(self):
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)
        # logger = logging.FileHandler('logfile.log')
        # logger.addHandler()   #filehandler object
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)   #filehandler object
        logger.setLevel(logging.DEBUG)
        return logger