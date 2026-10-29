from typing import List


class WKTValidator:
    coord_params = {
        'POINT': {'level': 1, 'min': 1, 'len_point': 2},
        'POINT Z': {'level': 1, 'min': 1, 'len_point': 3},
        'LINESTRING': {'level': 1, 'min': 2, 'len_point': 2},
        'LINESTRING Z': {'level': 1, 'min': 2, 'len_point': 3},
        'POLYGON': {'level': 2, 'min': 3, 'len_point': 2},
        'POLYGON Z': {'level': 2, 'min': 3, 'len_point': 3},
        'MULTIPOINT': {'level': 2, 'min': 1, 'len_point': 2},
        'MULTIPOINT Z': {'level': 2, 'min': 1, 'len_point': 3},
        'MULTILINESTRING': {'level': 2, 'min': 2, 'len_point': 2},
        'MULTILINESTRING Z': {'level': 2, 'min': 2, 'len_point': 3},
        'MULTIPOLYGON': {'level': 3, 'min': 3, 'len_point': 2},
        'MULTIPOLYGON Z': {'level': 3, 'min': 3, 'len_point': 3},
        'GEOMETRYCOLLECTION': 0,
    }

    @classmethod
    def split_and_add_to_list(cls, coords_list: list, coords_str: str):
        if coords_str.startswith('('):
            coords_str = coords_str[1:-1]
            for new_coords_str in coords_str.split('),('):
                new_list = []
                cls.split_and_add_to_list(coords_list=new_list, coords_str=new_coords_str)
                coords_list.append(new_list)
        else:
            for c in coords_str.split(','):
                x_y_z = tuple(float(co) for co in c.strip().split(' '))
                coords_list.append(x_y_z)

    @classmethod
    def validate_wkt(cls, input_string: str) -> bool:
        if not cls._has_parentheses(input_string):
            return False
        input_string = input_string.upper()
        geo_type = input_string.split(' (')[0]
        if not cls._is_supported_geo_type(geo_type):
            return False

        coords_list = cls.get_coords_list_from_wkt_string(input_string)
        level = cls.coord_params[geo_type]['level']
        if not cls._coord_shape_is_valid(coords_list, level):
            return False
        return cls._validate_coords_for_level(coords_list, geo_type, level)

    @classmethod
    def _has_parentheses(cls, input_string: str) -> bool:
        return '(' in input_string and ')' in input_string

    @classmethod
    def _is_supported_geo_type(cls, geo_type: str) -> bool:
        return geo_type in (
            'POINT',
            'POINT Z',
            'LINESTRING',
            'LINESTRING Z',
            'POLYGON',
            'POLYGON Z',
            'MULTIPOINT',
            'MULTIPOINT Z',
            'MULTILINESTRING',
            'MULTILINESTRING Z',
            'MULTIPOLYGON',
            'MULTIPOLYGON Z',
            'GEOMETRYCOLLECTION',
        )

    @classmethod
    def _coord_shape_is_valid(cls, coords_list: list, level: int) -> bool:
        if level == 1:
            return isinstance(coords_list[0], tuple)
        if level == 2:
            return isinstance(coords_list[0][0], tuple)
        return isinstance(coords_list[0][0][0], tuple)

    @classmethod
    def _validate_coords_for_level(cls, coords_list: list, geo_type: str, level: int) -> bool:
        if level == 1:
            return cls.validate_coords_list(coords_list, geo_type)
        if level == 2:
            return all(cls.validate_coords_list(coords, geo_type) for coords in coords_list)
        return cls._validate_coords_for_level_3(coords_list, geo_type)

    @classmethod
    def _validate_coords_for_level_3(cls, coords_list: list, geo_type: str) -> bool:
        for coords in coords_list:
            for coords2 in coords:
                if not cls.validate_coords_list(coords2, geo_type):
                    return False
        return True

    @classmethod
    def get_coords_list_from_wkt_string(cls, input_string) -> List:
        coords_string = input_string.split(' (')[1][:-1].replace(', ', ',').replace(' ,', ',')
        coords_list = []
        cls.split_and_add_to_list(coords_list, coords_string)
        return coords_list

    @classmethod
    def validate_coords_list(cls, coords_list, geo_type):
        len_point = cls.coord_params[geo_type]['len_point']
        min_point = cls.coord_params[geo_type]['min']

        if len(coords_list) < min_point:
            return False

        return all(cls._point_is_valid(point, len_point) for point in coords_list)

    @classmethod
    def _point_is_valid(cls, point, len_point: int) -> bool:
        if len(point) != len_point:
            return False
        if not cls._x_is_valid(point[0]):
            return False
        if not cls._y_is_valid(point[1]):
            return False
        return not (len_point == 3 and point[2] > 700)

    @classmethod
    def _x_is_valid(cls, value) -> bool:
        return not (value < 14637.2 or value > 291015.3)

    @classmethod
    def _y_is_valid(cls, value) -> bool:
        return not (value < 22608.2 or value > 246424.3)
