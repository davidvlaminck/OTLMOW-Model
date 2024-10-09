# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Fundering import Fundering
from ...Datatypes.DtcConstructiestaalspecificaties import DtcConstructiestaalspecificaties, DtcConstructiestaalspecificatiesWaarden
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter, KwantWrdInMillimeterWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class StalenSchroefpaal(Fundering, PuntGeometrie):
    """Stalen paal met een stalen schacht die is voorzien van een spiraalvormige schroefdraad aan het uiteinde. Deze schroefdraad zorgt ervoor dat deze stevig in de grond vast komt te zitten, zonder dat er traditionele graaf- of betonwerkzaamheden nodig zijn."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#StalenSchroefpaal'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Behuizing', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BekledingComponent', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Grondanker', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Hoppinzuil', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Inloopbehuizing', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#NietWeggebondenDetectie', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Seinlantaarn', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SteunStandaard', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Ventilatie', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersbord', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Waarschuwingslantaarn', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ZenderOntvangerToegang', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Binnenverlichtingstoestel', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ConstructieElement', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ComplexeGeleiding', direction='i')  # i = direction: incoming

        self._buitendiameter = OTLAttribuut(field=KwantWrdInMillimeter,
                                            naam='buitendiameter',
                                            label='buitendiameter',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#StalenSchroefpaal.buitendiameter',
                                            definition='De diameter gemeten aan de buitenkant van de stalen schroefpaal in millimeter.',
                                            owner=self)

        self._hoogteBovenMaaiveld = OTLAttribuut(field=KwantWrdInMillimeter,
                                                 naam='hoogteBovenMaaiveld',
                                                 label='hoogte boven het maaiveld',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#StalenSchroefpaal.hoogteBovenMaaiveld',
                                                 definition='Hoogte in millimeters van het hoogste punt van de stalen schroefpaal gemeten vanaf het maaiveld.',
                                                 owner=self)

        self._paallengte = OTLAttribuut(field=KwantWrdInMillimeter,
                                        naam='paallengte',
                                        label='paallengte',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#StalenSchroefpaal.paallengte',
                                        definition='De afstand, gemeten in millimeter, volgens de as van de stalen schroefpaal tussen de bovenkant en het aanzetpeil.',
                                        owner=self)

        self._staalspecificaties = OTLAttribuut(field=DtcConstructiestaalspecificaties,
                                                naam='staalspecificaties',
                                                label='staalspecificaties',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#StalenSchroefpaal.staalspecificaties',
                                                definition='Eigenschappen van het gebruikte constructiestaal.',
                                                owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#StalenSchroefpaal.technischeFiche',
                                             definition='De technische fiche van de stalen schroefpaal.',
                                             owner=self)

    @property
    def buitendiameter(self) -> KwantWrdInMillimeterWaarden:
        """De diameter gemeten aan de buitenkant van de stalen schroefpaal in millimeter."""
        return self._buitendiameter.get_waarde()

    @buitendiameter.setter
    def buitendiameter(self, value):
        self._buitendiameter.set_waarde(value, owner=self)

    @property
    def hoogteBovenMaaiveld(self) -> KwantWrdInMillimeterWaarden:
        """Hoogte in millimeters van het hoogste punt van de stalen schroefpaal gemeten vanaf het maaiveld."""
        return self._hoogteBovenMaaiveld.get_waarde()

    @hoogteBovenMaaiveld.setter
    def hoogteBovenMaaiveld(self, value):
        self._hoogteBovenMaaiveld.set_waarde(value, owner=self)

    @property
    def paallengte(self) -> KwantWrdInMillimeterWaarden:
        """De afstand, gemeten in millimeter, volgens de as van de stalen schroefpaal tussen de bovenkant en het aanzetpeil."""
        return self._paallengte.get_waarde()

    @paallengte.setter
    def paallengte(self, value):
        self._paallengte.set_waarde(value, owner=self)

    @property
    def staalspecificaties(self) -> DtcConstructiestaalspecificatiesWaarden:
        """Eigenschappen van het gebruikte constructiestaal."""
        return self._staalspecificaties.get_waarde()

    @staalspecificaties.setter
    def staalspecificaties(self, value):
        self._staalspecificaties.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> DtcDocumentWaarden:
        """De technische fiche van de stalen schroefpaal."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)
