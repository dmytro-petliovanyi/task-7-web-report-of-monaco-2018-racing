import os

from dotenv import load_dotenv


class DefaultConfig:
    load_dotenv()
    TARGET_DIR = os.environ["RACE_INFO_DIR"]
    DEBUG = True
    TESTING = True
