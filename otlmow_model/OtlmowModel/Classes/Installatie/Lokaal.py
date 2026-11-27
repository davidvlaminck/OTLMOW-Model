# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Behuizing import Behuizing
from ...Classes.Abstracten.Kokerruimte import Kokerruimte
from ...Classes.ImplementatieElement.NaampadObject import NaampadObject
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class Lokaal(Behuizing, Kokerruimte, NaampadObject):
    """Een ruimte binnen een gebouw."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Lokaal'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Toegangselement', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#ASTRIDInstallatie', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ALSB', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brandblusser', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkelement', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Spanningsomvormer', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Telefoontoestel', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#UPS', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AndereLaag', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Grondanker', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Aswegersite', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Funderingspaal', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._grondplan = OTLAttribuut(field=DtcDocument,
                                       naam='grondplan',
                                       label='grondplan',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Lokaal.grondplan',
                                       definition='Plattegrond van het lokaal met aanduidingen van de verschillende aanwezige elementen zoals kasten met kastnummers, toegangscontrole en meer.',
                                       owner=self)

    @property
    def grondplan(self) -> DtcDocumentWaarden:
        """Plattegrond van het lokaal met aanduidingen van de verschillende aanwezige elementen zoals kasten met kastnummers, toegangscontrole en meer."""
        return self._grondplan.get_waarde()

    @grondplan.setter
    def grondplan(self, value):
        self._grondplan.set_waarde(value, owner=self)
