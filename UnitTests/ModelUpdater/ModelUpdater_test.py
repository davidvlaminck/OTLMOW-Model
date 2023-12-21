import json
from pathlib import Path

import pytest

from UnitTests.TestModel.OtlmowModel.Classes.Onderdeel.AllCasesTestClass import AllCasesTestClass
from UnitTests.TestModel.OtlmowModel.Classes.Onderdeel.AnotherTestClass import AnotherTestClass
from UnitTests.TestModel.OtlmowModel.Classes.Onderdeel.DeprecatedTestClass import DeprecatedTestClass
from model_update.ModelUpdater import ModelUpdater
from otlmow_model.OtlmowModel.BaseClasses.MetaInfo import meta_info
from otlmow_model.OtlmowModel.Exceptions.ClassDeprecationWarning import ClassDeprecationWarning

fake_github_root_path = Path(__file__).parent / 'FakeGitHubRoot'


def generate_version_info(file_path: Path):
    if file_path.exists():
        file_path.unlink()

    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump({
            "current": {
                "model_version": "2.9.5.0",
                "otl_version": "2.9.0",
                "created_at": "2023-12-14T16:05:00",
                "created_by": "david.vlaminck"
            },
            "history": {
                "2.9.4.0": {
                    "previous_version": None,
                    "updated_class_model": False,
                    "updated_enums": False,
                    "enums_updated": []
                },
                "2.9.5.0": {
                    "previous_version": "2.9.4.0",
                    "updated_class_model": False,
                    "updated_enums": False,
                    "enums_updated": []
                }
            }
        }, file, indent=4)


def test_update_model_new_version():
    version_info_file_path = fake_github_root_path / 'otlmow_model' / 'version_info.json'
    generate_version_info(version_info_file_path)

    ModelUpdater(github_root=fake_github_root_path).update_model(
        model_version='2.9.6.0', otl_version='2.9.0', created_by='david.vlaminck')

    with open(version_info_file_path, encoding='utf-8') as file:
        written_data = json.load(file)

    assert written_data['current']['model_version'] == '2.9.6.0'
    assert written_data['current']['otl_version'] == '2.9.0'
    assert written_data['current']['created_by'] == 'david.vlaminck'
    assert written_data['history']['2.9.6.0']['previous_version'] == '2.9.5.0'

    version_info_file_path.unlink()

