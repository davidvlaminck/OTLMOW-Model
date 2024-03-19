import pytest

from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField
from otlmow_model.OtlmowModel.Exceptions.CouldNotConvertToCorrectTypeError import CouldNotConvertToCorrectTypeError
from otlmow_model.OtlmowModel.warnings.IncorrectTypeWarning import IncorrectTypeWarning


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


@pytest.mark.parametrize("value, expected", [
    (None, None),
    ('a', 'a'),
    ('', ''),
    ('1', '1')
])
def test_convert_to_correct_type(subtests, value, expected):
    with subtests.test(msg='Correct values'):
        assert StringField.convert_to_correct_type(value) == expected


@pytest.mark.parametrize("value, expected", [
    (True, 'True'),
    (1.0, '1.0'),
    (False, 'False'),
    (-1, '-1'),
    (2.000, '2.0')
])
def test_convert_to_correct_type_with_warnings(value, expected, caplog):
    with pytest.warns(IncorrectTypeWarning):
        assert StringField.convert_to_correct_type(value) == expected


@pytest.mark.parametrize("value", [
    NonStringableObject(), [], {}
])
def test_convert_to_incorrect_type(subtests, caplog, value):
    with subtests.test(msg='Could not perform conversion'):
        with pytest.raises(CouldNotConvertToCorrectTypeError):
            StringField.convert_to_correct_type(value)
