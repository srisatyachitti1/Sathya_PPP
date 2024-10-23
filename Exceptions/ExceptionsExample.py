import logging
import time
from logging import Logger

#create logger
logging.basicConfig(filename="c:\\python_examples\\pythonProject1\\problems.log", level= logging.DEBUG)
logger = logging.getLogger()
def read_file_timed(path):
    """return the contents of the file at path and measure the time required"""
    start_time = time.time()
    try:
        f= open(path, mode="rb")
        data=f.read()
        return data
    except FileNotFoundError as err:
        logging.error(err)
        raise
    else:
        f.close()
    finally:
        stop_time = time.time()
        dt= stop_time - start_time
        logger.info("Time required for {file} = {time}".format(file=path, time=dt))

        data= read_file_timed("D:\\SriSatya Doc\\Scrum.mp3") # 5 MB file