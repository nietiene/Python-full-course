# logging is the proces of recording events, error, warings or info during the program execution
# so instead of using print we use logging instead of print

import logging

logging.basicConfig(level=logging.DEBUG)

logging.debug("This is debug message") # internal info for debugging
logging.info("Thiis is an info message") # general info like server started
logging.warning("This is warning") # something unexpected but app keep runs
logging.error("This is an error") # serious error
logging.critical("This is critical") # program crash, security failure