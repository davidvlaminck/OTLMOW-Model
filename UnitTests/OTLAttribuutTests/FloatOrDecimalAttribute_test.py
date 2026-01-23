import pytest

from UnitTests.TestModel.OtlmowModel.Classes.Onderdeel.AllCasesTestClass import AllCasesTestClass
from UnitTests.TestModel.OtlmowModel.Exceptions.CouldNotConvertToCorrectTypeError import CouldNotConvertToCorrectTypeError
from UnitTests.TestModel.OtlmowModel.warnings.IncorrectTypeWarning import IncorrectTypeWarning


def test_full_test_on_testclass_kard_1(subtests):
    instance = AllCasesTestClass()
    with subtests.test(msg='empty instance'):
        assert instance.testDecimalField is None

    with subtests.test(msg='assign values to DecimalField with kard 1'):
        instance.testDecimalField = 1.0
        assert instance.testDecimalField == 1.0
        instance.testDecimalField = 2
        assert instance.testDecimalField == 2


def test_full_test_on_testclass_kard_more(subtests, caplog):
    with subtests.test(msg='empty instance'):
        instance = AllCasesTestClass()
        assert instance.testDecimalFieldMetKard is None

    with subtests.test(msg='assign value to DecimalField with kard * by using add_value method'):
        instance = AllCasesTestClass()
        instance._testDecimalFieldMetKard.add_value(1.0)
        assert instance.testDecimalFieldMetKard[0] == 1.0
        instance._testDecimalFieldMetKard.add_value(2)
        assert instance.testDecimalFieldMetKard[0] == 1.0
        assert instance.testDecimalFieldMetKard[1] == 2

    with subtests.test(msg='assign bad value to DecimalField with kard * by using add_value method'):
        instance = AllCasesTestClass()
        with pytest.raises(CouldNotConvertToCorrectTypeError):
            instance._testDecimalFieldMetKard.add_value('a')

    with subtests.test(msg='assign values directly to DecimalField with kard *'):
        instance = AllCasesTestClass()
        instance.testDecimalFieldMetKard = [1.0]
        assert instance.testDecimalFieldMetKard[0] == 1.0
        instance.testDecimalFieldMetKard = [2]
        assert instance.testDecimalFieldMetKard[0] == 2
        instance.testDecimalFieldMetKard = [1.0, 2]
        assert instance.testDecimalFieldMetKard[0] == 1.0
        assert instance.testDecimalFieldMetKard[1] == 2

    with subtests.test(msg='assign good and bad typed value directly to DecimalField with kard *'):
        with pytest.raises(CouldNotConvertToCorrectTypeError):
            instance.testDecimalFieldMetKard = ['a']
        with pytest.warns(IncorrectTypeWarning):
            instance.testDecimalFieldMetKard = [1.0, '2']
            assert instance.testDecimalFieldMetKard[0] == 1.0
            assert instance.testDecimalFieldMetKard[1] == 2
