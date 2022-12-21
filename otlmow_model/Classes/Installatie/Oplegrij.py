# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.BaseClasses.NonNegIntegerField import NonNegIntegerField
from otlmow_model.GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Oplegrij(AIMNaamObject, LijnGeometrie):
    """Een rij van opleggingen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Oplegrij'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        LijnGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kelderlandhoofd')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kelderpijler')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Landhoofd')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Pijler')

        self._aantalOpleggingenOpRij = OTLAttribuut(field=NonNegIntegerField,
                                                    naam='aantalOpleggingenOpRij',
                                                    label='aantal opleggingen op rij',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Oplegrij.aantalOpleggingenOpRij',
                                                    definition='Het aantal opleggingen die op een rij liggen.',
                                                    owner=self)

    @property
    def aantalOpleggingenOpRij(self) -> int:
        """Het aantal opleggingen die op een rij liggen."""
        return self._aantalOpleggingenOpRij.get_waarde()

    @aantalOpleggingenOpRij.setter
    def aantalOpleggingenOpRij(self, value):
        self._aantalOpleggingenOpRij.set_waarde(value, owner=self)
