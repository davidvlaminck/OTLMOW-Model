# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.Abstracten.Put import Put
from otlmow_model.Classes.Abstracten.PutRelatie import PutRelatie
from otlmow_model.Datatypes.DtcAfmetingBxlInCm import DtcAfmetingBxlInCm, DtcAfmetingBxlInCmWaarden
from otlmow_model.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Aswegerput(PutRelatie, Put, VlakGeometrie):
    """Een ondergrondse constructie die de elektronica van een asweger bevat."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aswegerput'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        PutRelatie.__init__(self)
        Put.__init__(self)
        VlakGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Weegcel')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Aswegersite')

        self._afmetingGrondvlak = OTLAttribuut(field=DtcAfmetingBxlInCm,
                                               naam='afmetingGrondvlak',
                                               label='afmeting grondvlak',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aswegerput.afmetingGrondvlak',
                                               definition='De binnenafmeting, breedte en lengte in cm van de aswegerput ter hoogte van het maaiveld.',
                                               owner=self)

    @property
    def afmetingGrondvlak(self) -> DtcAfmetingBxlInCmWaarden:
        """De binnenafmeting, breedte en lengte in cm van de aswegerput ter hoogte van het maaiveld."""
        return self._afmetingGrondvlak.get_waarde()

    @afmetingGrondvlak.setter
    def afmetingGrondvlak(self, value):
        self._afmetingGrondvlak.set_waarde(value, owner=self)
