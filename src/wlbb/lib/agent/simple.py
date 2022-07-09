#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A simple self-dependent agent.
"""

from wlbb.lib.logger import wlbb_logger

from wlbb.lib.agent.agent import WLBBAgent


class WLBBSimpleAgent(WLBBAgent):
    """
    A simple self-dependent WLBB agent.
    """

    config_sections = ["DEVICES"]

    def init(self):
        pass
