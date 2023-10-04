import datetime

import pytest

from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.BaseClasses.TimeField import TimeField
from otlmow_model.Exceptions.CouldNotConvertToCorrectTypeError import CouldNotConvertToCorrectTypeError


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


def test_convert_to_correct_type(subtests, caplog):
    with subtests.test(msg='Correct values'):
        assert TimeField.convert_to_correct_type(None) is None
        assert TimeField.convert_to_correct_type(datetime.time(10, 11, 12)) == datetime.time(10, 11, 12)

    convertable_values_list = [('10:11:12', datetime.time(10, 11, 12)), ('7:8:9', datetime.time(7, 8, 9)),
                               ('2020-1-1 10:11:12', datetime.time(10, 11, 12)), (datetime.date(1, 1, 1), datetime.time(0, 0, 0)),
                               ('1/1/2020 10:11:12', datetime.time(10, 11, 12)), (10000, datetime.time(2, 46, 40))]
    for value, expected in convertable_values_list:
        with subtests.test(msg=f'Correct value after conversion: value = {value}'):
            caplog.records.clear()
            assert TimeField.convert_to_correct_type(value) == expected
            assert len(caplog.records) == 1
            caplog.records.clear()

    incorrect_values = ['a', 0.1, '0.1', object(), [], {}, True, False, '24:99:00']
    for value in incorrect_values:
        with subtests.test(msg=f'Could not perform conversion: value = {value}'):
            with pytest.raises(CouldNotConvertToCorrectTypeError):
                TimeField.convert_to_correct_type(value)


def test_datetime_auto_converts_but_warns(caplog):
    time_attribute = OTLAttribuut(naam='time attribuut')
    assert TimeField.convert_to_correct_type(datetime.datetime(2021,11,12,22,12,12),time_attribute) == datetime.time(22,12,12)
    assert len(caplog.records) == 1
    caplog.records.clear()