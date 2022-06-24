#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Define a protocol to use configurations.
"""

from typing import Protocol

class ConfigProtocol(Protocol):
    """Configuration protocol for WLBB."""

    def set_config_dict(self, new_config):
        """Set the config dict to new_config."""

    def set_config_default_dict(self, new_config_default):
        """Set the config default dict to new_config_default."""

    def set_metadata_dict(self, new_metadata):
        """Set the metadata dict to new_metadata."""

    def get_config_dict(self):
        """Return the config dict."""

    def get_config_default_dict(self):
        """Return the config default dict."""

    def get_metadata_dict(self):
        """Return the metadata dict."""

    def load(self, config_name: str, config_manager=None):
        """Load the configuration named config_name from the specified config manager."""

    def save_as(self, new_config_name: str, config_manager=None):
        """Save this configuration as new_config_name with the specified config manager."""

    def save(self, config_manager=None):
        """Save this configuration with the specified config manager."""

    def add_param(self, param, defaul_value):
        """Add the parameter param to this configuration."""

    def del_param(self, param):
        """Delete the parameter param from this configuration."""

    def set_default(self, param, default_value):
        """Set the default value of a given parameter."""

    def get_default(self, param):
        """Return the default value of a given parameter."""

    def set_value(self, param, value):
        """Set the value of a given parameter."""

    def get_value(self, param):
        """Return the value of a given parameter."""

    def restore_default(self, param):
        """Restore the default value of a given parameter."""

    def get_param_list(self):
        """Return the list containing every parameter in this configuration."""
