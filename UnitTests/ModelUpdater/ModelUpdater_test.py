import json
from pathlib import Path

from model_update.ModelUpdater import ModelUpdater

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
        model_version='2.9.6.0', otl_version='2.9.0', created_by='david.vlaminck', updated_class_model=False,
        updated_enums=False, enums_updated=[])

    with open(version_info_file_path, encoding='utf-8') as file:
        written_data = json.load(file)

    assert written_data['current']['model_version'] == '2.9.6.0'
    assert written_data['current']['otl_version'] == '2.9.0'
    assert written_data['current']['created_by'] == 'david.vlaminck'
    assert written_data['history']['2.9.6.0']['previous_version'] == '2.9.5.0'

    version_info_file_path.unlink()


def test_find_changed_enums():
    kl_dir_path = Path(__file__).parent.parent.parent / 'otlmow_model' / 'OtlmowModel' / 'Datatypes'
    toestand_file_path = kl_dir_path / 'KlAIMToestand.py'
    new_file_path = kl_dir_path / 'KlNew.py'
    toestand_orig_file_contents = toestand_file_path.read_text(encoding='utf-8')

    toestand_file_path.write_text(f'{toestand_orig_file_contents}edited this file', encoding='utf-8')
    new_file_path.write_text('new file', encoding='utf-8')
    cmd = 'git add ./../../otlmow_model/OtlmowModel/Datatypes/KlNew.py'
    from subprocess import Popen, PIPE
    Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True).communicate()

    changed_enums = ModelUpdater(github_root=fake_github_root_path).find_changed_enums()
    assert changed_enums == ['KlAIMToestand', 'KlNew']

    toestand_file_path.write_text(toestand_orig_file_contents, encoding='utf-8')
    new_file_path.unlink()
