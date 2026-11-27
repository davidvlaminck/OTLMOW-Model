# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.ComplexeGeleiding import ComplexeGeleiding
from ...Datatypes.KlEcoPoorttype import KlEcoPoorttype
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class EcoPoort(ComplexeGeleiding, PuntGeometrie):
    """Een afsluitbare doorgang die mensen toegang biedt tot het gebied en voorkomt dat dieren het verlaten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#EcoPoort'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ComplexeGeleiding', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ConstructieElement', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._breedte = OTLAttribuut(field=KwantWrdInMeter,
                                     naam='breedte',
                                     label='breedte',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#EcoPoort.breedte',
                                     definition='De breedte van de poort in meter.',
                                     owner=self)

        self._poortType = OTLAttribuut(field=KlEcoPoorttype,
                                       naam='poortType',
                                       label='poort type',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#EcoPoort.poortType',
                                       definition='Bepaling van het type van poort.',
                                       owner=self)

    @property
    def breedte(self) -> KwantWrdInMeterWaarden:
        """De breedte van de poort in meter."""
        return self._breedte.get_waarde()

    @breedte.setter
    def breedte(self, value):
        self._breedte.set_waarde(value, owner=self)

    @property
    def poortType(self) -> str:
        """Bepaling van het type van poort."""
        return self._poortType.get_waarde()

    @poortType.setter
    def poortType(self, value):
        self._poortType.set_waarde(value, owner=self)
