import logging

# Configure logging
logging.basicConfig(
    filename='app.log', level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s' ,
    # filemode='w'
    )

# Logging messages
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message1")
logging.error("This is an error message")

logging.critical("This is a critical message")
