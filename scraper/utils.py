import logging
from typing import List, Dict, Any
import random
import os

import pandas as pd

from scraper.scraper_constants import BrickSet

logger = logging.getLogger(__name__)


def generate_sleep_time(min_sleep_time: int = BrickSet.MIN_SLEEP_TIME, max_sleep_time: int = BrickSet.MAX_SLEEP_TIME)\
        -> float:
    sleep_time = random.uniform(min_sleep_time, max_sleep_time)
    return round(sleep_time, 3)


def save_data(input_data: List[Dict[str, Any]], file_name: str):
    df = pd.DataFrame(input_data)
    root_path = os.getcwd()
    save_path = '/data/'
    complete_path = root_path + save_path + file_name + '.csv'

    df.to_csv(complete_path, index=None, header=True)
    logger.info('done saving data to {}'.format(complete_path))
