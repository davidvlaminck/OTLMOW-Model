import datetime
import json
from pathlib import Path
from typing import List

GITHUB_ROOT = Path(__file__).parent.parent


class ModelUpdater:
    @classmethod
    def update_model(cls, version_info_file_path: Path, otl_version: str, created_by: str, enums_updated: list):
        with open(version_info_file_path, encoding='utf-8') as file:
            version_info = json.load(file)

        current_otl_version = version_info['current']['otl_version']

        updated_class_model = (current_otl_version != otl_version)
        updated_enums = len(enums_updated) > 0

        current_model_version = version_info['current']['model_version']
        print(f'Current OTL version: {current_otl_version}')
        print(f'Current current_model_version version: {current_model_version}')
        print(f'New OTL version: {otl_version}')
        print(f'Updated class model: {updated_class_model}')
        model_version = cls.update_model_version(updated_class_model=updated_class_model, updated_enums=updated_enums,
                                                 model_version=current_model_version, otl_version=otl_version)

        print(f'Current OTL version: {current_otl_version}')
        print(f'Current current_model_version version: {current_model_version}')
        print(f'New OTL version: {otl_version}')
        print(f'Updated class model: {updated_class_model}')

        if current_model_version == model_version:
            print("MODEL_UPDATED=false")
            status_file = Path(__file__).parent / "model_update_status.txt"
            with status_file.open("w") as f:
                f.write("MODEL_UPDATED=false\n")
            return

        version_info['current'] = {
            'model_version': model_version,
            'otl_version': otl_version,
            'created_at': datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
            'created_by': created_by
        }

        version_info['history'][model_version] = {
            'previous_version': current_model_version,
            'updated_class_model': updated_class_model,
            'updated_enums': updated_enums,
            'enums_updated': enums_updated
        }

        with open(version_info_file_path, 'w', encoding='utf-8') as file:
            json.dump(version_info, file, indent=4)
        print("MODEL_UPDATED=true")
        status_file = Path(__file__).parent / "model_update_status.txt"
        with status_file.open("w") as f:
            f.write("MODEL_UPDATED=true\n")

    @classmethod
    def find_changed_enums(cls, model_path: str = 'otlmow_model/OtlmowModel') -> List:
        from subprocess import Popen, PIPE
        cmd = 'git status --porcelain'
        p = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True)
        stdout, stderr = p.communicate()
        files_changed_list = stdout.decode().splitlines()
        enums_changed = []
        for entry in files_changed_list:
            xy = entry[:2]
            if 'M' in xy or 'A' in xy:
                path = entry[3:]
                if (path.startswith(f'{model_path}/Datatypes/Kl') or path ==
                        f'{model_path}/Datatypes/AntiParkeerpaalType.py'):
                    enums_changed.append(path[(len(model_path) + 11):-3])
        return enums_changed

    @classmethod
    def update_model_version(cls, updated_class_model: bool, updated_enums: bool, model_version: str,
                             otl_version: str) -> str:
        major, minor, build, enum = model_version.split('.')
        otl_major, otl_minor, otl_patch = otl_version.split('.')
        if updated_class_model:
            if major == otl_major and minor == otl_minor:
                build = str(int(build) + 1)
            else:
                major = otl_major
                minor = otl_minor
                build = '0'
            enum = '0'
        elif updated_enums:
            enum = str(int(enum) + 1)
        return f'{major}.{minor}.{build}.{enum}'
