# -*- coding: utf-8 -*-

import logging
from pathlib import Path

from easydict import EasyDict

from util.config import Config


class Base:
    def __init__(self, filename):
        if not hasattr(self, "__config"):
            self.__config = {}
        self.__config = EasyDict(self.__config)

        module_name = Path(filename).name.strip(".py")
        self.__config.update(Config.get_config(module_name))

        logging.info("\n\tModule: {} \n\tConfig: {}".format(module_name, self.__config))

    def config(self, name, default=None):
        cfg = self.__config.get(name, default)
        if isinstance(cfg, str):
            cfg = cfg.strip()
        return cfg
