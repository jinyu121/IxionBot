# -*- coding: utf-8 -*-

from pathlib import Path

from util.config import Config


class BaseCommand:
    def __init__(self, filename):
        self.config = Config.get_config(Path(filename).name.strip(".py"))
