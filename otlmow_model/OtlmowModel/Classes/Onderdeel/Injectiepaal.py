# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Onderdeel.Funderingspaal import Funderingspaal
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KwantWrdInKubiekeMeterPerUur import KwantWrdInKubiekeMeterPerUur, KwantWrdInKubiekeMeterPerUurWaarden
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class Injectiepaal(Funderingspaal):
    """Trillingsvrij in de grond gevormde stalen buisschroefpaal, waarbij tijdens of na het schroef/draaiproces een mengsel van water en cement (= grout) door de holle boorschacht wordt geïnjecteerd."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Injectiepaal'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Behuizing')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BekledingComponent')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Grondanker')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Hoppinzuil')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Inloopbehuizing')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#NietWeggebondenDetectie')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Seinlantaarn')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SteunStandaard')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Ventilatie')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersbord')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Waarschuwingslantaarn')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ZenderOntvangerToegang')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Binnenverlichtingstoestel')

        self._nuttigeLengte = OTLAttribuut(field=KwantWrdInMeter,
                                           naam='nuttigeLengte',
                                           label='nuttige lengte',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Injectiepaal.nuttigeLengte',
                                           definition='Afstand gemeten, in meter, volgens de as van de injectiepaal tussen het aanzetpeil van de funderingszool boven de werkvloer (of, in geval van een vrijstaande paal, het afkappeil) en het aanzetpeil (definitief funderingspeil).',
                                           owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Injectiepaal.technischeFiche',
                                             definition='Document dat de technische details bijhoudt van de injectiepaal.',
                                             owner=self)

        self._volumeCementgrout = OTLAttribuut(field=KwantWrdInKubiekeMeterPerUur,
                                               naam='volumeCementgrout',
                                               label='volume cementgrout',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Injectiepaal.volumeCementgrout',
                                               definition='Volume van het cement per uur in kubieke meter.',
                                               owner=self)

    @property
    def nuttigeLengte(self) -> KwantWrdInMeterWaarden:
        """Afstand gemeten, in meter, volgens de as van de injectiepaal tussen het aanzetpeil van de funderingszool boven de werkvloer (of, in geval van een vrijstaande paal, het afkappeil) en het aanzetpeil (definitief funderingspeil)."""
        return self._nuttigeLengte.get_waarde()

    @nuttigeLengte.setter
    def nuttigeLengte(self, value):
        self._nuttigeLengte.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> DtcDocumentWaarden:
        """Document dat de technische details bijhoudt van de injectiepaal."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)

    @property
    def volumeCementgrout(self) -> KwantWrdInKubiekeMeterPerUurWaarden:
        """Volume van het cement per uur in kubieke meter."""
        return self._volumeCementgrout.get_waarde()

    @volumeCementgrout.setter
    def volumeCementgrout(self, value):
        self._volumeCementgrout.set_waarde(value, owner=self)
