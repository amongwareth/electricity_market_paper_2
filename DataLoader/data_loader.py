import logging

logger = logging.getLogger(__name__)


class DataCleaning(object):
    '''General class to start clean up of raw functional bids'''

    def __init__(self, **kwargs_gen):
        ''' Initialize the attributes with default values defined in the Config.config file '''
        super().__init__()
