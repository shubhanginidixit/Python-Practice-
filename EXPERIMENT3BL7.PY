import logging

# Configure logging format
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Logging at different levels
logging.info("Program started successfully.")
logging.warning("This is a warning message.")
logging.error("An error occurred while processing data.")
logging.critical("Critical issue! System may stop working.")