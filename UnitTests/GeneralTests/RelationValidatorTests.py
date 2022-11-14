import unittest

from UnitTests.TestClasses.Classes.Onderdeel.AllCasesTestClass import AllCasesTestClass
from UnitTests.TestClasses.Classes.Onderdeel.AnotherTestClass import AnotherTestClass
from otlmow_model.Classes.Onderdeel.Bevestiging import Bevestiging
from otlmow_model.Helpers.RelationValidator import RelationValidator


class RelationValidatorTests(unittest.TestCase):
    def test_nieuwe_implementatie_relaties(self):
        all_cases = AllCasesTestClass()
        validator = RelationValidator()
        another = AnotherTestClass()
        self.assertTrue(validator.is_valid_relation_instance(source=another, relation_instance=Bevestiging(),
                                                             target=all_cases))
        self.assertTrue(validator.is_valid_relation(source=another, relation=Bevestiging, target=all_cases))
