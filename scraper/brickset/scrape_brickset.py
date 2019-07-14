from typing import List, Dict, Any

from bs4 import BeautifulSoup

from scraper.browser_driver import Browser
from scraper.brickset.set_scraper import SetScraper


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
        set_scraper = SetScraper(set_url)
        set_info = set_scraper.set_data
        set_info_from_one_page.append(set_info)

    return set_info_from_one_page
