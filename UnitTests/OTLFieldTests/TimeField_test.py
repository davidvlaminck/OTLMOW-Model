import datetime

import pytest

from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.TimeField import TimeField
from otlmow_model.OtlmowModel.Exceptions.CouldNotConvertToCorrectTypeError import CouldNotConvertToCorrectTypeError
from otlmow_model.OtlmowModel.warnings.IncorrectTypeWarning import IncorrectTypeWarning


def test_validate():
    time_attribute = OTLAttribuut(naam='time attribuut')
    assert TimeField.validate(None, time_attribute)
    assert TimeField.validate(datetime.time(10, 11, 12), time_attribute)

    with pytest.raises(TypeError):
        TimeField.validate('a', time_attribute)
    with pytest.raises(TypeError):
        TimeField.validate('1', time_attribute)
    with pytest.raises(TypeError):
        TimeField.validate([], time_attribute)
    with pytest.raises(TypeError):
        TimeField.validate(object(), time_attribute)
    with pytest.raises(TypeError):
        TimeField.validate(1.0, time_attribute)


@pytest.mark.parametrize("value, expected", [
    (None, None),
    (datetime.time(10, 11, 12), datetime.time(10, 11, 12)),
])
def test_convert_to_correct_type(subtests, value, expected):
    with subtests.test(msg='Correct values'):
        assert TimeField.convert_to_correct_type(value) == expected


@pytest.mark.parametrize("value, expected", [
    ('10:11:12', datetime.time(10, 11, 12)),
    ('7:8:9', datetime.time(7, 8, 9)),
    ('2020-1-1 10:11:12', datetime.time(10, 11, 12)),
    (datetime.date(1, 1, 1), datetime.time(0, 0, 0)),
    ('1/1/2020 10:11:12', datetime.time(10, 11, 12)),
    (10000, datetime.time(2, 46, 40))
])
def test_convert_to_correct_type_with_warning(subtests, value, expected, caplog):
    with pytest.warns(IncorrectTypeWarning):
        assert TimeField.convert_to_correct_type(value) == expected


@pytest.mark.parametrize("value", [
    'a', 0.1, '0.1', object(), [], {}, True, False, '24:99:00'
])
def test_convert_to_incorrect_type(value):
    with pytest.raises(CouldNotConvertToCorrectTypeError):
        TimeField.convert_to_correct_type(value)
