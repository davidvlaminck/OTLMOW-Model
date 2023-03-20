import pytest

from UnitTests.TestClasses.Classes.Onderdeel.AllCasesTestClass import AllCasesTestClass
from otlmow_model.BaseClasses.BooleanField import BooleanField
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Exceptions.CouldNotConvertToCorrectTypeError import CouldNotConvertToCorrectTypeError


def test_full_test_on_testclass():
    instance = AllCasesTestClass()
    assert instance.testBooleanField is None
    instance.testBooleanField = True
    assert instance.testBooleanField
    instance.testBooleanField = False
    assert not instance.testBooleanField


def test_validate():
    boolean_attribute = OTLAttribuut(naam='boolean attribuut')
    assert BooleanField.validate(True, boolean_attribute)
    assert BooleanField.validate(False, boolean_attribute)
    with pytest.raises(TypeError):
        BooleanField.validate('a', boolean_attribute)
    with pytest.raises(TypeError):
        BooleanField.validate([], boolean_attribute)
    with pytest.raises(TypeError):
        BooleanField.validate(object(), boolean_attribute)
    with pytest.raises(TypeError):
        BooleanField.validate(1, boolean_attribute)
    with pytest.raises(TypeError):
        BooleanField.validate(1.0, boolean_attribute)


def test_convert_to_correct_type(subtests):
    with subtests.test(msg='Correct values'):
        assert BooleanField.convert_to_correct_type(None) is None
        assert BooleanField.convert_to_correct_type(True)
        assert not BooleanField.convert_to_correct_type(False)
        assert not BooleanField.convert_to_correct_type(0)
        assert BooleanField.convert_to_correct_type(1)

    incorrect_values = ['a', '1', 'y', 'Y', object(), [], {}]
    for value in incorrect_values:
        with subtests.test(msg=f'Could not perform conversion: value = {value}'):
            with pytest.raises(CouldNotConvertToCorrectTypeError):
                BooleanField.convert_to_correct_type(value)


def test_convert_to_correct_type_with_warning(subtests, caplog):
    convertable_values_dict = {'true': True, 'True': True, 'false': False, 'False': False}
    for value, expected in convertable_values_dict.items():
        with subtests.test(msg=f'Test correct value after conversion for value = {value}'):
            caplog.records.clear()
            assert BooleanField.convert_to_correct_type(value) == expected
            assert len(caplog.records) == 1
            assert 'Assigned a string to a boolean datatype. Automatically converted to the correct type. Please ' \
                   'change the type' in caplog.text
            caplog.records.clear()

    with subtests.test(msg=f'Test correct value after conversion for value = 0'):
        assert not BooleanField.convert_to_correct_type(0)
        assert len(caplog.records) == 1
        assert 'Assigned an integer to a boolean datatype. Automatically converted to the correct type. Please ' \
               'change the type' in caplog.text
        caplog.records.clear()

    with subtests.test(msg=f'Test correct value after conversion for value = 1'):
        assert BooleanField.convert_to_correct_type(1)
        assert len(caplog.records) == 1
        assert 'Assigned an integer to a boolean datatype. Automatically converted to the correct type. Please ' \
               'change the type' in caplog.text
        caplog.records.clear()
