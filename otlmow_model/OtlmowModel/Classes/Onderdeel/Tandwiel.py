# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KlTandwielMerk import KlTandwielMerk
from ...Datatypes.KlTandwielModelnaam import KlTandwielModelnaam
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Tandwiel(AIMNaamObject, PuntGeometrie):
    """Een tandwiel, tandrad of kamrad is een getand onderdeel van een machine of constructie in de vorm van een wiel of cilinder. Het wordt gebruikt om beweging in de vorm van rotatie en koppel over te brengen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Tandwiel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Tandwielkast', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Overbrenging', direction='o')  # o = direction: outgoing

        self._merk = OTLAttribuut(field=KlTandwielMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Tandwiel.merk',
                                  definition='het merk van het tandwiel.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlTandwielModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Tandwiel.modelnaam',
                                       definition='De modelnaam van het tandwiel.',
                                       owner=self)

    @property
    def merk(self) -> str:
        """het merk van het tandwiel."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van het tandwiel."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
