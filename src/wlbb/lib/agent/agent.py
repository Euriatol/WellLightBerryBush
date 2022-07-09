#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Define the abstraction of a WLBB agent whose instances are WLBB instances.
"""

import re
from enum import Enum
from abc import ABC, abstractmethod
from typing import List

from wlbb.lib.logger import WLBBLogger
from wlbb.lib.config.wlbb_config import ConfigLoader
from wlbb.lib.config.default import BuiltinDefaultConfigLoader
from wlbb.lib.config.wlbb_config import WLBBConfig


def assert_name_is_valid(name):
    """
    Raise a value error if the given name is invalid.
    """
    if not 3 <= len(name) <= 20:
        raise ValueError("Agent's name length must be between 3 and 20.")

    pattern = "[a-z_0-9]*"
    if not re.fullmatch(pattern, name):
        raise ValueError(
            "Agent's name must only contain minuscule letters, "
            + "digits and underscores."
        )


class Status(Enum):
    """
    Status in which a WLBB agent can be.
    """

    INACTIVE = 0
    ACTIVE = 1


class WLBBAgent(ABC):
    """
    Abstract definition of a WLBB Agent.
    """

    agent: str
    name: str
    agent_id: str

    config_sections: List[str]

    status: Status = Status.INACTIVE

    def __init__(self, name: str):
        assert_name_is_valid(name)
        self.name = name
        self.agent_id = "{agent}-{name}".format(agent=self.agent, name=self.name)

    @abstractmethod
    def init(self):
        """
        Initialize the agent.
        """

    @abstractmethod
    def start(self):
        """
        Start the agent's operation.
        """

    @abstractmethod
    def stop(self):
        """
        Stop the agent's operation.
        """

    @abstractmethod
    def quit(self):
        """
        Uninitialize the agent.
        """

    @abstractmethod
    def restart(self):
        """
        Restart the agent's operation.
        """

    @abstractmethod
    def reload(self):
        """
        Reload the agent.
        """

    # Setters
    def set_config(self, cfg: WLBBConfig):
        """
        Change the config.
        """
        self.config = cfg

    def set_config_loader(self, cfg_loader: ConfigLoader):
        """
        Change the config loader.
        """
        self.config_loader = cfg_loader

    # Getters
    def get_config_sections_list(self):
        """
        Return a list containing every config section required for this agent.
        """
        return self.config_sections

    def get_config(self):
        """
        Return the config.
        """
        return self.config

    def get_config_loader(self):
        """
        Return the config loader.
        """
        return self.config_loader
