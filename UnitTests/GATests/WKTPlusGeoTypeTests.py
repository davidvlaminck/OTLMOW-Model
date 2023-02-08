import unittest

from otlmow_model.Exceptions.WrongGeometryWarning import WrongGeometryWarning
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie
from otlmow_model.GeometrieTypes.VlakGeometrie import VlakGeometrie
from otlmow_model.BaseClasses.OTLAsset import OTLAsset


class PointTestClass(PuntGeometrie, OTLAsset):
    typeURI = '#PointTestClass'
    def __init__(self):
        PuntGeometrie.__init__(self)
        OTLAsset.__init__(self)


class PointPolygonTestClass(PuntGeometrie, VlakGeometrie, OTLAsset):
    typeURI = '#PointPolygonTestClass'
    def __init__(self):
        PuntGeometrie.__init__(self)
        VlakGeometrie.__init__(self)
        OTLAsset.__init__(self)


class WKTPlusGeoTypeTests(unittest.TestCase):
    def test_point(self):
        puntclass = PointTestClass()

        with self.subTest('valid point'):
            puntclass.geometry = 'POINT Z (200001 200002 3)'
            self.assertIsNotNone(puntclass.geometry)

        with self.subTest('invalid points'):
            with self.assertWarns(WrongGeometryWarning):
                puntclass.geometry = 'POINT (200001 200002)'
            with self.assertRaises(ValueError):
                puntclass.geometry = 'POINT Z (200001 200002,0 3)'
            with self.assertRaises(ValueError):
                puntclass.geometry = 'POINT Z (200001 200002,0 703)'

    def test_point_polygon(self):
        puntvlakclass = PointPolygonTestClass()

        with self.subTest('valid point'):
            puntvlakclass.geometry = 'POINT Z (200001 200002 3)'
            self.assertIsNotNone(puntvlakclass.geometry)

        with self.subTest('valid point with negative coordinate'):
            puntvlakclass.geometry = 'POINT Z (200001 200002 -3)'
            self.assertIsNotNone(puntvlakclass.geometry)

        with self.subTest('valid polygon'):
            puntvlakclass.geometry = 'POLYGON Z ((200010.0 200020.0 1, 200030.0 200040.0 2, 200050.0 200060.0 3))'
            self.assertIsNotNone(puntvlakclass.geometry)

        with self.subTest('invalid points'):
            with self.assertWarns(WrongGeometryWarning):
                puntvlakclass.geometry = 'POINT (200001 220000)'
            with self.assertRaises(ValueError):
                puntvlakclass.geometry = 'POINT Z (200001 200002,0 3)'

        with self.subTest('invalid points (outside box)'):
            with self.assertWarns(WrongGeometryWarning):
                puntvlakclass.geometry = 'POINT (200001 200002)'
            with self.assertRaises(ValueError):
                puntvlakclass.geometry = 'POINT Z (1 2,0 3)'

        with self.subTest('invalid polygons'):
            with self.assertWarns(WrongGeometryWarning):
                puntvlakclass.geometry = 'POLYGON ((200010 200020, 200030 200040, 200050 200060))'
            with self.assertRaises(ValueError):
                puntvlakclass.geometry = 'POLYGON Z ((200010.0 200020.0, 200030.0 200040.0 2, 200050.0 200060.0))'

    def test_invalid_geometry_based_on_geometry_artefact(self):
        instance = PointPolygonTestClass()
        with self.assertWarns(WrongGeometryWarning) as wrong_geometry_warning:
            instance.geometry = 'LINESTRING Z (200001 200002 10, 200003 200004 20)'
        expected_msg = "Asset type PointPolygonTestClass shouldn't be assigned a LINESTRING Z as geometry, " \
                       "valid types are POINT Z and POLYGON Z"
        self.assertEqual(expected_msg, str(wrong_geometry_warning.warning))
