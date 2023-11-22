import pytest

from UnitTests.TestModel.OtlmowModel.Classes.ImplementatieElement.AIMDBStatus import AIMDBStatus
from UnitTests.TestModel.OtlmowModel.Classes.ImplementatieElement.AIMObject import AIMObject
from UnitTests.TestModel.OtlmowModel.Classes.ImplementatieElement.AIMToestand import AIMToestand
from UnitTests.TestModel.OtlmowModel.Classes.Onderdeel.AllCasesTestClass import AllCasesTestClass


def test_ErrorsOnInstantiateAbstractClasses():
    with pytest.raises(TypeError):
        AIMDBStatus()
    with pytest.raises(TypeError):
        AIMToestand()
    with pytest.raises(TypeError):
        AIMObject()


def test_TestAssignmentsOnSameClasses():
    instance = AllCasesTestClass()
    assert instance.typeURI == "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass"
    assert isinstance(instance, AllCasesTestClass)
    assert isinstance(instance, AIMObject)
    instance2 = AllCasesTestClass()

    instance.notitie = "notitie1"
    instance2.notitie = "notitie2"
    assert instance.notitie == "notitie1"
    assert instance2.notitie == "notitie2"

    instance3 = AllCasesTestClass()
    assert instance3.notitie is None

    instance3.notitie = "notitie3"
    assert instance.notitie == "notitie1"
    assert instance2.notitie == "notitie2"
    assert instance3.notitie == "notitie3"
