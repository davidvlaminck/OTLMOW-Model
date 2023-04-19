import pytest

from otlmow_model.BaseClasses.NonNegIntegerField import NonNegIntegerField
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Exceptions.CouldNotConvertToCorrectTypeError import CouldNotConvertToCorrectTypeError


def test_validate():
    non_neg_integer_attribute = OTLAttribuut(naam='non neg integer attribuut')
    assert NonNegIntegerField.validate(0, non_neg_integer_attribute)
    assert NonNegIntegerField.validate(1, non_neg_integer_attribute)
    with pytest.raises(ValueError):
        NonNegIntegerField.validate(-1, non_neg_integer_attribute)
    with pytest.raises(TypeError):
        NonNegIntegerField.validate('a', non_neg_integer_attribute)
    with pytest.raises(TypeError):
        NonNegIntegerField.validate('1', non_neg_integer_attribute)
    with pytest.raises(TypeError):
        NonNegIntegerField.validate([], non_neg_integer_attribute)
    with pytest.raises(TypeError):
        NonNegIntegerField.validate(object(), non_neg_integer_attribute)
    with pytest.raises(TypeError):
        NonNegIntegerField.validate(1.0, non_neg_integer_attribute)


def test_convert_to_correct_type(subtests, caplog):
    with subtests.test(msg='Correct values'):
        assert NonNegIntegerField.convert_to_correct_type(None) is None
        assert NonNegIntegerField.convert_to_correct_type(0) == 0
        assert NonNegIntegerField.convert_to_correct_type(1) == 1

    convertable_values_list = [(True, 1), (1.0, 1), (False, 0), ('2.0000', 2)]
    for value, expected in convertable_values_list:
        with subtests.test(msg=f'Correct value after conversion: value = {value}'):
            caplog.records.clear()
            assert NonNegIntegerField.convert_to_correct_type(value) == expected
            assert len(caplog.records) == 1
            caplog.records.clear()

    incorrect_values = ['a', 0.1, '0.1', object(), [], {}]
    for value in incorrect_values:
        with subtests.test(msg=f'Could not perform conversion: value = {value}'):
            with pytest.raises(CouldNotConvertToCorrectTypeError):
                NonNegIntegerField.convert_to_correct_type(value)
