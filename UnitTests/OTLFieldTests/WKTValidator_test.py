import pytest

from otlmow_model.BaseClasses.WKTValidator import WKTValidator


def test_WKT_valid(subtests):
    with subtests.test(msg='testen POINT'):
        assert WKTValidator.validate_wkt("POINT (200001.0 200002.0)")
        assert WKTValidator.validate_wkt("POINT (200001 200002)")
        assert WKTValidator.validate_wkt("POINT (212345.678901 212345.678902)")
        assert WKTValidator.validate_wkt("POINT Z (200001.0 200002.0 3.0)")
        assert WKTValidator.validate_wkt("POINT Z (200001 200002 3)")
        assert not WKTValidator.validate_wkt("POINT Z (200001,0 200002,0 3,0)")
        assert not WKTValidator.validate_wkt("POINT Z (200001 200002)")
        assert not WKTValidator.validate_wkt("POINT (200001 200002 3)")
        assert not WKTValidator.validate_wkt("POINT(200001 200002)")
        assert not WKTValidator.validate_wkt("POINT (-200001 -200002)")
        assert not WKTValidator.validate_wkt("punt Z (200001 200002)")
        assert WKTValidator.validate_wkt("MULTIPOINT ((200001.0 200002.0), (200001.0 200002.0)")
        assert WKTValidator.validate_wkt("MULTIPOINT Z ((200001.0 200002.0 3.0), (200001.0 200002.0 3.0)")

    with subtests.test(msg='testen LINESTRING'):
        assert WKTValidator.validate_wkt("LINESTRING (200001.0 200002.0, 200003.0 200004.0)")
        assert WKTValidator.validate_wkt("LINESTRING (200001 200002, 200003 200004)")
        assert WKTValidator.validate_wkt("LINESTRING Z (200001.0 200002.0 3.0, 200004.0 200005.0 6.0)")
        assert WKTValidator.validate_wkt("LINESTRING Z (200001.0 200002.0 3.0, 200004.0 200005.0 6.0, "
                                         "200007.0 200008.0 9.0)")
        assert WKTValidator.validate_wkt("LINESTRING Z (200001 200002 3, 200004 200005 6, 200007 200008 9)")
        assert not WKTValidator.validate_wkt("LINESTRING (200001,0 200002,0, 200003,0 200004,0)")
        assert not WKTValidator.validate_wkt("LINESTRING Z (200001.0 200002.0, 200004.0 200005.0)")
        assert not WKTValidator.validate_wkt("LINESTRING (200001 200002 5, 200003 200004 6)")

    with subtests.test(msg='testen POLYGON'):
        assert WKTValidator.validate_wkt("POLYGON ((200010 200020, 200030 200040, 200050 200060))")
        assert not WKTValidator.validate_wkt("POLYGON ((200010 200020, 200030 200040))")
        assert WKTValidator.validate_wkt("POLYGON ((200010.0 200020.0, 200030.0 200040.0, 200050.0 200060.0))")
        assert WKTValidator.validate_wkt("POLYGON ((200010.0 200020.0, 200030.0 200040.0, 200050.0 200060.0, "
                                         "200070.0 200080.0))")
        assert WKTValidator.validate_wkt("POLYGON Z ((200010.0 200020.0 1, 200030.0 200040.0 2, 200050.0 200060.0 3))")
        assert not WKTValidator.validate_wkt("POLYGON Z ((200010.0 200020.0, 200030.0 200040.0 2, 200050.0 200060.0))")
        assert not WKTValidator.validate_wkt(
            "POLYGON ((200010.0 200020.0 1, 200030.0 200040.0 2, 200050.0 200060.0 3))")
        assert WKTValidator.validate_wkt("POLYGON ((200010.0 200020.0, 200030.0 200040.0, 200050.0 200060.0), "
                                         "(200110.0 200120.0, 200130.0 200140.0, 200150.0 200160.0))")


@pytest.mark.parametrize('input', [(1), (1.0), (object())])
def test_WKT_non_string_value(input):
    with pytest.raises(TypeError):
        WKTValidator.validate_wkt(input)
