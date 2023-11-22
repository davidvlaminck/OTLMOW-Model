import importlib
import sys
from pathlib import Path


from .GenericHelper import get_titlecase_from_ns, get_ns_and_name_from_uri


def dynamic_create_instance_from_ns_and_name(namespace: str, class_name: str,
                                             model_directory: Path = None):
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
    mod = importlib.import_module(f'OtlmowModel.Classes.{namespace}{class_name}')
    class_ = getattr(mod, class_name)
    instance = class_()
    return instance


    try:
        # TODO: check https://stackoverflow.com/questions/2724260/why-does-pythons-import-require-fromlist
        py_mod = __import__(name=f'OtlmowModel.Classes.{namespace}{class_name}', fromlist=f'{class_name}')
    except ModuleNotFoundError as ex:
        raise ex
        return None

    class_ = getattr(py_mod, class_name)
    instance = class_()
    return instance

    module = importlib.import_module(module_name, package=module_path)
    instance = module.AnotherTestClass()

    from OtlmowModel.Classes.Onderdeel.AnotherTestClass import AnotherTestClass
    instance = AnotherTestClass()
    print(instance)
    return instance

    if namespace == 'Onderdeel.' and class_name == 'AnotherTestClass':
        module_path = model_directory / 'Classes' / 'Onderdeel' / 'AnotherTestClass.py'
        module_name = 'AnotherTestClass'

        module = importlib.import_module(module_name, package=module_path)

        instance = module.AnotherTestClass()
        return instance


        spec = importlib.util.spec_from_file_location('AnotherTestClass', model_directory / 'Classes' / 'Onderdeel' / 'AnotherTestClass.py')
        module = importlib.util.module_from_spec(spec)
        sys.modules['AnotherTestClass'] = module
        spec.loader.exec_module(module)
        instance = module.AnotherTestClass()
        return instance



    if model_directory is None:
        model_directory = 'otlmow_model'

    try:
        # TODO: check https://stackoverflow.com/questions/2724260/why-does-pythons-import-require-fromlist
        py_mod = __import__(name=f'{model_directory}.Classes.{namespace}{class_name}', fromlist=f'{class_name}')
    except ModuleNotFoundError:
        return None
    class_ = getattr(py_mod, class_name)
    instance = class_()

    return instance


def dynamic_create_instance_from_uri(class_uri: str, model_directory: Path = None):
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
