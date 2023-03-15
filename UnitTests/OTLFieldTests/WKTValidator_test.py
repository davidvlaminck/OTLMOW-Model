import unittest

from otlmow_model.BaseClasses.OTLAsset import OTLAsset
from otlmow_model.BaseClasses.WKTValidator import WKTValidator


class ComplexDataTypeFieldTests(unittest.TestCase):
    def test_WKT_valid(self):
        with self.subTest('testen POINT'):
            self.assertTrue(WKTValidator.validate_wkt("POINT (200001.0 200002.0)"))
            self.assertTrue(WKTValidator.validate_wkt("POINT (200001 200002)"))
            self.assertTrue(WKTValidator.validate_wkt("POINT (212345.678901 212345.678902)"))
            self.assertTrue(WKTValidator.validate_wkt("POINT Z (200001.0 200002.0 3.0)"))
            self.assertTrue(WKTValidator.validate_wkt("POINT Z (200001 200002 3)"))
            self.assertFalse(WKTValidator.validate_wkt("POINT Z (200001,0 200002,0 3,0)"))
            self.assertFalse(WKTValidator.validate_wkt("POINT Z (200001 200002)"))
            self.assertFalse(WKTValidator.validate_wkt("POINT (200001 200002 3)"))
            self.assertFalse(WKTValidator.validate_wkt("POINT(200001 200002)"))
            self.assertFalse(WKTValidator.validate_wkt("POINT (-200001 -200002)"))
            self.assertFalse(WKTValidator.validate_wkt("punt Z (200001 200002)"))

        with self.subTest('testen LINESTRING'):
            self.assertTrue(WKTValidator.validate_wkt("LINESTRING (200001.0 200002.0, 200003.0 200004.0)"))
            self.assertTrue(WKTValidator.validate_wkt("LINESTRING (200001 200002, 200003 200004)"))
            self.assertTrue(WKTValidator.validate_wkt("LINESTRING Z (200001.0 200002.0 3.0, 200004.0 200005.0 6.0)"))
            self.assertTrue(WKTValidator.validate_wkt("LINESTRING Z (200001.0 200002.0 3.0, 200004.0 200005.0 6.0, 200007.0 200008.0 9.0)"))
            self.assertTrue(WKTValidator.validate_wkt("LINESTRING Z (200001 200002 3, 200004 200005 6, 200007 200008 9)"))
            self.assertFalse(WKTValidator.validate_wkt("LINESTRING (200001,0 200002,0, 200003,0 200004,0)"))
            self.assertFalse(WKTValidator.validate_wkt("LINESTRING Z (200001.0 200002.0, 200004.0 200005.0)"))
            self.assertFalse(WKTValidator.validate_wkt("LINESTRING (200001 200002 5, 200003 200004 6)"))

        with self.subTest('testen POLYGON'):
            self.assertTrue(WKTValidator.validate_wkt("POLYGON ((200010 200020, 200030 200040, 200050 200060))"))
            self.assertFalse(WKTValidator.validate_wkt("POLYGON ((200010 200020, 200030 200040))"))
            self.assertTrue(WKTValidator.validate_wkt("POLYGON ((200010.0 200020.0, 200030.0 200040.0, 200050.0 200060.0))"))
            self.assertTrue(WKTValidator.validate_wkt("POLYGON ((200010.0 200020.0, 200030.0 200040.0, 200050.0 200060.0, 200070.0 200080.0))"))
            self.assertTrue(WKTValidator.validate_wkt("POLYGON Z ((200010.0 200020.0 1, 200030.0 200040.0 2, 200050.0 200060.0 3))"))
            self.assertFalse(WKTValidator.validate_wkt("POLYGON Z ((200010.0 200020.0, 200030.0 200040.0 2, 200050.0 200060.0))"))
            self.assertFalse(WKTValidator.validate_wkt("POLYGON ((200010.0 200020.0 1, 200030.0 200040.0 2, 200050.0 200060.0 3))"))
            self.assertTrue(
                WKTValidator.validate_wkt("POLYGON ((200010.0 200020.0, 200030.0 200040.0, 200050.0 200060.0), "
                                          "(200110.0 200120.0, 200130.0 200140.0, 200150.0 200160.0))"))
