# coding=utf-8
from typing import ClassVar

from ...BaseClasses.BooleanField import BooleanField
from ...BaseClasses.OTLObject import OTLAttribuut
from ...BaseClasses.StringField import StringField
from ...Classes.Abstracten.Communicatieapparatuur import Communicatieapparatuur
from ...Classes.Abstracten.FirmwareObject import FirmwareObject
from ...Datatypes.DteIPv4Adres import DteIPv4Adres, DteIPv4AdresWaarden
from ...Datatypes.KlNetwerkconfiguratieWV import KlNetwerkconfiguratieWV


# Generated with OTLClassCreator. To modify: extend, do not edit
class Armatuurcontroller(Communicatieapparatuur, FirmwareObject):
    """Controller die op het verlichtingstoestel wordt gemonteerd en die één verlichtingstoestel aanstuurt."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Armatuurcontroller'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LEDDriver', 'u', '2.4.0'),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Montagekast', 'u', '2.4.0'),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Segmentcontroller', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voorschakelapparaat', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aftakking', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WVOpvoertransformator', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring', 'i', '2.4.0'),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WVOpvoertransformator', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VoedtAangestuurd', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LEDDriver', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VoedtAangestuurd', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VoedtAangestuurd', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Montagekast', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VoedtAangestuurd', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._ipAdres = OTLAttribuut(field=DteIPv4Adres,
                                     naam='ipAdres',
                                     label='IP-adres',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Armatuurcontroller.ipAdres',
                                     definition='Het IP-adres van de armatuurcontroller.',
                                     owner=self)

        self._isDummydot = OTLAttribuut(field=BooleanField,
                                        naam='isDummydot',
                                        label='is dummydot',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Armatuurcontroller.isDummydot',
                                        definition='Geeft aan of er in de toekomst een armatuurcontroller kan aangesloten worden op het verlichtingstoestel, maar dat het toestel voorlopig voorzien is van een kortsluitmodule (ook wel dummydot genoemd).',
                                        owner=self)

        self._merk = OTLAttribuut(field=StringField,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Armatuurcontroller.merk',
                                  definition='Merk van de armatuurcontroller.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=StringField,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Armatuurcontroller.modelnaam',
                                       definition='Modelnaam van de armatuurcontroller.',
                                       owner=self)

        self._netwerkconfiguratieWV = OTLAttribuut(field=KlNetwerkconfiguratieWV,
                                                   naam='netwerkconfiguratieWV',
                                                   label='netwerkconfiguratie wegverlichting',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Armatuurcontroller.netwerkconfiguratieWV',
                                                   definition='De netwerkconfiguratie omvat de instelling van het netwerk (de zogenaamde kleur van het netwerk) in het kader van de gesplitste netwerkenopstelling van de lichtpuntcontrole.',
                                                   owner=self)

        self._serienummer = OTLAttribuut(field=StringField,
                                         naam='serienummer',
                                         label='serienummer',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Armatuurcontroller.serienummer',
                                         definition='Het unieke nummer waarmee het toestel door de fabrikant geïdentificeerd is.',
                                         owner=self)

    @property
    def ipAdres(self) -> DteIPv4AdresWaarden:
        """Het IP-adres van de armatuurcontroller."""
        return self._ipAdres.get_waarde()

    @ipAdres.setter
    def ipAdres(self, value):
        self._ipAdres.set_waarde(value, owner=self)

    @property
    def isDummydot(self) -> bool:
        """Geeft aan of er in de toekomst een armatuurcontroller kan aangesloten worden op het verlichtingstoestel, maar dat het toestel voorlopig voorzien is van een kortsluitmodule (ook wel dummydot genoemd)."""
        return self._isDummydot.get_waarde()

    @isDummydot.setter
    def isDummydot(self, value):
        self._isDummydot.set_waarde(value, owner=self)

    @property
    def merk(self) -> str:
        """Merk van de armatuurcontroller."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """Modelnaam van de armatuurcontroller."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def netwerkconfiguratieWV(self) -> str:
        """De netwerkconfiguratie omvat de instelling van het netwerk (de zogenaamde kleur van het netwerk) in het kader van de gesplitste netwerkenopstelling van de lichtpuntcontrole."""
        return self._netwerkconfiguratieWV.get_waarde()

    @netwerkconfiguratieWV.setter
    def netwerkconfiguratieWV(self, value):
        self._netwerkconfiguratieWV.set_waarde(value, owner=self)

    @property
    def serienummer(self) -> str:
        """Het unieke nummer waarmee het toestel door de fabrikant geïdentificeerd is."""
        return self._serienummer.get_waarde()

    @serienummer.setter
    def serienummer(self, value):
        self._serienummer.set_waarde(value, owner=self)
