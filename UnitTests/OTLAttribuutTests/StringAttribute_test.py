import pytest

from UnitTests.TestModel.OtlmowModel.Classes.Onderdeel.AllCasesTestClass import AllCasesTestClass
from otlmow_model.OtlmowModel.Exceptions.CouldNotConvertToCorrectTypeError import CouldNotConvertToCorrectTypeError


class NonStringableObject(object):
    def __str__(self):
        pass


def test_full_test_on_testclass_kard_1(subtests):
    instance = AllCasesTestClass()
    with subtests.test(msg='empty instance'):
        assert instance.testStringField is None

    with subtests.test(msg='assign values to stringfield with kard 1'):
        instance.testStringField = '1'
        assert instance.testStringField == '1'
        instance.testStringField = '2'
        assert instance.testStringField == '2'


def test_full_test_on_testclass_kard_more(subtests):
    instance = AllCasesTestClass()
    with subtests.test(msg='empty instance'):
        assert instance.testStringFieldMetKard is None

    with subtests.test(msg='assign value to stringfield with kard * by using add_value method'):
        instance._testStringFieldMetKard.add_value('1')
        assert instance.testStringFieldMetKard[0] == '1'
        instance._testStringFieldMetKard.add_value('2')
        assert instance.testStringFieldMetKard[0] == '1'
        assert instance.testStringFieldMetKard[1] == '2'

    with subtests.test(msg='assign bad value to stringfield with kard * by using add_value method'):
        with pytest.raises(CouldNotConvertToCorrectTypeError):
            instance._testStringFieldMetKard.add_value(NonStringableObject())

    with subtests.test(msg='assign value directly to stringfield with kard *'):
        instance.testStringFieldMetKard = ['1']
        assert instance.testStringFieldMetKard[0] == '1'
        instance.testStringFieldMetKard = ['2']
        assert instance.testStringFieldMetKard[0] == '2'
        instance.testStringFieldMetKard = ['1', '2']
        assert instance.testStringFieldMetKard[0] == '1'
        assert instance.testStringFieldMetKard[1] == '2'
