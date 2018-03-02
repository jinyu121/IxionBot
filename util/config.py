# -*- coding: utf-8 -*-

import yaml
from easydict import EasyDict


class Config:
    _config = None

    @classmethod
    def load_config(cls, filename=None):
        if cls._config is None:
            assert filename, "Should specify config name"
            with open(filename) as f:
                cls._config = EasyDict(yaml.load(f))

    @classmethod
    def get_config(cls, name=None):
        assert cls._config, "Should load config first"
        if name is None:
            return cls._config
        else:
            return cls._config.config.get(name, {})
