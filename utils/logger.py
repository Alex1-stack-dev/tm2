import logging
def setup_logging():
    logging.basicConfig(filename='app.log', level=logging.INFO)
def log_error(e):
    logging.error(str(e))
