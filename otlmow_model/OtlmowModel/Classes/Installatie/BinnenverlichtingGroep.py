# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.NaampadObject import NaampadObject
from ...Datatypes.KlBinnenverlichtingGroepVerlichtGebied import (
    KlBinnenverlichtingGroepVerlichtGebied,
)
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class BinnenverlichtingGroep(NaampadObject, PuntGeometrie):
    """Een groep voor het groeperen van objecten van het type Binnenverlichtingstoestel."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#BinnenverlichtingGroep'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#ActivityComplex', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#ElectricityCable', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Beschermbuis', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Binnenverlichtingstoestel', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelTL', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedingskabel', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegkantkast', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LSSchuif', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._verlichtGebied = OTLAttribuut(field=KlBinnenverlichtingGroepVerlichtGebied,
                                            naam='verlichtGebied',
                                            label='verlicht gebied',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#BinnenverlichtingGroep.verlichtGebied',
                                            definition='Het gebied dat verlicht wordt door de binnenverlichtingstoestellen die deel uitmaken van de groep.',
                                            owner=self)

    @property
    def verlichtGebied(self) -> str:
        """Het gebied dat verlicht wordt door de binnenverlichtingstoestellen die deel uitmaken van de groep."""
        return self._verlichtGebied.get_waarde()

    @verlichtGebied.setter
    def verlichtGebied(self, value):
        self._verlichtGebied.set_waarde(value, owner=self)
