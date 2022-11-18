# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.ImplementatieElement.AIMObject import AIMObject
from otlmow_model.Datatypes.KlBouwputType import KlBouwputType
from otlmow_model.Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from otlmow_model.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Bouwput(AIMObject, VlakGeometrie):
    """De ontgraving die nodig is voor het maken van een ondergrondse constructie zoals bv. een put of putten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bouwput'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        VlakGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#PutRelatie')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Damwand')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KringsBerliner')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Rioleringsstelsel')

        self._putdiepte = OTLAttribuut(field=KwantWrdInMeter,
                                       naam='putdiepte',
                                       label='putdiepte',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bouwput.putdiepte',
                                       definition='Diepte tussen het maaiveld en onderkant bouwput in meter.',
                                       owner=self)

        self._type = OTLAttribuut(field=KlBouwputType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bouwput.type',
                                  definition='Het type van bouwput.',
                                  owner=self)

    @property
    def putdiepte(self) -> KwantWrdInMeterWaarden:
        """Diepte tussen het maaiveld en onderkant bouwput in meter."""
        return self._putdiepte.get_waarde()

    @putdiepte.setter
    def putdiepte(self, value):
        self._putdiepte.set_waarde(value, owner=self)

    @property
    def type(self) -> str:
        """Het type van bouwput."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
