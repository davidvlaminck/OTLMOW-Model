# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...BaseClasses.StringField import StringField
from ...Classes.ImplementatieElement.AIMObject import AIMObject
from ...Datatypes.KlWeegcomputerMerk import KlWeegcomputerMerk
from ...Datatypes.KlWeegcomputerModelnaam import KlWeegcomputerModelnaam
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Weegcomputer(AIMObject, PuntGeometrie):
    """Een verwerkingseenheid met als input de weeggegevens van de weegcellen en output het gewicht."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Weegcomputer'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IndoorKast', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Asweger', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Weegcel', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

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
                                         label='serienummer',
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
