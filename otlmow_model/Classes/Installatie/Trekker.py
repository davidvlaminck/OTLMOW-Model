# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.Datatypes.KlTypeTrekker import KlTypeTrekker
from otlmow_model.GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Trekker(AIMNaamObject, LijnGeometrie):
    """Een langwerpig (lijnvormig) element dat op trek wordt belast. Dit maakt de verbinding tussen het brugdek en de hoofddraagstructuur van het brugdeel (vb.: tussen boog en brugdek, tussen pyloon en brugdek, tussen draagkabel en brugdek, tussen windverband onder de brug en brugdek)."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Trekker'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        LijnGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brugdeel')

        self._type = OTLAttribuut(field=KlTypeTrekker,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Trekker.type',
                                  definition='Het type van de trekker.',
                                  owner=self)

    @property
    def type(self) -> str:
        """Het type van de trekker."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
