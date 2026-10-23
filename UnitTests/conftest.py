"""Bind the test datamodel to the runtime of this repository.

UnitTests/TestModel/OtlmowModel contains the *datamodel* only (group A).
Its generated classes import the runtime (group B) with relative imports
("from ...BaseClasses.OTLObject import OTLAttribuut"). Under a second
package name those relative imports would resolve to a *copy* of the
runtime, and the copy drifts (it already had drifted in 13 files).

Registering the repository's modules under the names the test tree uses
makes the import machinery pick them up: Python looks a module up in
sys.modules before it looks at the filesystem. The tests then always
execute the code in otlmow_model/OtlmowModel.
"""
import importlib
import pkgutil
import sys

# The two namespaces under which the test datamodel is loaded:
#  - the static one, when a test imports it directly;
#  - OtlmowModel, the top-level name the dynamic importer creates by putting
#    the model directory on sys.path (see BaseClasses/DynamicLoader.py).
NAMESPACES = ('UnitTests.TestModel.OtlmowModel', 'OtlmowModel')

RUNTIME_PACKAGES = ('BaseClasses', 'Exceptions', 'GeometrieTypes', 'warnings')

# Helpers is mixed: all_classes.py belongs to the datamodel (it lists the
# test datamodel's own classes and must keep resolving to the test tree);
# the other modules are runtime.
RUNTIME_MODULES_IN_HELPERS = (
    'OTLObjectHelper',
    'RelationCreator',
    'RelationValidator',
    'GenericHelper',
    'generated_lists',
    'all_functions',
    'AssetCreator',
)


def _alias_runtime(namespace: str) -> None:
    for package_name in RUNTIME_PACKAGES:
        package = importlib.import_module(f'otlmow_model.OtlmowModel.{package_name}')
        sys.modules[f'{namespace}.{package_name}'] = package
        for info in pkgutil.iter_modules(package.__path__):
            module = importlib.import_module(f'otlmow_model.OtlmowModel.{package_name}.{info.name}')
            sys.modules[f'{namespace}.{package_name}.{info.name}'] = module
    for module_name in RUNTIME_MODULES_IN_HELPERS:
        module = importlib.import_module(f'otlmow_model.OtlmowModel.Helpers.{module_name}')
        sys.modules[f'{namespace}.Helpers.{module_name}'] = module


for _namespace in NAMESPACES:
    _alias_runtime(_namespace)