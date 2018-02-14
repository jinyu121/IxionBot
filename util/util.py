# -*- coding: utf-8 -*-

from collections import defaultdict


def get_package_class(name):
    name = [x.capitalize() for x in name.split("_")]
    return "".join(name)


def keyword_format(format_string, content_map):
    return format_string.format_map(defaultdict(str, **content_map))
