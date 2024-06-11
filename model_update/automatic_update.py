import logging
import urllib.request
from pathlib import Path
from subprocess import Popen, PIPE

from otlmow_modelbuilder.ModelBuilder import ModelBuilder
from otlmow_modelbuilder.OSLOInMemoryCreator import OSLOInMemoryCreator

from ModelUpdater import ModelUpdater

logging.basicConfig(level=logging.INFO, format='%(message)s')

urllib.request.urlretrieve("https://github.com/davidvlaminck/OTLMOW-ModelBuilder/raw/master/otlmow_modelbuilder"
                           "/InputFiles/latest/OTL.db", 'OTL.db')
urllib.request.urlretrieve("https://github.com/davidvlaminck/OTLMOW-ModelBuilder/raw/master/otlmow_modelbuilder"
                           "/InputFiles/latest/Geometrie_Artefact.db", 'Geometrie_Artefact.db')
urllib.request.urlretrieve("https://github.com/davidvlaminck/OTLMOW-ModelBuilder/raw/master/otlmow_modelbuilder"
                           "/settings_otlmow_modelbuilder.json", 'settings_otlmow_modelbuilder.json')

current_dir = Path(__file__).parent
otl_subset_path = Path(current_dir / 'OTL.db')
GA_file_path = Path(current_dir / 'Geometrie_Artefact.db')
model_directory = Path(current_dir.parent / 'otlmow_model')
settings_path = Path(current_dir / 'settings_otlmow_modelbuilder.json')

with OSLOInMemoryCreator(otl_subset_path) as memory_creator:
    version = memory_creator.get_otl_version()

ModelBuilder.build_otl_datamodel(otl_subset_location=otl_subset_path, geometry_artefact_location=GA_file_path,
                                 directory=model_directory, settings_path=settings_path,
                                 environment='prd')

cmd = "git add ./../otlmow_model/OtlmowModel"
p = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True)
stdout, stderr = p.communicate()

updater = ModelUpdater(github_root=current_dir.parent)
enums_updated = updater.find_changed_enums()
updater.update_model(otl_version=version, created_by='david.vlaminck', enums_updated=enums_updated)
