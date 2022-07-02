#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Thu Jun 30 21:31:41 2022

@author: lothaire
"""

from abc import ABC, abstractmethod

from typing import List, Dict, Any

ParameterGroupDict = Dict[str, Any]
ConfigDict = Dict[str, ParameterGroupDict]


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


class WLBBParameterGroup:
    """
    A cluster of parameters which can be modified and accessed.
    """

    def __init__(self, name, pg_dict=None):
        self.name = name
        if pg_dict is None:
            self._dict = {}
        else:
            self._dict = pg_dict

    def get_dict(self):
        """
        Return the dictionnary representation of the parameter group.
        """
        return self._dict.copy()


class WLBBConfig:
    """
    The configuration interface for a WLBB instance which allow
    loading, saving, generating and modifying configurations.
    """

    _dict: Dict[str, WLBBParameterGroup]

    def __init__(self, wlbb_instance):
        """
        Create a config interface for the WLBB instance.
        """
        self._dict = {}

    def import_dict(self, new_config_dict: ConfigDict):
        """
        Import the config `new_config_dict`.
        """
        self._dict.clear()

        for pg_name, pg_dict in new_config_dict.items():
            self._dict[pg_name] = WLBBParameterGroup(pg_name, pg_dict)

    def import_default(self, cfg_loader: ConfigLoader = None):
        """
        Generate and import a default config compatible with the WLBB instance.
        """

    def import_config(self, cfg_name: str, cfg_loader: ConfigLoader = None):
        """
        Import the config named `cfg_name` if it exists and modify it to be
        compatible with the current WLBB instance.
        """

    def load(self, cfg_loader: ConfigLoader = None):
        """
        Load the WLBB instance's associated configuration using the given config
        loader or a default one.

        If there isn't any configuration file associated with this WLBB instance,
        an generated configuration file is created containing a compatible
        configuration.
        """

    def save(self, cfg_loader: ConfigLoader = None):
        """
        Save the current configuration in the WLBB instance's associated config file.
        """

    def get_config_dict(self) -> ConfigDict:
        """
        Return the dictionnary representation of the configuration.
        """
        new_dict = {}
        for pg_name, pg in self._dict.items():
            new_dict[pg_name] = pg.get_dict()

        return new_dict
