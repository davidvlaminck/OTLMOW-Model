import importlib
import sys
from pathlib import Path

from otlmow_model.OtlmowModel.Helpers.GenericHelper import get_titlecase_from_ns, get_ns_and_name_from_uri


def dynamic_create_type_from_ns_and_name(namespace: str, class_name: str, model_directory: Path = None) -> type:
    """Loads the OTL class module and attempts to instantiate the class using the name and namespace of the class

    :param namespace: namespace of the class
    :type: str
    :param class_name: class name to instantiate
    :type: str
    :param model_directory: directory where the model is located, defaults to otlmow_model's own model
    :type: str
    :return: returns an instance of class_name in the given namespace, located from directory, that inherits from AIMObject or RelatieObject
    :rtype: AIMObject, RelatieObject or None
    """
    if model_directory is None:
        current_file_path = Path(__file__)
        model_directory = current_file_path.parent.parent.parent

    if namespace is None:
        namespace = ''
    else:
        namespace = get_titlecase_from_ns(namespace) + '.'

    sys.path.insert(1, str(model_directory))
    try:
        mod = importlib.import_module(f'OtlmowModel.Classes.{namespace}{class_name}')
        class_ = getattr(mod, class_name)
        return class_
    except ModuleNotFoundError:
        raise ModuleNotFoundError(f'When dynamically creating an object of class {class_name}, the import failed. '
                                  f'Make sure you are directing to the (parent) directory where OtlmowModel is '
                                  f'located in.')


def dynamic_create_instance_from_ns_and_name(namespace: str, class_name: str, model_directory: Path = None) -> object:
    """Loads the OTL class module and attempts to instantiate the class using the name and namespace of the class

    :param namespace: namespace of the class
    :type: str
    :param class_name: class name to instantiate
    :type: str
    :param model_directory: directory where the model is located, defaults to otlmow_model's own model
    :type: str
    :return: returns an instance of class_name in the given namespace, located from directory, that inherits from AIMObject or RelatieObject
    :rtype: AIMObject, RelatieObject or None
    """
    if model_directory is None:
        current_file_path = Path(__file__)
        model_directory = current_file_path.parent.parent.parent

    if namespace is None:
        namespace = ''
    else:
        namespace = get_titlecase_from_ns(namespace) + '.'

    sys.path.insert(1, str(model_directory))
    try:
        mod = importlib.import_module(f'OtlmowModel.Classes.{namespace}{class_name}')
        class_ = getattr(mod, class_name)
        instance = class_()
        return instance
    except ModuleNotFoundError:
        raise ModuleNotFoundError(f'When dynamically creating an object of class {class_name}, the import failed. '
                                  f'Make sure you are directing to the (parent) directory where OtlmowModel is '
                                  f'located in.')


def dynamic_create_instance_from_uri(class_uri: str, model_directory: Path = None) -> object:
    if model_directory is None:
        current_file_path = Path(__file__)
        model_directory = current_file_path.parent.parent.parent

    if class_uri == 'http://purl.org/dc/terms/Agent':
        ns, name = None, 'Agent'
    else:
        ns, name = get_ns_and_name_from_uri(class_uri)
    created = dynamic_create_instance_from_ns_and_name(ns, name, model_directory=model_directory)
    if created is None:
        raise ValueError(f'{class_uri} is likely not a valid uri, it does not result in a created instance')
    return created


def dynamic_create_type_from_uri(class_uri: str, model_directory: Path = None) -> type:
    if model_directory is None:
        current_file_path = Path(__file__)
        model_directory = current_file_path.parent.parent.parent

    if class_uri == 'http://purl.org/dc/terms/Agent':
        ns, name = None, 'Agent'
    else:
        ns, name = get_ns_and_name_from_uri(class_uri)
    created = dynamic_create_type_from_ns_and_name(ns, name, model_directory=model_directory)
    if created is None:
        raise ValueError(f'{class_uri} is likely not a valid uri, it does not result in a created instance')
    return created

