from UnitTests.TestModel.OtlmowModel.Classes.Onderdeel.AllCasesTestClass import AllCasesTestClass


def test_from_dict_simple_attribute_with_cardinality_clear_values():
    instance = AllCasesTestClass()
    instance.testIntegerFieldMetKard = '88888888'
    instance.testStringFieldMetKard = '88888888'
    instance.testKeuzelijstMetKard = '88888888'

    assert instance.testIntegerFieldMetKard is None
    assert instance._testStringFieldMetKard.mark_to_be_cleared
    assert instance.testKeuzelijstMetKard is None
    assert instance._testKeuzelijstMetKard.mark_to_be_cleared
    assert instance.testStringFieldMetKard is None
    assert instance._testStringFieldMetKard.mark_to_be_cleared
