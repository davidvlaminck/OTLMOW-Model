import pytest

from UnitTests.TestClasses.Classes.Onderdeel.AllCasesTestClass import AllCasesTestClass
from otlmow_model.Exceptions.CouldNotConvertToCorrectTypeError import CouldNotConvertToCorrectTypeError


class NonStringableObject(object):
    def __str__(self):
        pass


def test_full_test_on_testclass_kard_1(subtests):
    instance = AllCasesTestClass()
    with subtests.test(msg='empty instance'):
        assert instance.testKwantWrd is not None
        assert instance._testKwantWrd.field.waarde_shortcut_applicable

    with subtests.test(msg='assign values to kwantWrdField with kard 1'):
        instance.testKwantWrd.waarde = 1
        assert instance.testKwantWrd.waarde == 1.0
        assert instance.testKwantWrd.standaardEenheid == '%'
        instance.testKwantWrd.waarde = 2
        assert instance.testKwantWrd.waarde == 2

    with subtests.test(msg='assigning to readonly field of kwantWrdField with kard 1'):
        with pytest.raises(AttributeError):
            instance.testKwantWrd.standaardEenheid = 'A'


def test_full_test_on_testclass_kard_more(subtests):
    instance = AllCasesTestClass()
    with subtests.test(msg='empty instance'):
        assert instance.testKwantWrdMetKard is not None
        assert instance._testKwantWrdMetKard.field.waarde_shortcut_applicable

    with subtests.test(msg='assign value directly to kwantWrdField with kard *'):
        instance.testKwantWrdMetKard[0].waarde = 1.0
        assert instance.testKwantWrdMetKard[0].waarde == 1

    with subtests.test(msg='assign value to kwantWrdField with kard * by using add_empty_value method'):
        instance._testKwantWrdMetKard.add_empty_value()
        assert instance.testKwantWrdMetKard[0].waarde == 1
        instance.testKwantWrdMetKard[1].waarde = '2.5'
        assert instance.testKwantWrdMetKard[1].waarde == 2.5

    with subtests.test(msg='assign bad value to kwantWrdField with kard *'):
        with pytest.raises(CouldNotConvertToCorrectTypeError):
            instance.testKwantWrdMetKard[0].waarde = 'a'
