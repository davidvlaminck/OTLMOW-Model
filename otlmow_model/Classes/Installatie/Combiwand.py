# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.Abstracten.AxiaalDraagvermogen import AxiaalDraagvermogen
from otlmow_model.Classes.Abstracten.AxiaalDraagvermogenWand import AxiaalDraagvermogenWand
from otlmow_model.Classes.Abstracten.Grondkeringen import Grondkeringen
from otlmow_model.Classes.Abstracten.WaterremmendeFunctie import WaterremmendeFunctie
from otlmow_model.Classes.ImplementatieElement.AIMObject import AIMObject
from otlmow_model.Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.Datatypes.KlPrimaireVormCombiwand import KlPrimaireVormCombiwand
from otlmow_model.Datatypes.KlSecundaireVormCombiwand import KlSecundaireVormCombiwand
from otlmow_model.Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class Combiwand(AxiaalDraagvermogen, AxiaalDraagvermogenWand, Grondkeringen, WaterremmendeFunctie, AIMObject):
    """Een gecombineerde wand bestaande uit verschillende damplanken en buispalen of H-profielen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Combiwand'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Grondanker')

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
