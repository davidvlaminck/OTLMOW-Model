import concurrent
import multiprocessing
import os
from concurrent.futures import ThreadPoolExecutor, ALL_COMPLETED
from os.path import isfile
from pathlib import Path

import pytest

from UnitTests.TestModel.OtlmowModel.Classes.Onderdeel.AnotherTestClass import AnotherTestClass
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import dynamic_create_instance_from_uri, \
    dynamic_create_instance_from_ns_and_name, dynamic_create_type_from_uri, dynamic_create_type_from_ns_and_name
from otlmow_model.OtlmowModel.Helpers.generated_lists import get_hardcoded_class_dict

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def test_dynamic_create_instance_from_uri():
    mof = dynamic_create_instance_from_uri('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aansluitmof')
    assert mof is not None

    agent = dynamic_create_instance_from_uri('http://purl.org/dc/terms/Agent')
    assert agent is not None

    with pytest.raises(ModuleNotFoundError):
        dynamic_create_instance_from_uri('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#NotAValidClassName')


def test_dynamic_create_instance_from_ns_and_name():
    lgc = dynamic_create_instance_from_ns_and_name('installatie', 'AB')
    assert lgc is not None

    mof = dynamic_create_instance_from_ns_and_name('onderdeel', 'Aansluitmof')
    assert mof is not None

    agent = dynamic_create_instance_from_ns_and_name('purl', 'Agent')
    assert agent is not None

    with pytest.raises(ModuleNotFoundError):
        dynamic_create_instance_from_ns_and_name('onderdeel', 'NotAValidClassName')


def test_dynamic_create_type_from_uri():
    agent_type = dynamic_create_type_from_uri('http://purl.org/dc/terms/Agent')
    assert agent_type is not None

    legacy_type = dynamic_create_type_from_uri('https://lgc.data.wegenenverkeer.be/ns/installatie#AB')
    assert legacy_type is not None

    mof_type = dynamic_create_type_from_uri('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aansluitmof')
    assert mof_type is not None

    with pytest.raises(ModuleNotFoundError):
        dynamic_create_type_from_uri('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#NotAValidClassName')


def test_dynamic_create_type_from_ns_and_name():
    mof_type = dynamic_create_type_from_ns_and_name('onderdeel', 'Aansluitmof')
    assert mof_type is not None

    with pytest.raises(ModuleNotFoundError):
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
    test_class = dynamic_create_instance_from_ns_and_name('onderdeel', 'AllCasesTestClass', model_directory=model_location)
    mof = dynamic_create_instance_from_ns_and_name('onderdeel', 'Aansluitmof', model_directory=None)

    assert test_class is not None
    assert mof is not None


@pytest.mark.filterwarnings("ignore::DeprecationWarning")
@pytest.mark.timeout(300)
def test_instantiate_all_classes_using_class_dict(subtests):
    classes_to_instantiate = [uri for uri, class_dict in get_hardcoded_class_dict().items() if not class_dict['abstract']]
    # use multithreading
    executor = ThreadPoolExecutor(8)
    futures = [executor.submit(subtest_instantiate, uri=uri, subtests=subtests) for uri in classes_to_instantiate]
    attempt = 5
    while futures and attempt > 0:
        attempt -= 1
        done, not_done = concurrent.futures.wait(futures, return_when=ALL_COMPLETED, timeout=60)
        futures = not_done
        print(f'{len(done)} done, {len(not_done)} not done')

def subtest_instantiate(uri: str, subtests):
    with subtests.test(msg=uri):
        instance = dynamic_create_instance_from_uri(uri)
        instance.fill_with_dummy_data()
        assert instance is not None, f'failed to instantiate {uri}'



