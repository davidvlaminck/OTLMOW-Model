import pytest


from UnitTests.TestModel.OtlmowModel.Classes.Onderdeel.AllCasesTestClass import AllCasesTestClass
from UnitTests.TestModel.OtlmowModel.Datatypes.DtcTestComplexType import DtcTestComplexTypeWaarden


def test_full_test_on_testclass_kard_1(subtests):
    instance = AllCasesTestClass()
    with subtests.test(msg='empty instance'):
        assert instance.testComplexType is not None

    with subtests.test(msg='assign values to testComplexType with kard 1'):
        assert instance.testComplexType is not None
        assert isinstance(instance.testComplexType, DtcTestComplexTypeWaarden)

        instance.testComplexType.testStringField = '1'
        assert instance.testComplexType.testStringField == '1'
        instance.testComplexType.testBooleanField = True
        assert instance.testComplexType.testBooleanField == True

    with subtests.test(msg='incorrect use of add_empty_value'):
        with pytest.raises(RuntimeError):
            instance._testComplexType.add_empty_value()

    with subtests.test(msg='incorrectly assign values to testComplexType with kard 1 directly'):
        with pytest.raises(ValueError):
            instance.testComplexType = '1'


def test_full_test_on_testclass_kard_more(subtests):
    instance = AllCasesTestClass()
    with subtests.test(msg='empty instance'):
        assert instance.testComplexTypeMetKard is not None

    with subtests.test(msg='assign value to ComplexType with kard * by using add_empty_value method'):
        assert instance.testComplexTypeMetKard is not None
        assert isinstance(instance.testComplexTypeMetKard, list)
        assert isinstance(instance.testComplexTypeMetKard[0], DtcTestComplexTypeWaarden)
        assert len(instance.testComplexTypeMetKard) == 1

        instance.testComplexTypeMetKard[0].testStringField = '1'
        assert instance.testComplexTypeMetKard[0].testStringField == '1'
        instance.testComplexTypeMetKard[0].testBooleanField = True
        assert instance.testComplexTypeMetKard[0].testBooleanField

        instance._testComplexTypeMetKard.add_empty_value()
        assert instance.testComplexTypeMetKard is not None
        assert isinstance(instance.testComplexTypeMetKard[1], DtcTestComplexTypeWaarden)
        assert len(instance.testComplexTypeMetKard) == 2

        instance.testComplexTypeMetKard[1].testStringField = '2'
        assert instance.testComplexTypeMetKard[1].testStringField == '2'
        instance.testComplexTypeMetKard[1].testBooleanField = False
        assert not instance.testComplexTypeMetKard[1].testBooleanField

    with subtests.test(msg='assign value directly to ComplexType with kard *'):
        waardeObject1 = DtcTestComplexTypeWaarden()
        waardeObject1.testStringField = '1'
        waardeObject1.testBooleanField = True

        waardeObject2 = DtcTestComplexTypeWaarden()
        waardeObject2.testStringField = '2'
        waardeObject2.testBooleanField = False

        instance.testComplexTypeMetKard = [waardeObject1]
        assert instance.testComplexTypeMetKard[0].testStringField == '1'
        assert instance.testComplexTypeMetKard[0].testBooleanField

        instance.testComplexTypeMetKard = [waardeObject2]
        assert instance.testComplexTypeMetKard[0].testStringField == '2'
        assert not instance.testComplexTypeMetKard[0].testBooleanField

        instance.testComplexTypeMetKard = [waardeObject1, waardeObject2]
        assert instance.testComplexTypeMetKard[0].testStringField == '1'
        assert instance.testComplexTypeMetKard[0].testBooleanField
        assert instance.testComplexTypeMetKard[1].testStringField == '2'
        assert not instance.testComplexTypeMetKard[1].testBooleanField


def test_complex_kard_in_complex_kard(subtests):
    instance = AllCasesTestClass()
    with subtests.test(msg='empty instance'):
        assert instance.testComplexTypeMetKard is not None

    with subtests.test(msg='assign value to ComplexType with kard *'):
        assert instance.testComplexTypeMetKard is not None
        assert isinstance(instance.testComplexTypeMetKard, list)
        assert isinstance(instance.testComplexTypeMetKard[0], DtcTestComplexTypeWaarden)
        assert len(instance.testComplexTypeMetKard) == 1
        instance.testComplexTypeMetKard[0].testStringField = '1'
        assert instance.testComplexTypeMetKard[0].testStringField == '1'
        instance.testComplexTypeMetKard[0].testBooleanField = True
        assert instance.testComplexTypeMetKard[0].testBooleanField

        instance._testComplexTypeMetKard.add_empty_value()
        assert instance.testComplexTypeMetKard is not None
        assert isinstance(instance.testComplexTypeMetKard[1], DtcTestComplexTypeWaarden)
        assert len(instance.testComplexTypeMetKard) == 2

        instance.testComplexTypeMetKard[1].testStringField = '2'
        assert instance.testComplexTypeMetKard[1].testStringField == '2'
        instance.testComplexTypeMetKard[1].testBooleanField = False
        assert not instance.testComplexTypeMetKard[1].testBooleanField

    with subtests.test(msg='assign value to ComplexType within ComplexType with kard *'):
        instance.testComplexTypeMetKard[0].testComplexType2MetKard[0].testStringField = '1.1'
        assert instance.testComplexTypeMetKard[0].testComplexType2MetKard[0].testStringField == '1.1'
