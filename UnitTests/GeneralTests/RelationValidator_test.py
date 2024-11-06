import pytest

from UnitTests.TestModel.OtlmowModel.Classes.Onderdeel.AllCasesTestClass import AllCasesTestClass
from UnitTests.TestModel.OtlmowModel.Classes.Onderdeel.AnotherTestClass import AnotherTestClass
from otlmow_model.OtlmowModel.BaseClasses.RelationInteractor import RelationInteractor
from otlmow_model.OtlmowModel.Classes.Onderdeel.Bevestiging import Bevestiging
from otlmow_model.OtlmowModel.Classes.Onderdeel.Laagspanningsbord import Laagspanningsbord
from otlmow_model.OtlmowModel.Classes.Onderdeel.Stroomkring import Stroomkring
from otlmow_model.OtlmowModel.Classes.Onderdeel.Voedt import Voedt
from otlmow_model.OtlmowModel.Exceptions.RelationDeprecationWarning import RelationDeprecationWarning
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie
from otlmow_model.OtlmowModel.Helpers.RelationValidator import is_valid_relation_instance, is_valid_relation


class A(RelationInteractor):
    def __init__(self):
        super().__init__()
        self.add_valid_relation('', 'D')


class C(PuntGeometrie):
    def __init__(self):
        super().__init__()


class B(A, C):
    def __init__(self):
        super().__init__()
        self.add_valid_relation('', 'E')


def test_is_valid_relation():
    all_cases = AllCasesTestClass()
    another = AnotherTestClass()
    assert is_valid_relation_instance(source=another, relation_instance=Bevestiging(), target=all_cases)
    assert is_valid_relation(source=another, relation_type=Bevestiging, target=all_cases)
    with pytest.warns(DeprecationWarning):
        assert is_valid_relation(source=all_cases, relation_type=Voedt, target=another)
    assert not is_valid_relation(source=another, relation_type=Voedt, target=all_cases)
    assert not is_valid_relation(source=all_cases, relation_type=Voedt, target=all_cases)


def test_is_valid_relation_typeURI():
    stroomkring = Stroomkring()
    laagspanningsbord = Laagspanningsbord()
    assert is_valid_relation(source_typeURI=stroomkring.typeURI, relation_type=Bevestiging,
                             target_typeURI=laagspanningsbord.typeURI)


def test_nieuwe_implementatie_relaties_deprecated():
    all_cases = AllCasesTestClass()
    another = AnotherTestClass()
    with pytest.warns(RelationDeprecationWarning):
        result_validation = is_valid_relation(source=all_cases, relation_type=Voedt, target=another)
    assert result_validation


def test_add_valid_relation_check_if_exists():
    b = B()
    assert len(b._valid_relations[''].keys()) == 2
