# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.AxiaalDraagvermogen import AxiaalDraagvermogen
from ...Classes.Abstracten.AxiaalDraagvermogenWand import AxiaalDraagvermogenWand
from ...Classes.Abstracten.Grondkeringen import Grondkeringen
from ...Classes.Abstracten.WaterremmendeFunctie import WaterremmendeFunctie
from ...Classes.ImplementatieElement.AIMObject import AIMObject
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KlPrimaireVormCombiwand import KlPrimaireVormCombiwand
from ...Datatypes.KlSecundaireVormCombiwand import KlSecundaireVormCombiwand
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class Combiwand(AxiaalDraagvermogen, AxiaalDraagvermogenWand, Grondkeringen, WaterremmendeFunctie, AIMObject):
    """Een gecombineerde wand bestaande uit verschillende damplanken en buispalen of H-profielen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Combiwand'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BalkGK', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Grondanker', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Grondanker', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#StalenCaisson', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#StalenFunderingsprofiel', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#StalenBuispaal', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#StalenDamplank', direction='i')  # i = direction: incoming

        self._primaireVorm = OTLAttribuut(field=KlPrimaireVormCombiwand,
                                          naam='primaireVorm',
                                          label='primaire vorm',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Combiwand.primaireVorm',
                                          definition='Keuzelijst dat de primaire vorm van de combiwand aangeeft.',
                                          owner=self)

        self._rekennotaCombiwand = OTLAttribuut(field=DtcDocument,
                                                naam='rekennotaCombiwand',
                                                label='rekennota combiwand',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Combiwand.rekennotaCombiwand',
                                                definition="De rekennota van de combiwand, met o.a. de vermelding van UGT's en GGT's.",
                                                owner=self)

        self._secundaireVorm = OTLAttribuut(field=KlSecundaireVormCombiwand,
                                            naam='secundaireVorm',
                                            label='secundaire vorm',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Combiwand.secundaireVorm',
                                            definition='Keuzelijst dat de secundaire vorm van de combiwand aangeeft.',
                                            owner=self)

        self._technischeFicheCombiwand = OTLAttribuut(field=DtcDocument,
                                                      naam='technischeFicheCombiwand',
                                                      label='technische fiche combiwand',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Combiwand.technischeFicheCombiwand',
                                                      definition='Document dat de technische details van de combiwand bijhoudt.',
                                                      owner=self)

        self._totaleLengteCombiwand = OTLAttribuut(field=KwantWrdInMeter,
                                                   naam='totaleLengteCombiwand',
                                                   label='totale lengte combiwand',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Combiwand.totaleLengteCombiwand',
                                                   definition='De totale horizontale lengte van de gehele combiwand in lopende meter.',
                                                   owner=self)

    @property
    def primaireVorm(self) -> str:
        """Keuzelijst dat de primaire vorm van de combiwand aangeeft."""
        return self._primaireVorm.get_waarde()

    @primaireVorm.setter
    def primaireVorm(self, value):
        self._primaireVorm.set_waarde(value, owner=self)

    @property
    def rekennotaCombiwand(self) -> DtcDocumentWaarden:
        """De rekennota van de combiwand, met o.a. de vermelding van UGT's en GGT's."""
        return self._rekennotaCombiwand.get_waarde()

    @rekennotaCombiwand.setter
    def rekennotaCombiwand(self, value):
        self._rekennotaCombiwand.set_waarde(value, owner=self)

    @property
    def secundaireVorm(self) -> str:
        """Keuzelijst dat de secundaire vorm van de combiwand aangeeft."""
        return self._secundaireVorm.get_waarde()

    @secundaireVorm.setter
    def secundaireVorm(self, value):
        self._secundaireVorm.set_waarde(value, owner=self)

    @property
    def technischeFicheCombiwand(self) -> DtcDocumentWaarden:
        """Document dat de technische details van de combiwand bijhoudt."""
        return self._technischeFicheCombiwand.get_waarde()

    @technischeFicheCombiwand.setter
    def technischeFicheCombiwand(self, value):
        self._technischeFicheCombiwand.set_waarde(value, owner=self)

    @property
    def totaleLengteCombiwand(self) -> KwantWrdInMeterWaarden:
        """De totale horizontale lengte van de gehele combiwand in lopende meter."""
        return self._totaleLengteCombiwand.get_waarde()

    @totaleLengteCombiwand.setter
    def totaleLengteCombiwand(self, value):
        self._totaleLengteCombiwand.set_waarde(value, owner=self)
