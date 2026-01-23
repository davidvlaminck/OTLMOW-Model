import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import warnings

import pytest

from UnitTests.TestModel.OtlmowModel.Classes.Onderdeel.AnotherTestClass import AnotherTestClass
from UnitTests.TestModel.OtlmowModel.Classes.Onderdeel.DeprecatedTestClass import DeprecatedTestClass
from otlmow_model.OtlmowModel.Exceptions.AttributeDeprecationWarning import AttributeDeprecationWarning
from otlmow_model.OtlmowModel.Exceptions.ClassDeprecationWarning import ClassDeprecationWarning
from UnitTests.TestModel.OtlmowModel.Classes.Onderdeel.Voedt import Voedt


def test_use_regular_class():
    instance = AnotherTestClass()
    if hasattr(instance, 'deprecated_version'):
        assert instance.deprecated_version is None
    else:
        assert True


def test_use_deprecated_class():
    with pytest.warns(ClassDeprecationWarning):
        DeprecatedTestClass()


def test_use_regular_attribute():
    with warnings.catch_warnings(record=True) as warns:
        v = Voedt()
        v.aansluitspanning.waarde = 230
    deprecated = list(filter(lambda x: isinstance(x, DeprecationWarning), warns))
    assert len(deprecated) == 0


def test_use_deprecated_attribute():
    with pytest.warns(AttributeDeprecationWarning):
        v = Voedt()
        v.aansluitvermogen.waarde = 20
