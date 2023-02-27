from typing import Union

from otlmow_model.Classes.ImplementatieElement.AIMObject import AIMObject
from otlmow_model.Classes.ImplementatieElement.RelatieObject import RelatieObject
from otlmow_model.Helpers.GenericHelper import get_titlecase_from_ns, get_ns_and_name_from_uri


def dynamic_create_instance_from_ns_and_name(namespace: str, class_name: str,
                                             directory: str = 'otlmow_model.Classes') -> Union[AIMObject, RelatieObject]:
    """Loads the OTL class module and attempts to instantiate the class using the name and namespace of the class

    :param namespace: namespace of the class
    :type: str
    :param class_name: class name to instantiate
    :type: str
    :param directory: directory where the class modules are located, defaults to OTLMOW.OTLModel.Classes
    :type: str
    :return: returns an instance of class_name in the given namespace, located from directory, that inherits from AIMObject or RelatieObject
    :rtype: AIMObject, RelatieObject or None
    """

    if directory is None:
        directory = 'otlmow_model.Classes'

    if namespace is None:
        namespace = ''
    else:
        namespace = get_titlecase_from_ns(namespace)

    try:
        # TODO: check https://stackoverflow.com/questions/2724260/why-does-pythons-import-require-fromlist
        py_mod = __import__(name=f'{directory}.{namespace}.{class_name}', fromlist=f'{class_name}')
    except ModuleNotFoundError:
        return None
    class_ = getattr(py_mod, class_name)
    instance = class_()

    return instance


def dynamic_create_instance_from_uri(class_uri: str, directory: str = None) -> Union[AIMObject, RelatieObject]:
    if directory is None:
        directory = 'otlmow_model.Classes'

    ns, name = get_ns_and_name_from_uri(class_uri)
    created = dynamic_create_instance_from_ns_and_name(ns, name, directory=directory)
    if created is None:
        raise ValueError(f'{class_uri} is likely not a valid uri, it does not result in a created instance')
    return created