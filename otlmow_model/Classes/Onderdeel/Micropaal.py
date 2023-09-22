# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.Onderdeel.Funderingspaal import Funderingspaal
from otlmow_model.Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.Datatypes.KlTypeMicropaal import KlTypeMicropaal
from otlmow_model.Datatypes.KwantWrdInKubiekeMeterPerUur import KwantWrdInKubiekeMeterPerUur, KwantWrdInKubiekeMeterPerUurWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class Micropaal(Funderingspaal):
    """In de grond gevormde paal met kleine diameter die bestaat uit een stalen inbouwelement (staaf) waarrond een groutkolom wordt gevormd."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Micropaal'
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
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SteunStandaard')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerankeringsplaatMicropaal')

        self._typeMicropaal = OTLAttribuut(field=KlTypeMicropaal,
                                           naam='typeMicropaal',
                                           label='type micropaal',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Micropaal.typeMicropaal',
                                           definition='Keuzelijst om het type micropaal te kunnen aangeven.',
                                           owner=self)

        self._uitvoeringsrapport = OTLAttribuut(field=DtcDocument,
                                                naam='uitvoeringsrapport',
                                                label='uitvoeringsrapport',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Micropaal.uitvoeringsrapport',
                                                definition='Rapport van de uitvoering per paal, met vermelding van de paalnummer, de nominale belasting, datum uitvoering boring, het volume van het cementgrout, details van de wapening, van het boorprofiel en van de injecties per fase,...',
                                                owner=self)

        self._volumeCementgrout = OTLAttribuut(field=KwantWrdInKubiekeMeterPerUur,
                                               naam='volumeCementgrout',
                                               label='volume cement grout',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Micropaal.volumeCementgrout',
                                               definition='Volume van het cement per uur in kubieke meter.',
                                               owner=self)

    @property
    def typeMicropaal(self) -> str:
        """Keuzelijst om het type micropaal te kunnen aangeven."""
        return self._typeMicropaal.get_waarde()

    @typeMicropaal.setter
    def typeMicropaal(self, value):
        self._typeMicropaal.set_waarde(value, owner=self)

    @property
    def uitvoeringsrapport(self) -> DtcDocumentWaarden:
        """Rapport van de uitvoering per paal, met vermelding van de paalnummer, de nominale belasting, datum uitvoering boring, het volume van het cementgrout, details van de wapening, van het boorprofiel en van de injecties per fase,..."""
        return self._uitvoeringsrapport.get_waarde()

    @uitvoeringsrapport.setter
    def uitvoeringsrapport(self, value):
        self._uitvoeringsrapport.set_waarde(value, owner=self)

    @property
    def volumeCementgrout(self) -> KwantWrdInKubiekeMeterPerUurWaarden:
        """Volume van het cement per uur in kubieke meter."""
        return self._volumeCementgrout.get_waarde()

    @volumeCementgrout.setter
    def volumeCementgrout(self, value):
        self._volumeCementgrout.set_waarde(value, owner=self)
