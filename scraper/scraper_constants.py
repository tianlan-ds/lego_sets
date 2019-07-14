import os


class BrickSet(object):
    sleep_time = int(os.environ.get("BRICKSET_SLEEP_TIME", "1"))
