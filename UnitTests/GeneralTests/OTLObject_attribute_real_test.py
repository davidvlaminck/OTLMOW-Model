"""Characterisation tests for the real package's OTLAttribuut attribute model.

These tests import from the real ``otlmow_model.OtlmowModel.BaseClasses`` modules
(hand-written, stable) and construct minimal attribute/owner objects inline, so
they do not depend on the generated ``Classes``/``Datatypes`` trees.

Purpose: pin the behaviour of the attribute model that was split out of
``OTLObject.py`` into ``BaseClasses/OTLAttribuut.py``
(code_quality/REFACTOR_LOG.md).
"""

import warnings

import pytest
from otlmow_model.OtlmowModel.BaseClasses.ComplexField import ComplexField
from otlmow_model.OtlmowModel.BaseClasses.IntegerField import IntegerField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde
from otlmow_model.OtlmowModel.BaseClasses.OTLAttribuut import OTLAttribuut, get_attribute_by_name, get_attribute_by_uri
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField
from otlmow_model.OtlmowModel.BaseClasses.UnionTypeField import UnionTypeField
from otlmow_model.OtlmowModel.BaseClasses.UnionWaarden import UnionWaarden
from otlmow_model.OtlmowModel.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.OtlmowModel.Exceptions.AttributeDeprecationWarning import AttributeDeprecationWarning
from otlmow_model.OtlmowModel.Exceptions.CanNotClearAttributeError import CanNotClearAttributeError
from otlmow_model.OtlmowModel.Exceptions.MethodNotApplicableError import MethodNotApplicableError


def _attr(field, naam, object_uri=None, owner=None, **kwargs):
    if object_uri is None:
        object_uri = 'https://example.com#T.' + naam
    return OTLAttribuut(field=field, naam=naam, label=naam, objectUri=object_uri, owner=owner, **kwargs)


class _Owner:
    def __init__(self):
        self._s = _attr(StringField, 's', owner=self)

    def __iter__(self):
        yield from vars(self).values()


class _ClearingIntegerField(IntegerField):
    clearing_value = 88888888


class _InvalidValueField(StringField):
    @classmethod
    def validate(cls, *args: object, **kwargs: object) -> bool:
        return False


class _DocWaarden(WaardenObject):
    def __init__(self):
        self._parent = None
        self._is_waarden_object = True
        self._bestandsnaam = _attr(StringField, 'bestandsnaam', owner=self)


class _DtcDoc(ComplexField):
    waardeObject = _DocWaarden


class _UnionWaarden(UnionWaarden):
    def __init__(self):
        super().__init__()
        self._a = _attr(StringField, 'a', owner=self)
        self._b = _attr(StringField, 'b', owner=self)


class _UnionField(UnionTypeField):
    waardeObject = _UnionWaarden


class _KwantWrdWaarden(WaardenObject):
    def __init__(self):
        self._parent = None
        self._is_waarden_object = True
        self._waarde = _attr(StringField, 'waarde', owner=self)


class _KwantWrdField(ComplexField):
    waarde_shortcut_applicable = True
    waardeObject = _KwantWrdWaarden


def test_get_attribute_by_name_and_uri():
    owner = _Owner()
    assert get_attribute_by_name(owner, 's') is owner._s
    assert get_attribute_by_name(owner, 'nope') is None
    assert get_attribute_by_uri(owner, 'https://example.com#T.s') is owner._s
    assert get_attribute_by_uri(owner, 'https://example.com#T.nope') is None


def test_clear_value_simple_attribute():
    attribute = _attr(StringField, 's')
    attribute.waarde = 'x'
    attribute.clear_value()
    assert attribute.waarde is None
    assert attribute.mark_to_be_cleared is True


def test_clear_value_readonly_attribute_raises():
    attribute = _attr(StringField, 's', readonly=True, readonlyValue='x')
    with pytest.raises(ValueError, match='is readonly'):
        attribute.clear_value()


def test_clear_value_blocked_attribute_raises():
    attribute = _attr(
        StringField,
        'naam',
        object_uri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMNaamObject.naam',
    )
    with pytest.raises(CanNotClearAttributeError, match='can not be cleared'):
        attribute.clear_value()


def test_clear_value_blocked_by_parent_dtc_identificator():
    class _Parent:
        def __init__(self):
            self.field = _attr(
                StringField,
                'field',
                object_uri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator',
            )

    class _DtcOwner:
        def __init__(self):
            self._parent = _Parent()

    owner = _DtcOwner()
    attribute = _attr(StringField, 's', owner=owner)
    with pytest.raises(CanNotClearAttributeError, match='can not be cleared'):
        attribute.clear_value()


def test_clear_value_complex_attribute():
    attribute = _attr(_DtcDoc, 'doc')
    attribute.add_empty_value()
    attribute.waarde._bestandsnaam.waarde = 'report.pdf'
    attribute.clear_value()
    assert attribute.waarde._bestandsnaam.mark_to_be_cleared is True
    assert attribute.waarde._bestandsnaam.waarde is None


def test_clear_value_complex_attribute_with_cardinality():
    attribute = _attr(_DtcDoc, 'docs', kardinaliteit_max='*')
    attribute.add_empty_value()
    attribute.add_empty_value()
    attribute.waarde[0]._bestandsnaam.waarde = 'a.pdf'
    attribute.waarde[1]._bestandsnaam.waarde = 'b.pdf'
    attribute.clear_value()
    for item in attribute.waarde:
        assert item._bestandsnaam.waarde is None
        assert item._bestandsnaam.mark_to_be_cleared is True


def test_set_waarde_none_resets_value():
    attribute = _attr(StringField, 's')
    attribute.waarde = 'x'
    attribute.set_waarde(None)
    assert attribute.waarde is None


def test_set_waarde_clearing_value_clears_attribute():
    attribute = _attr(_ClearingIntegerField, 'i')
    attribute.waarde = 5
    attribute.set_waarde(88888888)
    assert attribute.waarde is None
    assert attribute.mark_to_be_cleared is True


def test_set_waarde_list_with_cardinality():
    attribute = _attr(StringField, 's', kardinaliteit_max='*')
    attribute.set_waarde(['a', 'b'])
    assert attribute.waarde == ['a', 'b']


def test_set_waarde_list_too_few_elements_raises():
    attribute = _attr(StringField, 's', kardinaliteit_min='2', kardinaliteit_max='*')
    with pytest.raises(ValueError, match='expecting at least 2 element'):
        attribute.set_waarde(['a'])


def test_set_waarde_list_with_invalid_value_raises():
    attribute = _attr(_InvalidValueField, 's', kardinaliteit_max='*')
    with pytest.raises(ValueError, match='invalid value in list'):
        attribute.set_waarde(['a'])


def test_set_waarde_invalid_value_raises():
    attribute = _attr(_InvalidValueField, 'i')
    with pytest.raises(ValueError, match='is not valid'):
        attribute.set_waarde('not-a-number')


def test_set_waarde_keuzelijst_converts_to_invulwaarde():
    attribute = _attr(KeuzelijstField, 'k')
    attribute.field.options = {'a': KeuzelijstWaarde(invulwaarde='a', objectUri='https://example.com#a')}
    attribute.set_waarde('https://example.com#a')
    assert attribute.waarde == 'a'


def test_set_waarde_on_union_member_clears_other_props():
    union_waarden = _UnionWaarden()
    member = _attr(_KwantWrdField, 'unionKwantWrd', owner=union_waarden)
    union_waarden._a.waarde = 'kept'
    member.add_empty_value()
    member.waarde._waarde.set_waarde('12.5', owner=member)
    assert member.waarde._waarde.waarde == '12.5'
    assert union_waarden._a.waarde is None


def test_get_waarde_creates_empty_complex_value():
    attribute = _attr(_DtcDoc, 'doc')
    assert attribute.get_waarde() is not None
    assert isinstance(attribute.waarde, _DocWaarden)


def test_add_empty_value_on_simple_attribute_raises():
    attribute = _attr(StringField, 's')
    with pytest.raises(MethodNotApplicableError, match='one of these types'):
        attribute.add_empty_value()


def test_add_value_on_cardinality_one_attribute_raises():
    attribute = _attr(StringField, 's')
    with pytest.raises(MethodNotApplicableError, match='cardinality other than 1'):
        attribute.add_value('x')


def test_add_value_on_list_attribute_appends():
    attribute = _attr(StringField, 's', kardinaliteit_max='*')
    attribute.add_value('a')
    attribute.add_value('b')
    assert attribute.waarde == ['a', 'b']


def test_add_empty_value_twice_on_cardinality_one_raises():
    attribute = _attr(_DtcDoc, 'doc')
    attribute.add_empty_value()
    with pytest.raises(RuntimeError, match='cardinality other than 1'):
        attribute.add_empty_value()


def test_fill_with_dummy_data_readonly_is_noop():
    attribute = _attr(StringField, 's', readonly=True, readonlyValue='x')
    attribute.fill_with_dummy_data()
    assert attribute.waarde == 'x'


def test_fill_with_dummy_data_simple_attribute():
    attribute = _attr(StringField, 's')
    attribute.fill_with_dummy_data()
    assert attribute.waarde is not None


def test_fill_with_dummy_data_complex_attribute():
    attribute = _attr(_DtcDoc, 'doc')
    attribute.fill_with_dummy_data()
    assert attribute.waarde._bestandsnaam.waarde is not None


def test_fill_with_dummy_data_union_attribute():
    attribute = _attr(_UnionField, 'u')
    attribute.fill_with_dummy_data()
    assert attribute.waarde is not None


def test_deprecation_warning_on_deprecated_attribute():
    attribute = _attr(StringField, 's', deprecated_version='2.13.0')
    with pytest.warns(AttributeDeprecationWarning):
        attribute.set_waarde('x')


def test_deprecation_warning_on_deprecated_owner_with_typeuri():
    class _DeprecatedOwner:
        typeURI = 'https://example.com#Deprecated'
        deprecated_version = '2.13.0'

    class _Container:
        def __init__(self, parent):
            self._parent = parent

    attribute = _attr(StringField, 'waarde', owner=_Container(_DeprecatedOwner()))
    with pytest.warns(AttributeDeprecationWarning, match='https://example.com#Deprecated is deprecated'):
        attribute.set_waarde('x')


def test_deprecation_warning_on_deprecated_owner_without_typeuri():
    class _PlainDeprecatedOwner:
        deprecated_version = '2.13.0'

    class _Container:
        def __init__(self, parent):
            self._parent = parent

    attribute = _attr(StringField, 'waarde', owner=_Container(_PlainDeprecatedOwner()))
    with pytest.warns(AttributeDeprecationWarning, match='used a class that is deprecated'):
        attribute.set_waarde('x')


def test_deprecation_check_without_owner_does_not_warn():
    with warnings.catch_warnings():
        warnings.simplefilter('error')
        OTLAttribuut._perform_deprecation_check(None)


def test_set_waarde_invalid_value_raises_with_the_owner_of_the_attribute():
    class _OwnerWithoutParent:
        pass

    attribute = _attr(_InvalidValueField, 'i', owner=_OwnerWithoutParent())
    with pytest.raises(ValueError, match=r'Could not assign the best effort converted value to _OwnerWithoutParent\.i'):
        attribute.set_waarde('not-a-number')


def test_set_waarde_invalid_value_raises_with_the_parent_of_the_owner():
    class _Parent:
        naam = 'parent'

    class _OwnerWithParent:
        def __init__(self):
            self._parent = _Parent()

    attribute = _attr(_InvalidValueField, 'i', owner=_OwnerWithParent())
    with pytest.raises(ValueError, match=r'Could not assign the best effort converted value to parent\.i'):
        attribute.set_waarde('not-a-number')


def test_set_waarde_list_with_a_value_that_is_not_a_list_raises():
    attribute = _attr(StringField, 's', kardinaliteit_max='*')
    with pytest.raises(TypeError, match='expecting a list in'):
        attribute.set_waarde('not-a-list')


def test_set_waarde_list_with_too_many_elements_raises():
    attribute = _attr(StringField, 's', kardinaliteit_max='2')
    with pytest.raises(ValueError, match='expecting at most 2 element'):
        attribute.set_waarde(['a', 'b', 'c'])


def test_clear_value_complex_attribute_without_value_creates_one():
    attribute = _attr(_DtcDoc, 'doc')
    attribute.clear_value()
    assert attribute.waarde is not None
    assert attribute.waarde._bestandsnaam.mark_to_be_cleared is True


def test_attribute_str_contains_metadata():
    attribute = _attr(StringField, 's', definition='the definition', usagenote='the usagenote')
    text = str(attribute)
    assert 'naam: s' in text
    assert 'definition: the definition' in text
    assert 'usagenote: the usagenote' in text
