import pytest

from UnitTests.TestClasses.Classes.Onderdeel.AllCasesTestClass import AllCasesTestClass


def test__iter__(subtests):
    instance = AllCasesTestClass()
    with subtests.test(msg='complex datatype'):
        assert [attr.objectUri for attr in instance.testComplexType] == \
               ['https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType.testBooleanField',
                'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType.testComplexType2',
                'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType.testComplexType2MetKard',
                'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType.testKwantWrd',
                'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType.testKwantWrdMetKard',
                'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType.testStringField',
                'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcTestComplexType.testStringFieldMetKard']

    with subtests.test(msg='union datatype'):
        assert [attr.objectUri for attr in instance.testUnionType] == \
               ['https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtuTestUnionType.unionKwantWrd',
                'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtuTestUnionType.unionString']

    with subtests.test(msg='dte datatype'):
        assert [attr.objectUri for attr in instance.testEenvoudigType] == \
               ['https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DteTestEenvoudigType.waarde']

    with subtests.test(msg='kwant wrd datatype'):
        assert [attr.objectUri for attr in instance.testKwantWrd] == \
               ['https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdTest.standaardEenheid',
                'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdTest.waarde']

    with subtests.test(msg='non waarden attribute'):
        with pytest.raises(TypeError):
            assert [attr.objectUri for attr in instance.testStringField] == []

