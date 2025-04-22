from datetime import date, datetime, time

from UnitTests.TestModel.OtlmowModel.Datatypes.DtcTestComplexType import DtcTestComplexType
from UnitTests.TestModel.OtlmowModel.Datatypes.DtuTestUnionType import DtuTestUnionType
from UnitTests.TestModel.OtlmowModel.Datatypes.KlTestKeuzelijst import KlTestKeuzelijst
from UnitTests.TestModel.OtlmowModel.Datatypes.KwantWrdTest import KwantWrdTest
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from otlmow_model.OtlmowModel.BaseClasses.DateField import DateField
from otlmow_model.OtlmowModel.BaseClasses.DateTimeField import DateTimeField
from otlmow_model.OtlmowModel.BaseClasses.FloatOrDecimalField import FloatOrDecimalField
from otlmow_model.OtlmowModel.BaseClasses.IntegerField import IntegerField
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField
from otlmow_model.OtlmowModel.BaseClasses.TimeField import TimeField


def test_dummy_StringField():
    attr = OTLAttribuut(field=StringField)
    attr.fill_with_dummy_data()

    generated_dummy_waarde = attr.get_waarde()
    assert generated_dummy_waarde is not None
    assert isinstance(generated_dummy_waarde, str)
    assert generated_dummy_waarde.startswith('dummy_')
    assert 5 <= len(generated_dummy_waarde) <= 16


def test_dummy_StringFieldMetKard():
    attr = OTLAttribuut(field=StringField, kardinaliteit_max='*')
    attr.fill_with_dummy_data()

    generated_dummy_waarde = attr.get_waarde()
    assert  generated_dummy_waarde is not None
    assert isinstance(generated_dummy_waarde, list)
    assert len(generated_dummy_waarde) == 1
    assert isinstance(generated_dummy_waarde[0], str)
    assert generated_dummy_waarde[0].startswith('dummy_')
    assert 6 <= len(generated_dummy_waarde[0]) <= 16


def test_dummy_FloatOrDecimalField():
    attr = OTLAttribuut(field=FloatOrDecimalField)
    attr.fill_with_dummy_data()

    generated_dummy_waarde = attr.get_waarde()
    assert generated_dummy_waarde is not None
    assert isinstance(generated_dummy_waarde, float)


def test_dummy_IntegerField():
    attr = OTLAttribuut(field=IntegerField)
    attr.fill_with_dummy_data()

    generated_dummy_waarde = attr.get_waarde()
    assert generated_dummy_waarde is not None
    assert isinstance(generated_dummy_waarde, int)


def test_dummy_BooleanField():
    attr = OTLAttribuut(field=BooleanField)
    attr.fill_with_dummy_data()

    generated_dummy_waarde = attr.get_waarde()
    assert generated_dummy_waarde is not None
    assert generated_dummy_waarde in [False, True]


def test_dummy_DateField():
    attr = OTLAttribuut(field=DateField)
    attr.fill_with_dummy_data()

    generated_dummy_waarde = attr.get_waarde()
    assert generated_dummy_waarde is not None
    assert isinstance(generated_dummy_waarde, date)


def test_dummy_DateTimeField():
    attr = OTLAttribuut(field=DateTimeField)
    attr.fill_with_dummy_data()

    generated_dummy_waarde = attr.get_waarde()
    assert generated_dummy_waarde is not None
    assert isinstance(generated_dummy_waarde, datetime)


def test_dummy_TimeField():
    attr = OTLAttribuut(field=TimeField)
    attr.fill_with_dummy_data()

    generated_dummy_waarde = attr.get_waarde()
    assert generated_dummy_waarde is not None
    assert isinstance(generated_dummy_waarde, time)


def test_dummy_KeuzelijstField():
    attr = OTLAttribuut(field=KlTestKeuzelijst)
    attr.fill_with_dummy_data()

    generated_dummy_waarde = attr.get_waarde()
    assert generated_dummy_waarde is not None
    assert isinstance(generated_dummy_waarde, str)
    assert generated_dummy_waarde in attr.field.options.keys()


def test_dummy_KwantWrdField():
    attr = OTLAttribuut(field=KwantWrdTest)
    attr.fill_with_dummy_data()

    generated_dummy_waarde = attr.get_waarde()
    assert generated_dummy_waarde is not None
    assert generated_dummy_waarde.waarde is not None
    assert generated_dummy_waarde.standaardEenheid == '%'


def test_dummy_ComplexField():
    attr = OTLAttribuut(field=DtcTestComplexType)
    attr.fill_with_dummy_data()

    generated_dummy_waarde = attr.get_waarde()
    assert generated_dummy_waarde is not None
    assert generated_dummy_waarde.testStringFieldMetKard is not None
    assert generated_dummy_waarde.testBooleanField is not None
    assert generated_dummy_waarde.testComplexType2 is not None
    assert generated_dummy_waarde.testComplexType2MetKard[0].testKwantWrd.waarde is not None


def test_dummy_UnionField():
    attr = OTLAttribuut(field=DtuTestUnionType)
    attr.fill_with_dummy_data()

    generated_dummy_waarde = attr.get_waarde()
    assert generated_dummy_waarde is not None
    first = generated_dummy_waarde.unionKwantWrd.waarde is not None
    second = generated_dummy_waarde.unionString is not None
    assert first != second  # either first or second is True, but not both
