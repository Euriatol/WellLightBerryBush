#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Default config related module.
"""

from os import PathLike

from importlib_resources import files

from wlbb.lib.config.cfg_config_loader import CfgConfigLoader

__all__ = (
    "DEFAULT_CFG_NAME",
    "BuiltinDefaultConfigLoader",
    "get_builtin_default_config_dir",
)

DEFAULT_CFG_NAME = "default_config"
BuiltinDefaultConfigLoader = CfgConfigLoader


def get_builtin_default_config_dir() -> PathLike:
    return files("wlbb").joinpath("data")
