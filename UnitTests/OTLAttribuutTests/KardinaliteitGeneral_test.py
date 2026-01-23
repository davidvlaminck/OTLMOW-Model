import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import pytest

from UnitTests.TestModel.OtlmowModel.Classes.Onderdeel.AllCasesTestClass import AllCasesTestClass


def test_basic_assignment():
    instance = AllCasesTestClass()
    instance.testStringFieldMetKard = ['geel', 'rood']
    assert instance.testStringFieldMetKard[0] == "geel"
    assert instance.testStringFieldMetKard[1] == "rood"


def test_basic_reassign():
    instance = AllCasesTestClass()
    instance.testStringFieldMetKard = ['geel']
    assert instance.testStringFieldMetKard[0] == "geel"

    instance.testStringFieldMetKard = ['geel', 'rood']
    assert instance.testStringFieldMetKard[0] == "geel"
    assert instance.testStringFieldMetKard[1] == "rood"

    instance.testStringFieldMetKard = None
    assert instance.testStringFieldMetKard is None


def test_two_instances():
    instance = AllCasesTestClass()
    instance.testStringFieldMetKard = ['geel', 'rood']
    instance2 = AllCasesTestClass()
    instance2.testStringFieldMetKard = ['blauw']

    assert instance.testStringFieldMetKard[0] == "geel"
    assert instance.testStringFieldMetKard[1] == "rood"
    assert instance2.testStringFieldMetKard[0] == "blauw"


def test_errors():
    instance = AllCasesTestClass()

    with pytest.raises(TypeError) as exc_number:
        instance.testStringFieldMetKard = 2
    assert str(exc_number.value) == "expecting a list in AllCasesTestClass.testStringFieldMetKard"

    with pytest.raises(TypeError) as exc_dict:
        instance.testStringFieldMetKard = {}
    assert str(exc_dict.value) == "expecting a list in AllCasesTestClass.testStringFieldMetKard"

    instance._testStringFieldMetKard.kardinaliteit_min = "2"
    instance._testStringFieldMetKard.kardinaliteit_max = "2"
    with pytest.raises(ValueError) as exc_list_one_short:
        instance.testStringFieldMetKard = ["geel"]
    assert str(exc_list_one_short.value) == "expecting at least 2 element(s) in AllCasesTestClass.testStringFieldMetKard"
    with pytest.raises(ValueError) as exc_list_one_too_many:
        instance.testStringFieldMetKard = ["geel", "rood", "blauw"]
    assert str(exc_list_one_too_many.value) == "expecting at most 2 element(s) in AllCasesTestClass.testStringFieldMetKard"
