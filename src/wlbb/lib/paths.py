#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Some useful paths and utils to create file and directories.
"""

import os
import sys


def create_dir(path):
    os.makedirs(path, mode=0o622, exist_ok=True)


def create_file(path):
    if not os.path.isfile(path):
        os.mknod(path, mode=0o622)


def delete_file(path):
    if os.path.isfile(path):
        os.remove(path)


# def _xdg_get_config_path():
#    """
#    Return the base directory relative for user-specific configuration.
#    (According to XDG Base Directory Specification version 0.8 available here:
#        https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html)
#    """
#    if "XDG_CONFIG_HOME" in os.environ:
#        if os.environ["XDG_CONFIG_HOME"]:
#            return os.environ["XDG_CONFIG_HOME"]
#    return os.path.join(os.environ["HOME"], ".config")
#
#
# def _xdg_get_data_path():
#    """
#    Return the base directory relative for user-specific data.
#    (According to XDG Base Directory Specification version 0.8 available here:
#        https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html)
#    """
#    if "XDG_DATA_HOME" in os.environ:
#        if os.environ["XDG_DATA_HOME"]:
#            return os.environ["XDG_DATA_HOME"]
#    return os.path.join(os.environ["HOME"], ".local", "share")
#
#
# def _xdg_get_cache_path():
#    """
#    Return the base directory relative for user-specific cache.
#    (According to XDG Base Directory Specification version 0.8 available here:
#        https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html)
#    """
#    if "XDG_CACHE_HOME" in os.environ:
#        if os.environ["XDG_CACHE_HOME"]:
#            return os.environ["XDG_CACHE_HOME"]
#    return os.path.join(os.environ["HOME"], ".cache")


def get_data_path():
    """
    Return the data path.
    """
    if sys.platform == "linux":
        return "{HOME}/.wlbb".format(**os.environ)
    if sys.platform == "win32":
        # Maybe something in APP DATA
        raise NotImplementedError("Data dir path isn't yet implemented for Windows.")
    if sys.platform == "darwin":
        raise NotImplementedError("Data dir path isn't yet implemented for MacOS.")


def get_config_dir():
    """
    Return the path of the directory which should contain the other
    configuration files.
    """
    return os.path.join(get_data_path(), "configs")


def get_log_dir():
    """
    Return the path of the directory which should contain the logs.
    """
    return os.path.join(get_data_path(), "logs")
