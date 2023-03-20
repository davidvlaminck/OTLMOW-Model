import pytest

from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.BaseClasses.StringField import StringField
from otlmow_model.Exceptions.CouldNotConvertToCorrectTypeError import CouldNotConvertToCorrectTypeError


class NonStringableObject(object):
    def __str__(self):
        pass


def test_validate():
    string_attribute = OTLAttribuut(naam='string attribuut')
    assert StringField.validate('a', string_attribute)
    assert StringField.validate('', string_attribute)
    assert StringField.validate('abc', string_attribute)

    with pytest.raises(TypeError):
        StringField.validate(1, string_attribute)
    with pytest.raises(TypeError):
        StringField.validate(True, string_attribute)
    with pytest.raises(TypeError):
        StringField.validate([], string_attribute)
    with pytest.raises(TypeError):
        StringField.validate(object(), string_attribute)
    with pytest.raises(TypeError):
        StringField.validate(1.0, string_attribute)


def test_convert_to_correct_type(subtests, caplog):
    with subtests.test(msg='Correct values'):
        assert StringField.convert_to_correct_type(None) is None
        assert StringField.convert_to_correct_type('a') == 'a'
        assert StringField.convert_to_correct_type('') == ''
        assert StringField.convert_to_correct_type('1') == '1'

    convertable_values_list = [(True, 'True'), (1.0, '1.0'), (False, 'False'), (-1, '-1'), (2.000, '2.0')]
    for value, expected in convertable_values_list:
        with subtests.test(msg=f'Correct value after conversion: value = {value}'):
            caplog.records.clear()
            assert StringField.convert_to_correct_type(value) == expected
            assert len(caplog.records) == 1
            caplog.records.clear()

    incorrect_values = [NonStringableObject(), [], {}]
    for index, value in enumerate(incorrect_values):
        with subtests.test(msg=f'Could not perform conversion: valueindex = {index}'):
            with pytest.raises(CouldNotConvertToCorrectTypeError):
                StringField.convert_to_correct_type(value)
