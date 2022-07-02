#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test the WLBB's configuration interface.
"""

from wlbb.lib.config import WLBBConfig

# from wlbb.lib.config import WLBBParameterGroup

from wlbb.lib.paths import get_config_dir, get_default_config_dir
from wlbb.lib.config.default import DEFAULT_CFG_NAME

from . import WLBBDummyAgent
from . import TestingConfigLoader

TEST_DICT_DEFAULT = {
    "PARAM_GROUP1": {"parameter1": -1, "parameter2": -2},
    "PARAM_GROUP2": {"parameter3": -3, "parameter4": -4},
    "PARAM_GROUP3": {"parameter5": -5, "parameter6": -6},
}

#%% Testing import dict


def test_import_dict_simple():
    """
    Check if the method import_config work as expected when the test dict is a
    comptible config dict. ()
    """
    test_dict = {
        "PARAM_GROUP1": {"parameter1": 1, "parameter2": 2},
        "PARAM_GROUP2": {"parameter3": 3, "parameter4": 4},
    }
    test_dict_expected = test_dict.copy()

    test_config_loader = TestingConfigLoader(
        {get_default_config_dir(): {DEFAULT_CFG_NAME: TEST_DICT_DEFAULT.copy()}}
    )

    agent = WLBBDummyAgent("test_agent")
    agent.set_config_loader(test_config_loader)
    test_config = WLBBConfig(agent)

    test_config.import_dict(test_dict)
    assert (
        test_config.get_config_dict() == test_dict_expected
    ), "Testing WLBBConfig.import_config simple case failed."


def test_import_dict_missing_one():
    """
    Check if the method import_config work as expected when the test dict is a
    comptible config dict with a missing param group.
    """
    test_dict = {"PARAM_GROUP1": {"parameter1": 1, "parameter2": 2}}
    test_dict_expected = {
        "PARAM_GROUP1": {"parameter1": 1, "parameter2": 2},
        "PARAM_GROUP2": {"parameter3": -3, "parameter4": -4},
    }

    test_config_loader = TestingConfigLoader(
        {get_default_config_dir(): {DEFAULT_CFG_NAME: TEST_DICT_DEFAULT.copy()}}
    )

    agent = WLBBDummyAgent("test_agent")
    agent.set_config_loader(test_config_loader)
    test_config = WLBBConfig(agent)

    test_config.import_dict(test_dict)
    assert (
        test_config.get_config_dict() == test_dict_expected
    ), "Testing WLBBConfig.import_config missing one failed."


def test_import_dict_one_extra():
    """
    Check if the method import_config work as expected when the test dict is a
    comptible config dict with a extra param group.
    """
    test_dict = {
        "PARAM_GROUP1": {"parameter1": 1, "parameter2": 2},
        "PARAM_GROUP2": {"parameter3": 3, "parameter4": 4},
        "PARAM_GROUP3": {"parameter5": -5, "parameter6": -6},
    }
    test_dict_expected = {
        "PARAM_GROUP1": {"parameter1": 1, "parameter2": 2},
        "PARAM_GROUP2": {"parameter3": 3, "parameter4": 4},
    }

    test_config_loader = TestingConfigLoader(
        {get_default_config_dir(): {DEFAULT_CFG_NAME: TEST_DICT_DEFAULT.copy()}}
    )

    agent = WLBBDummyAgent("test_agent")
    agent.set_config_loader(test_config_loader)
    test_config = WLBBConfig(agent)

    test_config.import_dict(test_dict)
    assert (
        test_config.get_config_dict() == test_dict_expected
    ), "Testing WLBBConfig.import_config one extra failed."


def test_import_dict_missing_all():
    """
    Check if the method import_dict work as expected when the test dict is a
    comptible config dict with a missing param group.
    """
    test_dict = {}
    test_dict_expected = {
        "PARAM_GROUP1": {"parameter1": -1, "parameter2": -2},
        "PARAM_GROUP2": {"parameter3": -3, "parameter4": -4},
    }

    test_config_loader = TestingConfigLoader(
        {get_default_config_dir(): {DEFAULT_CFG_NAME: TEST_DICT_DEFAULT.copy()}}
    )

    agent = WLBBDummyAgent("test_agent")
    agent.set_config_loader(test_config_loader)
    test_config = WLBBConfig(agent)

    test_config.import_dict(test_dict)
    assert (
        test_config.get_config_dict() == test_dict_expected
    ), "Testing WLBBConfig.import_config missing all failed."


def test_import_dict_incompatible():
    """
    Check if the method import_dict work as expected when the test dict is a
    incomptible config dict. ()
    """
    test_dict = {
        "PARAM_GROUP3": {"parameter1": 1, "parameter2": 2},
        "PARAM_GROUP4": {"parameter3": 3, "parameter4": 4},
    }
    test_dict_expected = {
        "PARAM_GROUP1": {"parameter1": -1, "parameter2": -2},
        "PARAM_GROUP2": {"parameter3": -3, "parameter4": -4},
    }

    test_config_loader = TestingConfigLoader(
        {get_default_config_dir(): {DEFAULT_CFG_NAME: TEST_DICT_DEFAULT.copy()}}
    )

    agent = WLBBDummyAgent("test_agent")
    agent.set_config_loader(test_config_loader)
    test_config = WLBBConfig(agent)

    test_config.import_dict(test_dict)
    assert (
        test_config.get_config_dict() == test_dict_expected
    ), "Testing WLBBConfig.import_dict incompatible case failed."


#%% Testing import config


def test_import_config_simple():
    """
    Check if the method import_config work as expected when the test dict is a
    comptible config dict. ()
    """
    test_dict = {
        "PARAM_GROUP1": {"parameter1": 1, "parameter2": 2},
        "PARAM_GROUP2": {"parameter3": 3, "parameter4": 4},
    }
    test_dict_expected = test_dict.copy()

    test_config_loader = TestingConfigLoader(
        {
            get_config_dir(): {"test": test_dict},
            get_default_config_dir(): {DEFAULT_CFG_NAME: TEST_DICT_DEFAULT.copy()},
        }
    )

    test_config = WLBBConfig(WLBBDummyAgent("test_agent"))

    test_config.import_config("test", cfg_loader=test_config_loader)
    assert (
        test_config.get_config_dict() == test_dict_expected
    ), "Testing WLBBConfig.import_config simple case failed."


def test_import_config_missing_one():
    """
    Check if the method import_config work as expected when the test dict is a
    comptible config dict with a missing param group.
    """
    test_dict = {"PARAM_GROUP1": {"parameter1": 1, "parameter2": 2}}
    test_dict_expected = {
        "PARAM_GROUP1": {"parameter1": 1, "parameter2": 2},
        "PARAM_GROUP2": {"parameter3": -3, "parameter4": -4},
    }

    test_config_loader = TestingConfigLoader(
        {
            get_config_dir(): {"test": test_dict},
            get_default_config_dir(): {DEFAULT_CFG_NAME: TEST_DICT_DEFAULT.copy()},
        }
    )

    test_config = WLBBConfig(WLBBDummyAgent("test_agent"))

    test_config.import_config("test", cfg_loader=test_config_loader)
    assert (
        test_config.get_config_dict() == test_dict_expected
    ), "Testing WLBBConfig.import_config missing one failed."


def test_import_config_one_extra():
    """
    Check if the method import_config work as expected when the test dict is a
    comptible config dict with a extra param group.
    """
    test_dict = {
        "PARAM_GROUP1": {"parameter1": 1, "parameter2": 2},
        "PARAM_GROUP2": {"parameter3": 3, "parameter4": 4},
        "PARAM_GROUP3": {"parameter5": -5, "parameter6": -6},
    }
    test_dict_expected = {
        "PARAM_GROUP1": {"parameter1": 1, "parameter2": 2},
        "PARAM_GROUP2": {"parameter3": 3, "parameter4": 4},
    }

    test_config_loader = TestingConfigLoader(
        {
            get_config_dir(): {"test": test_dict},
            get_default_config_dir(): {DEFAULT_CFG_NAME: TEST_DICT_DEFAULT.copy()},
        }
    )

    test_config = WLBBConfig(WLBBDummyAgent("test_agent"))

    test_config.import_config("test", cfg_loader=test_config_loader)
    assert (
        test_config.get_config_dict() == test_dict_expected
    ), "Testing WLBBConfig.import_config one extra failed."


def test_import_config_missing_all():
    """
    Check if the method import_config work as expected when the test dict is a
    comptible config dict with a missing param group.
    """
    test_dict = {}
    test_dict_expected = {
        "PARAM_GROUP1": {"parameter1": -1, "parameter2": -2},
        "PARAM_GROUP2": {"parameter3": -3, "parameter4": -4},
    }

    test_config_loader = TestingConfigLoader(
        {
            get_config_dir(): {"test": test_dict},
            get_default_config_dir(): {DEFAULT_CFG_NAME: TEST_DICT_DEFAULT.copy()},
        }
    )

    test_config = WLBBConfig(WLBBDummyAgent("test_agent"))

    test_config.import_config("test", cfg_loader=test_config_loader)
    assert (
        test_config.get_config_dict() == test_dict_expected
    ), "Testing WLBBConfig.import_config missing all failed."


def test_import_config_incompatible():
    """
    Check if the method import_config work as expected when the test dict is a
    incomptible config dict. ()
    """
    test_dict = {
        "PARAM_GROUP3": {"parameter1": 1, "parameter2": 2},
        "PARAM_GROUP4": {"parameter3": 3, "parameter4": 4},
    }
    test_dict_expected = {
        "PARAM_GROUP1": {"parameter1": -1, "parameter2": -2},
        "PARAM_GROUP2": {"parameter3": -3, "parameter4": -4},
    }

    test_config_loader = TestingConfigLoader(
        {
            get_config_dir(): {"test": test_dict},
            get_default_config_dir(): {DEFAULT_CFG_NAME: TEST_DICT_DEFAULT.copy()},
        }
    )

    test_config = WLBBConfig(WLBBDummyAgent("test_agent"))

    test_config.import_config("test", cfg_loader=test_config_loader)
    assert (
        test_config.get_config_dict() == test_dict_expected
    ), "Testing WLBBConfig.import_config incompatible case failed."
