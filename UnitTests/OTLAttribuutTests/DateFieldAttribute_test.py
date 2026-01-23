import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import datetime
import pytest

from UnitTests.TestModel.OtlmowModel.Classes.Onderdeel.AllCasesTestClass import AllCasesTestClass
from UnitTests.TestModel.OtlmowModel.warnings.IncorrectTypeWarning import IncorrectTypeWarning


def test_datefield_with_correct_input(subtests):
    instance = AllCasesTestClass()
    with subtests.test(msg='empty instance'):
        assert instance.testDateField is None

    with subtests.test(msg='assign values to DateField with correct date'):
        with pytest.warns(IncorrectTypeWarning):
            instance.testDateField = '2020-01-01'
        assert instance.testDateField == datetime.date(2020, 1, 1)
        with pytest.warns(IncorrectTypeWarning):
            instance.testDateField = '2020-1-1'
        assert instance.testDateField == datetime.date(2020, 1, 1)
        with pytest.warns(IncorrectTypeWarning):
            instance.testDateField = '1/1/2020'
        assert instance.testDateField == datetime.date(2020, 1, 1)


def test_datefield_with_datetime_val(subtests,caplog):
    instance = AllCasesTestClass()
    with subtests.test(msg='empty instance'):
        assert instance.testDateField is None

    with pytest.warns(IncorrectTypeWarning):
        instance.testDateField = datetime.datetime(2020, 1, 1, 2, 2, 2)
