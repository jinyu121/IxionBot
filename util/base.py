# -*- coding: utf-8 -*-

import logging
from pathlib import Path

from easydict import EasyDict

from util.config import Config


class Base:
    def __init__(self, filename):
        if not hasattr(self, "config"):
            self.config = {}
        self.config = EasyDict(self.config)

        module_name = Path(filename).name.strip(".py")
        self.config.update(Config.get_config(module_name))
        self.config = EasyDict(self.config)

        logging.info("\n\tModule: {} \n\tConfig: {}".format(module_name, self.config))
