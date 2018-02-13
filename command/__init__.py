# -*- coding: utf-8 -*-

from pathlib import Path

from util.config import Config


class BaseCommand:
    def __init__(self, filename):
        module_name = Path(filename).name.strip(".py")
        self.__config = Config.get_config(module_name)

    def config(self, name, default=None):
        return self.__config.get(name, default)
