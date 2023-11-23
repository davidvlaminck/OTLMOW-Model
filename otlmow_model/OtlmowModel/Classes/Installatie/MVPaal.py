# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Onderdeel.Funderingspaal import Funderingspaal
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KwantWrdInKubiekeMeterPerUur import KwantWrdInKubiekeMeterPerUur, KwantWrdInKubiekeMeterPerUurWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class MVPaal(Funderingspaal):
    """Grondverdringende stalen paal met een inwendige en/of uitwendige injectie met grout-specie. Ze wordt vervaardigd door het heien van een stalen profiel/buis in de bodem onder gelijktijdig injecteren van een groutmengsel."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#MVPaal'
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

        self._technischeFicheMVPaal = OTLAttribuut(field=DtcDocument,
                                                   naam='technischeFicheMVPaal',
                                                   label='technische fiche MV paal',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#MVPaal.technischeFicheMVPaal',
                                                   definition='De technische gegevens van de MV-paal (detail afmetingen, dikte, hoogte, groutspecificaties,...)',
                                                   owner=self)

        self._volumeCementgrout = OTLAttribuut(field=KwantWrdInKubiekeMeterPerUur,
                                               naam='volumeCementgrout',
                                               label='volume cementgrout',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#MVPaal.volumeCementgrout',
                                               definition='Volume van het cement per uur in kubieke meter.',
                                               owner=self)

    @property
    def technischeFicheMVPaal(self) -> DtcDocumentWaarden:
        """De technische gegevens van de MV-paal (detail afmetingen, dikte, hoogte, groutspecificaties,...)"""
        return self._technischeFicheMVPaal.get_waarde()

    @technischeFicheMVPaal.setter
    def technischeFicheMVPaal(self, value):
        self._technischeFicheMVPaal.set_waarde(value, owner=self)

    @property
    def volumeCementgrout(self) -> KwantWrdInKubiekeMeterPerUurWaarden:
        """Volume van het cement per uur in kubieke meter."""
        return self._volumeCementgrout.get_waarde()

    @volumeCementgrout.setter
    def volumeCementgrout(self, value):
        self._volumeCementgrout.set_waarde(value, owner=self)
