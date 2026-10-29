import importlib
import sys
from difflib import get_close_matches
from pathlib import Path
from types import ModuleType
from typing import TYPE_CHECKING

from ..Exceptions.CouldNotCreateInstanceError import CouldNotCreateInstanceError
from ..Helpers.generated_lists import get_hardcoded_class_dict
from ..Helpers.GenericHelper import get_titlecase_from_ns

if TYPE_CHECKING:
    from .OTLObject import OTLObject

_imported_modules = {}


def dynamic_create_type_from_ns_and_name(
    namespace: str, class_name: str, model_directory: Path | None = None
) -> type:
    """Loads the OTL class module and attempts to return the type using the name and namespace of the class

    :param namespace: namespace of the class
    :type: str
    :param class_name: class name to instantiate
    :type: str
    :param model_directory: directory where the model is located, defaults to otlmow_model's own model
    :type: str
    :return: returns an instance of class_name in the given namespace, located from directory
    :rtype: type
    """
    class_dict = _get_class_dict(model_directory=model_directory)
    class_entry = next((c for c in class_dict.values() if c['ns'] == namespace and c['name'] == class_name), None)
    if class_entry is not None:
        return _create_type_from_class_dict_entry(class_entry, model_directory=model_directory)
    raise _class_not_found_error(class_dict=class_dict, namespace=namespace, class_name=class_name)


def dynamic_create_instance_from_ns_and_name(
    namespace: str, class_name: str, model_directory: Path | None = None
) -> 'OTLObject':
    """Loads the OTL class module and attempts to instantiate the class using the name and namespace of the class.
    Caches imported modules for performance improvement.

    :param namespace: namespace of the class
    :type: str
    :param class_name: class name to instantiate
    :type: str
    :param model_directory: directory where the model is located, defaults to otlmow_model's own model
    :type: Path
    :return: returns an instance of class_name in the given namespace, located from directory
    :rtype: OTLObject
    """
    type_ = dynamic_create_type_from_ns_and_name(
        namespace=namespace, class_name=class_name, model_directory=model_directory
    )
    return type_()


def dynamic_create_instance_from_uri(class_uri: str, model_directory: Path | None = None) -> 'OTLObject':
    """Loads the OTL class module and attempts to instantiate the class using the URI of the class.

    :param class_uri: URI of the class
    :type: str
    :param model_directory: directory where the model is located, defaults to otlmow_model's own model
    :type: Path
    :return: returns an instance of the class with the given URI, located from directory
    :rtype: OTLObject
    """
    type_ = dynamic_create_type_from_uri(class_uri, model_directory=model_directory)
    return type_()


def dynamic_create_type_from_uri(class_uri: str, model_directory: Path | None = None) -> type:
    """Loads the OTL class module and attempts to return the type using the URI of the class.

    :param class_uri: URI of the class
    :type: str
    :param model_directory: directory where the model is located, defaults to otlmow_model's own model
    :type: Path
    :return: returns a type object created from the class URI
    :rtype: type
    """
    class_dict = _get_class_dict(model_directory=model_directory)
    if class_uri in class_dict:
        return _create_type_from_class_dict_entry(class_dict[class_uri], model_directory=model_directory)
    raise _class_uri_not_found_error(class_dict=class_dict, class_uri=class_uri)


def _get_class_dict(model_directory: Path | None = None) -> dict:
    try:
        return get_hardcoded_class_dict(model_directory=model_directory)
    except FileNotFoundError as e:
        raise CouldNotCreateInstanceError(
            e.message + '\nMake sure you are directing to the (parent) directory where OtlmowModel is located in.'
        ) from e


def _class_not_found_error(class_dict: dict, namespace: str, class_name: str) -> CouldNotCreateInstanceError:
    error = CouldNotCreateInstanceError(
        f'The combination of the namespace {namespace} and the class name {class_name} is not found in the hardcoded '
        f'class dictionary.'
    )

    ns_match = next((c for c in class_dict.values() if c['ns'] == namespace), None)
    if ns_match is None:
        error.message += f'\nNo classes found with the namespace {namespace}.'
        error.message += _namespace_suggestion_message(class_dict=class_dict, namespace=namespace)
        raise error

    closest_matches = _closest_class_name_matches(class_dict=class_dict, class_name=class_name)
    closest_matches_string = '", "'.join(closest_matches)

    error.message += (
        f'\nNo classes found with the namespace {namespace}.'
        f'nDid you mean one of these class names? "{closest_matches_string}"'
    )
    error.closest_matches = closest_matches
    raise error


def _namespace_suggestion_message(class_dict: dict, namespace: str) -> str:
    closest_matches = get_close_matches(namespace, {c['ns'] for c in class_dict.values()}, n=5, cutoff=0.8)
    closest_matches_string = '", "'.join(closest_matches)
    return f'\nDid you mean one of these namespaces? "{closest_matches_string}"'


def _closest_class_name_matches(class_dict: dict, class_name: str) -> list:
    return get_close_matches(class_name, {c['name'] for c in class_dict.values()}, n=5, cutoff=0.8)


def _class_uri_not_found_error(class_dict: dict, class_uri: str) -> CouldNotCreateInstanceError:
    closest_matches = get_close_matches(class_uri, class_dict.keys(), n=5, cutoff=0.8)
    closest_matches_string = '", "'.join(closest_matches)

    error = CouldNotCreateInstanceError(
        f'Class URI {class_uri} is not found in the hardcoded class dictionary. '
        f'Did you mean one of these? "{closest_matches_string}"'
    )
    error.closest_matches = closest_matches
    raise error


def _create_type_from_class_dict_entry(
    class_dict_entry: dict[str, str], model_directory: Path | None = None
) -> type:
    """Creates a type from a class dictionary entry.

    :param class_dict_entry: dictionary containing the class information
    :type class_dict_entry: dict
    :param model_directory: directory where the model is located, defaults to otlmow_model's own model
    :type model_directory: Path
    :return: returns a type object created from the class dictionary entry
    :rtype: type
    """
    namespace = class_dict_entry['ns']
    class_name = class_dict_entry['name']
    module_key = (namespace, class_name)

    if module_key in _imported_modules:
        mod = _imported_modules[module_key]
    else:
        mod = _import_module(namespace=namespace, class_name=class_name, model_directory=model_directory)
        _imported_modules[module_key] = mod

    return getattr(mod, class_name)


def _import_module(namespace: str, class_name: str, model_directory: Path | None = None) -> ModuleType:
    model_directory_given = model_directory is not None
    if model_directory is None:
        model_directory = _default_model_directory()

    module_path = _module_path(namespace, class_name)

    try:
        _ensure_model_directory_on_path(model_directory)
        return importlib.import_module(module_path)
    except ModuleNotFoundError as e:
        raise _import_error(class_name, model_directory_given) from e


def _module_path(namespace: str, class_name: str) -> str:
    namespace_path = '' if namespace == '' else f'{get_titlecase_from_ns(namespace)}.'
    return f'OtlmowModel.Classes.{namespace_path}{class_name}'


def _ensure_model_directory_on_path(model_directory: Path) -> None:
    if str(model_directory) not in sys.path:
        sys.path.insert(1, str(model_directory))


def _import_error(class_name: str, model_directory_given: bool) -> CouldNotCreateInstanceError:
    error = CouldNotCreateInstanceError(
        f'When dynamically creating an object of class {class_name}, the import failed. '
    )
    if model_directory_given:
        error.message += 'Make sure you are directing to the (parent) directory where OtlmowModel is located in.'
    return error


def _default_model_directory() -> Path:
    return Path(__file__).parent.parent.parent
