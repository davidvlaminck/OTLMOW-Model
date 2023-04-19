import pytest

from UnitTests.TestClasses.Classes.Onderdeel.AllCasesTestClass import AllCasesTestClass
from UnitTests.TestClasses.Classes.Onderdeel.AnotherTestClass import AnotherTestClass
from UnitTests.TestClasses.Classes.Onderdeel.Bevestiging import Bevestiging
from otlmow_model.Helpers.GenericHelper import get_titlecase_from_ns


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
