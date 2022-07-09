#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Define the abstraction of a config loader.
"""

from abc import ABC, abstractmethod
from typing import List

from wlbb.lib.wlbb_typing import ConfigDict

__all__ = "ConfigLoader"


class ConfigLoader(ABC):
    """
    A config loader is used to create, delete, load and save configuration.
    """

    @abstractmethod
    def get_config_list(self, config_dir: str) -> List[str]:
        """
        Return a list containing all config name compatible with the config loader
        in the directory `config_dir`.
        """

    @abstractmethod
    def create_config(self, config_dir: str, config_name: str):
        """
        Create an empty config file in the directory `config_dir`.
        """

    @abstractmethod
    def delete_config(self, config_dir: str, config_name: str):
        """
        Delete the specified config file in the directory `config_dir` if it
        exists.
        """

    @abstractmethod
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

    @abstractmethod
    def save_config(self, config_dict: ConfigDict, config_dir: str, config_name: str):
        """
        Save the config's representation as a dict in the configuration file
        for `config_name` in the directory `config_dir`.
        If this config file doesn't exists yet, it is created.

        Example of the a config representation as a dict:
        {
            "PARAMETER_GROUP_1":{"parameter1":value1, "parameter2":value2}
        }
        """
