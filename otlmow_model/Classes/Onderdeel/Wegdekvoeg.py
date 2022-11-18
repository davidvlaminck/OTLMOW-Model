# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.ImplementatieElement.AIMObject import AIMObject
from otlmow_model.BaseClasses.BooleanField import BooleanField
from otlmow_model.Datatypes.KlWegdekvoegType import KlWegdekvoegType
from otlmow_model.Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from otlmow_model.GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Wegdekvoeg(AIMObject, LijnGeometrie):
    """Dwarsvoegen en langsvoegen met uitzondering van de krimpvoegen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegdekvoeg'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        LijnGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Bestrating')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BitumineuzeLaag')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cementbetonverharding')

        self._heeftDeuvels = OTLAttribuut(field=BooleanField,
                                          naam='heeftDeuvels',
                                          label='heeft deuvels',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegdekvoeg.heeftDeuvels',
                                          definition='Aanduiding of de voeg al dan niet verdeuveld is.',
                                          owner=self)

        self._lengte = OTLAttribuut(field=KwantWrdInMeter,
                                    naam='lengte',
                                    label='lengte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegdekvoeg.lengte',
                                    definition='De lengte van de wegdekvoeg.',
                                    owner=self)

        self._type = OTLAttribuut(field=KlWegdekvoegType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegdekvoeg.type',
                                  definition='Het type van wegdekvoeg.',
                                  owner=self)

    @property
    def heeftDeuvels(self) -> bool:
        """Aanduiding of de voeg al dan niet verdeuveld is."""
        return self._heeftDeuvels.get_waarde()

    @heeftDeuvels.setter
    def heeftDeuvels(self, value):
        self._heeftDeuvels.set_waarde(value, owner=self)

    @property
    def lengte(self) -> KwantWrdInMeterWaarden:
        """De lengte van de wegdekvoeg."""
        return self._lengte.get_waarde()

    @lengte.setter
    def lengte(self, value):
        self._lengte.set_waarde(value, owner=self)

    @property
    def type(self) -> str:
        """Het type van wegdekvoeg."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
