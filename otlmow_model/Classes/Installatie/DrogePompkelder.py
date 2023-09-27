# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.BaseClasses.BooleanField import BooleanField
from otlmow_model.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class DrogePompkelder(AIMNaamObject, VlakGeometrie):
    """Een droge pompkelder is dat gedeelte van een gebouw/kunstwerk dat (meestal) onder het maaiveld is gelegen,veelal om beheersvoorzieningen te herbergen en/of als een technische ruimte dat deel uitmaakt van een pompstation."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#DrogePompkelder'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestigingsbeugel')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Binnenverlichtingstoestel')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hijsinstallatie')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderstel')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PutBovenbouw')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Pompstation')

        self._isOndergronds = OTLAttribuut(field=BooleanField,
                                           naam='isOndergronds',
                                           label='is ondergronds',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#DrogePompkelder.isOndergronds',
                                           definition='Geeft aan of de droge pompkelder zich boven- of ondergronds bevindt.',
                                           owner=self)

    @property
    def isOndergronds(self) -> bool:
        """Geeft aan of de droge pompkelder zich boven- of ondergronds bevindt."""
        return self._isOndergronds.get_waarde()

    @isOndergronds.setter
    def isOndergronds(self, value):
        self._isOndergronds.set_waarde(value, owner=self)
