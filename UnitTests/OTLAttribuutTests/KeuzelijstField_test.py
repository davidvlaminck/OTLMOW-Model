import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import pytest

from UnitTests.TestModel.OtlmowModel.Classes.Onderdeel.AllCasesTestClass import AllCasesTestClass
from UnitTests.TestModel.OtlmowModel.Exceptions.InvalidOptionError import InvalidOptionError
from UnitTests.TestModel.OtlmowModel.Exceptions.RemovedOptionError import RemovedOptionError


def test_adms_status(subtests):
    instance = AllCasesTestClass()
    with subtests.test(msg='ingebruik value'):
        instance.testKeuzelijst = 'waarde-4'
        assert instance.testKeuzelijst == 'waarde-4'

    with subtests.test(msg='uitgebruik value'):
        with pytest.warns(DeprecationWarning):
            instance.testKeuzelijst = 'waarde-5'
            assert instance.testKeuzelijst == 'waarde-5'

    with subtests.test(msg='verwijderd value'):
        with pytest.raises(RemovedOptionError):
            instance.testKeuzelijst = 'waarde-6'


def test_using_full_uri():
    instance = AllCasesTestClass()
    instance.testKeuzelijst = 'https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTestKeuzelijst/waarde-1'
    assert instance.testKeuzelijst == 'waarde-1'


def test_using_label():
    instance = AllCasesTestClass()
    instance.testKeuzelijst = 'waarde 1'
    assert instance.testKeuzelijst == 'waarde-1'


def test_assign_hyphen_get_None(subtests):
    instance = AllCasesTestClass()
    instance.testKeuzelijst = '-'
    assert instance.testKeuzelijst is None


def test_full_test_on_test_class_kard_1(subtests):
    instance = AllCasesTestClass()
    with subtests.test(msg='empty instance'):
        assert instance.testKeuzelijst is None

    with subtests.test(msg='assign values to Keuzelijst with kard 1'):
        instance.testKeuzelijst = 'waarde-1'
        assert instance.testKeuzelijst == 'waarde-1'


def test_full_test_on_test_class_kard_more(subtests):
    instance = AllCasesTestClass()
    with subtests.test(msg='empty instance'):
        assert instance.testKeuzelijstMetKard is None
        assert not instance._testKeuzelijstMetKard.field.waarde_shortcut_applicable

    with subtests.test(msg='assign value directly to KeuzelijstMetKard with kard *'):
        instance.testKeuzelijstMetKard = ['waarde-1']
        assert instance.testKeuzelijstMetKard[0] == 'waarde-1'

    with subtests.test(msg='assign value directly to KeuzelijstMetKard with kard *'):
        instance.testKeuzelijstMetKard = ['waarde-1', 'waarde 2']
        assert instance.testKeuzelijstMetKard[0] == 'waarde-1'
        assert instance.testKeuzelijstMetKard[1] == 'waarde-2'

    with subtests.test(msg='assign value to KeuzelijstMetKard with kard * by using add_value method'):
        instance._testKeuzelijstMetKard.add_value('waarde-3')
        assert instance.testKeuzelijstMetKard[0] == 'waarde-1'
        assert instance.testKeuzelijstMetKard[1] == 'waarde-2'
        assert instance.testKeuzelijstMetKard[2] == 'waarde-3'

    with subtests.test(msg='assign bad value to KeuzelijstMetKard with kard *'):
        with pytest.raises(ValueError):
            instance.testKeuzelijstMetKard = ['waarde-1', 'a']


def test_print_keuzelijstwaarde():
    instance = AllCasesTestClass()
    assert str(instance._testKeuzelijst.field.options['waarde-4']) == 'waarde-4'
    assert str(instance._testKeuzelijst.field.options['waarde-5']) == 'waarde-5 (uitgebruik)'
    assert str(instance._testKeuzelijst.field.options['waarde-6']) == 'waarde-6 (verwijderd)'


def test_fuzzy_matching():
    instance = AllCasesTestClass()
    with pytest.raises(InvalidOptionError) as excinfo:
        instance.testKeuzelijst = 'waarde-4a'

    assert (str(excinfo.value) ==
            'waarde-4a is not a valid option for testKeuzelijst, find the valid options using print(meta_info('
            '<object>, attribute="testKeuzelijst"))\nDid you mean one of these? "waarde-4"')
    assert excinfo.value.closest_matches == ['waarde-4']