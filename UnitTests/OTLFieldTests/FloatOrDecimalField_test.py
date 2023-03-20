import decimal

import pytest

from otlmow_model.BaseClasses.FloatOrDecimalField import FloatOrDecimalField
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Exceptions.CouldNotConvertToCorrectTypeError import CouldNotConvertToCorrectTypeError


def test_validate():
    float_attribute = OTLAttribuut(naam='float attribuut')
    assert FloatOrDecimalField.validate(1.0, float_attribute)
    with pytest.raises(TypeError):
        FloatOrDecimalField.validate(1, float_attribute)
    with pytest.raises(TypeError):
        FloatOrDecimalField.validate('a', float_attribute)
    with pytest.raises(TypeError):
        FloatOrDecimalField.validate('1', float_attribute)
    with pytest.raises(TypeError):
        FloatOrDecimalField.validate([], float_attribute)
    with pytest.raises(TypeError):
        FloatOrDecimalField.validate(object(), float_attribute)


def test_convert_to_correct_type(subtests, caplog):
    with subtests.test(msg='Correct values'):
        assert FloatOrDecimalField.convert_to_correct_type(None) is None
        assert FloatOrDecimalField.convert_to_correct_type(1.0) == 1
        assert FloatOrDecimalField.convert_to_correct_type(-2) == -2
        assert FloatOrDecimalField.convert_to_correct_type(decimal.Decimal(1)) == 1.0
        assert FloatOrDecimalField.convert_to_correct_type(-2.345) == -2.345

    convertable_values_list = [(True, 1.0), (False, 0.0), ('-1', -1.0), ('2.0000', 2.0)]
    for value, expected in convertable_values_list:
        with subtests.test(msg=f'Correct value after conversion: value = {value}'):
            caplog.records.clear()
            assert FloatOrDecimalField.convert_to_correct_type(value) == expected
            assert len(caplog.records) == 1
            caplog.records.clear()

    incorrect_values = ['a', object(), [], {}]
    for value in incorrect_values:
        with subtests.test(msg=f'Could not perform conversion: value = {value}'):
            with pytest.raises(CouldNotConvertToCorrectTypeError):
                FloatOrDecimalField.convert_to_correct_type(value)
