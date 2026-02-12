# coding=utf-8
from datetime import date
from ...BaseClasses.OTLObject import OTLAttribuut
from abc import abstractmethod
from ...BaseClasses.DateField import DateField
from ...GeometrieTypes.GeenGeometrie import GeenGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class KeuringObject(GeenGeometrie):
    """Bundeling van de gemeenschappelijke eigenschappen en relaties."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KeuringObject'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self._keuringsdatum = OTLAttribuut(field=DateField,
                                           naam='keuringsdatum',
                                           label='keuringsdatum',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KeuringObject.keuringsdatum',
                                           definition='De datum waarop het asset laatst is gekeurd.',
                                           owner=self)

    @property
    def keuringsdatum(self) -> date:
        """De datum waarop het asset laatst is gekeurd."""
        return self._keuringsdatum.get_waarde()

    @keuringsdatum.setter
    def keuringsdatum(self, value):
        self._keuringsdatum.set_waarde(value, owner=self)
