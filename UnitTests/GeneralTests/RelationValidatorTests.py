import unittest

from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie

from otlmow_model.BaseClasses.RelationInteractor import RelationInteractor

from UnitTests.TestClasses.Classes.Onderdeel.AllCasesTestClass import AllCasesTestClass
from UnitTests.TestClasses.Classes.Onderdeel.AnotherTestClass import AnotherTestClass
from otlmow_model.Classes.Onderdeel.Bevestiging import Bevestiging
from otlmow_model.Classes.Onderdeel.Voedt import Voedt
from otlmow_model.Exceptions.RelationDeprecationWarning import RelationDeprecationWarning
from otlmow_model.Helpers.RelationValidator import RelationValidator


class A(RelationInteractor):
    def __init__(self):
        super().__init__()
        self.add_valid_relation('', 'A')


class C(PuntGeometrie):
    def __init__(self):
        super().__init__()


class B(A, C):
    def __init__(self):
        super().__init__()
        self.add_valid_relation('', 'B')


class RelationValidatorTests(unittest.TestCase):
    def test_nieuwe_implementatie_relaties(self):
        all_cases = AllCasesTestClass()
        another = AnotherTestClass()
        self.assertTrue(RelationValidator.is_valid_relation_instance(source=another, relation_instance=Bevestiging(),
                                                                     target=all_cases))
        self.assertTrue(RelationValidator.is_valid_relation(source=another, relation_type=Bevestiging, target=all_cases))
        self.assertFalse(RelationValidator.is_valid_relation(source=another, relation_type=Voedt, target=all_cases))
        self.assertFalse(RelationValidator.is_valid_relation(source=all_cases, relation_type=Voedt, target=all_cases))

    def test_nieuwe_implementatie_relaties_deprecated(self):
        all_cases = AllCasesTestClass()
        another = AnotherTestClass()
        with self.assertWarns(RelationDeprecationWarning):
            result_validation = RelationValidator.is_valid_relation(source=all_cases, relation_type=Voedt, target=another)
        self.assertTrue(result_validation)

    def test_add_valid_relation_check_if_exists(self):
        b = B()
        self.assertEqual(2, len(b._valid_relations[''].keys()))



