import warnings
from unittest import TestCase

from UnitTests.TestClasses.Classes.Onderdeel.AnotherTestClass import AnotherTestClass
from UnitTests.TestClasses.Classes.Onderdeel.DeprecatedTestClass import DeprecatedTestClass
from UnitTests.TestClasses.Classes.Onderdeel.Voedt import Voedt
from otlmow_model.Exceptions.AttributeDeprecationWarning import AttributeDeprecationWarning
from otlmow_model.Exceptions.ClassDeprecationWarning import ClassDeprecationWarning


class DeprecatedTests(TestCase):
    def test_use_regular_class(self):
        instance = AnotherTestClass()
        if hasattr(instance, 'deprecated_version'):
            self.assertIsNone(instance.deprecated_version)
        else:
            self.assertTrue(True)

    def test_use_deprecated_class(self):
        with self.assertWarns(ClassDeprecationWarning):
            DeprecatedTestClass()

    def test_use_regular_attribute(self):
        with warnings.catch_warnings(record=True) as warns:
            v = Voedt()
            v.aansluitspanning.waarde = 230
        deprecated = list(filter(lambda x: isinstance(x, DeprecationWarning), warns))
        self.assertEqual(0, len(deprecated))

    def test_use_deprecated_attribute(self):
        with self.assertWarns(AttributeDeprecationWarning):
            v = Voedt()
            v.aansluitvermogen.waarde = 20
