# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.ImplementatieElement.AIMObject import AIMObject
from otlmow_model.Datatypes.KlWeegcelMerk import KlWeegcelMerk
from otlmow_model.Datatypes.KlWeegcelModelnaam import KlWeegcelModelnaam
from otlmow_model.BaseClasses.StringField import StringField
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Weegcel(AIMObject, PuntGeometrie):
    """Een toestel dat op basis druk het gewicht meet van een object dat er rechtstreeks of via een tussenliggende plaat, bovenop geplaatst wordt"""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Weegcel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        PuntGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aswegerput')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Aswegersite')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Weegcomputer')

        self._merk = OTLAttribuut(field=KlWeegcelMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Weegcel.merk',
                                  definition='Merknaam van het toestel volgens de fabrikant.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlWeegcelModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Weegcel.modelnaam',
                                       definition='Modelnaam van het toestel volgens de fabrikant.',
                                       owner=self)

        self._serienummer = OTLAttribuut(field=StringField,
                                         naam='serienummer',
                                         label='serienummer',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Weegcel.serienummer',
                                         definition='De unieke identificatie van de fabrikant voor een concreet toestel.',
                                         owner=self)

    @property
    def merk(self):
        """Merknaam van het toestel volgens de fabrikant."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """Modelnaam van het toestel volgens de fabrikant."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def serienummer(self):
        """De unieke identificatie van de fabrikant voor een concreet toestel."""
        return self._serienummer.get_waarde()

    @serienummer.setter
    def serienummer(self, value):
        self._serienummer.set_waarde(value, owner=self)