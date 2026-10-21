from pathlib import Path

import pytest

from UnitTests.TestModel.OtlmowModel.Classes.Onderdeel.AllCasesTestClass import AllCasesTestClass
from UnitTests.TestModel.OtlmowModel.Classes.Onderdeel.AnotherTestClass import AnotherTestClass
from UnitTests.TestModel.OtlmowModel.Classes.Onderdeel.Bevestiging import Bevestiging
from UnitTests.TestModel.OtlmowModel.Classes.Onderdeel.Voedt import Voedt
from otlmow_model.OtlmowModel.BaseClasses.RelationInteractor import RelationInteractor
from otlmow_model.OtlmowModel.Classes.Agent import Agent
from otlmow_model.OtlmowModel.Exceptions.RelationDeprecationWarning import RelationDeprecationWarning
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie
from otlmow_model.OtlmowModel.Helpers.RelationValidator import is_valid_relation_instance, is_valid_relation, \
    is_valid_relation_using_relation_uri

model_directory = Path(__file__).parent.parent / 'TestModel'


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


class SubAnotherTestClass(AnotherTestClass):
    """A subclass of AnotherTestClass with its own typeURI.

    Used to exercise the "the target type is not listed, but one of its base
    classes is" branch of the relation validator.
    """

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SubAnotherTestClass'


class SubAllCasesTestClass(AllCasesTestClass):
    """A subclass of AllCasesTestClass with its own typeURI."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SubAllCasesTestClass'


def test_bug_relation_in_two_directions():
    all_cases = AllCasesTestClass()
    another = AnotherTestClass()
    all_cases._valid_relations['https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt'][
         'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AnotherTestClass']['i'] = ''
    another._valid_relations['https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt'][
         'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass']['o'] = ''

    with pytest.warns(RelationDeprecationWarning):
        assert is_valid_relation(source=another, relation_type=Voedt, target=all_cases)
    with pytest.warns(RelationDeprecationWarning):
        assert is_valid_relation(source=all_cases, relation_type=Voedt, target=another)



def test_is_valid_relation():
    all_cases = AllCasesTestClass()
    another = AnotherTestClass()
    assert is_valid_relation_instance(source=another, relation_instance=Bevestiging(), target=all_cases)
    assert is_valid_relation(source=another, relation_type=Bevestiging, target=all_cases)
    with pytest.warns(RelationDeprecationWarning):
        assert is_valid_relation(source=all_cases, relation_type=Voedt, target=another)
    assert not is_valid_relation(source=another, relation_type=Voedt, target=all_cases)
    assert not is_valid_relation(source=all_cases, relation_type=Voedt, target=all_cases)


def test_is_valid_relation_using_relation_uri():
    all_cases = AllCasesTestClass()
    another = AnotherTestClass()
    assert is_valid_relation_using_relation_uri(source=another, relation_uri=Bevestiging.typeURI, target=all_cases)
    with pytest.warns(RelationDeprecationWarning):
        assert is_valid_relation_using_relation_uri(source=all_cases, relation_uri=Voedt.typeURI, target=another)
    assert not is_valid_relation_using_relation_uri(source=another, relation_uri=Voedt.typeURI, target=all_cases)
    assert not is_valid_relation_using_relation_uri(source=all_cases, relation_uri=Voedt.typeURI, target=all_cases)


def test_is_valid_relation_typeURI():
    all_cases = AllCasesTestClass()
    another = AnotherTestClass()
    with pytest.warns(RelationDeprecationWarning):
        result_validation = is_valid_relation(source_typeURI=all_cases.typeURI, relation_type=Voedt,
                                              target_typeURI=another.typeURI, model_directory=model_directory)
    assert result_validation


def test_nieuwe_implementatie_relaties_deprecated():
    all_cases = AllCasesTestClass()
    another = AnotherTestClass()
    with pytest.warns(RelationDeprecationWarning):
        result_validation = is_valid_relation(source=all_cases, relation_type=Voedt, target=another)
    assert result_validation


def test_add_valid_relation_check_if_exists():
    b = B()
    assert len(b._valid_relations[''].keys()) == 2


def test_is_valid_relation_using_relation_uri_requires_a_source():
    with pytest.raises(ValueError, match='Exactly one of source or source_typeURI'):
        is_valid_relation_using_relation_uri(
            relation_uri=Bevestiging.typeURI, target=AnotherTestClass())


def test_is_valid_relation_using_relation_uri_requires_a_target():
    with pytest.raises(ValueError, match='Exactly one of target or target_typeURI'):
        is_valid_relation_using_relation_uri(
            relation_uri=Bevestiging.typeURI, source=AnotherTestClass())


def test_is_valid_relation_using_relation_uri_overrides_source_by_source_typeURI():
    all_cases = AllCasesTestClass()
    another = AnotherTestClass()
    with pytest.warns(RuntimeWarning, match='both source and source_typeURI are not None'):
        assert is_valid_relation_using_relation_uri(
            relation_uri=Bevestiging.typeURI,
            source=another,
            source_typeURI=all_cases.typeURI,
            target=another,
            model_directory=model_directory)


def test_is_valid_relation_using_relation_uri_overrides_target_by_target_typeURI():
    all_cases = AllCasesTestClass()
    another = AnotherTestClass()
    with pytest.warns(RuntimeWarning, match='both target and target_typeURI are not None'):
        assert is_valid_relation_using_relation_uri(
            relation_uri=Bevestiging.typeURI,
            source=all_cases,
            target=all_cases,
            target_typeURI=another.typeURI,
            model_directory=model_directory)


def test_is_valid_relation_using_relation_uri_accepts_lgc_namespaces():
    assert is_valid_relation_using_relation_uri(
        relation_uri=Bevestiging.typeURI,
        source_typeURI='lgc.something',
        target_typeURI='lgc.somethingelse')
    assert is_valid_relation_using_relation_uri(
        relation_uri=Bevestiging.typeURI,
        source_typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass',
        target_typeURI='lgc.somethingelse')


def test_is_valid_relation_using_relation_uri_with_unknown_relation():
    all_cases = AllCasesTestClass()
    another = AnotherTestClass()
    assert not is_valid_relation_using_relation_uri(
        relation_uri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DoesNotExist',
        source=all_cases,
        target=another)


def test_is_valid_relation_using_relation_uri_matches_a_base_class_of_the_target():
    all_cases = AllCasesTestClass()
    sub_another = SubAnotherTestClass()
    assert is_valid_relation_using_relation_uri(
        relation_uri=Bevestiging.typeURI, source=all_cases, target=sub_another)


def test_is_valid_relation_using_relation_uri_base_class_of_target_can_be_incoming_only():
    another = AnotherTestClass()
    sub_all_cases = SubAllCasesTestClass()
    assert not is_valid_relation_using_relation_uri(
        relation_uri=Voedt.typeURI, source=another, target=sub_all_cases)


def test_is_valid_relation_using_relation_uri_base_class_of_target_can_be_deprecated():
    all_cases = AllCasesTestClass()
    sub_another = SubAnotherTestClass()
    with pytest.warns(RelationDeprecationWarning):
        assert is_valid_relation_using_relation_uri(
            relation_uri=Voedt.typeURI, source=all_cases, target=sub_another)


def test_is_valid_relation_using_relation_uri_instantiates_the_target_when_only_a_typeURI_is_given():
    agent = Agent()
    # Baanlichaam is a concrete subclass of the abstract AIMObject, which is the
    # target type that Agent declares for the HeeftBetrokkene relation.
    assert not is_valid_relation_using_relation_uri(
        relation_uri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftBetrokkene',
        source=agent,
        target_typeURI='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Baanlichaam')


