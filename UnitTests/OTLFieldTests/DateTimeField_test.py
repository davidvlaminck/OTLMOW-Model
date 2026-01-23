import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import datetime

import pytest

from otlmow_model.OtlmowModel.BaseClasses.DateTimeField import DateTimeField
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.TimeField import TimeField
from otlmow_model.OtlmowModel.Exceptions.CouldNotConvertToCorrectTypeError import CouldNotConvertToCorrectTypeError
from otlmow_model.OtlmowModel.warnings.IncorrectTypeWarning import IncorrectTypeWarning


def test_validate():
    datetime_attribute = OTLAttribuut(naam='datetime attribuut')
    assert DateTimeField.validate(None, datetime_attribute)
    assert DateTimeField.validate(datetime.datetime(2022, 2, 2, 10, 11, 12), datetime_attribute)
    with pytest.raises(TypeError):
        TimeField.validate('a', datetime_attribute)
    with pytest.raises(TypeError):
        TimeField.validate('1', datetime_attribute)
    with pytest.raises(TypeError):
        TimeField.validate([], datetime_attribute)
    with pytest.raises(TypeError):
        TimeField.validate(object(), datetime_attribute)
    with pytest.raises(TypeError):
        TimeField.validate(1.0, datetime_attribute)


@pytest.mark.parametrize("value, expected", [
    (None, None),
    (datetime.datetime(2022, 2, 2, 10, 11, 12), datetime.datetime(2022, 2, 2, 10, 11, 12)),
])
def test_convert_to_correct_type_no_warnings(value, expected, caplog):
    assert DateTimeField.convert_to_correct_type(value) == expected
    assert len(caplog.records) == 0


@pytest.mark.parametrize("value, expected", [
    ('2020-2-2 10:11:12', datetime.datetime(2020, 2, 2, 10, 11, 12)),
    ('2/2/2020 10:11:12', datetime.datetime(2020, 2, 2, 10, 11, 12)),
    (datetime.date(2020, 2, 2), datetime.datetime(2020, 2, 2)),
    (10000000, datetime.datetime(1970, 4, 26, 17, 46, 40))
])
def test_convert_to_correct_type_with_warnings(value, expected, caplog):
    with pytest.warns(IncorrectTypeWarning):
        assert DateTimeField.convert_to_correct_type(value) == expected


@pytest.mark.parametrize("value", [
    'a', 0.1, '0.1', object(), [], {}, True, False, '24:99:00'
])
def test_convert_to_incorrect_type(value):
    with pytest.raises(CouldNotConvertToCorrectTypeError):
        DateTimeField.convert_to_correct_type(value)