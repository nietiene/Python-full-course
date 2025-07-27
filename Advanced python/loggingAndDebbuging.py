# logging is the proces of recording events, error, warings or info during the program execution
# so instead of using print we use logging instead of print

import logging

logging.basicConfig(level=logging.DEBUG)

logging.debug("This is debug message")
logging.info("Thiis is an info message")
logging.warning("This is warning")
logging.error("This is an error")
logging.critical("This is critical")