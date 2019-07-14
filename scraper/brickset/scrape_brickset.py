from typing import List, Dict, Any
import logging

from bs4 import BeautifulSoup

from scraper.browser_driver import Browser
from scraper.brickset.set_scraper import SetScraper
from scraper.scraper_constants import BrickSet

logger = logging.getLogger(__name__)


def get_href_link(page_url: str) -> List[str]:
    """
    Find all the hyper links given a theme list page url.

    :param page_url: theme list page url
    :return: a list of hyper links that can link to each individual set page
    """
    browser = Browser()
    browser.get(page_url)
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
    all_set = soup.find_all("div", {"class": "meta"})
    href_list = [one_set.find('a', href=True)['href'] for one_set in all_set]
    return href_list


def scrape_one_page(page_url: str) -> List[Dict[str, Any]]:
    """
    Given a theme list page url, scrape all the set information on that page.

    :param page_url: theme list page url
    :return: a list of dictionary which contains the attribute name and value
    """
    start_url = 'https://brickset.com'
    href_list = get_href_link(page_url)
    set_info_from_one_page = []
    for href in href_list:
        set_url = start_url + href
        set_scraper = SetScraper(set_url, sleep_time=BrickSet.SLEEP_TIME)
        set_info = set_scraper.set_data
        set_number = set_info['set_number']
        set_name = set_info['set_name']
        logger.info('done scraping set {} {}'.format(set_number, set_name))
        # if the set name has {} in it, it means the set is just a place holder and it is not released yet. Then log
        # this information and skip saving the data
        if '{' in set_name and '}' in set_name:
            logger.info('not saving set {} {}, as it is not released yet'.format(set_number, set_name))
        else:
            set_info_from_one_page.append(set_info)

    return set_info_from_one_page


def scrape_one_theme(theme_name: str) -> List[Dict[str, Any]]:
    """
    Given a theme name, loop through all pages, and scrape each set data on each page.

    :param theme_name: theme name
    :return: all the set data for the given theme name
    """
    logger.info('scraping theme {}'.format(theme_name))
    start_url = 'https://brickset.com/sets/theme-{}/page-'.format(theme_name)
    page_num = 1
    all_set_data = []
    while True:
        page_url = start_url + str(page_num)
        logger.info('scraping page {}, url: {}'.format(str(page_num), page_url))
        set_data_from_one_page = scrape_one_page(page_url)
        if len(set_data_from_one_page) > 0:
            all_set_data.extend(set_data_from_one_page)
            page_num += 1
        else:
            break

    logger.info('done scraping theme {}'.format(theme_name))

    return all_set_data


def scrape_all_theme(theme_list: List[str]) -> List[Dict[str, Any]]:
    """
    Loop through the theme list and scrape data for all the set within each theme.

    :param theme_list: a list of theme to scrape
    :return: all the set data for the entire theme list
    """
    all_set_data = []
    for theme_name in theme_list:
        one_theme_data = scrape_one_theme(theme_name)
        all_set_data.extend(one_theme_data)

    return all_set_data
