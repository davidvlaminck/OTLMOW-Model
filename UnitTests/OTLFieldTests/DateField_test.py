import datetime

import pytest

from otlmow_model.OtlmowModel.BaseClasses.DateField import DateField
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.Exceptions.CouldNotConvertToCorrectTypeError import CouldNotConvertToCorrectTypeError
from otlmow_model.OtlmowModel.warnings.IncorrectTypeWarning import IncorrectTypeWarning


def test_validate():
    date_attribute = OTLAttribuut(naam='date attribuut')
    assert DateField.validate(None, date_attribute)
    assert DateField.validate(datetime.date(2022, 1, 1), date_attribute)
    with pytest.raises(TypeError):
        DateField.validate('a', date_attribute)
    with pytest.raises(TypeError):
        DateField.validate('1', date_attribute)
    with pytest.raises(TypeError):
        DateField.validate([], date_attribute)
    with pytest.raises(TypeError):
        DateField.validate(object(), date_attribute)
    with pytest.raises(TypeError):
        DateField.validate(1.0, date_attribute)


def test_convert_to_correct_type(subtests):
    with subtests.test(msg='Correct values'):
        assert DateField.convert_to_correct_type(None) is None
        assert DateField.convert_to_correct_type(datetime.date(2020, 1, 1)) == datetime.date(2020, 1, 1)

    convertable_values_list = [('2020-01-01', datetime.date(2020, 1, 1)),
                               ('2020-1-1', datetime.date(2020, 1, 1)),
                               ('1/1/2020', datetime.date(2020, 1, 1)),
                               (10000000, datetime.date(1970, 4, 26)),
                               (datetime.datetime(2020, 1, 1, 2, 2, 2), datetime.date(2020, 1, 1))]
    for value, expected in convertable_values_list:
        with subtests.test(msg=f'Correct value after conversion: value = {value}'):
            with pytest.warns(IncorrectTypeWarning):
                assert DateField.convert_to_correct_type(value) == expected

    incorrect_values = ['a', 0.1, '0.1', object(), [], {}, True, False, datetime.time(2, 2, 2)]
    for value in incorrect_values:
        with subtests.test(msg=f'Could not perform conversion: value = {value}'):
            with pytest.raises(CouldNotConvertToCorrectTypeError):
                DateField.convert_to_correct_type(value)
