import logging

logging.basicConfig(filename='loggger.log', level=logging.INFO, filemode='w',format='%(asctime)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',)

logger = logging.getLogger('ParentLo')
logger.info('sdsddsdsdsd')
