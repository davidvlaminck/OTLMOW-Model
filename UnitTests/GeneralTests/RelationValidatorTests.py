import unittest

from UnitTests.TestClasses.Classes.Onderdeel.AllCasesTestClass import AllCasesTestClass
from UnitTests.TestClasses.Classes.Onderdeel.AnotherTestClass import AnotherTestClass
from otlmow_model.Classes.Onderdeel.Bevestiging import Bevestiging
from otlmow_model.Classes.Onderdeel.Voedt import Voedt
from otlmow_model.Exceptions.RelationDeprecationWarning import RelationDeprecationWarning
from otlmow_model.Helpers.RelationValidator import RelationValidator


class RelationValidatorTests(unittest.TestCase):
    def test_nieuwe_implementatie_relaties(self):
        all_cases = AllCasesTestClass()
        another = AnotherTestClass()
        self.assertTrue(RelationValidator.is_valid_relation_instance(source=another, relation_instance=Bevestiging(),
                                                             target=all_cases))
        self.assertTrue(RelationValidator.is_valid_relation(source=another, relation=Bevestiging, target=all_cases))
        self.assertFalse(RelationValidator.is_valid_relation(source=another, relation=Voedt, target=all_cases))
        self.assertFalse(RelationValidator.is_valid_relation(source=all_cases, relation=Voedt, target=all_cases))

    def test_nieuwe_implementatie_relaties_deprecated(self):
        all_cases = AllCasesTestClass()
        another = AnotherTestClass()
        with self.assertWarns(RelationDeprecationWarning):
            result_validation = RelationValidator.is_valid_relation(source=all_cases, relation=Voedt, target=another)
        self.assertTrue(result_validation)
