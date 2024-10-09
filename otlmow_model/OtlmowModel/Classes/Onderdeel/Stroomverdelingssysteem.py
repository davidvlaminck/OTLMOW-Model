# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.ElektrischComponentennummerObject import ElektrischComponentennummerObject
from ...Classes.Abstracten.SerienummerObject import SerienummerObject
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.DteIPv4Adres import DteIPv4Adres, DteIPv4AdresWaarden
from ...Datatypes.KlPDUMerk import KlPDUMerk
from ...Datatypes.KlPDUModelnaam import KlPDUModelnaam
from otlmow_model.OtlmowModel.BaseClasses.NonNegIntegerField import NonNegIntegerField
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Stroomverdelingssysteem(ElektrischComponentennummerObject, SerienummerObject, AIMNaamObject, PuntGeometrie):
    """Een stroomverdelingssysteem, ook wel Power Distribution Unit of PDU genoemd, is een inrichting met verschillende outputs voor het distribueren van elektriciteit."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomverdelingssysteem'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#UPS', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#UPS', direction='o')  # o = direction: outgoing

        self._aantalAansluitpunten = OTLAttribuut(field=NonNegIntegerField,
                                                  naam='aantalAansluitpunten',
                                                  label='aantal aansluitpunten',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomverdelingssysteem.aantalAansluitpunten',
                                                  definition='Geeft aan hoeveel aparte bronnen voor afname van stroom voorzien zijn in het verdeelsysteem.',
                                                  owner=self)

        self._heeftAlgemeneAanUit = OTLAttribuut(field=BooleanField,
                                                 naam='heeftAlgemeneAanUit',
                                                 label='heeft algemene aan-uit',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomverdelingssysteem.heeftAlgemeneAanUit',
                                                 definition='Geeft aan of het verdeelsysteem voorzien is van een eigen aan/uit schakelaar om de stroomverdeling naar alle aansluitpunten tegelijk uit en aan te schakelen.',
                                                 owner=self)

        self._ipAdres = OTLAttribuut(field=DteIPv4Adres,
                                     naam='ipAdres',
                                     label='IP-adres',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomverdelingssysteem.ipAdres',
                                     definition='Het adres waarmee een online stroomverdelingssyteem vindbaar is op een IP-netwerk voor de sturing van de voeding van de gekoppelde technieken.',
                                     owner=self)

        self._merk = OTLAttribuut(field=KlPDUMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomverdelingssysteem.merk',
                                  definition='Het merk van het stroomverdelingssysteem.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlPDUModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomverdelingssysteem.modelnaam',
                                       definition='De modelnaam van het stroomverdelingssysteem.',
                                       owner=self)

    @property
    def aantalAansluitpunten(self) -> int:
        """Geeft aan hoeveel aparte bronnen voor afname van stroom voorzien zijn in het verdeelsysteem."""
        return self._aantalAansluitpunten.get_waarde()

    @aantalAansluitpunten.setter
    def aantalAansluitpunten(self, value):
        self._aantalAansluitpunten.set_waarde(value, owner=self)

    @property
    def heeftAlgemeneAanUit(self) -> bool:
        """Geeft aan of het verdeelsysteem voorzien is van een eigen aan/uit schakelaar om de stroomverdeling naar alle aansluitpunten tegelijk uit en aan te schakelen."""
        return self._heeftAlgemeneAanUit.get_waarde()

    @heeftAlgemeneAanUit.setter
    def heeftAlgemeneAanUit(self, value):
        self._heeftAlgemeneAanUit.set_waarde(value, owner=self)

    @property
    def ipAdres(self) -> DteIPv4AdresWaarden:
        """Het adres waarmee een online stroomverdelingssyteem vindbaar is op een IP-netwerk voor de sturing van de voeding van de gekoppelde technieken."""
        return self._ipAdres.get_waarde()

    @ipAdres.setter
    def ipAdres(self, value):
        self._ipAdres.set_waarde(value, owner=self)

    @property
    def merk(self) -> str:
        """Het merk van het stroomverdelingssysteem."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van het stroomverdelingssysteem."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
