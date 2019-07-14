import os


class BrickSet(object):
    SLEEP_TIME = int(os.environ.get("BRICKSET_SLEEP_TIME", "1"))

    THEME_LIST = ['Creator-Expert', 'Architecture', 'Ideas', 'Star-Wars', 'Technic']
