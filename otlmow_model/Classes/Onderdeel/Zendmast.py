# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.Datatypes.KlZendmastType import KlZendmastType
from otlmow_model.Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from otlmow_model.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Zendmast(AIMNaamObject, VlakGeometrie):
    """Een constructie, doorgaans hoger dan 10 meter,  die door mensen beklimbaar is en waarop apparatuur kan worden geïnstalleerd. Aan de mast is doorgaans een koppelstuk voorzien dat rond de mast klemt en bevestigbaar is op verschillende hoogtes met de nodige doorgangen voor de aansluitkabels, dat toelaat de antenne's te bevestigen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Zendmast'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        VlakGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Antenne')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestigingsbeugel')

        self._hoogte = OTLAttribuut(field=KwantWrdInMeter,
                                    naam='hoogte',
                                    label='hoogte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Zendmast.hoogte',
                                    definition='De hoogte van de zendmast.',
                                    owner=self)

        self._type = OTLAttribuut(field=KlZendmastType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Zendmast.type',
                                  definition='Het type zendmast.',
                                  owner=self)

    @property
    def hoogte(self) -> KwantWrdInMeterWaarden:
        """De hoogte van de zendmast."""
        return self._hoogte.get_waarde()

    @hoogte.setter
    def hoogte(self, value):
        self._hoogte.set_waarde(value, owner=self)

    @property
    def type(self) -> str:
        """Het type zendmast."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
