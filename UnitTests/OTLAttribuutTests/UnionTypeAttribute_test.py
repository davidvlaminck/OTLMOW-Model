import pytest

from UnitTests.TestModel.OtlmowModel.Classes.Onderdeel.AllCasesTestClass import AllCasesTestClass
from UnitTests.TestModel.OtlmowModel.Exceptions.CouldNotConvertToCorrectTypeError import CouldNotConvertToCorrectTypeError
from UnitTests.TestModel.OtlmowModel.Exceptions.UnionTypeError import UnionTypeError


class NonStringableObject(object):
    def __str__(self):
        pass


def test_full_test_on_testclass_kard_1(subtests):
    instance = AllCasesTestClass()
    with subtests.test(msg='empty instance'):
        assert instance.testStringField is None

    with subtests.test(msg='assign values to UnionType with kard 1'):
        instance.testUnionType.unionString = '1'
        assert instance.testUnionType.unionString == '1'
        instance.testUnionType.unionKwantWrd.waarde = 2
        assert instance.testUnionType.unionKwantWrd.waarde == 2
        assert instance.testUnionType.unionString is None

    with subtests.test(msg='setting None to UnionType with kard 1'):
        instance.testUnionType.unionKwantWrd.waarde = None
        assert instance.testUnionType.unionKwantWrd.waarde is None
        assert instance.testUnionType.unionString is None


def test_full_test_on_testclass_kard_more(subtests):
    instance = AllCasesTestClass()
    with subtests.test(msg='empty instance'):
        assert instance.testUnionTypeMetKard is not None

    with subtests.test(msg='assign value to UnionType with kard * by using add_empty_value method'):
        instance.testUnionTypeMetKard[0].unionString = '1'
        assert instance.testUnionTypeMetKard[0].unionString == '1'
        instance._testUnionTypeMetKard.add_empty_value()
        instance.testUnionTypeMetKard[1].unionKwantWrd.waarde = 2
        assert instance.testUnionTypeMetKard[0].unionString == '1'
        assert instance.testUnionTypeMetKard[1].unionKwantWrd.waarde == 2

    with subtests.test(msg='assign bad value to UnionType with kard *'):
        with pytest.raises(CouldNotConvertToCorrectTypeError):
            instance.testUnionTypeMetKard[1].unionKwantWrd.waarde = 'a'

    with subtests.test(msg='assign value directly to UnionType with kard *'):
        with pytest.raises(UnionTypeError):
            instance.testUnionTypeMetKard = ['1']
