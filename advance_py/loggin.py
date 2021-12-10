import logging
from logging import root

def test():
    print('-'*30)
    level = logging.getLevelName(logging.getLogger().getEffectiveLevel())
    print(f"Log Level:{level}")
    logging.debug('debug message here')
    logging.info('inf message here')
    logging.warning('warring message here')
    logging.error('error message here')
    logging.critical('critical message here')
    print('-'*30)

test(),