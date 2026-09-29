import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import pytest

import otlmow_model.OtlmowModel.Helpers.generated_lists as generated_lists


@pytest.fixture
def empty_caches():
    saved_class_dict = dict(generated_lists.global_class_dict_by_model)
    saved_relation_dict = dict(generated_lists.global_relation_dict_by_model)
    generated_lists.global_class_dict_by_model.clear()
    generated_lists.global_relation_dict_by_model.clear()
    yield
    generated_lists.global_class_dict_by_model.clear()
    generated_lists.global_class_dict_by_model.update(saved_class_dict)
    generated_lists.global_relation_dict_by_model.clear()
    generated_lists.global_relation_dict_by_model.update(saved_relation_dict)


@pytest.fixture
def count_json_loads(monkeypatch):
    calls = []

    def counting_load(fp, *args, **kwargs):
        calls.append(fp.name)
        return json_load(fp, *args, **kwargs)

    json_load = generated_lists.json.load
    monkeypatch.setattr(generated_lists.json, 'load', counting_load)
    return calls


def test_get_hardcoded_class_dict_default_argument_is_cached(empty_caches, count_json_loads):
    first = generated_lists.get_hardcoded_class_dict()
    second = generated_lists.get_hardcoded_class_dict()

    assert len(count_json_loads) == 1
    assert first is second


def test_get_hardcoded_relation_dict_default_argument_is_cached(empty_caches, count_json_loads):
    first = generated_lists.get_hardcoded_relation_dict()
    second = generated_lists.get_hardcoded_relation_dict()

    assert len(count_json_loads) == 1
    assert first is second


def test_get_hardcoded_class_dict_uses_resolved_path_as_cache_key(empty_caches):
    generated_lists.get_hardcoded_class_dict()

    assert list(generated_lists.global_class_dict_by_model.keys()) == [str(generated_lists.MODEL_ROOT_PATH)]


def test_get_hardcoded_relation_dict_uses_resolved_path_as_cache_key(empty_caches):
    generated_lists.get_hardcoded_relation_dict()

    assert list(generated_lists.global_relation_dict_by_model.keys()) == [str(generated_lists.MODEL_ROOT_PATH)]


def test_get_hardcoded_class_dict_shares_cache_with_explicit_model_directory(empty_caches, count_json_loads):
    from_explicit = generated_lists.get_hardcoded_class_dict(generated_lists.MODEL_ROOT_PATH)
    from_default = generated_lists.get_hardcoded_class_dict()

    assert len(count_json_loads) == 1
    assert from_default is from_explicit


def test_get_hardcoded_relation_dict_shares_cache_with_explicit_model_directory(empty_caches, count_json_loads):
    from_explicit = generated_lists.get_hardcoded_relation_dict(generated_lists.MODEL_ROOT_PATH)
    from_default = generated_lists.get_hardcoded_relation_dict()

    assert len(count_json_loads) == 1
    assert from_default is from_explicit
