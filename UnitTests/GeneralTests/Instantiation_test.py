import concurrent
import logging
import os
from concurrent.futures import ThreadPoolExecutor, ALL_COMPLETED
from pathlib import Path

import pytest

from UnitTests.TestModel.OtlmowModel.Classes.Onderdeel.AnotherTestClass import AnotherTestClass
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import dynamic_create_instance_from_uri, \
    dynamic_create_instance_from_ns_and_name, dynamic_create_type_from_uri, dynamic_create_type_from_ns_and_name
from otlmow_model.OtlmowModel.Exceptions.CouldNotCreateInstanceError import CouldNotCreateInstanceError
from otlmow_model.OtlmowModel.Helpers.generated_lists import get_hardcoded_class_dict

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def test_dynamic_create_instance_from_uri():
    mof = dynamic_create_instance_from_uri('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aansluitmof')
    assert mof is not None

    agent = dynamic_create_instance_from_uri('http://purl.org/dc/terms/Agent')
    assert agent is not None

    with pytest.raises(CouldNotCreateInstanceError):
        dynamic_create_instance_from_uri('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#NotAValidClassName')


def test_dynamic_create_instance_from_ns_and_name():
    lgc = dynamic_create_instance_from_ns_and_name('legacy', 'AB')
    assert lgc is not None

    mof = dynamic_create_instance_from_ns_and_name('onderdeel', 'Aansluitmof')
    assert mof is not None

    agent = dynamic_create_instance_from_ns_and_name('', 'Agent')
    assert agent is not None

    with pytest.raises(CouldNotCreateInstanceError):
        dynamic_create_instance_from_ns_and_name('onderdeel', 'NotAValidClassName')


def test_dynamic_create_type_from_uri():
    agent_type = dynamic_create_type_from_uri('http://purl.org/dc/terms/Agent')
    assert agent_type is not None

    legacy_type = dynamic_create_type_from_uri('https://lgc.data.wegenenverkeer.be/ns/installatie#AB')
    assert legacy_type is not None

    mof_type = dynamic_create_type_from_uri('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aansluitmof')
    assert mof_type is not None

    with pytest.raises(CouldNotCreateInstanceError):
        dynamic_create_type_from_uri('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#NotAValidClassName')


@pytest.mark.parametrize(
    "uri",
    [
        'https://lgc.data.wegenenverkeer.be/ns/installatie#RIS',
        'https://lgc.data.wegenenverkeer.be/ns/installatie#ITSApp-RIS',
        'https://lgc.data.wegenenverkeer.be/ns/installatie#HY.GR',
        'https://lgc.data.wegenenverkeer.be/ns/installatie#HY.CI',
        'https://lgc.data.wegenenverkeer.be/ns/installatie#Fietstel',
        'https://lgc.data.wegenenverkeer.be/ns/installatie#Brug',
        'https://lgc.data.wegenenverkeer.be/ns/installatie#Voedingskeuzeschakelaar',
    ]
)
def test_dynamic_create_type_from_uri_legacy_exceptions(uri):
    legacy_instance = dynamic_create_instance_from_uri(uri)
    assert legacy_instance is not None


def test_dynamic_create_type_from_ns_and_name():
    mof_type = dynamic_create_type_from_ns_and_name('onderdeel', 'Aansluitmof')
    assert mof_type is not None

    with pytest.raises(CouldNotCreateInstanceError):
        dynamic_create_type_from_ns_and_name('onderdeel', 'NotAValidClassName')


def test_instantiate_test_class_with_asset_creator():
    model_location = Path(ROOT_DIR).parent / 'TestModel'
    another_test_class = dynamic_create_instance_from_uri(
        class_uri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AnotherTestClass',
        model_directory=model_location)
    assert another_test_class is not None
    assert another_test_class.typeURI == AnotherTestClass.typeURI
    test_class = dynamic_create_instance_from_uri(
        class_uri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass',
        model_directory=model_location)
    assert test_class is not None


def test_instantiate_test_and_real_classes_using_dynamic_import():
    model_location = Path(ROOT_DIR).parent / 'TestModel'
    mof = dynamic_create_instance_from_ns_and_name('onderdeel', 'Aansluitmof', model_directory=None)
    test_class = dynamic_create_instance_from_ns_and_name('onderdeel', 'AllCasesTestClass', model_directory=model_location)

    assert test_class is not None
    assert mof is not None


@pytest.mark.filterwarnings("ignore::DeprecationWarning")
@pytest.mark.timeout(300)
def test_instantiate_all_classes_using_class_dict():
    classes_to_instantiate = [uri for uri, class_dict in get_hardcoded_class_dict().items() if not class_dict['abstract']]
    # use multithreading
    executor = ThreadPoolExecutor(8)
    futures = [executor.submit(subtest_instantiate, uri=uri) for uri in classes_to_instantiate]
    attempt = 5
    while futures and attempt > 0:
        attempt -= 1
        done, not_done = concurrent.futures.wait(futures, return_when=ALL_COMPLETED, timeout=60)
        futures = not_done
        logging.info(f'{len(done)} done, {len(not_done)} not done')
    assert not futures

def subtest_instantiate(uri: str, ):
    try:
        instance = dynamic_create_instance_from_uri(uri)
        instance.fill_with_dummy_data()
        if instance is None:
            logging.info(f'instance is None for {uri}\n')
            raise CouldNotCreateInstanceError(f'instance is None for {uri}')
        print(f'successfully instantiated {uri}')
    except Exception as e:
        logging.info(f'could not create an instance for {uri}')
        raise e
