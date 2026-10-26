"""Characterisation tests for the dynamic loader of the real package.

These tests import from the real ``otlmow_model.OtlmowModel.BaseClasses`` modules
(hand-written, stable) and only use the generated model for the lookups that
cannot be faked (a class URI has to exist in the hardcoded class dictionary).

Purpose: pin the behaviour of ``BaseClasses/DynamicLoader.py`` before that file
is refactored (code_quality/REFACTOR_LOG.md).
"""

import sys
from pathlib import Path

import pytest
from otlmow_model.OtlmowModel.BaseClasses.DynamicLoader import (
    _import_module,
    dynamic_create_instance_from_ns_and_name,
    dynamic_create_type_from_ns_and_name,
    dynamic_create_type_from_uri,
)
from otlmow_model.OtlmowModel.Exceptions.CouldNotCreateInstanceError import CouldNotCreateInstanceError

KLIMATISATIE_URI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Klimatisatie'


def test_dynamic_create_type_from_ns_and_name():
    created_type = dynamic_create_type_from_ns_and_name('onderdeel', 'Klimatisatie')
    assert created_type.typeURI == KLIMATISATIE_URI


def test_dynamic_create_instance_from_ns_and_name():
    instance = dynamic_create_instance_from_ns_and_name('onderdeel', 'Klimatisatie')
    assert instance.typeURI == KLIMATISATIE_URI


def test_dynamic_create_type_from_ns_and_name_with_an_unknown_namespace():
    with pytest.raises(CouldNotCreateInstanceError) as error:
        dynamic_create_type_from_ns_and_name('onbekend', 'Klimatisatie')
    assert 'No classes found with the namespace onbekend.' in error.value.message
    assert error.value.closest_matches == []


def test_dynamic_create_type_from_ns_and_name_with_an_unknown_class_name():
    with pytest.raises(CouldNotCreateInstanceError) as error:
        dynamic_create_type_from_ns_and_name('onderdeel', 'Klimatisati')
    assert 'Did you mean one of these class names?' in error.value.message
    assert 'Klimatisatie' in error.value.closest_matches


def test_dynamic_create_type_from_uri_with_an_unknown_uri():
    with pytest.raises(CouldNotCreateInstanceError) as error:
        dynamic_create_type_from_uri('https://example.com#Unknown')
    assert 'is not found in the hardcoded class dictionary' in error.value.message


def test_import_module_with_an_unknown_class_raises():
    with pytest.raises(CouldNotCreateInstanceError) as error:
        _import_module(namespace='onderdeel', class_name='NotAnExistingClass')
    assert 'the import failed' in error.value.message
    assert 'Make sure you are directing to the (parent) directory' not in error.value.message


def test_import_module_with_an_unknown_class_and_a_given_model_directory_raises():
    model_directory = Path('/otlmow-model-does-not-exist')
    try:
        with pytest.raises(CouldNotCreateInstanceError) as error:
            _import_module(namespace='onderdeel', class_name='NotAnExistingClass', model_directory=model_directory)
        assert 'the import failed' in error.value.message
        assert 'Make sure you are directing to the (parent) directory' in error.value.message
    finally:
        if str(model_directory) in sys.path:
            sys.path.remove(str(model_directory))
