# coding=utf-8
from typing import ClassVar

from ...BaseClasses.IntegerField import IntegerField
from ...BaseClasses.NonNegIntegerField import NonNegIntegerField
from ...BaseClasses.OTLObject import OTLAttribuut
from ...BaseClasses.URIField import URIField
from ...Classes.ImplementatieElement.NaampadObject import NaampadObject
from ...Datatypes.KlKabelnettoegangNetwerksoort import KlKabelnettoegangNetwerksoort
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class KabelnetToegang(NaampadObject, PuntGeometrie):
    """Knooppunt van Kabelnet dat toegang geeft tot de informatie die in Kabelnet bewaard wordt."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KabelnetToegang'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Behuizing', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Beschermbuis', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftNetwerktoegang', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Behuizing', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#MeetstationAbstract', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersregelaar', 'u', None),  # u = unidirectional
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._geschatRUGebruik = OTLAttribuut(field=NonNegIntegerField,
                                              naam='geschatRUGebruik',
                                              label='geschat aantal rack units in gebruik',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KabelnetToegang.geschatRUGebruik',
                                              usagenote='Deze waarde wordt aangeleverd vanuit de Kabelnet-toepassing.',
                                              definition='Het aantal gebruikte rack units dat voor de betrokken toegang in gebruik is op basis van een berekening in Kabelnet.',
                                              owner=self)

        self._kabelnetToegangId = OTLAttribuut(field=IntegerField,
                                               naam='kabelnetToegangId',
                                               label='kabelnettoegang ID',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KabelnetToegang.kabelnetToegangId',
                                               definition='Uniek nummer uit de Kabelnet toepassing dat deze toegang identificeert.',
                                               owner=self)

        self._kabelnetURL = OTLAttribuut(field=URIField,
                                         naam='kabelnetURL',
                                         label='kabelnet URL',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KabelnetToegang.kabelnetURL',
                                         definition='Knooppunt van Kabelnet dat toegang geeft tot de informatie die in Kabelnet bewaard wordt.',
                                         owner=self)

        self._netwerkSoort = OTLAttribuut(field=KlKabelnettoegangNetwerksoort,
                                          naam='netwerkSoort',
                                          label='netwerk soort',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KabelnetToegang.netwerkSoort',
                                          kardinaliteit_max='*',
                                          definition='Type netwerk dat bereikbaar is via het toegangspunt.',
                                          owner=self)

    @property
    def geschatRUGebruik(self) -> int:
        """Het aantal gebruikte rack units dat voor de betrokken toegang in gebruik is op basis van een berekening in Kabelnet."""
        return self._geschatRUGebruik.get_waarde()

    @geschatRUGebruik.setter
    def geschatRUGebruik(self, value):
        self._geschatRUGebruik.set_waarde(value, owner=self)

    @property
    def kabelnetToegangId(self) -> int:
        """Uniek nummer uit de Kabelnet toepassing dat deze toegang identificeert."""
        return self._kabelnetToegangId.get_waarde()

    @kabelnetToegangId.setter
    def kabelnetToegangId(self, value):
        self._kabelnetToegangId.set_waarde(value, owner=self)

    @property
    def kabelnetURL(self) -> str:
        """Knooppunt van Kabelnet dat toegang geeft tot de informatie die in Kabelnet bewaard wordt."""
        return self._kabelnetURL.get_waarde()

    @kabelnetURL.setter
    def kabelnetURL(self, value):
        self._kabelnetURL.set_waarde(value, owner=self)

    @property
    def netwerkSoort(self) -> list[str]:
        """Type netwerk dat bereikbaar is via het toegangspunt."""
        return self._netwerkSoort.get_waarde()

    @netwerkSoort.setter
    def netwerkSoort(self, value):
        self._netwerkSoort.set_waarde(value, owner=self)
