from UnitTests.TestClasses.Classes.Onderdeel.AllCasesTestClass import AllCasesTestClass
from otlmow_model.Exceptions.CouldNotConvertToCorrectTypeError import CouldNotConvertToCorrectTypeError
from otlmow_model.Exceptions.UnionTypeError import UnionTypeError


class NonStringableObject(object):
    def __str__(self):
        pass


def test_full_test_on_testclass_kard_1(subtests):
    instance = AllCasesTestClass()
    with subtests.test(msg='empty instance'):
        assert instance.testStringField is None

    with subtests.test(msg='assign values to UnionType with kard 1'):
        instance.testUnionType.unionString = '1'
        self.assertEqual('1', instance.testUnionType.unionString)
        instance.testUnionType.unionKwantWrd.waarde = 2
        self.assertEqual(2, instance.testUnionType.unionKwantWrd.waarde)
        self.assertEqual(None, instance.testUnionType.unionString)

    with subtests.test(msg='setting None to UnionType with kard 1'):
        instance.testUnionType.unionKwantWrd.waarde = None
        self.assertEqual(None, instance.testUnionType.unionKwantWrd.waarde)
        self.assertEqual(None, instance.testUnionType.unionString)

def test_full_test_on_testclass_kard_more(self):
    instance = AllCasesTestClass()
    with subtests.test(msg='empty instance'):
        self.assertIsNotNone(instance.testUnionTypeMetKard)

    with subtests.test(msg='assign value to UnionType with kard * by using add_empty_value method'):
        instance.testUnionTypeMetKard[0].unionString = '1'
        self.assertEqual('1', instance.testUnionTypeMetKard[0].unionString)
        instance._testUnionTypeMetKard.add_empty_value()
        instance.testUnionTypeMetKard[1].unionKwantWrd.waarde = 2
        self.assertEqual('1', instance.testUnionTypeMetKard[0].unionString)
        self.assertEqual(2, instance.testUnionTypeMetKard[1].unionKwantWrd.waarde)

    with subtests.test(msg='assign bad value to UnionType with kard *'):
        with self.assertRaises(CouldNotConvertToCorrectTypeError):
            instance.testUnionTypeMetKard[1].unionKwantWrd.waarde = 'a'

    with subtests.test(msg='assign value directly to UnionType with kard *'):
        with self.assertRaises(UnionTypeError):
            instance.testUnionTypeMetKard = ['1']
