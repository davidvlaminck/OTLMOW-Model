import unittest

from UnitTests.TestClasses.Classes.ImplementatieElement.AIMDBStatus import AIMDBStatus
from UnitTests.TestClasses.Classes.ImplementatieElement.AIMObject import AIMObject
from UnitTests.TestClasses.Classes.ImplementatieElement.AIMToestand import AIMToestand
from UnitTests.TestClasses.Classes.Onderdeel.AllCasesTestClass import AllCasesTestClass


class AbstractBehaviour(unittest.TestCase):
    def test_ErrorsOnInstantiateAbstractClasses(self):
        with self.assertRaises(TypeError):
            AIMDBStatus()
        with self.assertRaises(TypeError):
            AIMToestand()
        with self.assertRaises(TypeError):
            AIMObject()

    def test_TestAssignmentsOnSameClasses(self):
        instance = AllCasesTestClass()
        self.assertTrue(instance.typeURI == "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AllCasesTestClass")
        self.assertTrue(isinstance(instance, AllCasesTestClass))
        self.assertTrue(isinstance(instance, AIMObject))
        instance2 = AllCasesTestClass()

        instance.notitie = "notitie1"
        instance2.notitie = "notitie2"
        self.assertTrue(instance.notitie == "notitie1")
        self.assertTrue(instance2.notitie == "notitie2")

        instance3 = AllCasesTestClass()
        self.assertTrue(instance3.notitie is None)

        instance3.notitie = "notitie3"
        self.assertTrue(instance.notitie == "notitie1")
        self.assertTrue(instance2.notitie == "notitie2")
        self.assertTrue(instance3.notitie == "notitie3")
