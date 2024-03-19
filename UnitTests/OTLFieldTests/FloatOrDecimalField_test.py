import decimal

import pytest

from otlmow_model.OtlmowModel.BaseClasses.FloatOrDecimalField import FloatOrDecimalField
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.Exceptions.CouldNotConvertToCorrectTypeError import CouldNotConvertToCorrectTypeError
from otlmow_model.OtlmowModel.warnings.IncorrectTypeWarning import IncorrectTypeWarning


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


@pytest.mark.parametrize("value, expected", [
    (None, None),
    (1.0, 1),
    (-2, -2),
    (decimal.Decimal(1), 1.0),
    (-2.345, -2.345)
])
def test_convert_to_correct_type(subtests, value, expected, caplog):
    with subtests.test(msg='Correct values'):
        assert FloatOrDecimalField.convert_to_correct_type(value) == expected
        assert len(caplog.records) == 0


@pytest.mark.parametrize("value, expected", [
    (True, 1.0),
    (False, 0.0),
    ('-1', -1.0),
    ('2.0000', 2.0)
])
def test_convert_to_correct_type_with_warning(subtests, value, expected, caplog):
    with pytest.warns(IncorrectTypeWarning):
        assert FloatOrDecimalField.convert_to_correct_type(value) == expected

@pytest.mark.parametrize("value", [
    'a', object(), [], {}
])
def test_convert_to_incorrect_type(subtests, value):
    with subtests.test(msg='Incorrect values'):
        with pytest.raises(CouldNotConvertToCorrectTypeError):
            FloatOrDecimalField.convert_to_correct_type(value)



