# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.ComplexeGeleiding import ComplexeGeleiding
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.KlEcoPaalmateriaal import KlEcoPaalmateriaal
from ...Datatypes.KlRasterMazen import KlRasterMazen
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Ecoraster(ComplexeGeleiding, LijnGeometrie):
    """Een geleiding om dieren te leiden naar een plaats (ecoduct, ecotunnel, ...) waar ze veilig een drukke weg kunnen oversteken."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ecoraster'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Geleidingswand', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Wilddetectiezone', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ComplexeGeleiding', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ConstructieElement', direction='i')  # i = direction: incoming

        self._heeftPrikkeldraad = OTLAttribuut(field=BooleanField,
                                               naam='heeftPrikkeldraad',
                                               label='heeft prikkeldraad',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ecoraster.heeftPrikkeldraad',
                                               definition='Aanduiding of het ecoraster is voorzien van prikkeldraad.',
                                               owner=self)

        self._heeftSpandraden = OTLAttribuut(field=BooleanField,
                                             naam='heeftSpandraden',
                                             label='heeft spandraden',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ecoraster.heeftSpandraden',
                                             definition='Aanduiding of het ecoraster is voorzien van spandraden.',
                                             owner=self)

        self._lengte = OTLAttribuut(field=KwantWrdInMeter,
                                    naam='lengte',
                                    label='lengte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ecoraster.lengte',
                                    definition='De lengte van het ecoraster in meter.',
                                    owner=self)

        self._paalMateriaal = OTLAttribuut(field=KlEcoPaalmateriaal,
                                           naam='paalMateriaal',
                                           label='paal materiaal',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ecoraster.paalMateriaal',
                                           definition='Het materiaal van de paal in het ecoraster.',
                                           owner=self)

        self._paalhoogte = OTLAttribuut(field=KwantWrdInMeter,
                                        naam='paalhoogte',
                                        label='paalhoogte',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ecoraster.paalhoogte',
                                        definition='De hoogte van de paal in het ecoraster in meter.',
                                        owner=self)

        self._typeMazen = OTLAttribuut(field=KlRasterMazen,
                                       naam='typeMazen',
                                       label='type mazen',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ecoraster.typeMazen',
                                       definition='Het type van de mazen in het ecoraster.',
                                       owner=self)

    @property
    def heeftPrikkeldraad(self) -> bool:
        """Aanduiding of het ecoraster is voorzien van prikkeldraad."""
        return self._heeftPrikkeldraad.get_waarde()

    @heeftPrikkeldraad.setter
    def heeftPrikkeldraad(self, value):
        self._heeftPrikkeldraad.set_waarde(value, owner=self)

    @property
    def heeftSpandraden(self) -> bool:
        """Aanduiding of het ecoraster is voorzien van spandraden."""
        return self._heeftSpandraden.get_waarde()

    @heeftSpandraden.setter
    def heeftSpandraden(self, value):
        self._heeftSpandraden.set_waarde(value, owner=self)

    @property
    def lengte(self) -> KwantWrdInMeterWaarden:
        """De lengte van het ecoraster in meter."""
        return self._lengte.get_waarde()

    @lengte.setter
    def lengte(self, value):
        self._lengte.set_waarde(value, owner=self)

    @property
    def paalMateriaal(self) -> str:
        """Het materiaal van de paal in het ecoraster."""
        return self._paalMateriaal.get_waarde()

    @paalMateriaal.setter
    def paalMateriaal(self, value):
        self._paalMateriaal.set_waarde(value, owner=self)

    @property
    def paalhoogte(self) -> KwantWrdInMeterWaarden:
        """De hoogte van de paal in het ecoraster in meter."""
        return self._paalhoogte.get_waarde()

    @paalhoogte.setter
    def paalhoogte(self, value):
        self._paalhoogte.set_waarde(value, owner=self)

    @property
    def typeMazen(self) -> str:
        """Het type van de mazen in het ecoraster."""
        return self._typeMazen.get_waarde()

    @typeMazen.setter
    def typeMazen(self, value):
        self._typeMazen.set_waarde(value, owner=self)
