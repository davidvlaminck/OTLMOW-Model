import pytest

from otlmow_model.OtlmowModel.Classes.ImplementatieElement.AIMNaamObject import NaamField


@pytest.mark.parametrize("value, expected, id", [
    ("validName123", True, "valid_alphanumeric"),
    ("valid.name-123", True, "valid_with_special_chars"),
    ("", True, "empty_string"),
    ("a", True, "single_character"),
    ("invalid name!", False, "invalid_with_space_and_exclamation"),
    ("invalid@name", False, "invalid_with_at_symbol")])
def test_validate(value, expected, id):
    result = NaamField.validate(value, None)
    assert result == expected, f"Test case '{id}' failed: expected {expected} but got {result}"
