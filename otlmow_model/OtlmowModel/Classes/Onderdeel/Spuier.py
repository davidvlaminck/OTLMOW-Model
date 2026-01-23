# coding=utf-8
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.TechnischDocument import TechnischDocument
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...BaseClasses.BooleanField import BooleanField
from ...Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter, KwantWrdInMillimeterWaarden
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Spuier(TechnischDocument, AIMNaamObject, PuntGeometrie):
    """Een doorvoer in een kunstwerk, bedoeld voor het gecontroleerd afvoeren van water uit de constructie naar een onderliggend afwateringssysteem of open water."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Spuier'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#HorizontaleConstructieplaat', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Epoxydrain', direction='u')  # u = unidirectional

        self._diameter = OTLAttribuut(field=KwantWrdInMillimeter,
                                      naam='diameter',
                                      label='diameter',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Spuier.diameter',
                                      definition='De diameter van de spuier.',
                                      owner=self)

        self._heeftOntluchtingsbuis = OTLAttribuut(field=BooleanField,
                                                   naam='heeftOntluchtingsbuis',
                                                   label='heeft ontluchtingsbuis',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Spuier.heeftOntluchtingsbuis',
                                                   definition='Geeft aan of er een ontluchtingsbuis aanwezig is.',
                                                   owner=self)

        self._lengte = OTLAttribuut(field=KwantWrdInMillimeter,
                                    naam='lengte',
                                    label='lengte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Spuier.lengte',
                                    definition='De lengte van de spuier.',
                                    owner=self)

    @property
    def diameter(self) -> KwantWrdInMillimeterWaarden:
        """De diameter van de spuier."""
        return self._diameter.get_waarde()

    @diameter.setter
    def diameter(self, value):
        self._diameter.set_waarde(value, owner=self)

    @property
    def heeftOntluchtingsbuis(self) -> bool:
        """Geeft aan of er een ontluchtingsbuis aanwezig is."""
        return self._heeftOntluchtingsbuis.get_waarde()

    @heeftOntluchtingsbuis.setter
    def heeftOntluchtingsbuis(self, value):
        self._heeftOntluchtingsbuis.set_waarde(value, owner=self)

    @property
    def lengte(self) -> KwantWrdInMillimeterWaarden:
        """De lengte van de spuier."""
        return self._lengte.get_waarde()

    @lengte.setter
    def lengte(self, value):
        self._lengte.set_waarde(value, owner=self)
