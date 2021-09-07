import logging


logging.basicConfig(level=logging.DEBUG, filename='file.log')
name = 'Wanderson'
logging.debug(f'DEBUG {name}')

if __name__ == '__main__':
    # Debug
    # Useful to debug functions in code
    name = 'Wanderson'
    logging.debug(f'DEBUG {name}')

    # Info
    # Used to record general information about the system
    logging.info(f'Test Info {name}')

    # Waring
    # Using to point out a warning of a possible error that could happen
    logging.warning(f'Test Waring {name}')

    # Error
    # Using to point out an error when executing a function or piece of code
    logging.error(f'Test Error {name}')

    # Critical
    logging.critical(f'Test Critical{name}')