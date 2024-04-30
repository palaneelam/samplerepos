import logging


def test_loggingDemo():
    logger = logging.getLogger(__name__)

    # logger.addHandler()   #filehandler object
    fileHandler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)  # filehandler object
    logger.setLevel(logging.WARNING)

    logger.debug("A debug statement is executed")
    logger.info("Information statement")
    logger.warning("Something is in warning mode")
    logger.error("A major error has happened")
    logger.critical("Critical Issue")

    # logger = logging.getLogger(__name__)
    # filehandler = logging.FileHandler('logfile.log')
    # formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
    # filehandler.setFormatter(formatter)
    # logger.addHandler(filehandler)
    # logger.setLevel(logging.INFO)
    #
    # logging.debug("Debug stattement is printed")
    # logging.info("INfo stattement is printed")
    # logging.warning("Warning stattement is printed")
    # logging.error("Error stattement is printed")
    # logging.critical("Critical stattement is printed")