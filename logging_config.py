import logging
with open('latest.log', 'w'):
    pass
logging.basicConfig(filename='latest.log', level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')