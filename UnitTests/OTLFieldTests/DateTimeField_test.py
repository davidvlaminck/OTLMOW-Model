import datetime

import pytest

from otlmow_model.BaseClasses.DateTimeField import DateTimeField
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.BaseClasses.TimeField import TimeField
from otlmow_model.Exceptions.CouldNotConvertToCorrectTypeError import CouldNotConvertToCorrectTypeError


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


def test_convert_to_correct_type(subtests, caplog):
    with subtests.test(msg='Correct values'):
        assert DateTimeField.convert_to_correct_type(None) is None
        assert DateTimeField.convert_to_correct_type(datetime.datetime(2022, 2, 2, 10, 11, 12)) == datetime.datetime(2022, 2, 2, 10, 11, 12)

    convertable_values_list = [('2020-2-2 10:11:12', datetime.datetime(2020, 2, 2, 10, 11, 12)),
                               ('2/2/2020 10:11:12', datetime.datetime(2020, 2, 2, 10, 11, 12)),
                               (datetime.date(2020, 2, 2), datetime.datetime(2020, 2, 2)),
                               (10000000, datetime.datetime(1970, 4, 26, 17, 46, 40))]
    for value, expected in convertable_values_list:
        with subtests.test(msg=f'Correct value after conversion: value = {value}'):
            caplog.records.clear()
            assert DateTimeField.convert_to_correct_type(value) == expected
            assert len(caplog.records) == 1
            caplog.records.clear()

    incorrect_values = ['a', 0.1, '0.1', object(), [], {}, True, False, '24:99:00']
    for value in incorrect_values:
        with subtests.test(msg=f'Could not perform conversion: value = {value}'):
            with pytest.raises(CouldNotConvertToCorrectTypeError):
                DateTimeField.convert_to_correct_type(value)
