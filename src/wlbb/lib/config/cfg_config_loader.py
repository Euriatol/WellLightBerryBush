#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Define CfgConfigLoader.
"""

import os
from typing import List
from configparser import ConfigParser

from wlbb.lib.config.config_loader import ConfigLoader
from wlbb.lib.config.config_loader import ConfigDict
from wlbb.lib.paths import create_dir, create_file, delete_file


def configparser_to_dict(config_parser: ConfigParser) -> ConfigDict:
    """
    Convert a config parser into a config dict.
    """
    old_dict = dict(config_parser)
    new_dict = {}
    for section in old_dict:
        new_dict[section] = dict(old_dict[section])

    return new_dict


class CfgConfigLoader(ConfigLoader):
    """
    A config loader using the builtin module configparser.
    """

    def __init__(self):
        self.ext = "cfg"
        self.config_parser = ConfigParser(default_section="WLBB_CONFIG")
        self.config_parser.clear()

    def get_config_list(self, config_dir: str) -> List[str]:
        if not os.path.isdir(config_dir):
            return []

        cfgs = []
        for conf_file in os.listdir(config_dir):
            name, ext = os.path.splitext(conf_file)
            if ext == self.ext:
                cfgs.append(name)

        return cfgs

    def create_config(self, config_dir: str, config_name: str):
        config_file = "{name}.{ext}".format(name=config_name, ext=self.ext)
        path = os.path.join(config_dir, config_file)

        if not os.path.isdir(config_dir):
            create_dir(config_dir)

        if config_name not in self.get_config_list(config_dir):
            create_file(path)

    def delete_config(self, config_dir: str, config_name: str):
        config_file = "{name}.{ext}".format(name=config_name, ext=self.ext)
        path = os.path.join(config_dir, config_file)

        if not os.path.isdir(config_dir):
            return
        if config_name not in self.get_config_list(config_dir):
            return

        delete_file(path)

    def load_config(self, config_dir: str, config_name: str) -> ConfigDict:
        config_file = "{name}.{ext}".format(name=config_name, ext=self.ext)
        path = os.path.join(config_dir, config_file)

        if not os.path.isdir(config_dir):
            return {}
        if config_name not in self.get_config_list(config_dir):
            return {}

        self.config_parser.read(path)
        return configparser_to_dict(self.config_parser)

    def save_config(self, config_dict: ConfigDict, config_dir: str, config_name: str):
        config_file = "{name}.{ext}".format(name=config_name, ext=self.ext)
        path = os.path.join(config_dir, config_file)

        self.create_config(config_dir, config_name)
        self.config_parser.read_dict(config_dict)
        with open(path, "w") as cfg:
            self.config_parser.write(cfg)
