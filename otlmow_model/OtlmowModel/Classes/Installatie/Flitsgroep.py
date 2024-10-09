# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.NaampadObject import NaampadObject
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Flitsgroep(NaampadObject, VlakGeometrie):
    """Groepering om de flitspalen van een kruispunt of bepaalde zone in onder te brengen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Flitsgroep'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Flitspaal', direction='i')  # i = direction: incoming

        self._isRoodLicht = OTLAttribuut(field=BooleanField,
                                         naam='isRoodLicht',
                                         label='is rood licht',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Flitsgroep.isRoodLicht',
                                         definition='Duidt aan of de groepering een snelheids- of roodlichtcamera installatie betreft.',
                                         owner=self)

    @property
    def isRoodLicht(self) -> bool:
        """Duidt aan of de groepering een snelheids- of roodlichtcamera installatie betreft."""
        return self._isRoodLicht.get_waarde()

    @isRoodLicht.setter
    def isRoodLicht(self, value):
        self._isRoodLicht.set_waarde(value, owner=self)
