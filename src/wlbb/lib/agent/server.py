#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
server.py
"""

from wlbb.lib.config import Config
from wlbb.lib.profile import Profile


def get_server_id(server_name: str):
    if server_name:
        return "server_" + server_name
    else:
        return "server"


class WLBBServer:
    def __init__(self, server_name: str = ""):
        self.server_id = get_server_id(server_name)

        self.config = Config()
        self.profile = Profile()

    def init(self):
        pass

    def mainloop(self):
        pass

    def start(self):
        pass

    def stop(self):
        pass

    def restart(self):
        pass

    def get_profile(self):
        pass

    def load_profile(self, new_profile):
        pass

    def reload(self):
        pass
