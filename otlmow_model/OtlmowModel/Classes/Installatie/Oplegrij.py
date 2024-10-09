# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.BaseClasses.NonNegIntegerField import NonNegIntegerField
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Oplegrij(AIMNaamObject, LijnGeometrie):
    """Een rij van opleggingen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Oplegrij'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#VoorzieningNegatieveReactie', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Oplegging', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brugdeel', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kelderlandhoofd', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kelderpijler', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kokercomplex', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Landhoofd', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Pijler', direction='o')  # o = direction: outgoing

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
