# coding=utf-8
from typing import List
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.Abstracten.SelNietSelLus import SelNietSelLus
from otlmow_model.BaseClasses.BooleanField import BooleanField
from otlmow_model.Datatypes.KlVriLusFunctie import KlVriLusFunctie
from otlmow_model.Datatypes.KlVriLusSoortvoertuig import KlVriLusSoortvoertuig


# Generated with OTLClassCreator. To modify: extend, do not edit
class NietSelectieveDetectielus(SelNietSelLus):
    """Een niet-selectieve detectielus werkt onder invloed van een wijziging in de zelfinductie van een lus in het wegdek wanneer het metaal van een voertuig binnen het gevoeligheidsgebied van de lus komt."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#NietSelectieveDetectielus'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Fietstelinstallatie')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Flitspaal')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Fietstelsysteem')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IOKaart')

        self._functie = OTLAttribuut(field=KlVriLusFunctie,
                                     naam='functie',
                                     label='functie',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#NietSelectieveDetectielus.functie',
                                     definition='Type niet-selectieve detectielus bv. file, afstand, hiaat,...',
                                     owner=self)

        self._isMotorgevoelig = OTLAttribuut(field=BooleanField,
                                             naam='isMotorgevoelig',
                                             label='is motorgevoelig',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#NietSelectieveDetectielus.isMotorgevoelig',
                                             definition='Geeft aan of de lus motorgevoelig is of niet.',
                                             owner=self)

        self._isRichtingsgevoelig = OTLAttribuut(field=BooleanField,
                                                 naam='isRichtingsgevoelig',
                                                 label='is richtingsgevoelig',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#NietSelectieveDetectielus.isRichtingsgevoelig',
                                                 definition='Geeft aan of de detectielus gevoelig is voor de richting waarin het voertuig het gevoeligheidsgebied van de lus al dan niet binnenkomt.',
                                                 owner=self)

        self._soortVoertuig = OTLAttribuut(field=KlVriLusSoortvoertuig,
                                           naam='soortVoertuig',
                                           label='soort voertuig',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#NietSelectieveDetectielus.soortVoertuig',
                                           kardinaliteit_max='*',
                                           definition='Type voertuig dat de detectielus volgens zijn instellingen kan detecteren.',
                                           owner=self)

    @property
    def functie(self) -> str:
        """Type niet-selectieve detectielus bv. file, afstand, hiaat,..."""
        return self._functie.get_waarde()

    @functie.setter
    def functie(self, value):
        self._functie.set_waarde(value, owner=self)

    @property
    def isMotorgevoelig(self) -> bool:
        """Geeft aan of de lus motorgevoelig is of niet."""
        return self._isMotorgevoelig.get_waarde()

    @isMotorgevoelig.setter
    def isMotorgevoelig(self, value):
        self._isMotorgevoelig.set_waarde(value, owner=self)

    @property
    def isRichtingsgevoelig(self) -> bool:
        """Geeft aan of de detectielus gevoelig is voor de richting waarin het voertuig het gevoeligheidsgebied van de lus al dan niet binnenkomt."""
        return self._isRichtingsgevoelig.get_waarde()

    @isRichtingsgevoelig.setter
    def isRichtingsgevoelig(self, value):
        self._isRichtingsgevoelig.set_waarde(value, owner=self)

    @property
    def soortVoertuig(self) -> List[str]:
        """Type voertuig dat de detectielus volgens zijn instellingen kan detecteren."""
        return self._soortVoertuig.get_waarde()

    @soortVoertuig.setter
    def soortVoertuig(self, value):
        self._soortVoertuig.set_waarde(value, owner=self)
