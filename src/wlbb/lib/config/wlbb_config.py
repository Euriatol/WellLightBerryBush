#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Thu Jun 30 21:31:41 2022

@author: lothaire
"""

from typing import List, Dict, Any

from wlbb.lib.logger import wlbb_logger

from wlbb.lib.config.config_loader import ConfigLoader
from wlbb.lib.wlbb_typing import ConfigSectionDict, ConfigDict

from wlbb.lib.config.default import get_builtin_default_config_dir
from wlbb.lib.config.default import DEFAULT_CFG_NAME, BuiltinDefaultConfigLoader

from wlbb.lib.paths import get_config_dir

__all__ = ("WLBBConfig", "WLBBConfigSection")


class WLBBConfigSection:
    """
    A cluster of parameters which can be modified and accessed.
    """

    def __init__(self, name: str, section_dict: dict = None):
        self.name = name
        if section_dict is None:
            self.section_dict = {}
        else:
            self.section_dict = section_dict

    def get_dict(self) -> ConfigSectionDict:
        """
        Return the dictionnary representation of the config section.
        """
        return self.section_dict.copy()

    def get_parameter_list(self) -> List[str]:
        """
        Return a list containing every parameter name in this section.
        """
        return list(self.get_dict())

    def add_parameter(self, parameter: str, value: Any):
        """
        Add a new parameter.
        """
        if not parameter in self.get_parameter_list():
            self.section_dict[parameter] = value
        else:
            pass


class WLBBConfig:
    """
    The configuration interface for a WLBB instance which allow
    loading, saving, generating and modifying configurations.
    """

    cfg_name: str
    cfg_dict: ConfigDict
    sections: Dict[str, WLBBConfigSection]

    def __init__(self, wlbb_instance):
        """
        Create a config interface for the WLBB instance.
        """
        self.wlbb_instance = wlbb_instance
        self.cfg_name = self.wlbb_instance.name
        self.cfg_dict = {}
        self.sections = {}

    def _raw_import_dict(self, new_config_dict: ConfigDict):
        self.cfg_dict.clear()
        self.sections.clear()

        for cs_name, cs_dict in new_config_dict.items():
            if cs_name in self.wlbb_instance.get_config_sections_list():
                self.cfg_dict[cs_name] = cs_dict

    def _raw_import_config(
        self, cfg_dir: str, cfg_name: str, cfg_loader: ConfigLoader = None
    ):
        if cfg_loader is None:
            cfg_loader = self.wlbb_instance.get_config_loader()

        new_config_dict = cfg_loader.load_config(cfg_dir, cfg_name)

        self._raw_import_dict(new_config_dict)

    def import_default(self):
        """
        Generate and import a default config compatible with the WLBB instance.
        """
        cfg_loader = BuiltinDefaultConfigLoader()

        self._raw_import_config(
            get_builtin_default_config_dir(), DEFAULT_CFG_NAME, cfg_loader
        )

        if len(self.wlbb_instance.get_config_sections()) > len(self.get_config_dict()):
            wlbb_logger.warning(
                "Builtin default config doesn't contain every config section."
            )
            sections = set(self.wlbb_instance.get_config_sections())
            sections_found = set(self.get_config_dict())
            missing_sections = list(sections.difference(sections_found))
            wlbb_logger.debug(
                "Sections missing in the default config : %a." % missing_sections
            )

    def import_dict(self, new_config_dict: ConfigDict, complete_default=True):
        """
        Import the config `new_config_dict`.
        """
        if not complete_default:
            self._raw_import_dict(new_config_dict)
            return

        self.import_default()

        default_config_dict = self.cfg_dict

        for section_name, section_dict in new_config_dict.items():
            if section_name in self.wlbb_instance.get_config_sections():
                if section_name in default_config_dict:
                    default_config_dict.update(section_dict)

    def import_config(
        self, cfg_name: str, cfg_loader: ConfigLoader = None, complete_default=True
    ):
        """
        Import the config named `cfg_name` if it exists and modify it to be
        compatible with the current WLBB instance.
        """
        if cfg_loader is None:
            cfg_loader = self.wlbb_instance.get_config_loader()

        new_config_dict = cfg_loader.load_config(get_config_dir(), cfg_name)

        self.import_dict(new_config_dict, complete_default)

    def load(self, cfg_loader: ConfigLoader = None):
        """
        Load the WLBB instance's associated configuration using the given config
        loader or a default one.

        If there isn't any configuration file associated with this WLBB instance,
        an generated configuration file is created containing a compatible
        configuration.
        """
        self.import_config(self.cfg_name, cfg_loader)

    def save(self, cfg_loader: ConfigLoader = None):
        """
        Save the current configuration in the WLBB instance's associated config file.
        """
        if cfg_loader is None:
            cfg_loader = self.wlbb_instance.get_config_loader()

        cfg_loader.save_config(self.get_config_dict(), get_config_dir(), self.cfg_name)

    def get_config_dict(self) -> ConfigDict:
        """
        Return the dictionnary representation of the configuration.
        """
        return self.cfg_dict.copy()

    def get_config_section(self, section_name: str) -> WLBBConfigSection:
        """
        Return the requested config section if it exists.
        """
