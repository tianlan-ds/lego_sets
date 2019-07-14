from typing import List, Optional, Dict, Any

from scraper.browser_driver import Browser


class SetScraper(object):
    _attribute_mapping = {
        'set_number': ('set number', None),
        'set_name': ('name', None),
        'set_type': ('set type', None),
        'theme_group': ('theme group', None),
        'theme': ('theme', None),
        'subtheme': ('subtheme', None),
        'year_released': ('year released', None),
        'pieces': ('pieces', None),
        'minifigs_count': ('minifigs', 0),
        'msrp': ('rrp', None),
        'packaging': ('packaging', None),
        'dimensions': ('dimensions', None),
        'weight': ('weight', None),
        'availability': ('availability', None)
    }

    def __init__(self, set_url: str, sleep_time: int = 3):
        self._browser = Browser()
        self._set_url = set_url  # type: str
        self._sleep_time = sleep_time  # type: int
        self._set_info_raw_list = self._scrape_one_set()  # type: List[str]
        self._set_data = self._format_data()  # type: Dict[str, Any]

    def _scrape_one_set(self) -> List[str]:
        """
        Create a Chrome browser and scrape raw set data based on the set url.

        :return: a list of raw set attribute names and values
        """
        self._browser.get(self._set_url)
        info = self._browser.find_elements_by_class_name('text')
        set_info_raw_list = info.text.lower().split('\n')
        self._browser.tear_down(self._sleep_time)
        return set_info_raw_list

    def _get_attribute_data(self, attribute_name: str) -> Optional[str]:
        """
        A helper function to get attribute value based on an attribute name.

        :param attribute_name: attribute name
        :return: attribute value
        """
        search_word, default_value = self._attribute_mapping.get(attribute_name)
        try:
            search_word_index = self._set_info_raw_list.index(search_word)
            return self._set_info_raw_list[search_word_index + 1]
        except:
            return default_value

    def _format_data(self) -> Dict[str, Any]:
        """
        Format the raw set data into a dictionary that contains attribute name and value.

        :return: a dictionary that contains attribute name and value
        """
        set_data = dict()
        for attribute_name, _ in self._attribute_mapping.items():
            attribute_value = self._get_attribute_data(attribute_name)
            set_data[attribute_name] = attribute_value

        return set_data

    @property
    def set_data(self) -> Dict[str, Any]:
        return self._set_data
