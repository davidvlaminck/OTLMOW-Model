import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from otlmow_model.OtlmowModel.BaseClasses.WKTValidator import WKTValidator


def test_WKT_valid(subtests):
    with subtests.test(msg='testen POINT'):
        assert WKTValidator.validate_wkt('POINT (200001.0 200002.0)')
        assert WKTValidator.validate_wkt('POINT (200001 200002)')
        assert WKTValidator.validate_wkt('POINT (212345.678901 212345.678902)')
        assert WKTValidator.validate_wkt('POINT Z (200001.0 200002.0 3.0)')
        assert WKTValidator.validate_wkt('POINT Z (200001 200002 3)')
        assert not WKTValidator.validate_wkt('POINT Z (200001,0 200002,0 3,0)')
        assert not WKTValidator.validate_wkt('POINT Z (200001 200002)')
        assert not WKTValidator.validate_wkt('POINT (200001 200002 3)')
        assert not WKTValidator.validate_wkt('POINT(200001 200002)')
        assert not WKTValidator.validate_wkt('POINT (-200001 -200002)')
        assert not WKTValidator.validate_wkt('punt Z (200001 200002)')
        assert WKTValidator.validate_wkt('MULTIPOINT ((200001.0 200002.0), (200001.0 200002.0)')
        assert WKTValidator.validate_wkt('MULTIPOINT Z ((200001.0 200002.0 3.0), (200001.0 200002.0 3.0)')

    with subtests.test(msg='testen LINESTRING'):
        assert WKTValidator.validate_wkt('LINESTRING (200001.0 200002.0, 200003.0 200004.0)')
        assert WKTValidator.validate_wkt('LINESTRING (200001 200002, 200003 200004)')
        assert WKTValidator.validate_wkt('LINESTRING Z (200001.0 200002.0 3.0, 200004.0 200005.0 6.0)')
        assert WKTValidator.validate_wkt(
            'LINESTRING Z (200001.0 200002.0 3.0, 200004.0 200005.0 6.0, 200007.0 200008.0 9.0)'
        )
        assert WKTValidator.validate_wkt('LINESTRING Z (200001 200002 3, 200004 200005 6, 200007 200008 9)')
        assert not WKTValidator.validate_wkt('LINESTRING (200001,0 200002,0, 200003,0 200004,0)')
        assert not WKTValidator.validate_wkt('LINESTRING Z (200001.0 200002.0, 200004.0 200005.0)')
        assert not WKTValidator.validate_wkt('LINESTRING (200001 200002 5, 200003 200004 6)')

    with subtests.test(msg='testen POLYGON'):
        assert WKTValidator.validate_wkt('POLYGON ((200010 200020, 200030 200040, 200050 200060))')
        assert not WKTValidator.validate_wkt('POLYGON ((200010 200020, 200030 200040))')
        assert WKTValidator.validate_wkt('POLYGON ((200010.0 200020.0, 200030.0 200040.0, 200050.0 200060.0))')
        assert WKTValidator.validate_wkt(
            'POLYGON ((200010.0 200020.0, 200030.0 200040.0, 200050.0 200060.0, 200070.0 200080.0))'
        )
        assert WKTValidator.validate_wkt('POLYGON Z ((200010.0 200020.0 1, 200030.0 200040.0 2, 200050.0 200060.0 3))')
        assert not WKTValidator.validate_wkt('POLYGON Z ((200010.0 200020.0, 200030.0 200040.0 2, 200050.0 200060.0))')
        assert not WKTValidator.validate_wkt(
            'POLYGON ((200010.0 200020.0 1, 200030.0 200040.0 2, 200050.0 200060.0 3))'
        )
        assert WKTValidator.validate_wkt(
            'POLYGON ((200010.0 200020.0, 200030.0 200040.0, 200050.0 200060.0), '
            '(200110.0 200120.0, 200130.0 200140.0, 200150.0 200160.0))'
        )


def test_validate_wkt_without_parentheses_is_invalid():
    assert not WKTValidator.validate_wkt('POINT')
    assert not WKTValidator.validate_wkt('FOO BAR')
    assert not WKTValidator.validate_wkt('')
    assert not WKTValidator.validate_wkt('POINT (')


def test_validate_wkt_level1_nested_is_invalid():
    # coords_list[0] is a list instead of a tuple for a level-1 geometry
    assert not WKTValidator.validate_wkt('POINT ((200001 200002))')


def test_validate_wkt_multipolygon_is_valid():
    assert WKTValidator.validate_wkt('MULTIPOLYGON (((200010 200020, 200030 200040, 200050 200060, 200010 200020)))')


def test_validate_wkt_y_out_of_range_is_invalid():
    assert not WKTValidator.validate_wkt('POINT (200001 999999)')


def test_validate_wkt_z_too_high_is_invalid():
    assert not WKTValidator.validate_wkt('POINT Z (200001 200002 999)')


def test_validate_wkt_multipolygon_with_an_invalid_inner_ring_is_invalid():
    assert not WKTValidator.validate_wkt(
        'MULTIPOLYGON (((200010 200020, 200030 200040, 200050 200060, 200010 200020), '
        '(200110 999999, 200130 200140, 200150 200160, 200110 999999)))'
    )


def test_validate_coords_list_with_too_few_points_is_invalid():
    assert WKTValidator.validate_coords_list([(200001.0, 200002.0)], 'LINESTRING') is False


def test_validate_coords_list_with_a_wrong_number_of_coordinates_is_invalid():
    assert WKTValidator.validate_coords_list([(200001.0, 200002.0, 3.0)], 'POINT') is False
    assert WKTValidator.validate_coords_list([(200001.0, 200002.0)], 'POINT Z') is False


def test_validate_coords_list_with_an_x_out_of_range_is_invalid():
    assert WKTValidator.validate_coords_list([(999999.0, 200002.0)], 'POINT') is False
