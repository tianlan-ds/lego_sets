import os


class BrickSet(object):
    MIN_SLEEP_TIME = int(os.environ.get("BRICKSET_MIN_SLEEP_TIME", "1"))
    MAX_SLEEP_TIME = int(os.environ.get("BRICKSET_MAX_SLEEP_TIME", "3"))

    THEME_LIST = ['Creator-Expert', 'Architecture', 'Ideas', 'Star-Wars', 'Technic']
