from otlmow_model.Helpers.GenericHelper import get_titlecase_from_ns, get_ns_and_name_from_uri


def dynamic_create_instance_from_ns_and_name(namespace: str, class_name: str,
                                             model_directory: str = 'otlmow_model'):
    """Loads the OTL class module and attempts to instantiate the class using the name and namespace of the class

    :param namespace: namespace of the class
    :type: str
    :param class_name: class name to instantiate
    :type: str
    :param directory: directory where the model is located, defaults to otlmow_model
    :type: str
    :return: returns an instance of class_name in the given namespace, located from directory, that inherits from AIMObject or RelatieObject
    :rtype: AIMObject, RelatieObject or None
    """

    if model_directory is None:
        model_directory = 'otlmow_model'

    if namespace is None:
        namespace = ''
    else:
        namespace = get_titlecase_from_ns(namespace) + '.'

    try:
        # TODO: check https://stackoverflow.com/questions/2724260/why-does-pythons-import-require-fromlist
        py_mod = __import__(name=f'{model_directory}.Classes.{namespace}{class_name}', fromlist=f'{class_name}')
    except ModuleNotFoundError:
        return None
    class_ = getattr(py_mod, class_name)
    instance = class_()

    return instance


def dynamic_create_instance_from_uri(class_uri: str, model_directory: str = None):
    if model_directory is None:
        model_directory = 'otlmow_model'

    if class_uri == 'http://purl.org/dc/terms/Agent':
        ns, name = None, 'Agent'
    else:
        ns, name = get_ns_and_name_from_uri(class_uri)
    created = dynamic_create_instance_from_ns_and_name(ns, name, model_directory=model_directory)
    if created is None:
        raise ValueError(f'{class_uri} is likely not a valid uri, it does not result in a created instance')
    return created
