#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Define testing classes.
"""

from typing import Dict, List

from wlbb.lib.agent.agent import WLBBAgent, Status
from wlbb.lib.config.wlbb_config import ConfigLoader, ConfigDict


class WLBBDummyAgent(WLBBAgent):
    """
    A dummy agent which should be used for testing.
    """

    agent = "dummy"
    parameter_groups = ["PARAM_GROUP1", "PARAM_GROUP2"]

    def init(self):
        pass

    def quit(self):
        pass

    def start(self):
        self.status = Status.ACTIVE

    def stop(self):
        self.status = Status.INACTIVE

    def restart(self):
        pass

    def reload(self):
        pass


class TestingConfigLoader(ConfigLoader):
    """
    A config loader used for testing.
    """

    def __init__(self, configs: Dict[str, Dict[str, ConfigDict]] = {}) -> List[str]:
        self.configs = configs

    def get_config_list(self, config_dir: str):
        """
        Return a list containing all config name compatible with the config loader
        in the virtual directory `config_dir`.
        """
        if config_dir not in self.configs:
            return []
        return list(self.configs[config_dir])

    def create_config(self, config_dir: str, config_name: str):
        """
        Create an empty config in the virtual directory `config_dir`.
        """
        if config_dir not in self.configs:
            self.configs[config_dir] = {}
        if config_name not in self.configs[config_dir]:
            self.configs[config_dir][config_name] = {}

    def delete_config(self, config_dir: str, config_name: str):
        """
        Delete the specified config file in the virtual directory `config_dir`
        if it exists.
        """
        if config_dir not in self.configs:
            return
        if config_name not in self.configs[config_dir]:
            return
        self.configs[config_dir].pop(config_name)

    def load_config(self, config_dir: str, config_name: str) -> ConfigDict:
        """
        Return the requested configuration if it exists as a dictionnary
        associating parameter groups name with their representation : another
        dictionnary associating parameters with their value.

        Example of the a config representation as a dict:
        {
            "PARAMETER_GROUP_1":{"parameter1":value1, "parameter2":value2}
        }
        """
        if config_dir not in self.configs:
            return {}
        if config_name not in self.configs[config_dir]:
            return {}
        return self.configs[config_dir][config_name]

    def save_config(self, config_dict: ConfigDict, config_dir: str, config_name: str):
        """
        Save the config's representation as a dict in the configuration
        for `config_name` in the virtual directory `config_dir`.
        If this config doesn't exists yet, it is created.

        Example of the a config representation as a dict:
        {
            "PARAMETER_GROUP_1":{"parameter1":value1, "parameter2":value2}
        }
        """
        if config_dir not in self.configs:
            self.configs[config_dir] = {}
        self.configs[config_dir][config_name] = config_dict
