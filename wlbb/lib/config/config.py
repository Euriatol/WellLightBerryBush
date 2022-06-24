#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
config.py
"""

from config_manager import get_config_manager as _get_config_manager

class NotAParameterError(ValueError):
    pass

def _assert_param_in_config(param, config):
    if param not in config._config:
        raise NotAParameterError("%a isn't a parameter."%param)

class Config:
    def __init__(self):
        self.config_name = None
        self._config_default = {}
        self._config = {}
    
    def load(self, config_name, config_manager=None):
        if config_manager is None:
            config_manager = _get_config_manager()
        
        config_manager.load(config_name, self)
        self.config_name = config_name
        
        return self
    
    def save_as(self, new_config_name, config_manager=None):
        if config_manager is None:
            config_manager = _get_config_manager()
        
        config_manager.save(self, new_config_name)
        
        return self
    
    def save(self, config_manager=None):
        self.save_as(self.config_name, config_manager)
        
        return self
    
    def add_param(self, param, defaul_value):
        self._config_default[param] = defaul_value
        self._config[param] = defaul_value
        
        return self
    
    def del_param(self, param):
        _assert_param_in_config(param, self)
        
        self._config_default.pop(param)
        self._config.pop(param)
        
        return self
    
    def set_default(self, param, default_value):
        _assert_param_in_config(param, self)
        
        self._config_default[param] = default_value
        
        return self
    
    def get_default(self, param):
        _assert_param_in_config(param, self)
        
        return self._config_default[param]
    
    def set_value(self, param, value):
        _assert_param_in_config(param, self)
        
        self._config[param] = value
        
        return self
    
    def get_value(self, param):
        _assert_param_in_config(param, self)
        
        return self._config[param]
    
    def restore_default(self, param):
        self.set_value(param, self.get_default(param))
        
        return self