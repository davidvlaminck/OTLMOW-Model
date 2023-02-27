import os
from os.path import isfile, join
from pathlib import Path
from unittest import TestCase

from otlmow_model.Helpers.AssetCreator import dynamic_create_instance_from_uri

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


class InstantiationTests(TestCase):
    def test_instantiate_single_class_with_asset_creator(self):
        mof = dynamic_create_instance_from_uri('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aansluitmof')
        self.assertIsNotNone(mof)

    def test_instantiate_all_classes(self):
        classes_to_instantiate = {}

        class_location = Path(ROOT_DIR) / '../../otlmow_model/Classes/'
        installatie_location = class_location / 'Installatie'
        onderdeel_location = class_location / 'Onderdeel'
        levenscyclus_location = class_location / 'Levenscyclus'
        proefenmeting_location = class_location / 'ProefEnMeting'

        for dir_location in [installatie_location, onderdeel_location, levenscyclus_location, proefenmeting_location]:
            for f in os.listdir(dir_location):
                f = str(f)
                if not isfile(dir_location / f):
                    continue
                classes_to_instantiate[Path(f).stem] = Path(dir_location / Path(f).stem).resolve()

        classes_to_instantiate['Agent'] = class_location / 'Agent'
        classes_to_instantiate['ActivityComplex'] = class_location / 'ImplementatieElement' / 'ActivityComplex'
        classes_to_instantiate['ElectricityAppurtenance'] = class_location / 'ImplementatieElement' / 'ElectricityAppurtenance'
        classes_to_instantiate['Derdenobject'] = class_location / 'ImplementatieElement' / 'Derdenobject'
        classes_to_instantiate['ElectricityCable'] = class_location / 'ImplementatieElement' / 'ElectricityCable'
        classes_to_instantiate['Pipe'] = class_location / 'ImplementatieElement' / 'Pipe'
        classes_to_instantiate['TelecommunicationsAppurtenance'] = class_location / 'ImplementatieElement' / 'TelecommunicationsAppurtenance'
        classes_to_instantiate['TelecommunicationsCable'] = class_location / 'ImplementatieElement' / 'TelecommunicationsCable'

        for class_name, file_path in classes_to_instantiate.items():
            with self.subTest(f'Trying to instantiate {class_name}'):
                try:
                    import_path = f'{file_path.parts[-3]}.{file_path.parts[-2]}.{file_path.parts[-1]}'
                    if 'otlmow_model' not in import_path:
                        import_path = 'otlmow_model.' + import_path
                    py_mod = __import__(name=import_path, fromlist=f'{class_name}')
                except ModuleNotFoundError:
                    raise ModuleNotFoundError(f'Could not import the module for {import_path}')
                class_ = getattr(py_mod, class_name)
                instance = class_()
                self.assertTrue(True)
