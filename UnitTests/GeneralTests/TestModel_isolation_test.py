"""The test datamodel must contain the datamodel only.

The runtime (BaseClasses, Exceptions, GeometrieTypes, warnings, Helpers) has
exactly one implementation: the one in otlmow_model/OtlmowModel. A copy under
UnitTests/TestModel is a second implementation that can drift - and it had
already drifted (13 files differed, and the copied OTLObject.py was still the
pre-refactor monolith). The tests would then exercise code that does not ship.

The tests below are the guarantee: the first forbids the copy from
coming back, the others prove that the code the tests execute is the
repository's runtime - through the static import path and through the
dynamic importer, which loads the test datamodel under a third namespace.
"""
import sys
from pathlib import Path

from otlmow_model.OtlmowModel.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import dynamic_create_instance_from_uri

TEST_MODEL_ROOT = Path(__file__).parent.parent / 'TestModel' / 'OtlmowModel'
RUNTIME_DIRECTORIES = ('BaseClasses', 'Exceptions', 'GeometrieTypes', 'warnings')
ALL_CASES_TEST_CLASS_URI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass'


def _first_attribute(instance):
    return next(v for v in vars(instance).values() if getattr(v, 'is_otl_attribute', False))


def test_test_model_contains_no_copy_of_the_runtime():
    offenders = [
        str(path.relative_to(TEST_MODEL_ROOT))
        for directory in RUNTIME_DIRECTORIES
        for path in (TEST_MODEL_ROOT / directory).rglob('*.py')
    ]
    assert not offenders, (
        f'The runtime must not be copied into the test datamodel: {offenders}. '
        f'Import it from otlmow_model.OtlmowModel instead.'
    )


def test_statically_imported_test_datamodel_executes_the_repository_runtime():
    from UnitTests.TestModel.OtlmowModel.Classes.Onderdeel.AllCasesTestClass import AllCasesTestClass

    assert isinstance(_first_attribute(AllCasesTestClass()), OTLAttribuut)


def test_dynamically_imported_test_datamodel_executes_the_repository_runtime():
    instance = dynamic_create_instance_from_uri(
        ALL_CASES_TEST_CLASS_URI, model_directory=Path(__file__).parent.parent / 'TestModel')
    assert isinstance(_first_attribute(instance), OTLAttribuut)


def test_the_re_exported_attribuut_is_the_same_object():
    from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut as re_exported
    assert re_exported is OTLAttribuut