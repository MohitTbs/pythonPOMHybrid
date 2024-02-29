import logging


class LogGen2:
    static_logger = None

    @staticmethod
    def loggen():
        logger = logging.getLogger(__name__)
        fileHandler = logging.FileHandler('logfile.log', mode='w')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        LogGen2.static_logger = logger
        return LogGen2.static_logger

# Character
# Meaning
#
# 'r'
#
# open for reading (default)
#
# 'w'
#
# open for writing, truncating the file first
#
# 'x'
#
# open for exclusive creation, failing if the file already exists
#
# 'a'
#
# open for writing, appending to the end of file if it exists
#
# 'b'
#
# binary mode
#
# 't'
#
# text mode (default)
#
# '+'
#
# open for updating (reading and writing)
