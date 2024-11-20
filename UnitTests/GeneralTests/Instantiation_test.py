import concurrent
import multiprocessing
import os
from concurrent.futures import ThreadPoolExecutor
from os.path import isfile
from pathlib import Path

import pytest

from UnitTests.TestModel.OtlmowModel.Classes.Onderdeel.AnotherTestClass import AnotherTestClass
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import dynamic_create_instance_from_uri, \
    dynamic_create_instance_from_ns_and_name, dynamic_create_type_from_uri, dynamic_create_type_from_ns_and_name

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def test_dynamic_create_instance_from_uri():
    mof = dynamic_create_instance_from_uri('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aansluitmof')
    assert mof is not None

    agent = dynamic_create_instance_from_uri('http://purl.org/dc/terms/Agent')
    assert agent is not None

    with pytest.raises(ModuleNotFoundError):
        dynamic_create_instance_from_uri('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#NotAValidClassName')


def test_dynamic_create_instance_from_ns_and_name():
    mof = dynamic_create_instance_from_ns_and_name('onderdeel', 'Aansluitmof')
    assert mof is not None

    with pytest.raises(ModuleNotFoundError):
        dynamic_create_instance_from_ns_and_name('onderdeel', 'NotAValidClassName')


def test_dynamic_create_type_from_uri():
    mof_type = dynamic_create_type_from_uri('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aansluitmof')
    assert mof_type is not None

    agent_type = dynamic_create_type_from_uri('http://purl.org/dc/terms/Agent')
    assert agent_type is not None

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
def test_instantiate_all_classes(subtests):
    classes_to_instantiate = {}

    class_location = Path(ROOT_DIR) / '../../otlmow_model/OtlmowModel/Classes/'
    installatie_location = class_location / 'Installatie'
    onderdeel_location = class_location / 'Onderdeel'
    levenscyclus_location = class_location / 'Levenscyclus'
    proefenmeting_location = class_location / 'ProefEnMeting'

    for dir_location in {installatie_location, onderdeel_location, levenscyclus_location, proefenmeting_location}:
        for f in os.listdir(dir_location):
            if not isfile(dir_location / f):
                continue
            class_name = f[:-3]
            classes_to_instantiate[class_name] = (dir_location.stem, class_name)

    classes_to_instantiate['Agent'] = (None, 'Agent')
    classes_to_instantiate['ActivityComplex'] = ('ImplementatieElement', 'ActivityComplex')
    classes_to_instantiate['ElectricityAppurtenance'] = ('ImplementatieElement', 'ElectricityAppurtenance')
    classes_to_instantiate['Derdenobject'] = ('ImplementatieElement', 'Derdenobject')
    classes_to_instantiate['ElectricityCable'] = ('ImplementatieElement', 'ElectricityCable')
    classes_to_instantiate['Pipe'] = ('ImplementatieElement', 'Pipe')
    classes_to_instantiate['TelecommunicationsAppurtenance'] = ('ImplementatieElement', 'TelecommunicationsAppurtenance')
    classes_to_instantiate['TelecommunicationsCable'] = ('ImplementatieElement', 'TelecommunicationsCable')


    # # use multithreading
    # executor = ThreadPoolExecutor(8)
    # futures = [executor.submit(subtest_instantiate, namespace=namespace, class_name=class_name, subtests=subtests)
    #            for namespace, class_name in classes_to_instantiate.values()]
    # concurrent.futures.wait(futures)

    for namespace, class_name in classes_to_instantiate.values():
        subtest_instantiate(namespace, class_name, subtests)


def subtest_instantiate(namespace, class_name, subtests):
    with subtests.test(msg=f'Trying to instantiate {class_name}'):
        instance = dynamic_create_instance_from_ns_and_name(namespace, class_name)
        assert instance is not None
        instance.fill_with_dummy_data()


