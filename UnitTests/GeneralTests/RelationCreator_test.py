from pathlib import Path

import pytest

from UnitTests.TestModel.OtlmowModel.Classes.Onderdeel.AllCasesTestClass import AllCasesTestClass
from UnitTests.TestModel.OtlmowModel.Classes.Onderdeel.AnotherTestClass import AnotherTestClass
from UnitTests.TestModel.OtlmowModel.Classes.Onderdeel.Bevestiging import Bevestiging
from UnitTests.TestModel.OtlmowModel.Classes.Onderdeel.Voedt import Voedt
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import dynamic_create_instance_from_ns_and_name
from otlmow_model.OtlmowModel.Classes.Onderdeel.HoortBij import HoortBij
from otlmow_model.OtlmowModel.Exceptions.CouldNotCreateRelationError import CouldNotCreateRelationError
from otlmow_model.OtlmowModel.Exceptions.RelationDeprecationWarning import RelationDeprecationWarning
from otlmow_model.OtlmowModel.Helpers.RelationCreator import create_relation


model_directory_path = Path(__file__).parent.parent / 'TestModel'

def test_create_valid_relation():
    all_cases = AllCasesTestClass()
    all_cases.assetId.identificator = 'all_cases'
    another = AnotherTestClass()
    another.assetId.identificator = 'another'

    relation = create_relation(source=another, target=all_cases, relation_type=Bevestiging)
    assert relation is not None
    assert relation.typeURI == Bevestiging.typeURI
    assert relation.bronAssetId.identificator == another.assetId.identificator
    assert relation.doelAssetId.identificator == all_cases.assetId.identificator
    assert relation.assetId.identificator == 'Bevestiging_-_another_-_all_cases'


def test_create_relation_input_parameters(subtests):
    all_cases = AllCasesTestClass()
    all_cases.assetId.identificator = 'all_cases'
    another = AnotherTestClass()
    another.assetId.identificator = 'another'

    with subtests.test(msg='testing if there are enough not None parameters'):
        with pytest.raises(ValueError):
            create_relation(source=None, source_typeURI=None, source_uuid='', target=all_cases,
                            relation_type=Bevestiging,
                            model_directory=model_directory_path)
        with pytest.raises(ValueError):
            create_relation(source=None, source_typeURI='', source_uuid=None, target=all_cases,
                            relation_type=Bevestiging,
                            model_directory=model_directory_path)
        with pytest.raises(ValueError):
            create_relation(target=None, target_typeURI=None, target_uuid='', source=all_cases,
                            relation_type=Bevestiging,
                            model_directory=model_directory_path)
        with pytest.raises(ValueError):
            create_relation(target=None, target_typeURI='', target_uuid=None, source=all_cases,
                            relation_type=Bevestiging,
                            model_directory=model_directory_path)

    with subtests.test(msg='testing uuid format'):
        relation = create_relation(source_typeURI=another.typeURI, target=all_cases,
                                   source_uuid='00000000-0000-0000-0000-000000000000',
                                   relation_type=Bevestiging, model_directory=model_directory_path)
        assert relation is not None

        relation = create_relation(target_typeURI=another.typeURI, source=all_cases,
                                   target_uuid='00000000-0000-0000-0000-000000000000',
                                   relation_type=Bevestiging, model_directory=model_directory_path)
        assert relation is not None

        with pytest.raises(ValueError):
            create_relation(source_typeURI=another.typeURI, source_uuid='', target=all_cases,
                            relation_type=Bevestiging, model_directory=model_directory_path)

        with pytest.raises(ValueError):
            create_relation(target_typeURI=another.typeURI, target_uuid='', source=all_cases,
                            relation_type=Bevestiging, model_directory=model_directory_path)

    with subtests.test(msg='testing for warning if there are too many not None parameters'):
        with pytest.warns(RuntimeWarning):
            create_relation(source=another, source_typeURI=another.typeURI, source_uuid='', target=all_cases,
                            relation_type=Bevestiging,
                            model_directory=model_directory_path)
        with pytest.warns(RuntimeWarning):
            create_relation(source=another, target=all_cases, target_typeURI=all_cases.typeURI,
                            relation_type=Bevestiging)

    with subtests.test(msg='creating relations using uuid and typeURI'):
        relation = create_relation(source_typeURI=another.typeURI, source_uuid='00000000-0000-0000-0000-000000000000',
                                   target=all_cases, relation_type=Bevestiging,
                                   model_directory=model_directory_path)
        assert relation is not None
        assert relation.typeURI == Bevestiging.typeURI
        assert relation.bronAssetId.identificator == '00000000-0000-0000-0000-000000000000' \
                                                     '-b25kZXJkZWVsI0Fub3RoZXJUZXN0Q2xhc3M'
        assert relation.doelAssetId.identificator == all_cases.assetId.identificator

        relation = create_relation(target_typeURI=another.typeURI, target_uuid='00000000-0000-0000-0000-000000000000',
                                   source=all_cases, relation_type=Bevestiging,
                                   model_directory=model_directory_path)
        assert relation is not None
        assert relation.typeURI == Bevestiging.typeURI
        assert relation.doelAssetId.identificator == '00000000-0000-0000-0000-000000000000' \
                                                     '-b25kZXJkZWVsI0Fub3RoZXJUZXN0Q2xhc3M'
        assert relation.bronAssetId.identificator == all_cases.assetId.identificator

    with subtests.test(msg='creating relations using instances of objects'):
        relation = create_relation(source=another, target=all_cases, relation_type=Bevestiging,
                                   model_directory=model_directory_path)
        assert relation is not None
        assert relation.typeURI == Bevestiging.typeURI
        assert relation.bronAssetId.identificator == another.assetId.identificator
        assert relation.doelAssetId.identificator == all_cases.assetId.identificator
        assert relation.assetId.identificator == 'Bevestiging_-_another_-_all_cases'

    with subtests.test(msg='real test'):
        kast = dynamic_create_instance_from_ns_and_name(namespace='onderdeel', class_name='Wegkantkast')
        uuid: str = '847a91b3-569d-4bae-87bf-7e148e8f7de9'
        typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#Beheersys'
        kast.assetId.identificator = '0000'

        relation = create_relation(source=kast, target_uuid=uuid, target_typeURI=typeURI,
                                   relation_type=HoortBij)
        assert relation is not None
        assert relation.doelAssetId.identificator == '847a91b3-569d-4bae-87bf-7e148e8f7de9-bGdjOmluc3RhbGxhdGllI0JlaGVlcnN5cw'
        assert relation.assetId.identificator == 'HoortBij_-_0000_-_847a91b3-569d-4bae-87bf-7e148e8f7de9-bGdjOmluc3RhbGxhdGllI0JlaGVlcnN5cw'


def test_create_invalid_relation():
    all_cases = AllCasesTestClass()
    all_cases.assetId.identificator = 'all_cases'
    another = AnotherTestClass()
    another.assetId.identificator = 'another'

    with pytest.raises(CouldNotCreateRelationError):
        create_relation(source=another, target=all_cases, relation_type=Voedt)


def test_create_deprecated_relation():
    all_cases = AllCasesTestClass()
    all_cases.assetId.identificator = 'all_cases'
    another = AnotherTestClass()
    another.assetId.identificator = 'another'

    with pytest.warns(RelationDeprecationWarning):
        relation = create_relation(source=all_cases, target=another, relation_type=Voedt)

    assert relation is not None


def test_create_valid_relation_without_assetIds():
    all_cases = AllCasesTestClass()
    another = AnotherTestClass()

    with pytest.raises(AttributeError):
        create_relation(source=another, target=all_cases, relation_type=Bevestiging)
