# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Grondkeringen import Grondkeringen
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter, KwantWrdInCentimeterWaarden
from ...Datatypes.KwantWrdInDecimaleGraden import KwantWrdInDecimaleGraden, KwantWrdInDecimaleGradenWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class VernageldeWand(Grondkeringen, AIMNaamObject, LijnGeometrie, VlakGeometrie):
    """Versteviging van de grond door een rooster van ankers (nagels), waarbij de oppervlakte tussen de ankers gestabiliseerd wordt door middel van gewapend spuitbeton."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#VernageldeWand'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BalkGK', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Grondanker', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Grondanker', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Geotextiel', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Spuitbeton', direction='i')  # i = direction: incoming

        self._detailplan = OTLAttribuut(field=DtcDocument,
                                        naam='detailplan',
                                        label='detailplan',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#VernageldeWand.detailplan',
                                        definition='Plan met details van de opbouw van de vernagelde wand.',
                                        owner=self)

        self._hOhAfstandGrondankers = OTLAttribuut(field=KwantWrdInCentimeter,
                                                   naam='hOhAfstandGrondankers',
                                                   label='h. o. h. afstand grondankers',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#VernageldeWand.hOhAfstandGrondankers',
                                                   definition='Hart op hart afstand tussen grondankers in de wand.',
                                                   owner=self)

        self._hellingshoek = OTLAttribuut(field=KwantWrdInDecimaleGraden,
                                          naam='hellingshoek',
                                          label='hellingshoek',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#VernageldeWand.hellingshoek',
                                          definition='Hoek van de vernagelde wand t.o.v. de grond in decimale graden.',
                                          owner=self)

        self._rekennota = OTLAttribuut(field=DtcDocument,
                                       naam='rekennota',
                                       label='rekeningnota',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#VernageldeWand.rekennota',
                                       definition='De bijhorende rekennota met berekeningen.',
                                       owner=self)

    @property
    def detailplan(self) -> DtcDocumentWaarden:
        """Plan met details van de opbouw van de vernagelde wand."""
        return self._detailplan.get_waarde()

    @detailplan.setter
    def detailplan(self, value):
        self._detailplan.set_waarde(value, owner=self)

    @property
    def hOhAfstandGrondankers(self) -> KwantWrdInCentimeterWaarden:
        """Hart op hart afstand tussen grondankers in de wand."""
        return self._hOhAfstandGrondankers.get_waarde()

    @hOhAfstandGrondankers.setter
    def hOhAfstandGrondankers(self, value):
        self._hOhAfstandGrondankers.set_waarde(value, owner=self)

    @property
    def hellingshoek(self) -> KwantWrdInDecimaleGradenWaarden:
        """Hoek van de vernagelde wand t.o.v. de grond in decimale graden."""
        return self._hellingshoek.get_waarde()

    @hellingshoek.setter
    def hellingshoek(self, value):
        self._hellingshoek.set_waarde(value, owner=self)

    @property
    def rekennota(self) -> DtcDocumentWaarden:
        """De bijhorende rekennota met berekeningen."""
        return self._rekennota.get_waarde()

    @rekennota.setter
    def rekennota(self, value):
        self._rekennota.set_waarde(value, owner=self)
