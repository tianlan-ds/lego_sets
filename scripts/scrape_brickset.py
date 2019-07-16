#!/usr/bin/env python3

import logging
import sys

from typing import List

from scraper.brickset.scrape_brickset import scrape_all_theme
from scraper.utils import save_data
from scraper.scraper_constants import BrickSet

logging.basicConfig(level=logging.INFO,
                    format='[%(process)6s] %(asctime)s %(levelname)8s [%(name)s] %(message)s',
                    stream=sys.stdout)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def main(theme_list: List[str]):
    data_dict = scrape_all_theme(theme_list)
    file_name = 'new_scrape_data'
    save_data(data_dict, file_name)
    return


if __name__ == "__main__":
    if len(sys.argv) == 1:
        theme_list = BrickSet.THEME_LIST
    else:
        theme_list = [sys.argv[1]]

    main(theme_list)
