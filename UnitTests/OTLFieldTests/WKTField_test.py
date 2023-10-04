import pytest

from otlmow_model.BaseClasses.WKTField import WKTField


@pytest.mark.parametrize("input", [1, 1.0, object()])
def test_no_string_input(input):
    wkt_attribute = WKTField()
    with pytest.raises(TypeError):
        WKTField.validate(input, wkt_attribute)
