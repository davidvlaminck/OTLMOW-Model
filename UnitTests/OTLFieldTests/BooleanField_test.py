import pytest

from UnitTests.TestModel.OtlmowModel.Classes.Onderdeel.AllCasesTestClass import AllCasesTestClass
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.Exceptions.CouldNotConvertToCorrectTypeError import CouldNotConvertToCorrectTypeError
from otlmow_model.OtlmowModel.warnings.IncorrectTypeWarning import IncorrectTypeWarning


def test_full_test_on_testclass():
    instance = AllCasesTestClass()
    assert instance.testBooleanField is None
    instance.testBooleanField = True
    assert instance.testBooleanField
    instance.testBooleanField = False
    assert not instance.testBooleanField


def test_validate():
    boolean_attribute = OTLAttribuut(naam='boolean attribuut')
    assert BooleanField.validate(True, boolean_attribute)
    assert BooleanField.validate(False, boolean_attribute)
    with pytest.raises(TypeError):
        BooleanField.validate('a', boolean_attribute)
    with pytest.raises(TypeError):
        BooleanField.validate([], boolean_attribute)
    with pytest.raises(TypeError):
        BooleanField.validate(object(), boolean_attribute)
    with pytest.raises(TypeError):
        BooleanField.validate(1, boolean_attribute)
    with pytest.raises(TypeError):
        BooleanField.validate(1.0, boolean_attribute)


@pytest.mark.parametrize("value, expected", [
    (None, None),
    (True, True),
    (False, False)
])
def test_convert_to_correct_type(subtests, value, expected):
    with subtests.test(msg='Correct values'):
        assert BooleanField.convert_to_correct_type(value) == expected


@pytest.mark.parametrize("value", [
    'a', '1', 'y', 'Y', object(), [], {}
])
def test_convert_to_incorrect_type(value):
    with pytest.raises(CouldNotConvertToCorrectTypeError):
        BooleanField.convert_to_correct_type(value)


@pytest.mark.parametrize("value, expected", [
    ('true', True),
    ('True', True),
    ('false', False),
    ('False', False),
    (1, True),
    (0, False)
])
def test_convert_to_correct_type_with_warning(subtests, value, expected, caplog):
    with pytest.warns(IncorrectTypeWarning):
        assert BooleanField.convert_to_correct_type(value) == expected
