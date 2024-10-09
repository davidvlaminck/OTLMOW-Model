# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KlPositieKolk import KlPositieKolk
from ...Datatypes.KlVWCDroogzetbaarheid import KlVWCDroogzetbaarheid
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Kolk(AIMNaamObject, VlakGeometrie):
    """Vaste waterbouwkundige constructie van een sluis tussen sluishoofden, met een regelbaar waterniveau, waarin een schip van het ene niveau naar het andere kan gaan."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kolk'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AanhorigheidSluisStuw', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#VasteWaterbouwkundigeConstructie', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kolkvloer', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kolkwand', direction='i')  # i = direction: incoming

        self._breedteKolk = OTLAttribuut(field=KwantWrdInMeter,
                                         naam='breedteKolk',
                                         label='breedte van de kolk',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kolk.breedteKolk',
                                         definition='De breedte de kolk, tussen de dagvlakken, uitgedrukt in meter.',
                                         owner=self)

        self._droogzetbaarheid = OTLAttribuut(field=KlVWCDroogzetbaarheid,
                                              naam='droogzetbaarheid',
                                              label='droogzetbaarheid',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kolk.droogzetbaarheid',
                                              definition='De verschillende mogelijkheid m.b.t. droogzetbaarheid van de kolk.',
                                              owner=self)

        self._nuttigeKolklengte = OTLAttribuut(field=KwantWrdInMeter,
                                               naam='nuttigeKolklengte',
                                               label='nuttige kolklengte',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kolk.nuttigeKolklengte',
                                               definition='De lengte van de kolk uitgedrukt in meter dat daadwerkelijk gebruikt wordt voor het versassen van schepen.',
                                               owner=self)

        self._positieKolk = OTLAttribuut(field=KlPositieKolk,
                                         naam='positieKolk',
                                         label='positie van de kolk',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kolk.positieKolk',
                                         definition='De mogelijke posities van de kolk binnen het geheel van de waterbouwkundige structuur.',
                                         owner=self)

    @property
    def breedteKolk(self) -> KwantWrdInMeterWaarden:
        """De breedte de kolk, tussen de dagvlakken, uitgedrukt in meter."""
        return self._breedteKolk.get_waarde()

    @breedteKolk.setter
    def breedteKolk(self, value):
        self._breedteKolk.set_waarde(value, owner=self)

    @property
    def droogzetbaarheid(self) -> str:
        """De verschillende mogelijkheid m.b.t. droogzetbaarheid van de kolk."""
        return self._droogzetbaarheid.get_waarde()

    @droogzetbaarheid.setter
    def droogzetbaarheid(self, value):
        self._droogzetbaarheid.set_waarde(value, owner=self)

    @property
    def nuttigeKolklengte(self) -> KwantWrdInMeterWaarden:
        """De lengte van de kolk uitgedrukt in meter dat daadwerkelijk gebruikt wordt voor het versassen van schepen."""
        return self._nuttigeKolklengte.get_waarde()

    @nuttigeKolklengte.setter
    def nuttigeKolklengte(self, value):
        self._nuttigeKolklengte.set_waarde(value, owner=self)

    @property
    def positieKolk(self) -> str:
        """De mogelijke posities van de kolk binnen het geheel van de waterbouwkundige structuur."""
        return self._positieKolk.get_waarde()

    @positieKolk.setter
    def positieKolk(self, value):
        self._positieKolk.set_waarde(value, owner=self)
