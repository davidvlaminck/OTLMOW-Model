# coding=utf-8
from abc import abstractmethod
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Detectie import Detectie
from ...Datatypes.DtcAfmetingBxlInM import DtcAfmetingBxlInM, DtcAfmetingBxlInMWaarden
from ...Datatypes.DtcTijdsduur import DtcTijdsduur, DtcTijdsduurWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class Detectielus(Detectie):
    """Abstracte voor een detectielus. Een detectielus is een kabel onder het wegdek die in staat is om voertuigen te detecteren teneinde de verkeersregelaar aan te sturen. Selectieve lussen zijn in staat om gecodeerde informatie door te geven van prioritaire voertuigen, niet-selectieve lussen geven informatie door van alle voertuigen die het detectie gebied passeren."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Detectielus'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#IVRIComponent', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SoftwareToegang', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#CoordinatiesysteemVRI', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ITSapp', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LogischePoort', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RIS', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Software', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TLCfiPoort', 'u', None),  # u = unidirectional
    ]

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._afmetingenBL = OTLAttribuut(field=DtcAfmetingBxlInM,
                                          naam='afmetingenBL',
                                          label='afmetingen b l',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Detectielus.afmetingenBL',
                                          definition='Afmetingen breedte x lengte van de lus.',
                                          owner=self)

        self._bewakingstijd = OTLAttribuut(field=DtcTijdsduur,
                                           naam='bewakingstijd',
                                           label='bewakingstijd',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Detectielus.bewakingstijd',
                                           definition='Wachttijd (in uren) waarna een alarm pas mag optreden.',
                                           owner=self)

    @property
    def afmetingenBL(self) -> DtcAfmetingBxlInMWaarden:
        """Afmetingen breedte x lengte van de lus."""
        return self._afmetingenBL.get_waarde()

    @afmetingenBL.setter
    def afmetingenBL(self, value):
        self._afmetingenBL.set_waarde(value, owner=self)

    @property
    def bewakingstijd(self) -> DtcTijdsduurWaarden:
        """Wachttijd (in uren) waarna een alarm pas mag optreden."""
        return self._bewakingstijd.get_waarde()

    @bewakingstijd.setter
    def bewakingstijd(self, value):
        self._bewakingstijd.set_waarde(value, owner=self)
