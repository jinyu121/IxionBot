# -*- coding: utf-8 -*-


def get_package_class(name):
    name = [x.capitalize() for x in name.split("_")]
    return "".join(name)
