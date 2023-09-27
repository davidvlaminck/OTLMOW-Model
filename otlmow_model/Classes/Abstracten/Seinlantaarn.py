# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from abc import abstractmethod
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.BaseClasses.BooleanField import BooleanField
from otlmow_model.Datatypes.KlLantaarnVormgeving import KlLantaarnVormgeving
from otlmow_model.Datatypes.KlSeinlantaarnDiameter import KlSeinlantaarnDiameter
from otlmow_model.Datatypes.KlSeinlantaarnMerk import KlSeinlantaarnMerk
from otlmow_model.Datatypes.KlSeinlantaarnModelnaam import KlSeinlantaarnModelnaam
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Seinlantaarn(AIMNaamObject, PuntGeometrie):
    """Abstracte voor het geheel van één of meerdere verkeerslichten die boven elkaar worden opgesteld en worden bevestigd op een steun,teneinde de beweging van een weggebruiker die een bepaald traject volgt,te verhinderen of toe te laten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Seinlantaarn'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#VRIDraagconstructie')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeerslicht')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestigingsbeugel')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerkeerslichtGroen')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerkeerslichtOranjegeel')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerkeerslichtRood')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerkeerslichtWit')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lichtsensor')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#StroomMeetmodule')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersregelaar')

        self._diameter = OTLAttribuut(field=KlSeinlantaarnDiameter,
                                      naam='diameter',
                                      label='diameter',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Seinlantaarn.diameter',
                                      definition='Diameter (in mm) van de lens van de verkeerslichten waaruit de lantaarn is samengesteld.',
                                      owner=self)

        self._heeftContrastscherm = OTLAttribuut(field=BooleanField,
                                                 naam='heeftContrastscherm',
                                                 label='heeft contrastscherm aanwezig',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Seinlantaarn.heeftContrastscherm',
                                                 definition='Aanduiding of er een contrastscherm aanwezig is op de lantaarn.',
                                                 owner=self)

        self._merk = OTLAttribuut(field=KlSeinlantaarnMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Seinlantaarn.merk',
                                  definition='Het merk van een de seinlantaarn.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlSeinlantaarnModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Seinlantaarn.modelnaam',
                                       definition='De modelnaam/product range van de seinlantaarn.',
                                       owner=self)

        self._vormgeving = OTLAttribuut(field=KlLantaarnVormgeving,
                                        naam='vormgeving',
                                        label='vormgeving',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Seinlantaarn.vormgeving',
                                        definition='Type vormgeving van de seinlantaarn.',
                                        owner=self)

    @property
    def diameter(self) -> str:
        """Diameter (in mm) van de lens van de verkeerslichten waaruit de lantaarn is samengesteld."""
        return self._diameter.get_waarde()

    @diameter.setter
    def diameter(self, value):
        self._diameter.set_waarde(value, owner=self)

    @property
    def heeftContrastscherm(self) -> bool:
        """Aanduiding of er een contrastscherm aanwezig is op de lantaarn."""
        return self._heeftContrastscherm.get_waarde()

    @heeftContrastscherm.setter
    def heeftContrastscherm(self, value):
        self._heeftContrastscherm.set_waarde(value, owner=self)

    @property
    def merk(self) -> str:
        """Het merk van een de seinlantaarn."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam/product range van de seinlantaarn."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def vormgeving(self) -> str:
        """Type vormgeving van de seinlantaarn."""
        return self._vormgeving.get_waarde()

    @vormgeving.setter
    def vormgeving(self, value):
        self._vormgeving.set_waarde(value, owner=self)
