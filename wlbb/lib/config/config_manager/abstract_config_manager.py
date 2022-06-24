#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Define a protocol to load and save configurations.
"""

from typing import Protocol

from wlbb.lib.config.abstract_config import ConfigProtocol

class ConfigManagerProtocol(Protocol):
    """Protocol to load and save configurations."""
    def load_config(self, config_name: str, config: ConfigProtocol):
        """Load the requested configuration into config."""

    def save_config(self, config: ConfigProtocol, config_name: str):
        """Save config as config_name."""

    def list_configs(self):
        """Return the list of all configurations"""
