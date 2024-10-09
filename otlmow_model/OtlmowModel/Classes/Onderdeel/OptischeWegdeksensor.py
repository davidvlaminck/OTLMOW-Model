# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Sensoropstelling import Sensoropstelling
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KlOptischeWegdeksensorMerk import KlOptischeWegdeksensorMerk
from ...Datatypes.KlOptischeWegdeksensorModelnaam import KlOptischeWegdeksensorModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class OptischeWegdeksensor(Sensoropstelling, AIMNaamObject):
    """Een meettoestel dat gebruik maakt van optische eigenschappen om de wegdekcondities zoals nat, ijs, sneeuw en vorst te meten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OptischeWegdeksensor'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Draagconstructie', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ThermoHygrometer', direction='u')  # u = unidirectional

        self._merk = OTLAttribuut(field=KlOptischeWegdeksensorMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OptischeWegdeksensor.merk',
                                  definition='Het merk van de optische wegdeksensor.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlOptischeWegdeksensorModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OptischeWegdeksensor.modelnaam',
                                       definition='De modelnaam van de optische wegdeksensor.',
                                       owner=self)

    @property
    def merk(self) -> str:
        """Het merk van de optische wegdeksensor."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van de optische wegdeksensor."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
