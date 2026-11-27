# coding=utf-8
from typing import ClassVar

from ..BaseClasses.OTLObject import OTLAttribuut, OTLObject
from ..BaseClasses.RelationInteractor import RelationInteractor
from ..BaseClasses.StringField import StringField
from ..Classes.ImplementatieElement.AIMDBStatus import AIMDBStatus
from ..Classes.ImplementatieElement.AIMVersie import AIMVersie
from ..Datatypes.DtcContactinfo import DtcContactinfo, DtcContactinfoWaarden
from ..Datatypes.DtcIdentificator import DtcIdentificator, DtcIdentificatorWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class Agent(AIMDBStatus, AIMVersie, RelationInteractor, OTLObject):
    """Iemand die of iets dat kan handelen of een effect kan teweeg brengen."""

    typeURI = 'http://purl.org/dc/terms/Agent'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftBetrokkene', 'http://purl.org/dc/terms/Agent', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftBetrokkene', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AbstracteAanvullendeGeometrie', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftBetrokkene', 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftBetrokkene', 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Derdenobject', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftBetrokkene', 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Toegangsprocedure', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._agentId = OTLAttribuut(field=DtcIdentificator,
                                     naam='agentId',
                                     label='agent identificatie',
                                     objectUri='http://purl.org/dc/terms/Agent.agentId',
                                     definition='Identificatie van de agent volgens een bepaalde bron.',
                                     owner=self)

        self._contactinfo = OTLAttribuut(field=DtcContactinfo,
                                         naam='contactinfo',
                                         label='contactinfo',
                                         objectUri='http://purl.org/dc/terms/Agent.contactinfo',
                                         kardinaliteit_max='*',
                                         definition='Algemene contactgegevens voor de agent.',
                                         owner=self)

        self._naam = OTLAttribuut(field=StringField,
                                  naam='naam',
                                  label='naam',
                                  objectUri='http://purl.org/dc/terms/Agent.naam',
                                  definition='De naam waarmee de agent doorgaans benoemd wordt.',
                                  owner=self)

    @property
    def agentId(self) -> DtcIdentificatorWaarden:
        """Identificatie van de agent volgens een bepaalde bron."""
        return self._agentId.get_waarde()

    @agentId.setter
    def agentId(self, value):
        self._agentId.set_waarde(value, owner=self)

    @property
    def contactinfo(self) -> list[DtcContactinfoWaarden]:
        """Algemene contactgegevens voor de agent."""
        return self._contactinfo.get_waarde()

    @contactinfo.setter
    def contactinfo(self, value):
        self._contactinfo.set_waarde(value, owner=self)

    @property
    def naam(self) -> str:
        """De naam waarmee de agent doorgaans benoemd wordt."""
        return self._naam.get_waarde()

    @naam.setter
    def naam(self, value):
        self._naam.set_waarde(value, owner=self)
