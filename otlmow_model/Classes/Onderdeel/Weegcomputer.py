# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.ImplementatieElement.AIMObject import AIMObject
from otlmow_model.Datatypes.KlWeegcomputerMerk import KlWeegcomputerMerk
from otlmow_model.Datatypes.KlWeegcomputerModelnaam import KlWeegcomputerModelnaam
from otlmow_model.BaseClasses.StringField import StringField
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Weegcomputer(AIMObject, PuntGeometrie):
    """Een verwerkingseenheid met als input de weeggegevens van de weegcellen en output het gewicht."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Weegcomputer'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IndoorKast')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Weegcel')

        self._checksum = OTLAttribuut(field=StringField,
                                      naam='checksum',
                                      label='checksum',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Weegcomputer.checksum',
                                      definition='Een tekenreeks waarmee kan gecontroleerd worden of de vooropgestelde waardes van paramaters van de weegcomputer correct en ongewijzigd gebleven zijn.',
                                      owner=self)

        self._merk = OTLAttribuut(field=KlWeegcomputerMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Weegcomputer.merk',
                                  definition='Merknaam van het toestel volgens de fabrikant.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlWeegcomputerModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Weegcomputer.modelnaam',
                                       definition='Modelnaam van het toestel volgens de fabrikant.',
                                       owner=self)

        self._serienummer = OTLAttribuut(field=StringField,
                                         naam='serienummer',
                                         label='Serienummer',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Weegcomputer.serienummer',
                                         definition='Unieke identificatie van het toestel, toegekend door de fabrikant.',
                                         owner=self)

    @property
    def checksum(self) -> str:
        """Een tekenreeks waarmee kan gecontroleerd worden of de vooropgestelde waardes van paramaters van de weegcomputer correct en ongewijzigd gebleven zijn."""
        return self._checksum.get_waarde()

    @checksum.setter
    def checksum(self, value):
        self._checksum.set_waarde(value, owner=self)

    @property
    def merk(self) -> str:
        """Merknaam van het toestel volgens de fabrikant."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """Modelnaam van het toestel volgens de fabrikant."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def serienummer(self) -> str:
        """Unieke identificatie van het toestel, toegekend door de fabrikant."""
        return self._serienummer.get_waarde()

    @serienummer.setter
    def serienummer(self, value):
        self._serienummer.set_waarde(value, owner=self)
