# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.AanhorigheidSluisStuw import AanhorigheidSluisStuw
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KlTypeFendering import KlTypeFendering
from ...Datatypes.KwantWrdInMegajoule import KwantWrdInMegajoule, KwantWrdInMegajouleWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Fendering(AanhorigheidSluisStuw, AIMNaamObject, PuntGeometrie, LijnGeometrie):
    """Een fender dient om de kinetische energie van een afmerend schip op te vangen en op die manier schade aan een schip of de achterliggende constructie."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Fendering'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Dukdalf', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kesp', direction='u')  # u = unidirectional

        self._energie = OTLAttribuut(field=KwantWrdInMegajoule,
                                     naam='energie',
                                     label='energie',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Fendering.energie',
                                     definition='De karakteristieke energie die de fender kan opnemen uitgedrukt in megajoule.',
                                     owner=self)

        self._typeFendering = OTLAttribuut(field=KlTypeFendering,
                                           naam='typeFendering',
                                           label='type fendering',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Fendering.typeFendering',
                                           definition='Het type fendering.',
                                           owner=self)

    @property
    def energie(self) -> KwantWrdInMegajouleWaarden:
        """De karakteristieke energie die de fender kan opnemen uitgedrukt in megajoule."""
        return self._energie.get_waarde()

    @energie.setter
    def energie(self, value):
        self._energie.set_waarde(value, owner=self)

    @property
    def typeFendering(self) -> str:
        """Het type fendering."""
        return self._typeFendering.get_waarde()

    @typeFendering.setter
    def typeFendering(self, value):
        self._typeFendering.set_waarde(value, owner=self)
