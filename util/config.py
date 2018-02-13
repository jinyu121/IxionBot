# -*- coding: utf-8 -*-

import yaml
from easydict import EasyDict


class Config:
    __config = None

    @classmethod
    def get_config(cls, name=None):
        if cls.__config is None:
            with open("config.yml") as f:
                cls.__config = EasyDict(yaml.load(f))
        if name is None:
            return cls.__config
        else:
            return cls.__config.config.get(name, {})
