import logging


class NonStandardAttributeWarning(Warning):
    def __init__(self, msg):
        logging.warning(msg)
