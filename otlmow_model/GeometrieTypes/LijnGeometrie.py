from abc import abstractmethod, ABC

from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.BaseClasses.WKTField import WKTField


class LijnGeometrie(ABC):
    @abstractmethod
    def __init__(self):
        if not hasattr(self, '_geometry_types'):
            self._geometry_types = []
        self._geometry_types.append('LINESTRING Z')
        self._geometry = OTLAttribuut(field=WKTField,
                                      naam='geometry',
                                      label='geometry',
                                      objectUri='https://loc.data.wegenenverkeer.be/ns/implementatieelement#Locatie.geometrie',
                                      definition='geometry voor DAVIE',
                                      owner=self)

    @property
    def geometry(self):
        """geometry voor DAVIE"""
        return self._geometry.waarde

    @geometry.setter
    def geometry(self, value):
        self._geometry.set_waarde(value, owner=self)