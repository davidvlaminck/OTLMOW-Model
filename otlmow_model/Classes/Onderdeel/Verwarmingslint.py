# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.ImplementatieElement.AIMObject import AIMObject
from otlmow_model.Datatypes.KwantWrdInWatt import KwantWrdInWatt, KwantWrdInWattWaarden
from otlmow_model.GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Verwarmingslint(AIMObject, LijnGeometrie):
    """Verwarmbare omwikkeling voor onderdelen die moeten beschermd worden tegen bevriezing."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verwarmingslint'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Brandvoorziening')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brandleiding')

        self._vermogen = OTLAttribuut(field=KwantWrdInWatt,
                                      naam='vermogen',
                                      label='vermogen',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verwarmingslint.vermogen',
                                      definition='Het vereiste vermogen in watt voor de correcte werking van het verwarmingslint.',
                                      owner=self)

    @property
    def vermogen(self) -> KwantWrdInWattWaarden:
        """Het vereiste vermogen in watt voor de correcte werking van het verwarmingslint."""
        return self._vermogen.get_waarde()

    @vermogen.setter
    def vermogen(self, value):
        self._vermogen.set_waarde(value, owner=self)
