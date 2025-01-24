# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Grondkeringen import Grondkeringen
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from ...Datatypes.KwantWrdInMeterTAW import KwantWrdInMeterTAW, KwantWrdInMeterTAWWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class GewapendeGrond(Grondkeringen, AIMNaamObject, LijnGeometrie):
    """Grondkering waarbij constructieve elementen van staal of geotextiel/geogrid samenwerken met de grond en daaruit stabiliteit ontwikkelen. Gewapende grond is ook wel gekend als 'terre armée'."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GewapendeGrond'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BalkGK', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Grondanker', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#FunderingOpStaal', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Geotextiel', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Schanskorf', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Funderingspaal', direction='o')  # o = direction: outgoing

        self._aanzetpeil = OTLAttribuut(field=KwantWrdInMeterTAW,
                                        naam='aanzetpeil',
                                        label='aanzetpeil',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GewapendeGrond.aanzetpeil',
                                        definition='Het aanzetpeil van de gewapende grond in mTaw.',
                                        owner=self)

        self._detailplan = OTLAttribuut(field=DtcDocument,
                                        naam='detailplan',
                                        label='detailplan',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GewapendeGrond.detailplan',
                                        definition='Plan met details van de opbouw van de gewapende grond.',
                                        owner=self)

        self._grondkerendeHoogte = OTLAttribuut(field=KwantWrdInMeter,
                                                naam='grondkerendeHoogte',
                                                label='grondkerende hoogte',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GewapendeGrond.grondkerendeHoogte',
                                                definition='De hoogte van de teen tot de kop van de grondkering van het maaiveld.',
                                                owner=self)

        self._maximaalUitgravingspeil = OTLAttribuut(field=KwantWrdInMeterTAW,
                                                     naam='maximaalUitgravingspeil',
                                                     label='maximaal uitgravingspeil',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GewapendeGrond.maximaalUitgravingspeil',
                                                     definition='Het maximale uitgravingspeil.',
                                                     owner=self)

        self._rekennota = OTLAttribuut(field=DtcDocument,
                                       naam='rekennota',
                                       label='rekeningnota',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GewapendeGrond.rekennota',
                                       definition='De bijhorende rekennota met berekeningen.',
                                       owner=self)

    @property
    def aanzetpeil(self) -> KwantWrdInMeterTAWWaarden:
        """Het aanzetpeil van de gewapende grond in mTaw."""
        return self._aanzetpeil.get_waarde()

    @aanzetpeil.setter
    def aanzetpeil(self, value):
        self._aanzetpeil.set_waarde(value, owner=self)

    @property
    def detailplan(self) -> DtcDocumentWaarden:
        """Plan met details van de opbouw van de gewapende grond."""
        return self._detailplan.get_waarde()

    @detailplan.setter
    def detailplan(self, value):
        self._detailplan.set_waarde(value, owner=self)

    @property
    def grondkerendeHoogte(self) -> KwantWrdInMeterWaarden:
        """De hoogte van de teen tot de kop van de grondkering van het maaiveld."""
        return self._grondkerendeHoogte.get_waarde()

    @grondkerendeHoogte.setter
    def grondkerendeHoogte(self, value):
        self._grondkerendeHoogte.set_waarde(value, owner=self)

    @property
    def maximaalUitgravingspeil(self) -> KwantWrdInMeterTAWWaarden:
        """Het maximale uitgravingspeil."""
        return self._maximaalUitgravingspeil.get_waarde()

    @maximaalUitgravingspeil.setter
    def maximaalUitgravingspeil(self, value):
        self._maximaalUitgravingspeil.set_waarde(value, owner=self)

    @property
    def rekennota(self) -> DtcDocumentWaarden:
        """De bijhorende rekennota met berekeningen."""
        return self._rekennota.get_waarde()

    @rekennota.setter
    def rekennota(self, value):
        self._rekennota.set_waarde(value, owner=self)
