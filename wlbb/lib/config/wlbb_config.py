#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Implement the configuration interface class.
"""

import string as _string

from wlbb.lib.config.config_manager import get_config_manager as _get_config_manager
from wlbb.lib.config.config_manager import ConfigManagerProtocol

VALID_ALPHABET = _string.ascii_letters + _string.digits + "_-"

class NotAParameterError(ValueError):
    """Inexistant parameter."""

class InvalidConfigNameError(ValueError):
    """Invalid configuration's name."""

def config_name_valid(config_name):
    """Return True if config_name is a valid name for a configuration."""
    return all([l in VALID_ALPHABET for l in config_name])

def _assert_param_in_config(param, config):
    """Raise an error if param isn't a parameter in config."""
    if param not in config.get_config_dict():
        raise NotAParameterError("%a isn't a parameter."%param)

def _assert_config_name_is_valid(config_name):
    """Raise an error if config_name isn't a valid name for a configuration."""
    if not config_name_valid(config_name):
        raise InvalidConfigNameError("%a isn't a valid name for a configuration."%config_name)

class Config:
    """Configuration interface for WLBB."""

    def __init__(self):
        self.config_name = None
        self._config_default = {}
        self._config = {}
        self._metadata = {}

    def set_config_dict(self, new_config):
        """Set the config dict to new_config."""
        self._config = dict(new_config)

    def set_config_default_dict(self, new_config_default):
        """Set the config default dict to new_config_default."""
        self._config_default = dict(new_config_default)

    def set_metadata_dict(self, new_metadata):
        """Set the metadata dict to new_metadata."""
        self._metadata = dict(new_metadata)

    def get_config_dict(self):
        """Return the config dict."""
        return self._config

    def get_config_default_dict(self):
        """Return the config default dict."""
        return self._config_default

    def get_metadata_dict(self):
        """Return the metadata dict."""
        return self._metadata

    def load(self, config_name: str, config_manager: ConfigManagerProtocol = None):
        """Load the configuration named config_name from the specified config manager."""
        _assert_config_name_is_valid(config_name)

        if config_manager is None:
            config_manager = _get_config_manager()

        config_manager.load_config(config_name, self)
        self.config_name = config_name

        return self

    def save_as(self, new_config_name: str, config_manager: ConfigManagerProtocol = None):
        """Save this configuration as new_config_name with the specified config manager."""
        _assert_config_name_is_valid(new_config_name)

        if config_manager is None:
            config_manager = _get_config_manager()

        config_manager.save_config(self, new_config_name)

        return self

    def save(self, config_manager: ConfigManagerProtocol = None):
        """Save this configuration with the specified config manager."""
        self.save_as(self.config_name, config_manager)

        return self

    def add_param(self, param, defaul_value):
        """Add the parameter param to this configuration."""
        self._config_default[param] = defaul_value
        self._config[param] = defaul_value

        return self

    def del_param(self, param):
        """Delete the parameter param from this configuration."""
        _assert_param_in_config(param, self)

        self._config_default.pop(param)
        self._config.pop(param)

        return self

    def set_default(self, param, default_value):
        """Set the default value of a given parameter."""
        _assert_param_in_config(param, self)

        self._config_default[param] = default_value

        return self

    def get_default(self, param):
        """Return the default value of a given parameter."""
        _assert_param_in_config(param, self)

        return self._config_default[param]

    def set_value(self, param, value):
        """Set the value of a given parameter."""
        _assert_param_in_config(param, self)

        self._config[param] = value

        return self

    def get_value(self, param):
        """Return the value of a given parameter."""
        _assert_param_in_config(param, self)

        return self._config[param]

    def restore_default(self, param):
        """Restore the default value of a given parameter."""
        self.set_value(param, self.get_default(param))

        return self

    def get_param_list(self):
        """Return the list containing every parameter in this configuration."""
        return list(self._config)
