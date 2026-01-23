import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import time
from concurrent.futures import ThreadPoolExecutor, as_completed
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
@pytest.mark.timeout(100)
def test_instantiate_all_classes_using_class_dict():
    # gather all non-abstract class URIs
    uris = [uri for uri, class_dict in get_hardcoded_class_dict().items() if not class_dict['abstract']]

    errors = []
    with ThreadPoolExecutor(max_workers=8) as executor:
        future_to_uri = {
            executor.submit(instantiate_with_retry, uri): uri
            for uri in uris
        }

        for future in as_completed(future_to_uri, timeout=240):
            uri = future_to_uri[future]
            try:
                # will re-raise if instantiate_with_retry exhausted its retries
                future.result(timeout=60)
            except Exception as exc:
                errors.append((uri, exc))

    if errors:
        lines = [f"{u}: {type(e).__name__}: {e}" for u, e in errors]
        pytest.fail(
            "Failed to instantiate the following URIs after retries:\n"
            + "\n".join(lines)
        )


def instantiate_with_retry(uri: str, retries: int = 5, delay: float = 0.1) -> object:
    """
    Try to instantiate and fill dummy data up to `retries` times.
    Raises the final exception if all attempts fail.
    """
    for attempt in range(1, retries + 1):
        try:
            inst = dynamic_create_instance_from_uri(uri)
            inst.fill_with_dummy_data()
            if inst is None:
                raise CouldNotCreateInstanceError(f"instance is None for {uri}")
            return inst
        except CouldNotCreateInstanceError as exc:
            print(f"Attempt {attempt} for {uri} failed: {type(exc).__name__}: {exc}")
            if attempt == retries:
                # final failure — let it bubble
                raise exc
            time.sleep(delay)
        except Exception as exc:
            print(f"Attempt {attempt} for {uri} failed: {type(exc).__name__}: {exc}")
            raise exc
    return None
