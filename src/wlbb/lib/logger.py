#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
WLBB Logger
"""

from logging import getLogger, DEBUG, INFO, WARNING, ERROR, CRITICAL


class WLBBLogger:
    """
    A interface between a WLBB instance and multiple loggers.
    """

    def __init__(self):
        self.loggers = {"system": getLogger()}

    def add_logger(self, name, new_logger):
        """
        Add a new logger.
        """
        self.loggers[name] = new_logger

    def get_logger(self, name):
        """
        Get a specific logger.
        """
        if name not in self.loggers:
            raise ValueError("Unknown logger name : %a." % name)
        return self.loggers[name]

    def log(self, level, msg, *args, **kwargs):
        """
        Log `msg` at a given level.
        """
        for logger in self.loggers.values():
            logger.log(level, msg, *args, **kwargs)

    def debug(self, msg, *args, **kwargs):
        """
        Log `msg` at the debug level.
        """
        self.log(DEBUG, msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        """
        Log `msg` at the info level.
        """
        self.log(INFO, msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        """
        Log `msg` at the warning level.
        """
        self.log(WARNING, msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        """
        Log `msg` at the error level.
        """
        self.log(ERROR, msg, *args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        """
        Log `msg` at the critical error level.
        """
        self.log(CRITICAL, msg, *args, **kwargs)


wlbb_logger = getLogger()
