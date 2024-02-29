import logging
import sys


class LogGen:

    @staticmethod
    def loggen():
        logging.basicConfig(filename='logginfile.log',
                            format='%(asctime)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                            filemode='w', level=logging.INFO)
        logger = logging.getLogger(__name__)
        # logger.setLevel(logging.INFO)
        return logger

        # logging.basicConfig(level=logging.INFO,
        #                     format="%(asctime)s [%(levelname)s] %(message)s",
        #                     handlers=[
        #                         logging.FileHandler("abc.log"),
        #                         logging.StreamHandler()
        #                     ])
        # return logging.getLogger()

        """
        # logger = logging.getLogger(__name__)
        stdoutHandler = logging.StreamHandler(stream=sys.stdout)
        fileHandler = logging.FileHandler(".\\Logs\\automation.log")
        logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)
        logger = logging.getLogger()
        logger.addHandler(stdoutHandler)
        logger.addHandler(fileHandler)

        logger.setLevel(logging.INFO)
        """
