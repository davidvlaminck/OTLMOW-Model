import pytest

from otlmow_model.OtlmowModel.Helpers.GenericHelper import get_titlecase_from_ns, get_aim_id_from_uuid_and_typeURI, \
    get_shortened_uri, get_ns_and_name_from_uri


def test_get_titlecase_from_ns(subtests):
    for ns_input, expected_output in {
        'ABSTRACTEN': 'Abstracten',
        'abstracten': 'Abstracten',
        'implementatieelement': 'ImplementatieElement',
        'installatie': 'Installatie',
        'levenscyclus': 'Levenscyclus',
        'onderdeel': 'Onderdeel',
        'proefenmeting': 'ProefEnMeting'
    }.items():
        with subtests.test(msg=f'testing {ns_input}, expecting {expected_output}'):
            assert get_titlecase_from_ns(ns_input) == expected_output

    with subtests.test(msg=f'unknown value'):
        with pytest.raises(ValueError):
            get_titlecase_from_ns('wrong input')


def test_get_aim_id_from_uuid_and_typeURI_happy_flow():
    uuid = '12345678-1234-1234-1234-123456789012'
    type_uri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TLCfiPoort'
    aim_id_expected = '12345678-1234-1234-1234-123456789012-b25kZXJkZWVsI1RMQ2ZpUG9vcnQ'

    assert get_aim_id_from_uuid_and_typeURI(uuid, type_uri) == aim_id_expected


def test_get_aim_id_from_uuid_and_typeURI_happy_flow_agent():
    uuid = '12345678-1234-1234-1234-123456789012'
    type_uri = 'http://purl.org/dc/terms/Agent'
    aim_id_expected = '12345678-1234-1234-1234-123456789012-cHVybDpBZ2VudA'

    assert get_aim_id_from_uuid_and_typeURI(uuid, type_uri) == aim_id_expected


def test_get_aim_id_from_uuid_and_typeURI_happy_flow_legacy():
    uuid = '12345678-1234-1234-1234-123456789012'
    type_uri = 'https://lgc.data.wegenenverkeer.be/ns/installatie#VPLMast'
    aim_id_expected = '12345678-1234-1234-1234-123456789012-bGdjOmluc3RhbGxhdGllI1ZQTE1hc3Q'

    assert get_aim_id_from_uuid_and_typeURI(uuid, type_uri) == aim_id_expected


def test_get_aim_id_from_uuid_and_typeURI_invalid_uuid():
    uuid = '0000'
    type_uri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TLCfiPoort'

    with pytest.raises(ValueError):
        get_aim_id_from_uuid_and_typeURI(uuid, type_uri)


def test_get_aim_id_from_uuid_and_typeURI_type_uri_not_a_uri():
    uuid = '12345678-1234-1234-1234-123456789012'
    type_uri = 'wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TLCfiPoort'

    with pytest.raises(ValueError):
        get_aim_id_from_uuid_and_typeURI(uuid, type_uri)

def test_get_shortened_uri():
    object_uri = 'https://lgc.data.wegenenverkeer.be/ns/installatie#AB'
    expected_output = 'lgc:installatie#AB'
    assert get_shortened_uri(object_uri) == expected_output

    object_uri = 'http://purl.org/dc/terms/Agent'
    expected_output = 'purl:Agent'
    assert get_shortened_uri(object_uri) == expected_output

    object_uri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersregelaar'
    expected_output = 'onderdeel#Verkeersregelaar'
    assert get_shortened_uri(object_uri) == expected_output

    with pytest.raises(ValueError):
        get_shortened_uri('invalid_uri')


def test_get_ns_and_name_from_uri():
    object_uri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersregelaar'
    expected_ns = 'onderdeel'
    expected_name = 'Verkeersregelaar'
    assert get_ns_and_name_from_uri(object_uri) == (expected_ns, expected_name)

    object_uri = 'https://lgc.data.wegenenverkeer.be/ns/installatie#AB'
    expected_ns = 'installatie'
    expected_name = 'AB'
    assert get_ns_and_name_from_uri(object_uri) == (expected_ns, expected_name)

    object_uri = 'http://purl.org/dc/terms/Agent'
    expected_ns = 'purl'
    expected_name = 'Agent'
    assert get_ns_and_name_from_uri(object_uri) == (expected_ns, expected_name)

    with pytest.raises(ValueError):
        get_ns_and_name_from_uri('invalid_uri')