import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from UnitTests.TestModel.OtlmowModel.Helpers.all_classes import *

def test_instantiate_test_using_import_all_script():
    test_class = AllCasesTestClass()
    assert test_class is not None
