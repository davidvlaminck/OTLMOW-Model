import pytest

from otlmow_model.OtlmowModel.BaseClasses.IntegerField import IntegerField
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.Exceptions.CouldNotConvertToCorrectTypeError import CouldNotConvertToCorrectTypeError
from otlmow_model.OtlmowModel.warnings.IncorrectTypeWarning import IncorrectTypeWarning


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


@pytest.mark.parametrize("value, expected", [
    (None, None),
    (1, 1),
    (-2, -2)
])
def test_convert_to_correct_type_no_warnings(value, expected, caplog):
    assert IntegerField.convert_to_correct_type(value) == expected
    assert len(caplog.records) == 0


@pytest.mark.parametrize("value, expected", [
    (True, 1),
    (1.0, 1),
    (False, 0),
    ('-1', -1),
    ('2.0000', 2)
])
def test_convert_to_correct_type_with_warnings(value, expected, caplog):
    with pytest.warns(IncorrectTypeWarning):
        assert IntegerField.convert_to_correct_type(value) == expected


@pytest.mark.parametrize("value", [
    'a', 0.1, '0.1', object(), [], {}
])
def test_convert_to_incorrect_type(value):
    with pytest.raises(CouldNotConvertToCorrectTypeError):
        IntegerField.convert_to_correct_type(value)
