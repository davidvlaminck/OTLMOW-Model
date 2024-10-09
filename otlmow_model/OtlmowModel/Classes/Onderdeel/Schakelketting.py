# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KlSchakelkettingFabrikant import KlSchakelkettingFabrikant
from ...Datatypes.KlSchakelkettingMateriaal import KlSchakelkettingMateriaal
from ...Datatypes.KwantWrdInMegaPascal import KwantWrdInMegaPascal, KwantWrdInMegaPascalWaarden
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from ...Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter, KwantWrdInMillimeterWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Schakelketting(AIMNaamObject, PuntGeometrie):
    """Een schakelketting bestaat uit een reeks met elkaar verbonden schakels. Ze worden doorgaans gebruikt om trekkrachten uit te oefenen, zoals bv. bij hijsinstallaties."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Schakelketting'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hijsinstallatie', direction='u')  # u = unidirectional

        self._breedteSchakel = OTLAttribuut(field=KwantWrdInMillimeter,
                                            naam='breedteSchakel',
                                            label='breedte schakel',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Schakelketting.breedteSchakel',
                                            definition='De breedte van één schakel van de ketting. Indien de schakel ovaalvormig is, gaat het dus om de kleinste diameter van de ovaal.',
                                            owner=self)

        self._dikteSchakel = OTLAttribuut(field=KwantWrdInMillimeter,
                                          naam='dikteSchakel',
                                          label='dikte schakel',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Schakelketting.dikteSchakel',
                                          definition='De dikte van één schakel van de ketting.',
                                          owner=self)

        self._fabrikant = OTLAttribuut(field=KlSchakelkettingFabrikant,
                                       naam='fabrikant',
                                       label='fabrikant',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Schakelketting.fabrikant',
                                       definition='De fabrikant of producent van de ketting.',
                                       owner=self)

        self._hoogteSchakel = OTLAttribuut(field=KwantWrdInMillimeter,
                                           naam='hoogteSchakel',
                                           label='hoogte schakel',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Schakelketting.hoogteSchakel',
                                           definition='De hoogte van één schakel van de ketting. Indien de schakel ovaalvormig is, gaat het dus om de grootste diameter van de ovaal.',
                                           owner=self)

        self._lengte = OTLAttribuut(field=KwantWrdInMeter,
                                    naam='lengte',
                                    label='lengte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Schakelketting.lengte',
                                    definition='De totale lengte van de ketting.',
                                    owner=self)

        self._materiaal = OTLAttribuut(field=KlSchakelkettingMateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Schakelketting.materiaal',
                                       definition='het materiaal waaruit de schakels van de kettings vervaardigd zijn.',
                                       owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Schakelketting.technischeFiche',
                                             definition='De technische fiche van de ketting. Deze bevat ten minste een detailtekening van één schakel en va de ketting als geheel.',
                                             owner=self)

        self._treksterkte = OTLAttribuut(field=KwantWrdInMegaPascal,
                                         naam='treksterkte',
                                         label='treksterkte',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Schakelketting.treksterkte',
                                         definition='De treksterkte van een ketting is de maximale trekkracht die de ketting aan kan.',
                                         owner=self)

    @property
    def breedteSchakel(self) -> KwantWrdInMillimeterWaarden:
        """De breedte van één schakel van de ketting. Indien de schakel ovaalvormig is, gaat het dus om de kleinste diameter van de ovaal."""
        return self._breedteSchakel.get_waarde()

    @breedteSchakel.setter
    def breedteSchakel(self, value):
        self._breedteSchakel.set_waarde(value, owner=self)

    @property
    def dikteSchakel(self) -> KwantWrdInMillimeterWaarden:
        """De dikte van één schakel van de ketting."""
        return self._dikteSchakel.get_waarde()

    @dikteSchakel.setter
    def dikteSchakel(self, value):
        self._dikteSchakel.set_waarde(value, owner=self)

    @property
    def fabrikant(self) -> str:
        """De fabrikant of producent van de ketting."""
        return self._fabrikant.get_waarde()

    @fabrikant.setter
    def fabrikant(self, value):
        self._fabrikant.set_waarde(value, owner=self)

    @property
    def hoogteSchakel(self) -> KwantWrdInMillimeterWaarden:
        """De hoogte van één schakel van de ketting. Indien de schakel ovaalvormig is, gaat het dus om de grootste diameter van de ovaal."""
        return self._hoogteSchakel.get_waarde()

    @hoogteSchakel.setter
    def hoogteSchakel(self, value):
        self._hoogteSchakel.set_waarde(value, owner=self)

    @property
    def lengte(self) -> KwantWrdInMeterWaarden:
        """De totale lengte van de ketting."""
        return self._lengte.get_waarde()

    @lengte.setter
    def lengte(self, value):
        self._lengte.set_waarde(value, owner=self)

    @property
    def materiaal(self) -> str:
        """het materiaal waaruit de schakels van de kettings vervaardigd zijn."""
        return self._materiaal.get_waarde()

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> DtcDocumentWaarden:
        """De technische fiche van de ketting. Deze bevat ten minste een detailtekening van één schakel en va de ketting als geheel."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)

    @property
    def treksterkte(self) -> KwantWrdInMegaPascalWaarden:
        """De treksterkte van een ketting is de maximale trekkracht die de ketting aan kan."""
        return self._treksterkte.get_waarde()

    @treksterkte.setter
    def treksterkte(self, value):
        self._treksterkte.set_waarde(value, owner=self)
