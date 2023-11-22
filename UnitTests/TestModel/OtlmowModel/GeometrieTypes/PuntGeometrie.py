from abc import abstractmethod, ABC

from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.BaseClasses.WKTField import WKTField
from otlmow_model.GeometrieTypes.AbstracteGeometrie import AbstracteGeometrie


class PuntGeometrie(AbstracteGeometrie):
    @abstractmethod
    def __init__(self):
        super().__init__()
        self._geometry_types.append('POINT Z')
