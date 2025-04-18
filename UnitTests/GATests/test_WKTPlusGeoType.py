import pytest

from otlmow_model.OtlmowModel.BaseClasses.OTLAsset import OTLAsset
from otlmow_model.OtlmowModel.Exceptions.WrongGeometryTypeError import WrongGeometryTypeError
from otlmow_model.OtlmowModel.Exceptions.WrongGeometryWarning import WrongGeometryWarning
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


class PointTestClass(PuntGeometrie, OTLAsset):
    typeURI = '#PointTestClass'

    def __init__(self):
        super().__init__()


class PointPolygonTestClass(PuntGeometrie, VlakGeometrie, OTLAsset):
    typeURI = '#PointPolygonTestClass'

    def __init__(self):
        super().__init__()


def test_point(subtests):
    puntclass = PointTestClass()

    with subtests.test(msg='valid point'):
        puntclass.geometry = 'POINT Z (200001 200002 3)'
        assert puntclass.geometry is not None

    with subtests.test(msg='invalid points'):
        with pytest.raises(WrongGeometryTypeError):
            puntclass.geometry = 'POINT (200001 200002)'
        with pytest.raises(ValueError):
            puntclass.geometry = 'POINT Z (200001 200002,0 3)'
        with pytest.raises(ValueError):
            puntclass.geometry = 'POINT Z (200001 200002,0 703)'


def test_point_polygon(subtests):
    puntvlakclass = PointPolygonTestClass()

    with subtests.test(msg='valid point'):
        puntvlakclass.geometry = 'POINT Z (200001 200002 3)'
        assert puntvlakclass.geometry is not None

    with subtests.test(msg='valid point with negative coordinate'):
        puntvlakclass.geometry = 'POINT Z (200001 200002 -3)'
        assert puntvlakclass.geometry is not None

    with subtests.test(msg='valid polygon'):
        puntvlakclass.geometry = 'POLYGON Z ((200010.0 200020.0 1, 200030.0 200040.0 2, 200050.0 200060.0 3))'
        assert puntvlakclass.geometry is not None

    with subtests.test(msg='invalid points'):
        with pytest.raises(WrongGeometryTypeError):
            puntvlakclass.geometry = 'POINT (200001 220000)'
        with pytest.raises(ValueError):
            puntvlakclass.geometry = 'POINT Z (200001 200002,0 3)'

    with subtests.test(msg='invalid points (outside box)'):
        with pytest.raises(WrongGeometryTypeError):
            puntvlakclass.geometry = 'POINT (200001 200002)'
        with pytest.raises(ValueError):
            puntvlakclass.geometry = 'POINT Z (1 2,0 3)'

    with subtests.test(msg='invalid polygons'):
        with pytest.raises(WrongGeometryTypeError):
            puntvlakclass.geometry = 'POLYGON ((200010 200020, 200030 200040, 200050 200060))'
        with pytest.raises(ValueError):
            puntvlakclass.geometry = 'POLYGON Z ((200010.0 200020.0, 200030.0 200040.0 2, 200050.0 200060.0))'


def test_invalid_geometry_based_on_geometry_artefact():
    instance = PointPolygonTestClass()
    with pytest.raises(WrongGeometryTypeError) as wrong_geometry_exception:
        instance.geometry = 'LINESTRING Z (200001 200002 10, 200003 200004 20)'
    expected_msg = "Asset type PointPolygonTestClass shouldn't be assigned a LINESTRING Z as geometry, " \
                   "valid types are POINT Z and POLYGON Z"
    assert expected_msg == wrong_geometry_exception.value.args[0]
