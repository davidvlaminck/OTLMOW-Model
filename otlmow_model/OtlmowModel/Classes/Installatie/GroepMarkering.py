# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.NaampadObject import NaampadObject
from ...Datatypes.KwantWrdInVierkanteMeter import (
    KwantWrdInVierkanteMeter,
    KwantWrdInVierkanteMeterWaarden,
)
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class GroepMarkering(NaampadObject, PuntGeometrie):
    """Groepering om alle soorten markeringen te groeperen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GroepMarkering'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#DwarseMarkeringToegang', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#FiguratieMarkeringToegang', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GroepDwarseMarkeringEnFiguratie', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GroepMarkering', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GekleurdWegvlakMarkering', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LijnvormigElementMarkering', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OverlangseMarkering', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._totaleGroepOppervlakte = OTLAttribuut(field=KwantWrdInVierkanteMeter,
                                                    naam='totaleGroepOppervlakte',
                                                    label='totale oppervlakte groepering',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GroepMarkering.totaleGroepOppervlakte',
                                                    definition='De totale oppervlakte van de totale markering groepering.',
                                                    owner=self)

    @property
    def totaleGroepOppervlakte(self) -> KwantWrdInVierkanteMeterWaarden:
        """De totale oppervlakte van de totale markering groepering."""
        return self._totaleGroepOppervlakte.get_waarde()

    @totaleGroepOppervlakte.setter
    def totaleGroepOppervlakte(self, value):
        self._totaleGroepOppervlakte.set_waarde(value, owner=self)
