# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.ElektrischComponentennummerObject import ElektrischComponentennummerObject
from ...Classes.Abstracten.MotorVermogenskring import MotorVermogenskring
from ...Classes.Abstracten.SerienummerObject import SerienummerObject
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KlMotorbeveiligingMerk import KlMotorbeveiligingMerk
from ...Datatypes.KlMotorbeveiligingModelnaam import KlMotorbeveiligingModelnaam
from ...Datatypes.KlMotorbeveiligingType import KlMotorbeveiligingType


# Generated with OTLClassCreator. To modify: extend, do not edit
class Motorbeveiligingsschakelaar(ElektrischComponentennummerObject, MotorVermogenskring, SerienummerObject, AIMNaamObject):
    """Techniek voor het beveiliging van een moter tegen schade door overbelasting."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Motorbeveiligingsschakelaar'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VoedtAangestuurd', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#MotorVermogenskring', direction='i')  # i = direction: incoming

        self._instellingen = OTLAttribuut(field=DtcDocument,
                                          naam='instellingen',
                                          label='instellingen',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Motorbeveiligingsschakelaar.instellingen',
                                          definition='Een bestandsbijlage met de gedetailleerde beschrjiving van de instellingen van het toestel.',
                                          owner=self)

        self._isInstelbaar = OTLAttribuut(field=BooleanField,
                                          naam='isInstelbaar',
                                          label='is instelbaar',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Motorbeveiligingsschakelaar.isInstelbaar',
                                          definition='Geeft aan of het toestel instelbaar is na oplevering of niet.',
                                          owner=self)

        self._merk = OTLAttribuut(field=KlMotorbeveiligingMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Motorbeveiligingsschakelaar.merk',
                                  definition='Merk van de motorbeveiligingsschakelaar volgens de fabrikant.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlMotorbeveiligingModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Motorbeveiligingsschakelaar.modelnaam',
                                       definition='Naam die de fabrikant zelf geeft aan het model of de uitvoering van de motorbeveiligingsschakelaar.',
                                       owner=self)

        self._type = OTLAttribuut(field=KlMotorbeveiligingType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Motorbeveiligingsschakelaar.type',
                                  definition='Het type van motorbeveiliging volgens de gebruikte techniek.',
                                  owner=self)

    @property
    def instellingen(self) -> DtcDocumentWaarden:
        """Een bestandsbijlage met de gedetailleerde beschrjiving van de instellingen van het toestel."""
        return self._instellingen.get_waarde()

    @instellingen.setter
    def instellingen(self, value):
        self._instellingen.set_waarde(value, owner=self)

    @property
    def isInstelbaar(self) -> bool:
        """Geeft aan of het toestel instelbaar is na oplevering of niet."""
        return self._isInstelbaar.get_waarde()

    @isInstelbaar.setter
    def isInstelbaar(self, value):
        self._isInstelbaar.set_waarde(value, owner=self)

    @property
    def merk(self) -> str:
        """Merk van de motorbeveiligingsschakelaar volgens de fabrikant."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """Naam die de fabrikant zelf geeft aan het model of de uitvoering van de motorbeveiligingsschakelaar."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def type(self) -> str:
        """Het type van motorbeveiliging volgens de gebruikte techniek."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
