# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KlMateriaalGolfplaat import KlMateriaalGolfplaat
from ...Datatypes.KlVormGolfplaat import KlVormGolfplaat
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Golfplaat(AIMNaamObject, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Dit is een gegolfd constructie-element van metaal of kunststof, gebruikt in bouw- en infrastructuurprojecten zoals tunnels en duikers. Het biedt verhoogde stijfheid en sterkte en verdeelt belastingen en spanningen efficiënt."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Golfplaat'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#HorizontaleConstructieplaat', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Wand', direction='o')  # o = direction: outgoing

        self._materiaal = OTLAttribuut(field=KlMateriaalGolfplaat,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Golfplaat.materiaal',
                                       definition='Het materiaal van de golfplaat.',
                                       owner=self)

        self._vorm = OTLAttribuut(field=KlVormGolfplaat,
                                  naam='vorm',
                                  label='vorm',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Golfplaat.vorm',
                                  definition='De verschillende mogelijke vormen van de golfplaat.',
                                  owner=self)

    @property
    def materiaal(self) -> str:
        """Het materiaal van de golfplaat."""
        return self._materiaal.get_waarde()

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)

    @property
    def vorm(self) -> str:
        """De verschillende mogelijke vormen van de golfplaat."""
        return self._vorm.get_waarde()

    @vorm.setter
    def vorm(self, value):
        self._vorm.set_waarde(value, owner=self)
