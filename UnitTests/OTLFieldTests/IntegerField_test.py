import pytest

from otlmow_model.BaseClasses.IntegerField import IntegerField
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Exceptions.CouldNotConvertToCorrectTypeError import CouldNotConvertToCorrectTypeError


def test_validate():
    integer_attribute = OTLAttribuut(naam='integer attribuut')
    assert IntegerField.validate(None, integer_attribute)
    assert IntegerField.validate(0, integer_attribute)
    assert IntegerField.validate(1, integer_attribute)
    assert IntegerField.validate(-1, integer_attribute)
    with pytest.raises(TypeError):
        IntegerField.validate('a', integer_attribute)
    with pytest.raises(TypeError):
        IntegerField.validate('1', integer_attribute)
    with pytest.raises(TypeError):
        IntegerField.validate([], integer_attribute)
    with pytest.raises(TypeError):
        IntegerField.validate(object(), integer_attribute)
    with pytest.raises(TypeError):
        IntegerField.validate(1.0, integer_attribute)


def test_convert_to_correct_type(subtests, caplog):
    with subtests.test(msg='Correct values'):
        assert IntegerField.convert_to_correct_type(None) is None
        assert IntegerField.convert_to_correct_type(1) == 1
        assert IntegerField.convert_to_correct_type(-2) == -2

    convertable_values_list = [(True, 1), (1.0, 1), (False, 0), ('-1', -1), ('2.0000', 2)]
    for value, expected in convertable_values_list:
        with subtests.test(msg=f'Correct value after conversion: value = {value}'):
            caplog.records.clear()
            assert IntegerField.convert_to_correct_type(value) == expected
            assert len(caplog.records) == 1
            caplog.records.clear()

    incorrect_values = ['a', 0.1, '0.1', object(), [], {}]
    for value in incorrect_values:
        with subtests.test(msg=f'Could not perform conversion: value = {value}'):
            with pytest.raises(CouldNotConvertToCorrectTypeError):
                IntegerField.convert_to_correct_type(value)
