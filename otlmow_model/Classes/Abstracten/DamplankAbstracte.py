# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from abc import abstractmethod
from otlmow_model.Classes.Abstracten.Fundering import Fundering
from otlmow_model.Classes.Abstracten.Grondkeringen import Grondkeringen
from otlmow_model.Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class DamplankAbstracte(Fundering, Grondkeringen, PuntGeometrie):
    """Abstracte om eigenschappen van de damplank te bundelen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#DamplankAbstracte'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
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
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Damwand')

        self._planklengte = OTLAttribuut(field=KwantWrdInMeter,
                                         naam='planklengte',
                                         label='planklengte',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#DamplankAbstracte.planklengte',
                                         definition='Lengte van de damplank in meter.',
                                         owner=self)

        self._steek = OTLAttribuut(field=KwantWrdInMeter,
                                   naam='steek',
                                   label='steek',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#DamplankAbstracte.steek',
                                   definition='Geeft de steek van de damplank aan in meter.',
                                   owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#DamplankAbstracte.technischeFiche',
                                             definition='Technische fiche dat de technische details bijhoudt van de damplank.',
                                             owner=self)

    @property
    def planklengte(self) -> KwantWrdInMeterWaarden:
        """Lengte van de damplank in meter."""
        return self._planklengte.get_waarde()

    @planklengte.setter
    def planklengte(self, value):
        self._planklengte.set_waarde(value, owner=self)

    @property
    def steek(self) -> KwantWrdInMeterWaarden:
        """Geeft de steek van de damplank aan in meter."""
        return self._steek.get_waarde()

    @steek.setter
    def steek(self, value):
        self._steek.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> DtcDocumentWaarden:
        """Technische fiche dat de technische details bijhoudt van de damplank."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)
